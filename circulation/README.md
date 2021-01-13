# dev_env_for_circulation

My custom docker-compose enviroment to run the [NYPL Simplified Circulation](https://github.com/NYPL-Simplified/circulation).

To run the env just run: `docker-compose up`
It will up:
* Postgres for dev
* Postgres for tests
* Minio
* Elasticsearch
* PyPI server

To run the circulation API or scripts, it should run with local machine python in the circulation directory.

