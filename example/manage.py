#!/usr/bin/env python
"""Aquilo's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("AQUILO_SETTINGS_MODULE", "kelodraken.config.settings")
    os.environ.setdefault("AQUILO_APPS_MODULE", "kelodraken.apps")
    try:
        from src.aquilo import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Aquilo. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
