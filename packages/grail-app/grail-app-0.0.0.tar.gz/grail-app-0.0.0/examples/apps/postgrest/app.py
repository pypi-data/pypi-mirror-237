import flask
import subprocess
import time
import atexit
import requests
import pathlib
from extensions import settings
app = flask.Flask(__name__)

processes = {}

# TODO: Replace proxy code with werkzeug.middleware.http_proxy:ProxyMiddleware

@app.route("/<db>/<schemas>/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/<db>/<schemas>/", defaults={"path": ""})
def api(db, schemas, path=""):
    global processes
    process = processes.get(db+"-"+schemas)
    if not process:
        # Start PostgREST in the background
        pgrest_map = flask.current_app.config.get("POSTGREST_URI",{})
        uri = pgrest_map.get(db)
        if not uri:
            return flask.jsonify({"error": f"PostgREST-{db} not configured."}), 500
        
        port = str(8090+len(processes))
        process = PostgREST(db, port=port, uri=uri,schemas=schemas, binary=flask.current_app.config['POSTGREST_BINARY'])
        process.start()

        # Give PostgREST some time to start. You can adjust the sleep time as needed.
        time.sleep(2)

        # Check if PostgREST is running
        if process.is_running():
            app.logger.info("PostgREST is running in the background.")
        elif process._process:
            app.logger.error(f"Failed to start PostgREST-{process._name}.")
            # Print the error message if PostgREST failed to start
            _, stderr = process._process.communicate()
            app.logger.error("Error:", stderr.decode())
            return flask.jsonify({"error": f"Failed to start PostgREST-{process._name}."}), 500
        else:
            app.logger.error("Failed to start PostgREST.")
            return flask.jsonify({"error": f"Failed to start PostgREST-{process._name}."}), 500

        processes[db+"-"+schemas] = process

    # Forward the request to PostgREST

    # Get the original request method, headers, and data
    method = flask.request.method
    headers = {key: value for key, value in flask.request.headers if key != "Host"}
    data = flask.request.get_data()

    # URL of the app to which the request should be forwarded
    forward_url = f"http://0.0.0.0:{process._port}/" + path

    # Forward the request to another app
    response = requests.request(
        method, forward_url, headers=headers, data=data, timeout=5
    )

    # Return the response received from the forwarded app

    if response.headers.get('content-type') == 'application/json':
        return flask.jsonify(response.json()), response.status_code

    return response.text, response.status_code


def killall():
    global processes
    for name, process in list(processes.items()):
        process._process.kill()
        del processes[name]


atexit.register(killall)


PGREST_CONFIG_TEMPLATE = """
## The database role to use when no client authentication is provided
db-anon-role = "{{anon_role}}"

## Notification channel for reloading the schema cache
db-channel = "pgrst"

## Enable or disable the notification channel
db-channel-enabled = true

## Enable in-database configuration
db-config = true

## Function for in-database configuration
## db-pre-config = "postgrest.pre_config"

## Extra schemas to add to the search_path of every request
db-extra-search-path = "public"

## Limit rows in response
# db-max-rows = 1000

## Allow getting the EXPLAIN plan through the `Accept: application/vnd.pgrst.plan` header
# db-plan-enabled = false

## Number of open connections in the pool
db-pool = 10

## Time in seconds to wait to acquire a slot from the connection pool
# db-pool-acquisition-timeout = 10

## Time in seconds after which to recycle pool connections
# db-pool-max-lifetime = 1800

## Time in seconds after which to recycle unused pool connections
# db-pool-max-idletime = 30

## Allow automatic database connection retrying
# db-pool-automatic-recovery = true

## Stored proc to exec immediately after auth
# db-pre-request = "stored_proc_name"

## Enable or disable prepared statements. disabling is only necessary when behind a connection pooler.
## When disabled, statements will be parametrized but won't be prepared.
db-prepared-statements = true

## The name of which database schema to expose to REST clients
db-schemas = "{{schemas}}"

## How to terminate database transactions
## Possible values are:
## commit (default)
##   Transaction is always committed, this can not be overriden
## commit-allow-override
##   Transaction is committed, but can be overriden with Prefer tx=rollback header
## rollback
##   Transaction is always rolled back, this can not be overriden
## rollback-allow-override
##   Transaction is rolled back, but can be overriden with Prefer tx=commit header
db-tx-end = "commit"

## The standard connection URI format, documented at
## https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
db-uri = "{{uri}}"
## Determine if GUC request settings for headers, cookies and jwt claims use the legacy names (string with dashes, invalid starting from PostgreSQL v14) with text values instead of the new names (string without dashes, valid on all PostgreSQL versions) with json values.
## For PostgreSQL v14 and up, this setting will be ignored.
db-use-legacy-gucs = true

# jwt-aud = "your_audience_claim"

## Jspath to the role claim key
jwt-role-claim-key = ".role"

## Choose a secret, JSON Web Key (or set) to enable JWT auth
## (use "@filename" to load from separate file)
# jwt-secret = "secret_with_at_least_32_characters"
jwt-secret-is-base64 = false

## Enables and set JWT Cache max lifetime, disables caching with 0
# jwt-cache-max-lifetime = 0

## Logging level, the admitted values are: crit, error, warn and info.
log-level = "error"

## Determine if the OpenAPI output should follow or ignore role privileges or be disabled entirely.
## Admitted values: follow-privileges, ignore-privileges, disabled
openapi-mode = "follow-privileges"  

## Base url for the OpenAPI output
openapi-server-proxy-uri = "http://0.0.0.0:8000/pgrest/{{name}}/{{schemas}}"

## Content types to produce raw output
# raw-media-types="image/png, image/jpg"

server-host = "!4"
server-port = {{port}}

## Unix socket location
## if specified it takes precedence over server-port
# server-unix-socket = "/tmp/pgrst.sock"

## Unix socket file mode
## When none is provided, 660 is applied by default
# server-unix-socket-mode = "660"
"""


class PostgREST:
    def __init__(
        self,
        name,
        port: str,
        uri: str,
        binary="/usr/local/bin/postgrest",
        template=None,
        schemas="public",
        anon_role="web_anon",
    ) -> None:
        self._port: str = port
        self._name = name
        self._process = None
        self._app = app
        self._uri = uri
        self._binary = binary
        self._anon_role = anon_role
        self._schemas = schemas
        self._template = template or PGREST_CONFIG_TEMPLATE

    def start(self) -> None:
        filepath = pathlib.Path(f"/tmp/{self._name}.pgrest.conf")
        context = {
            "uri": self._uri,
            "port": self._port,
            "anon_role": self._anon_role,
            "schemas": self._schemas,
            "name":self._name
        }
        rendered_config = flask.render_template_string(self._template, **context)
        filepath.write_text(rendered_config)
        command = [self._binary, filepath.absolute()]
        self._process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

    def is_running(self) -> bool:
        if self._process:
            return self._process.poll() is None
        return False

    def stop(self) -> None:
        if self._process:
            self._process.kill()

settings.init_app(app)

if __name__ == "__main__":
    app.run()