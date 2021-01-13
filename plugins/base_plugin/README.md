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
To upload a plugin to a PyPI server, first must configure the `~/.pypirc` file. Should looks like:
```bash
[distutils]
index-servers =
  pypi
  local_pypi

[pypi]
repository=https://pypi.python.org/pypi
username= # username
password= # password

[<pypi_server_name>]
repository: <pypi_server_url>
username= # if no username is required, leave with anything but blank
password = # if no password is required, leave with anything but blank
```

To upload, just run:
`python setup.py sdist upload -r <pypi_server_name>`

Note: it's legacy, but works fine for now! Updating to twine if once get stable


## Appendix
To create a local PyPI serve can be created using docker just run:
`docker run -p 44444:8080 pypiserver/pypiserver:latest -P . -a . -v`
(it wo

[Documentation](https://hub.docker.com/r/pypiserver/pypiserve).


