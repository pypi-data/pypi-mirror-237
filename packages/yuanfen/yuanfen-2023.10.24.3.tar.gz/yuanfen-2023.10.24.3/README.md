# Yuanfen Python Library

## build && upload

```bash
$ python3 setup.py sdist bdist_wheel
$ python3 -m twine upload dist/*
```

## utils.config

Support .json, .yaml, .ini files.
Support auto reloading while config file changes.

```python
config_json = Config(os.path.abspath("config.json"))
config_yaml = Config(os.path.abspath("config.yaml"))
config_ini = Config(os.path.abspath("config.ini"))

print(config_ini["app"]["config_a"])
print(config_yaml["movie"]["name"])
```

## utils.logger

Stream and TimedRotatingFile handlers for logging.

```python
logger = Logger(name="my-logger", level=logging.INFO)

logger.debug("debug log")
logger.info("info log")
logger.warn("warn log")
logger.error("error log")
```