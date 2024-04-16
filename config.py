import configparser

config_parser = configparser.ConfigParser()
config_parser.read("config.ini")

TOKEN = config_parser["VK"]["Token"]
