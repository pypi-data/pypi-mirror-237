import json

from IPython.display import display

from .manager import WidgetsManager


class App:
    def __init__(
        self,
        title="",
        description="",
        show_code=False,
        show_prompt=False,
        output="app",
        schedule="",
        notify={},
        continuous_update=True,
        static_notebook=False,
        show_sidebar=True,
        full_screen=True,
        allow_download=True,
        stop_on_error=False,
    ):
        self.code_uid = WidgetsManager.get_code_uid("App")
        self.title = title
        self.description = description
        self.show_code = show_code
        self.show_prompt = show_prompt
        self.output = output
        self.schedule = schedule
        self.notify = notify
        self.continuous_update = continuous_update
        self.static_notebook = static_notebook
        self.show_sidebar = show_sidebar
        self.full_screen = full_screen
        self.allow_download = allow_download
        self.stop_on_error = stop_on_error
        display(self)

    def __repr__(self):
        return f"mercury.App"

    def _repr_mimebundle_(self, **kwargs):
        data = {}
        data["text/plain"] = repr(self)
        data[
            "text/html"
        ] = "<h3>Mercury Application</h3><small>This output won't appear in the web app.</small>"
        view = {
            "widget": "App",
            "title": self.title,
            "description": self.description,
            "show_code": self.show_code,
            "show_prompt": self.show_prompt,
            "output": self.output,
            "schedule": self.schedule,
            "notify": json.dumps(self.notify),
            "continuous_update": self.continuous_update,
            "static_notebook": self.static_notebook,
            "show_sidebar": self.show_sidebar,
            "full_screen": self.full_screen,
            "allow_download": self.allow_download,
            "stop_on_error": self.stop_on_error,
            "model_id": "mercury-app",
            "code_uid": self.code_uid,
        }
        data["application/mercury+json"] = json.dumps(view, indent=4)
        return data
