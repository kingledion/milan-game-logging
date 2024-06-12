from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

stream = open("../23-24/seriea-1-bologna.yaml", "r")
f = load(stream, Loader=Loader)

print(stream)