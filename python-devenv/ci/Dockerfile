FROM oraclelinux:8

# Variabile build-time (impostata automaticamente da Docker)
ARG TARGETARCH
ARG CS_VERSION="4.89.1"

# Dipendenze di base
RUN dnf install -y \
    curl \
    tar \
    gzip \
    git \
    python3 \
    python3-pip \
    && dnf clean all

# Directory di installazione
ENV CODESERVER_DIR=/usr/local/lib/code-server

# Scarica e installa code-server in base all'architettura
RUN if [ "$TARGETARCH" = "amd64" ]; then \
        URL="https://github.com/coder/code-server/releases/latest/download/code-server-linux-amd64.tar.gz"; \
    elif [ "$TARGETARCH" = "arm64" ]; then \
        URL="https://github.com/coder/code-server/releases/download/v${CS_VERSION}/code-server-${CS_VERSION}-linux-arm64.tar.gz"; \
    else \
        echo "Architettura non supportata: $TARGETARCH" && exit 1; \
    fi && \
    curl -fsSL "$URL" -o /tmp/code-server.tar.gz && \
    mkdir -p /usr/local/lib/code-server && \
    tar -xzf /tmp/code-server.tar.gz -C /usr/local/lib/code-server --strip-components=1 && \
    ln -s /usr/local/lib/code-server/bin/code-server /usr/local/bin/code-server && \
    rm -f /tmp/code-server.tar.gz



# Utente dedicato
RUN useradd -m coder
USER coder
WORKDIR /home/coder/project

# Preinstallazione estensioni VS Code
RUN code-server --install-extension ms-python.python && \
    code-server --install-extension ms-python.black-formatter && \
    code-server --install-extension eamodio.gitlens


# Configurazione sicura
ENV PASSWORD="changeme"
ENV BIND_ADDR="0.0.0.0:8089"

EXPOSE 8089

CMD ["sh", "-c", "code-server --bind-addr ${BIND_ADDR} --auth password /home/coder/project"]
