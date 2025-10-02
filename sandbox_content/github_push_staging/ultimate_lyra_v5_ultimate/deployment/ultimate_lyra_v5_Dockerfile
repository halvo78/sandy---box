FROM alpine:3.20

LABEL maintainer="Ultimate Lyra Trading System" \
      version="3.12.0-lyra" \
      description="Ngrok All Functions - Multi-Tunnel Oversight" \
      io.lyra.mode="spot_monitoring" \
      io.lyra.compliance="ISO_27001_ATO"

ARG NGROK_VERSION=3.12.0
ARG TARGETARCH=amd64

RUN apk add --no-cache curl unzip bash jq python3 py3-pip && \
    curl -sSL https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-v3-stable-linux-${TARGETARCH}.zip -o ngrok.zip && \
    unzip ngrok.zip && rm ngrok.zip && \
    chmod +x ngrok && mv ngrok /usr/local/bin/

WORKDIR /app

COPY requirements.txt ./
COPY tunnel_manager.py ./
COPY ngrok_config.yml ./
COPY start_ngrok.sh ./
COPY safe_tunnel_policies.py ./
COPY manus_verification.py ./

RUN pip3 install -r requirements.txt

RUN adduser -D lyra_user && \
    chown -R lyra_user:lyra_user /app && \
    chmod +x start_ngrok.sh

USER lyra_user

HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD ngrok api tunnels list | jq -e 'length > 0' || exit 1

EXPOSE 4040 8081 8000 3000 8086

CMD ["./start_ngrok.sh"]
