import configparser
import sys

class ConfigParser:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def get(self):
        env_index = sys.argv.index('--env')
        env = sys.argv[env_index + 1]
        return self.config.get(env, 'base_url')
    
