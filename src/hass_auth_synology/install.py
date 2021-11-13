"""CLI script for installing the provider."""
import os
import shutil
import sys

from homeassistant.auth.providers import homeassistant


def cli(args=None) -> None:
    """Read args as main entrypoint through CLI."""
    if not args:
        args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: hass-auth-synology install")
        sys.exit(1)
    command = args[0].lower()

    if command == "install":
        install()
        sys.exit(0)

    print(f"Unknown command: {command}")
    sys.exit(1)


def install() -> None:
    """Install the Synology authentication provider in the system's Home Assistant."""
    hass_provider_path = os.path.abspath(homeassistant.__file__)
    providers_dir_path = os.path.dirname(hass_provider_path)
    target_path = os.path.join(providers_dir_path, "synology.py")
    current_path = os.path.abspath(__file__)
    current_dir_path = os.path.dirname(current_path)
    source_path = os.path.join(current_dir_path, "synology.py")

    print(f"Installing Synology provider from {source_path} into {target_path}")
    shutil.copyfile(source_path, target_path)


if __name__ == "__main__":
    cli()
