# CM with plugins enabled

## Setting the environment

### Dockerzied enviroment
To make things easier, was created a single docker-compose running all that is necessary to run CM.
To use this env:

```bash
git clone https://github.com/arielmorelli/dev_env_for_circulation dev_env_for_circulation
cd dev_env_for_circulation/circulation
docker-compose up
```

### Clone Circulation Manager with plugin enabled.
Once I'm doing POCs, this forked repository must be used: https://github.com/arielmorelli/circulation in the branch `add_plugin_support`. Create a virtualenv and add all dependencies.

```bash
git clone https://github.com/arielmorelli/circulation circulation-plugin
cd circulation-plugin
git checkout add_plugin_support
git submodule init
git submodule update
virtualenv env
source env/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Add new plugins

Note: To install plugins it is necessary that they are on a pypi server. Every script should document how to upload to a pypi server. Some examples:
* [cm_plugin_hello](https://github.com/arielmorelli/cm_plugin_hello)
* [cm_plugin_list_libraries](https://github.com/arielmorelli/cm_plugin_list_libraries)


To install plugin you must know the name of the plugin package and run with CM python virtualenv activated:
```
pip install -U --index-url http://localhost:44444/simple/ cm-plugin-hello
```

## Running CM plugins

* To run the CM API, set some envvar and run with virtualenv activated:
```
export SIMPLIFIED_PRODUCTION_DATABASE="postgres://simplified:test@localhost:5432/simplified_circ_db"
export SIMPLIFIED_TEST_DATABASE="postgres://simplified:test@localhost:5433/simplified_circ_db"
export SIMPLIFIED_TEST_ELASTICSEARCH="http://localhost:9200"
export SIMPLIFIED_DB_TASK="ignore"
python app.py
```
* To run plugin script, run with virtualenv activated:
```
./bin/run_plugins_script
```

