# Base for plugins

This is just a base for a plugin, containing the minium a plugin must have.

# Plugin changes
## Routes
Describre which routes are added with this plugin
* "/hello_world" print a hello world

## Scripts
Describre what script will run with this plugin
* HelloWorld: print a hello_world in the log everytime it runs

# Upload to a PyPI server

To upload a package twine is used.
`pip install twine`

1. Build the package
`python setup.py sdist bdist_wheel`

2. Upload to a PyPI server
`twine upload --repository-url <pypi_server_name> dist/*`

Note: To use a local pypi server, please follow [this tutorial](https://github.com/arielmorelli/dev_env_for_circulation/tree/main/plugins)

# Installing the plugin

Please use `pip install -U --index-url <pypi_server_name> cm-plugin-name`

# Running tests

Once the plugin needs the server_core packages to run, it's necessary to have it under the core folder.
To to this, clone the server_core:
`git clone https://github.com/arielmorelli/server_core core`

To run tests, just run `nosetests tests/` (don't forget to activate the virtualenv activated and install all requirements packages)

