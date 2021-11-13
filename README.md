# Authentication provider using Synology DSM users for Home Assistant

## Installation

### Home Assistant Container

Use this package's container instead of the Home Assistant one.

```
ghcr.io/home-assistant/home-assistant:stable
```

### Home Assistant Core

The installation will have to be redone everytime you update Home Assistant.

1. Make sure the Home Assistant virtualenv is activated: `source bin/activate`
2. Install this package: `pip3 install hass-auth-synology`
3. Run the install command: `hass-auth-synology install`

### Home Assistant Supervised

The installation will have to be redone everytime you update Home Assistant.

1. Search for the “SSH & Web Terminal” add-on in the add-on store and install it.
2. Configure the username and password/authorized_keys options.
3. Start the “SSH & Web Terminal” add-on
4. Run the following code through the web terminal:
    ```shell
    pip3 install hass-auth-synology
   hass-auth-synology install
    ```
5. You can now disable and remove the “SSH & Web Terminal” add-on again.

## License & attribution

Apache v2.0

Test utilities under `tests` are coming from [Home Assistant Core](https://github.com/home-assistant/core).
