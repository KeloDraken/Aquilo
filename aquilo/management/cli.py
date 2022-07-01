import os
from importlib import import_module
from inspect import getmembers, isfunction

from aquilo.main import Aquilo

settings = import_module(os.environ.get("AQUILO_SETTINGS_MODULE"))

app = Aquilo(debug=settings.DEBUG)


def execute_from_command_line(args: list[str]) -> None:
    if len(args) == 1:
        raise ValueError("No command specified.")

    command = args[1]
    if command == "runserver":
        apps_list: list[str] = settings.APPS

        if len(apps_list) == 0:
            raise ValueError(
                "No apps specified."
                "Please specify apps in settings.APPS."
            )

        for application in apps_list:
            app_module = import_module(f"{os.environ.get('AQUILO_APPS_MODULE')}.{application}.pages")

            for member in getmembers(app_module, isfunction):
                if member[0].startswith("page_"):
                    app.page(member[1])

        app.run()
