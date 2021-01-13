from core.scripts import Script


# A route view funcion always will recieve app as argument.
# Tip: To use the CM DB, just use app.manager._db
def example_view_func(app):
    return "example route"


# A script should always inherit from Scripts and must have __name__, __frequency__ and run defined
class ExampleScript(Script):
    __name__ = "example_pluging"
    __frequency__= "1" # frequency in minimum hours
    
    def run(self):
        # run don't accept any arguments but self
        print("running")
