from core.scripts import Script


# A script should always inherit from Scripts and must have __name__, __frequency__ and run defined
class ExampleScript(Script):
    __name__ = "example_pluging"
    __frequency__= "1" # frequency in minimum hours
    
    def run(self):
        # run don't accept any arguments but self
        print("running")

class Plugin(object):
    SCRIPTS = [ExampleScript]

    def __init__(self):
        pass

    def activate(self, app):
        # Activate function will create flask routes
        # Tip: To use the CM DB, just use app.manager._db

        @app.route("/new_route")
        def route_a():
             return "example route"       

    def run_scripts(self):
        for script in self.SCRIPTS:
            script().run()

