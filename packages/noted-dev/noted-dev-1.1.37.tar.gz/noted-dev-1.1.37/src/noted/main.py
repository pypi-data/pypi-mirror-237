# © Copyright 2022 CERN. This software is distributed under the terms of
# the GNU General Public Licence version 3 (GPL Version 3), copied verbatim
# in the file 'LICENCE.txt'. In applying this licence, CERN does not waive
# the privileges and immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.

# carmen@itcs-wifi-macbook gitlab_workspace % python3 noted/src/noted/main.py noted/src/noted/config/config-all.yaml
# SC23 FNAL Configuration: comment line 92 in query.py

__docformat__ = 'google'

import os
import time
import logging
import threading
import pandas  as pd
from threading import Thread
from modules.query      import *                  # Query functions
from modules.tools      import *                  # Tools functions
from modules.emails     import *                  # Email functions
from modules.mysqlnoted import *                  # MySQL NOTED functions
from modules.mysqlspectrum  import *              # MySQL Spectrum functions
from modules.ftsoptimizer   import FtsOptimizer   # FtsOptimizer class
from modules.transferbroker import TransferBroker # TransferBroker class

pd.set_option('display.width', None)
pd.set_option('expand_frame_repr',   False)
pd.set_option('display.max_columns', None, 'display.max_rows',  None)

class_fts_optimizer_   = FtsOptimizer()
class_transfer_broker_ = TransferBroker()

def set_transfer_broker_attributes(config):
    """Function to set the attributes of TransferBroker class.

    Args:
        config (dict): dictionary with the yaml configuration file.
    """
    class_transfer_broker_.set_list_source(config['source'])
    class_transfer_broker_.set_list_destination(config['destination'])
    class_transfer_broker_.set_from_email_address(config['from_email_address'])
    class_transfer_broker_.set_to_email_address(config['to_email_address'])
    class_transfer_broker_.set_subject_email(config['subject_email'])
    class_transfer_broker_.set_message_email(config['message_email'])
    class_transfer_broker_.set_unidirectional(config['unidirectional_link'])
    class_transfer_broker_.set_events_to_wait(config['events_to_wait_until_notification'])
    class_transfer_broker_.set_max_throughput(config['max_throughput_threshold_link'])
    class_transfer_broker_.set_min_throughput(config['min_throughput_threshold_link'])
    class_transfer_broker_.set_num_circuits(config['number_of_dynamic_circuits'])
    class_transfer_broker_.set_sense_uuid(config['sense_uuid'])
    class_transfer_broker_.set_sense_vlan(config['sense_vlan'])
    class_transfer_broker_.set_sense_uuid_2(config['sense_uuid_2'])
    class_transfer_broker_.set_sense_vlan_2(config['sense_vlan_2'])
    class_transfer_broker_.set_auth_token(config['auth_token'])
    class_transfer_broker_.set_alarm_id(config['alarm_id'])
    class_transfer_broker_.set_alarm_timestamp(float(config['alarm_timestamp'].split('_')[0]))
    logging.info('Source: %s' % config['source'])
    logging.info('Destination: %s' % config['destination'])

def set_fts_optimizer_attributes(df_last_event):
    """Function to set the attributes of FtsOptimizer class.

    Args:
        df_last_event (dataframe): last FTS optimizer event.
    """
    if df_last_event.empty: class_fts_optimizer_.set_zero()
    class_fts_optimizer_.set_timestamp(df_last_event['timestamp'].values[0])
    class_fts_optimizer_.set_data_gigabytes(round(df_last_event['filesize_avg'].values[0]/1e9, 2))      # Amount of data [GB]
    class_fts_optimizer_.set_throughput_gigabits(round(8*df_last_event['throughput'].values[0]/1e9, 2)) # Throughput [Gb/s]
    # class_fts_optimizer_.set_throughput_gigabits(round(10.04, 2)) # @remove. Just for testing pourposes
    class_fts_optimizer_.set_parallel_transfers(df_last_event['active_count'].values[0])      # TCP parallel transfers
    class_fts_optimizer_.set_queued_transfers(df_last_event['submitted_count'].values[0])     # Transfers in the queue

