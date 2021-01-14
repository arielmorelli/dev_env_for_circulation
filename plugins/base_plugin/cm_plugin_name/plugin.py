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
    """
    __name__ = "example_pluging"
    __frequency__= "1" # not defined yet how it will woks

    SCRIPTS = [ExampleScript]

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

    def run_scripts(self):
        """ Run scripts is supose to run all expected scripts.
        run_scripts doesn't expect any argument but self. """
        for script in self.SCRIPTS:
            script().run()

