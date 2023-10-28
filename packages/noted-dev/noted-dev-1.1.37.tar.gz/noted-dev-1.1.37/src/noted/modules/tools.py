# © Copyright 2022 CERN. This software is distributed under the terms of
# the GNU General Public Licence version 3 (GPL Version 3), copied verbatim
# in the file "LICENCE.txt". In applying this licence, CERN does not waive
# the privileges and immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.

import os
import yaml
import logging
import configparser
from datetime import datetime
from argparse import ArgumentParser
from modules.tier    import Tier                  # Tier class
from modules.country import Country               # Country class
from modules.federation   import Federation       # Federation class
from modules.countrycode  import CountryCode      # CountryCode class
from modules.officialsite import OfficialSite     # OfficialSite class
from modules.experimentsite import ExperimentSite # ExperimentSite class

def load_yaml_file(filename):
    """Function to load a yaml file.

    Args:
        filename (str): name of the yaml file.

    Returns:
        dict: data in a dictionary structure.
    """
    logging.debug('Loading YAML file: %s' % filename.split('/')[2])
    with open(filename) as file:
        return yaml.load(file, Loader = yaml.FullLoader)

def parser_params_ini_file():
    """Function to parser params.ini file.

    Args:

    Returns: configparser: pointing to params.ini file
    """
    params = configparser.ConfigParser(interpolation = configparser.ExtendedInterpolation())
    params.read(''.join([os.getcwd(), '/noted/src/noted/params/params.ini']))
    return params

def parser_argument_command_line():
    """Function to parser the parameters of NOTED entered through the console.

    Args:

    Returns: ArgumentParser: pointing to the parameters of NOTED entered through the console.
    """
    args_parser = ArgumentParser(description = 'NOTED: a framework to optimise network traffic via the analysis of data from File Transfer Services.')
    args_parser.add_argument('config_file', help = 'name of the configuration file [config-example.yaml]')
    args_parser.add_argument('-v', '--verbosity', help = 'define the logging level [debug, info, warning]')
    return args_parser.parse_args()

def parser_attributes(data, classname):
    """Function to parser the attributes of NOTED configuration file.

    Args:
        data (list): data to parser based on the class (Enum).
        classname (class): name of the class (Enum) to parser the data.
    """
    values = [member.value for member in classname]
    if all(item in values for item in data): return
    else:
        print('\nWARNING: The configuration file of NOTED has an error in %s.\n' %data)
        logging.warning('WARNING: The configuration file of NOTED has an error in %s.' %data)
        exit()

def parser_config_file_attributes(data, classname):
    """Function to parser attributes of TransferBroker class.

    Args:
        data (list): list with data from yaml configuration file.
        classname (class): name of the class (Enum) to parser the data.
    """
    if 'tier' in classname: parser_attributes(data, Tier)
    elif 'federation'   in classname: parser_attributes(data, Federation)
    elif 'country_code' in classname: parser_attributes(data, CountryCode)
    elif 'country'      in classname: parser_attributes(data, Country) # Note: check country_code before country
    elif 'official_site'   in classname: parser_attributes(data, OfficialSite)
    elif 'experiment_site' in classname: parser_attributes(data, ExperimentSite)

def create_log_file(params, args, timestamp):
    """Function to create a log file based on the severity enter by the user.

    Args: args (ArgumentParser): points to the parameters of NOTED entered through the console.
    """
    logging.basicConfig(level = logging.NOTSET, filename = ''.join([os.getcwd(), '/', params.get('FILENAME PARAMETERS', 'filename_transfer_broker') + '_' + timestamp + '.log']), filemode = 'w', format = '%(asctime)s %(name)s - %(levelname)s - %(threadName)s: %(message)s')
    logging.getLogger('numexpr.utils').setLevel(logging.WARNING) # Hide logging messages from numexpr.utils module
    # Set verbosity level
    if args.verbosity is not None:
        if   'debug'   in args.verbosity: logging.getLogger().setLevel(logging.DEBUG)
        elif 'info'    in args.verbosity: logging.getLogger().setLevel(logging.INFO)
        elif 'warning' in args.verbosity: logging.getLogger().setLevel(logging.WARNING)
    logging.debug('Creating logging file: %s' % (params.get('FILENAME PARAMETERS', 'filename_transfer_broker') + '_' + timestamp + '.log').split('/')[2])

def append_data_to_log_file(filename, class_fts_optimizer_):
    """Function to append data to a log file.

    Args:
        filename (str): name of the file to append data.
    """
    logging.debug('Transfer broker: append data to log file %s.' % filename)
    with open(filename + '.txt', 'a+') as f: f.write('timestamp: ' + str(class_fts_optimizer_.get_timestamp()) + ', datetime: ' + str(datetime.now()) + ', data_gigabytes [GB]: ' + str(class_fts_optimizer_.get_data_gigabytes()) + ', throughput_gigabits [Gb/s]: ' + str(class_fts_optimizer_.get_throughput_gigabits()) + ', parallel_transfers: ' + str(class_fts_optimizer_.get_parallel_transfers()) + ', queued_transfers: ' + str(class_fts_optimizer_.get_queued_transfers()) + '\n')

def save_data_to_log_file(params, timestamp, thread_name, class_fts_optimizer_):
    """
    Function to save data to a log file.

    Args:
        params (configparser): parameters file.
        data (str): data to save into a log file.
    """
    if 'source' in thread_name: filename = params.get('FILENAME PARAMETERS', 'filename_transfers_src')
    else: filename = params.get('FILENAME PARAMETERS', 'filename_transfers_dst')
    append_data_to_log_file(filename + '_' + timestamp, class_fts_optimizer_)

def generate_noted_config_file(params, type, list_federation):
    """Function to generate the config file to automatically launch NOTED based on that.

    Args:
        params (configparser): parameters file.
        type (str): type of the alarm {IN, OUT}.
        list_federation (list): source or destination federation that the alarm belongs to.
    """
    config = load_yaml_file(''.join([os.getcwd(), '/', params.get('FILENAME PARAMETERS', 'filename_config_spectrum')]))
    if 'IN' in type: 
        config['source'] = list_federation
        config['destination'] = ['CH-CERN']
    else: 
        config['source'] = ['CH-CERN']
        config['destination'] = list_federation
    with open(''.join([os.getcwd(), '/', params.get('FILENAME PARAMETERS', 'filename_config_spectrum')]), 'w') as f: yaml.dump(config, f, default_flow_style = None) # Write config spectrum file