def monitor_queue_before_alert(params, action):
    """Function to monitor FTS queue for X events to check if it is just instantaneous traffic or a huge transfer is going to take place.

    Args:
        params (configparser): parameters file.
        action (str): action to execute, it can take two values {start, stop}.
    """
    logging.warning('Link under supervision: monitor queue before alert.')
    number_of_events = 0
    last_timestamp = ''
    while True:
        inspect_transfers(params)          
        # Count events if there are with different timestamp, i.e. if there are different FTS Optimizer events
        if last_timestamp != str(class_fts_optimizer_.get_timestamp()):
            if number_of_events < class_transfer_broker_.get_events_to_wait(): save_data_to_log_file(params, class_transfer_broker_.get_timestamp(), threading.current_thread().name, class_fts_optimizer_) # If stop save the last events
            if number_of_events < class_transfer_broker_.get_events_to_wait()-1: append_data_to_log_file(params.get('FILENAME PARAMETERS', 'filename_all_transfers') + '_' + class_transfer_broker_.get_timestamp(), class_fts_optimizer_)
            # Interrupt the start/stop sequence because the throughput changed its expected behaviour
            if (class_fts_optimizer_.get_throughput_gigabits() < class_transfer_broker_.get_max_throughput() and action == 'start') or (class_fts_optimizer_.get_throughput_gigabits() > class_transfer_broker_.get_min_throughput() and action == 'stop'): return False
            # Update last timestamp to the new one and count the events
            last_timestamp = str(class_fts_optimizer_.get_timestamp())
            number_of_events = number_of_events + 1
            # Monit Grafana
            noted_mysql_update_alarm('noted_status', 'Decision-making', class_transfer_broker_.get_alarm_id())
            noted_mysql_update_alarm('description', 'An action on the link may be required: number of events: ' + str(number_of_events) + '. Throughput [Gb/s]: ' + str(class_fts_optimizer_.get_throughput_gigabits()), class_transfer_broker_.get_alarm_id()) 
            logging.warning('Link under supervision: monitor queue before alert: action %s, number of events %d' % (action, number_of_events))
            logging.warning('df_last_event: timestamp: %s, throughput [Gb/s]: %s, parallel_transfers: %s, queued_transfers: %s' % (class_fts_optimizer_.get_timestamp(), class_fts_optimizer_.get_throughput_gigabits(), class_fts_optimizer_.get_parallel_transfers(), class_fts_optimizer_.get_queued_transfers()))
            logging.warning('There are %d transfers with a total of %f GB - Throughput: %f Gb/s' % (class_fts_optimizer_.get_parallel_transfers(), class_fts_optimizer_.get_data_gigabytes(), class_fts_optimizer_.get_throughput_gigabits()))
            if number_of_events == class_transfer_broker_.get_events_to_wait(): return True
        time.sleep(60) # FTS OptimizerInterval = 60s

