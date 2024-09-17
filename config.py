import configparser
import os.path

from loguru import logger


def create_config():
    config = configparser.ConfigParser()

    config['General'] = {'log_level': 'info',
                         'cups_printer_name': 'Office',
                         'file_read_delay': '1'
                         }

    config['Database'] = {'db_path': './',
                          'db_file': 'messages.db',
                          'db_table': 'messages'
                          }

    config['Messages'] = {'msgs_path': 'pager_msgs'}

    config['PDF'] = {'left_margin': '10',
                     'right_margin': '20',
                     'top_margin': '2',
                     'bottom_margin': '9.75'

    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    logger.info("Config file created.")


def read_config():
    config = configparser.ConfigParser()

    if not os.path.isfile('config.ini'):
        create_config()

    config.read('config.ini')

    log_level = config.get('General', 'log_level')
    cups_printer_name = config.get('General', 'cups_printer_name')
    file_read_delay = config.getint('General', 'file_read_delay')
    db_path = config.get('Database', 'db_path')
    db_file = config.get('Database', 'db_file')
    db_table = config.get('Database', 'db_table')
    msgs_path = config.get('Messages', 'msgs_path')
    left_margin = config.getfloat('PDF', "left_margin")
    right_margin = config.getfloat('PDF', "right_margin")
    top_margin = config.getfloat('PDF', "top_margin")
    bottom_margin = config.getfloat('PDF', "bottom_margin")

    config_values = {
        'log_level': log_level,
        'cups_printer_name': cups_printer_name,
        'file_read_delay': file_read_delay,
        'db_path': db_path,
        'db_file': db_file,
        'db_table': db_table,
        'msgs_path': msgs_path,
        'left_margin': left_margin,
        'right_margin': right_margin,
        'top_margin': top_margin,
        'bottom_margin': bottom_margin
    }

    return config_values


