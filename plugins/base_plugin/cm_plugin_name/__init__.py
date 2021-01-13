from plugin import example_view_func, ExampleScript

# A list of routes using from flask add_url_rule syntax
# https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.add_url_rule
# A rule always starts with '/'
routes = [
    {"rule": "/example", "view_func": example_view_func},
]

# A list of script to run with the plugin
scripts = [
        ExampleScript
]