def execute_action_sense_api(params, task, message):
    """Function to provide or cancel a dynamic circuit by using sense-o autogole northbound API.

    Args:
        params (configparser): parameters file.
        task (str): action to be executed in sense-o, it can take two values: {provision, cancel}.
        message (str): message to send in the email notification
    """
    logging.warning('Calling to sense-o API to %s a dynamic circuit.' % task)
    # Provision dynamic circuit with sense-o
    if 'provision' in task:
        cmd = os.popen(str('sh noted/sense-o/sense-provision.sh ' + class_transfer_broker_.get_sense_uuid()   + ' ' + class_transfer_broker_.get_sense_vlan()));
        if class_transfer_broker_.get_num_circuits == 2: cmd = os.popen(str('sh noted/sense-o/sense-provision.sh ' + class_transfer_broker_.get_sense_uuid_2() + ' ' + class_transfer_broker_.get_sense_vlan_2()));
        # Monit Grafana
        noted_mysql_update_alarm('sense_status', 'Provided', class_transfer_broker_.get_alarm_id())
        noted_mysql_update_alarm('sense_start', datetime.now().replace(microsecond = 0), class_transfer_broker_.get_alarm_id())
    # Cancel dynamic circuit with sense-o
    else:
        cmd = os.popen(str('sh noted/sense-o/sense-cancel.sh ' + class_transfer_broker_.get_sense_uuid()   + ' ' + class_transfer_broker_.get_sense_vlan()));
        if class_transfer_broker_.get_num_circuits == 2: cmd = os.popen(str('sh noted/sense-o/sense-cancel.sh ' + class_transfer_broker_.get_sense_uuid_2() + ' ' + class_transfer_broker_.get_sense_vlan_2()));
        # Monit Grafana
        noted_mysql_update_alarm('noted_status', 'Stopped', class_transfer_broker_.get_alarm_id())
        noted_mysql_update_alarm('sense_status', 'Released', class_transfer_broker_.get_alarm_id())
        noted_mysql_update_alarm('noted_end', datetime.now().replace(microsecond = 0), class_transfer_broker_.get_alarm_id())
        noted_mysql_update_alarm('sense_end', datetime.now().replace(microsecond = 0), class_transfer_broker_.get_alarm_id())
        noted_mysql_update_alarm('description', 'The large data transfer is finished.', class_transfer_broker_.get_alarm_id()) 
        df_alarms = get_spectrum_alarms()
        alarm_timestamp = class_transfer_broker_.get_alarm_timestamp()
        df_timestamp = df_alarms.query('Start == @alarm_timestamp', engine = 'python')
        if df_timestamp['End'].notna().any(): noted_mysql_update_alarm('alarm_end', datetime.fromtimestamp(int(df_timestamp['End'])), class_transfer_broker_.get_alarm_id())
        if class_transfer_broker_.get_pid() != '0': cmd = os.popen('kill ' + class_transfer_broker_.get_pid())
    send_email(params, message, class_transfer_broker_, class_fts_optimizer_, threading.current_thread().name)
    
def make_decision_before_alert(params, action, message):
    """Function to make a decision on the link for loooking into the FTS queue before alert.

    Args:
        params (configparser): parameters file.
        action (str): action to be execute on the link, it can take two values: {start, stop}
        message (str): message to send in the email notification
    """
    logging.warning('Link under supervision: make decision before alert: action %s' % action)
    # This is for not Spectrum mode so we need to generate the alarm in MONIT Grafana
    if class_transfer_broker_.get_pid() == '0' and action == 'start':
        logging.warning('Exported alarm from NOTED to MONIT.')
        alarm_id = noted_mysql_entry_alarm(class_transfer_broker_.get_list_source()[0] + ' to ' + class_transfer_broker_.get_list_destination()[0], datetime.now().replace(microsecond = 0), 'CUSTOM', 'NOTED generated an alarm for a custom link.')
        class_transfer_broker_.set_alarm_id(alarm_id)
        class_transfer_broker_.set_alarm_timestamp('0')
    # Look to FTS queue for X events to see if it is just instaneous traffic fluctuations or not, if true send alert email notification
    bool_email = monitor_queue_before_alert(params, action)
    if bool_email:
        # Check the current state of the link. This is used to synchronize TX and RX threads because the start and stop should be send only once
        if not class_transfer_broker_.get_unidirectional():
            # If TX and RX are not congested -> activate dynamic circuit and update state of the link and send an email
            if action == 'start' and not class_transfer_broker_.get_link_src_state() and not class_transfer_broker_.get_link_dst_state():
                logging.warning('Link under supervision: update link state: True')
                if 'source' in threading.current_thread().name: class_transfer_broker_.set_link_src_state(True)
                else: class_transfer_broker_.set_link_dst_state(True)
                execute_action_sense_api(params, 'provision', message)
            # If TX congested but RX not: set only RX and do not send an email
            elif action == 'start' and class_transfer_broker_.get_link_src_state() and not class_transfer_broker_.get_link_dst_state():
                logging.warning('Link under supervision: update dst link state: True')
                class_transfer_broker_.set_link_dst_state(True)
            # If RX congested but TX not: set only TX and do not send an email
            elif action == 'start' and not class_transfer_broker_.get_link_src_state() and class_transfer_broker_.get_link_dst_state():
                logging.warning('Link under supervision: update link state: True')
                class_transfer_broker_.set_link_src_state(True)
            # Stop condition -> TX are RX are congested, not send an email
            elif action == 'stop' and class_transfer_broker_.get_link_src_state() and class_transfer_broker_.get_link_dst_state():
                # Update state of the link
                logging.warning('Link under supervision: update link state: False')
                if 'source' in threading.current_thread().name: class_transfer_broker_.set_link_src_state(False)
                else: class_transfer_broker_.set_link_dst_state(False)
            # If TX is not congested and RX will be not congested -> send email
            elif action == 'stop' and not class_transfer_broker_.get_link_src_state() and class_transfer_broker_.get_link_dst_state():
                logging.warning('Link under supervision: update dst link state: False')
                class_transfer_broker_.set_link_dst_state(False)
                execute_action_sense_api(params, 'cancel', message)
            # If RX is not congested and TX will be not congested -> send email
            elif action == 'stop' and class_transfer_broker_.get_link_src_state() and not class_transfer_broker_.get_link_dst_state():
                logging.warning('Link under supervision: update src link state: False')
                class_transfer_broker_.set_link_src_state(False)
                execute_action_sense_api(params, 'cancel', message)
        # It's an unidirectional link so all the start/stop conditions should be applied to TX
        else:
            if action == 'start':
                execute_action_sense_api(params, 'provision', message)
                class_transfer_broker_.set_link_src_state(True)
            else:
                execute_action_sense_api(params, 'cancel', message)
                class_transfer_broker_.set_link_src_state(False)

