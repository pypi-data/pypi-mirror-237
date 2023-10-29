FROM unit:1.31.0-python3.11

# Install PostgREST
#RUN curl -sSL https://get.haskellstack.org/ | sh && stack upgrade && git clone https://github.com/PostgREST/postgrest.git && cd postgrest && stack build --install-ghc --copy-bins --local-bin-path /usr/local/bin
COPY --from=postgrest/postgrest /bin/postgrest /usr/local/bin

# Install Postgres Client
RUN apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*


# Install Code Server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Install Python App
RUN pip install --upgrade pip
COPY deploy/requirements/prod.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY pyproject.toml /app/pyproject.toml
COPY grail /app/grail
RUN python3 -m pip install -e /app/

COPY examples/apps/unit.json /docker-entrypoint.d/config.json
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
