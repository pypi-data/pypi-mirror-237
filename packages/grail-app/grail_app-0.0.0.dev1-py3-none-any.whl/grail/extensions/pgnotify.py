import psycopg2
import flask
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class PgNotify:
    def __init__(self, uri, channel="default") -> None:
        self.conn = None
        self.uri = uri
        self.channel = channel

    def notify(self, channel, data):
        self.conn = self.conn or create_con(self.uri)
        return dbnotify(self.conn, channel=channel or self.channel, data=data)

    def listen(self, channel, handler):
        self.conn = self.conn or create_con(self.uri)
        return dblisten(self.conn, channel or self.channel, handler)


def create_con(uri):
    conn = psycopg2.connect(uri)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return conn


def dbnotify(conn, channel, data):
    cur = conn.cursor()
    return cur.execute(f"NOTIFY {channel}, '{data}'")


def dblisten(conn, channel, handler):
    """
    Open a db connection and add notifications to *q*.
    """
    cur = conn.cursor()
    cur.execute(f"LISTEN {channel};")
    while 1:
        conn.poll()
        while conn.notifies:
            n = conn.notifies.pop()
            handler(n)


def init_app(app: flask.Flask):
    uri = app.config.get("SQLALCHEMY_DATABASE_URI") or app.config.get("POSTGRES_URI")

    if not uri:
        return

    app.extensions["pgnotify"] = PgNotify(uri=uri, channel=app.name)

    @app.route("/listen/<channel>")
    def listen(channel):
        flask.current_app.extensions["pgnotify"].listen(channel, print)

        return f"Listening to {channel}"

    @app.route("/notify/<channel>/<data>")
    def notify(channel, data):
        n = flask.current_app.extensions["pgnotify"]
        import threading

        t = threading.Thread(target=notify, args=(channel, data), daemon=True)
        t.start()
        return f"Notified {channel} with {data}"


if __name__ == "__main__":
    import sys

    uri = sys.argv[1]
    conn = create_con(uri)

    if len(sys.argv) == 2:
        dblisten(conn, "data", print)
    elif len(sys.argv) == 3:
        data = sys.argv[2]
        dbnotify(conn, "data", data)