def make_decision_link(params):
    """Function to make a decision on the link [start/stop events].

    Args:
        params (configparser): parameters file.
    """
    logging.debug('Inspecting transfers: make decision.')
    # Get current state of the link
    if 'source' in threading.current_thread().name: link_state = class_transfer_broker_.get_link_src_state()
    else: link_state = class_transfer_broker_.get_link_dst_state()
    # If throughput > X Gb/s and the link is not congested send an email because the link will be congested
    if   class_fts_optimizer_.get_throughput_gigabits() > class_transfer_broker_.get_max_throughput() and not link_state: make_decision_before_alert(params, 'start', 'START MESSAGE: there is an on-going large data transfer that could potentially congest the link.')
    # If the link was congested but now the transfers takes throughput < X Gb/s, the link will not be congested anymore
    elif class_fts_optimizer_.get_throughput_gigabits() < class_transfer_broker_.get_min_throughput() and link_state: make_decision_before_alert(params, 'stop', 'STOP MESSAGE: the on-going large data transfer is ending so there is not expecting more congestion on the link.')

def inspect_transfers(params):
    """Function to inspect transfers parameters in FTS.

    Args:
        params (configparser): parameters file.

    Returns:
        dataframe: last event of FTS optimizer.
    """
    logging.debug('Inspecting transfers.')
    df_fts_optimizer_data = query_fts_optimizer(params, class_transfer_broker_.get_auth_token(), threading.current_thread().name)
    # Get list of endpoints [needed to execute the curl command - not remove it]
    list_src_endpoints = class_transfer_broker_.get_list_src_endpoints() # Please do not remove it
    list_dst_endpoints = class_transfer_broker_.get_list_dst_endpoints() # Please do not remove it
    if 'source' in threading.current_thread().name: df_query = df_fts_optimizer_data.query(params.get('QUERY PARAMETERS', 'query_src_site'), engine = 'python').drop_duplicates(subset = ['source_se', 'dest_se'], keep = 'first').reset_index(drop = True)
    else: df_query = df_fts_optimizer_data.query(params.get('QUERY PARAMETERS', 'query_dst_site'), engine = 'python').drop_duplicates(subset = ['source_se', 'dest_se'], keep = 'first').reset_index(drop = True)
    df_query = df_query.query('throughput != 0 & active_count > 0').reset_index(drop = True) # Get latest FTS Optimizer event (first row), i.e. the most recent event generated by FTS Optimizer.
    # The link is 'inactive', i.e. df_query empty -> FTS Optimizer is updated every 5 min because the link is 'inactive'
    if not df_query.empty: 
        df_last_event = pd.DataFrame({'source_se': [df_query['source_se'][0]], 'dest_se': [df_query['dest_se'][0]], 'timestamp': [df_query['timestamp'][0]], 'throughput': [df_query['throughput'].sum()], 'filesize_avg': [df_query['filesize_avg'].sum()], 'active_count': [df_query['active_count'].sum()], 'submitted_count': [df_query['submitted_count'].sum()]})
        set_fts_optimizer_attributes(df_last_event)
    else:
        logging.warning('No transfers found for the given {src, dst} pair.')
        # Monit Grafana
        noted_mysql_update_alarm('description', 'No transfers in FTS. NOTED will run until Spectrum clears the alarm.', class_transfer_broker_.get_alarm_id())
        noted_mysql_update_alarm('noted_status', 'Monitoring', class_transfer_broker_.get_alarm_id())
        # Get spectrum alarms, if it already ended set the end timestamp and kill the process since there are no transfers
        df_alarms = get_spectrum_alarms()
        alarm_timestamp = class_transfer_broker_.get_alarm_timestamp()
        df_timestamp = df_alarms.query('Start == @alarm_timestamp', engine = 'python')
        if df_timestamp['End'].notna().any(): 
            noted_mysql_update_alarm('alarm_end', datetime.fromtimestamp(int(df_timestamp['End'])), class_transfer_broker_.get_alarm_id())
            df_data = noted_mysql_get_alarm('sense_status', class_transfer_broker_.get_alarm_id())
            if df_data['sense_status'][0] == 'Provided': 
                noted_mysql_update_alarm('sense_status', 'Released', class_transfer_broker_.get_alarm_id())
                noted_mysql_update_alarm('sense_end', datetime.now().replace(microsecond = 0), class_transfer_broker_.get_alarm_id())
            noted_mysql_update_alarm('noted_end', datetime.now().replace(microsecond = 0), class_transfer_broker_.get_alarm_id())
            noted_mysql_update_alarm('description', 'No transfers in FTS. The spectrum alarm is cleared.', class_transfer_broker_.get_alarm_id())
            noted_mysql_update_alarm('noted_status', 'Stopped', class_transfer_broker_.get_alarm_id()) # @new added
        if class_transfer_broker_.get_pid() != '0': cmd = os.popen('kill ' + class_transfer_broker_.get_pid())
        # If the link is active and suddenly it goes down
        if 'source' in threading.current_thread().name and class_transfer_broker_.get_link_src_state(): 
            class_transfer_broker_.set_link_src_state(False)
            if not class_transfer_broker_.get_link_dst_state():
                save_data_to_log_file(params, class_transfer_broker_.get_timestamp(), threading.current_thread().name, class_fts_optimizer_)
                execute_action_sense_api(params, 'cancel', 'STOP MESSAGE: the large data transfer is ending.')
        elif class_transfer_broker_.get_link_dst_state(): 
            class_transfer_broker_.set_link_dst_state(False)
            if not class_transfer_broker_.get_link_src_state():
                save_data_to_log_file(params, class_transfer_broker_.get_timestamp(), threading.current_thread().name, class_fts_optimizer_)
                execute_action_sense_api(params, 'cancel', 'STOP MESSAGE: the large data transfer is ending.')
        time.sleep(5*60) # FTS OptimizerSteadyInterval = 300s = 5min
        df_last_event = pd.DataFrame(columns = ['source_se', 'dest_se', 'timestamp', 'throughput', 'filesize_avg', 'active_count', 'submitted_count'])

