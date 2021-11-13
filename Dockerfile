ARG HASS_VERSION=latest
FROM homeassistant/home-assistant:${HASS_VERSION}

RUN mkdir -p /tmp/hass-auth-synology
COPY dist /tmp/hass-auth-synology/

RUN pip install /tmp/hass-auth-synology/*.whl
RUN hass-auth-synology install
