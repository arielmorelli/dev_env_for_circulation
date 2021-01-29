# dev_env_for_circulation

My custom docker-compose enviroment to run the [NYPL Simplified Circulation](https://github.com/NYPL-Simplified/circulation).

To run the env just run: `docker-compose up`
It will up:
* Postgres for dev
* Postgres for tests
* Minio
* Elasticsearch
* PyPI server



To set the my development enviroment I replace the submodules for the real cloned repository, so I can garantee my changes will work without sync every time.
My workdir looks like:
```
.
├── circulation     -> https://github.com/NYPL-Simplified/circulation
│   ├── core        -> https://github.com/NYPL-Simplified/server_core
└── circulation-web ->https://github.com/NYPL-Simplified/circulation-web
```


Instead of init the git submodules, we're cloning the repositories and adding simbolic links, when necessary.
This script will create all necessary folders:
```bash
git clone https://github.com/arielmorelli/dev_env_for_circulation dev_env_for_circulation
git clone https://github.com/NYPL-Simplified/circulation circulation
git clone https://github.com/NYPL-Simplified/circulation-web circulation-web
cd circulation-web
npm install
npm link
cd ../circulation/api/admin
npm link simplified-circulation-web
cd ../..
git clone https://github.com/NYPL-Simplified/server_core core
echo "core/" >> .git/info/exclude
virtualenv env
source env/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Running CM
1. Run the docker-compose to start all needed thins like DB and elastic search.
```bash
cd dev_env_for_circulation/circulation
docker-compose up
```
2. Runing the circulation manager API
```bash
cd circulation
source env/bin/activate
python app.py
```