def monitor_transfers(params):
    """Function to monitor transfers in FTS, this function is used by TX/RX threads.

    Args:
        params (configparser): parameters file.
    """
    logging.info('Monitoring transfers.')
    # Declare variables
    last_timestamp = ''
    while True:
        # Get the metrics of the link
        if class_fts_optimizer_.get_timestamp() == '0': link_state = False
        inspect_transfers(params)
        if class_fts_optimizer_.get_throughput_gigabits() != 0:
            if 'source' in threading.current_thread().name: link_state = class_transfer_broker_.get_link_src_state()
            else: link_state = class_transfer_broker_.get_link_dst_state()
            make_decision_link(params)
            # Append data to a log file for traceability purposes of the events
            if link_state and class_fts_optimizer_.get_timestamp() != last_timestamp: save_data_to_log_file(params, class_transfer_broker_.get_timestamp(), threading.current_thread().name, class_fts_optimizer_)
            if class_fts_optimizer_.get_timestamp() != last_timestamp:
                append_data_to_log_file(params.get('FILENAME PARAMETERS', 'filename_all_transfers') + '_' + class_transfer_broker_.get_timestamp(), class_fts_optimizer_)
                # Monit Grafana
                # Get the maximum FTS throughput achieve during the whole data transfer and export it to MONIT Grafana
                filename = ''.join([os.getcwd(), '/', params.get('FILENAME PARAMETERS', 'filename_transfer_broker') + '_' + class_transfer_broker_.get_timestamp() + '.log'])
                with open(filename, 'r') as f: df_throughput = pd.DataFrame(f.readlines(), columns = ['Data'])
                df_max_throughput = df_throughput.query('Data.str.contains("transfers with a total of")', engine = 'python').reset_index(drop = True)
                df_max_throughput['Data'] = df_max_throughput['Data'].str.split('Throughput:').str[1]
                df_max_throughput['Data'] = round(df_max_throughput['Data'].str.split('Gb/s').str[0].str.strip().astype(float), 2)
                noted_mysql_update_alarm('max_fts_throughput', df_max_throughput['Data'].max(), class_transfer_broker_.get_alarm_id())
                # Two status: action (circuit provided) or monitoring (not provided because throughput < max_throughput)
                df_data = noted_mysql_get_alarm('sense_status', class_transfer_broker_.get_alarm_id())
                if df_data['sense_status'][0] == 'Provided': 
                    noted_mysql_update_alarm('description', 'On-going SDN. FTS throughput [Gb/s]: ' + str(class_fts_optimizer_.get_throughput_gigabits()), class_transfer_broker_.get_alarm_id()) 
                    noted_mysql_update_alarm('noted_status', 'Action', class_transfer_broker_.get_alarm_id())
                else: 
                    noted_mysql_update_alarm('description', 'Monitoring transfers. FTS throughput [Gb/s]: ' + str(class_fts_optimizer_.get_throughput_gigabits()), class_transfer_broker_.get_alarm_id()) 
                    noted_mysql_update_alarm('noted_status', 'Running', class_transfer_broker_.get_alarm_id())
                # Get spectrum end timestamp, if it is already set
                df_alarms = get_spectrum_alarms()
                alarm_timestamp = class_transfer_broker_.get_alarm_timestamp()
                df_timestamp = df_alarms.query('Start == @alarm_timestamp', engine = 'python')
                if df_timestamp['End'].notna().any(): noted_mysql_update_alarm('alarm_end', datetime.fromtimestamp(int(df_timestamp['End'])), class_transfer_broker_.get_alarm_id())
                logging.info('df_last_event: timestamp: %s, throughput [Gb/s]: %s, parallel_transfers: %s, queued_transfers: %s' % (class_fts_optimizer_.get_timestamp(), class_fts_optimizer_.get_throughput_gigabits(), class_fts_optimizer_.get_parallel_transfers(), class_fts_optimizer_.get_queued_transfers()))
                logging.info('There are %d transfers with a total of %f GB - Throughput: %f Gb/s' % (class_fts_optimizer_.get_parallel_transfers(), class_fts_optimizer_.get_data_gigabytes(), class_fts_optimizer_.get_throughput_gigabits()))
                last_timestamp = class_fts_optimizer_.get_timestamp()
            time.sleep(60) # FTS OptimizerInterval = 60s
        # If the link is active and suddenly it goes down
        elif class_fts_optimizer_.get_throughput_gigabits() == 0 and link_state:
            if 'source' in threading.current_thread().name: class_transfer_broker_.set_link_src_state(False)
            else: class_transfer_broker_.set_link_dst_state(False)
            save_data_to_log_file(params, class_transfer_broker_.get_timestamp(), threading.current_thread().name, class_fts_optimizer_)
            execute_action_sense_api(params, 'cancel', 'STOP MESSAGE: the large data transfer is ending.')

