# Run a script

To run a script, first start the docker container by running `docker-compose up -d`.

Then run whatever command you need in python container:

```
docker-compose run --rm python bash -c "your command" 
```

For example:

```
docker-compose run --rm python bash -c "python demo.py" 
```

If you want to log into your python container and work as usual, then simply do this:

```
docker-compose run --rm python bash
pip install -r requirements.txt
python demo.py
```

# Shut down the environment

To shut down database and python container just run `docker-compose down`

# Drop database

As simple as removing `.posgresql` folder.