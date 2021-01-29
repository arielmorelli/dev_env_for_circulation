from core.scripts import Script


class ExampleScript(Script):
    """ A script should always inherit from Scripts to have acess
    to DB with self._db variable.
    """ 
    def run(self):
        print("running")


class Plugin(object):
    """ A Plugin is defined as a class that define activate and run_scripts
    functions.

    Attributes:
    FREQUENCY (int, optional): integer represing minimum hours to execute.
    SCRIPTS (list): List of scripts to run in the backend of CM.
    FIELDS (list): List of fields to add in the admin interface of CM.
    """

    FREQUENCY = None
    SCRIPTS = [ExampleScript]
    FIELDS = [{
        "key": "example-field",
        "label": "just a example",
        "description": "Example of required field",
        "type": "input",
        "required": True,
        "default": "example",
    }]

    def __init__(self):
        pass

    def activate(self, app):
        """ Activate function is used to create flask routes. As best practices
        routes will be defined with decorators.
        Tip: To use the CM DB, just use app.manager._db

        param: app: a flask app instance
        """

        @app.route("/new_route")
        def route_a():
             return "example route"       

    def run_scripts(self, plugin_name): # this argument will be passed by CM
        """ Run scripts is supose to run all expected scripts.
        param: plugin_name: a string with the plugin name
        . """
        for script in self.SCRIPTS:
            script().run()
