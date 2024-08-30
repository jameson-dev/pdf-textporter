import configparser
import time

from loguru import logger


def create_config():
    config = configparser.ConfigParser()

    config['General'] = {'log_level': 'info',
                         'sumatra_path': r'D:\Program Files\SumatraPDF'
                         }

    config['Database'] = {'db_path': './',
                          'db_file': 'messages.db',
                          'db_table': 'messages'
                          }

    config['Messages'] = {'msgs_path': 'pager_msgs'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    logger.info("Config file created.")


def read_config():
    config = configparser.ConfigParser()

    config.read('config.ini')

    log_level = config.get('General', 'log_level')
    sumatra_path = config.get('General', 'sumatra_path')
    db_path = config.get('Database', 'db_path')
    db_file = config.get('Database', 'db_file')
    db_table = config.get('Database', 'db_table')
    msgs_path = config.get('Messages', 'msgs_path')

    config_values = {
        'log_level': log_level,
        'sumatra_path': sumatra_path,
        'db_path': db_path,
        'db_file': db_file,
        'db_table': db_table,
        'msgs_path': msgs_path
    }

    return config_values


