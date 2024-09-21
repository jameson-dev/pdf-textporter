import configparser
import os.path

from loguru import logger


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.config_file_path = os.path.join(parent_dir, 'config.ini')

        self.load_config()

    def check_config(self):

        logger.info(f"Checking for config at: {self.config_file_path}")

        if not os.path.exists(self.config_file_path):
            self.create_config()
        else:
            logger.info("Configuration file found.")

    def create_config(self):
        config = configparser.ConfigParser()

        config['General'] = {'log_level': 'info',
                             'cups_printer_name': 'Office',
                             'file_read_delay': '1'
                             }

        config['Database'] = {'db_path': '..\\',
                              'db_file': 'messages.db',
                              'db_table': 'messages'
                              }

        config['Messages'] = {'msgs_path': '..\\pager_msgs'}

        config['PDF'] = {'left_margin': '10',
                         'right_margin': '20',
                         'top_margin': '2',
                         'bottom_margin': '9.75'
                         }

        with open(self.config_file_path, 'w') as configfile:
            config.write(configfile)

        logger.info(f"Config file created at {self.config_file_path}")

    def load_config(self):

        self.config = configparser.ConfigParser()

        self.config.read(self.config_file_path)

    def get(self, section, option):
        return self.config.get(section, option)

    def getint(self, section, option):
        return self.config.getint(section, option)

    def getfloat(self, section, option):
        return self.config.getfloat(section, option)