def build_thread(params, type):
    """Function to create a thread per link for monitoring the transfers.

    Args:
        params (configparser): parameters file.
        type (str): direction of the link, it can take two values: {tx, rx}.

    Returns:
        thread: pointing to a defined link.
    """
    logging.debug('Building thread %s%s.' % ('transfer_broker_', type))
    transfers = Thread(name = 'transfer_broker_' + type, target = monitor_transfers, args = [params])
    return transfers

def start_threads(transfers_tx, transfers_rx, unidirectional):
    """Function to start thread and monitor the transfers.

    Args:
        transfers_tx (thread): tx thread.
        transfers_rx (thread): rx thread.
    """
    logging.debug('Starting thread %s.' % transfers_tx.name)
    logging.debug('Starting thread %s.' % transfers_rx.name)
    # Start threads
    transfers_tx.start()
    transfers_tx.join()
    if not unidirectional: 
        transfers_rx.start()
        transfers_rx.join()

def main():
    """Main function.
    
    Args:
    """
    # Config parser, argument parser and create logging
    params = parser_params_ini_file()
    args   = parser_argument_command_line()
    create_log_file(params, args, class_transfer_broker_.get_timestamp())
    # Load yaml config file, parser config file and set attributes of TransBroker class
    config = load_yaml_file(args.config_file)
    parser_config_file_attributes(config['source'], config['get_by'][0])
    parser_config_file_attributes(config['destination'], config['get_by'][1])
    set_transfer_broker_attributes(config)
    class_fts_optimizer_.set_zero()
    # If Spectrum mode get PID and update state in MONIT Grafana
    if 'spectrum' in args.config_file: 
        noted_mysql_update_alarm('noted_status', 'Running', class_transfer_broker_.get_alarm_id())
        class_transfer_broker_.set_pid(os.popen('ps aux --sort -pid | grep main.py').readlines()[2].split()[1]) # If Spectrum mode get PID to kill NOTED if there are no transfers
        logging.debug('PID %s. Datetime: %s' % (os.popen('ps aux --sort -pid | grep main.py').readlines()[2].split()[1], datetime.now()))
    # Query CRIC database and generate queries
    df_cric_database   = query_cric_database(params, class_transfer_broker_.get_auth_token())
    list_src_endpoints = generate_query_fts_optimizer(config, params, 'source', df_cric_database, config['get_by'][0])
    list_dst_endpoints = generate_query_fts_optimizer(config, params, 'destination', df_cric_database, config['get_by'][1])
    # Set list of endpoint attributes of TransBroker class
    class_transfer_broker_.set_list_src_endpoints(list_src_endpoints)
    class_transfer_broker_.set_list_dst_endpoints(list_dst_endpoints)
    # Build threads
    transfers_tx = build_thread(params, 'source_' + class_transfer_broker_.get_timestamp())
    transfers_rx = build_thread(params, 'destination_' + class_transfer_broker_.get_timestamp())
    # Start threads
    start_threads(transfers_tx, transfers_rx, class_transfer_broker_.get_unidirectional())

if __name__ == '__main__':
    main()
