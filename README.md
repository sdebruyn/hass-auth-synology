# Authentication provider using Synology DSM users for Home Assistant

![PyPI](https://img.shields.io/pypi/v/hass-auth-synology)
![GitHub branch checks state](https://img.shields.io/github/checks-status/sdebruyn/hass-auth-synology/main?label=build)
![Codecov](https://img.shields.io/codecov/c/github/sdebruyn/hass-auth-synology?token=XC9UFW1RKH)
![Maintenance](https://img.shields.io/maintenance/yes/2021)
![GitHub](https://img.shields.io/github/license/sdebruyn/hass-auth-synology)

The Synology authentication provider lets you authenticate using the users in your Synology DSM. Anyone with a user account on your Synology NAS will be able to login.

The provider supports 2-factor authentication, according to what is configured in DSM.
When logging in, there will be a field to enter the 2FA code. The field is optional, but it should be used if your account in DSM requires 2FA. Otherwise, it can be left empty.

The use of 2FA within this provider is independent of the 2FA configuration in Home Assistant. If you enable 2FA in Home Assistant, and it is also enabled in Synology, you will have to enter 2 2FA codes.

The provider requires DSM 7.0 or newer.

## Installation

### Home Assistant Container

Use this package's container instead of the Home Assistant one.

```
ghcr.io/sdebruyn/hass-auth-synology:latest
```

### Home Assistant Core

The installation will have to be redone everytime you update Home Assistant.

1. Make sure the Home Assistant virtualenv is activated: `source bin/activate`
2. Install this package: `pip3 install hass-auth-synology`
3. Run the installation command: `hass-auth-synology install`

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

## Configuration

Add the following to your Home Assistant configuration:

```yaml
homeassistant:
  auth_providers:
    - type: synology
      host: nas.local
      port: 443
      secure: true
      verify_cert: true
```

* `host`: IP address or hostname of your NAS.
* `port`: Port on which DSM is available. Make sure to use one corresponding to HTTP or HTTPS as configured with `secure` .
* `secure` (optional): Enable this to use HTTPS instead of HTTP. (default: false)
* `verify_cert` (optional): Enable this to verify the certificate when using HTTPS (default: false).
Make sure to disable this when using self-signed certificates or an IP address instead of a hostname.
The setting is ignored when `secure` is false.

## Troubleshooting

If any errors occur, make sure to check your Home Assistant logs. If the connection succeeds, but authentication fails, Synology DSM will output an error code.
The meaning of the error code can be found [in the Synology DSM Login API documentation](https://global.download.synology.com/download/Document/Software/DeveloperGuide/Os/DSM/All/enu/DSM_Login_Web_API_Guide_enu.pdf).

Feel free to open an issue on GitHub if you encounter any issues.

## License & attribution

Apache v2.0

Test utilities under `tests` are coming from [Home Assistant Core](https://github.com/home-assistant/core).
