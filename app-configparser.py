#!python3
import configparser
parser = configparser.ConfigParser()

parser.read("sim.conf")

print(parser.get("config", "option1"))
print(parser.get("config", "option2"))
print(parser.get("config", "option3"))
