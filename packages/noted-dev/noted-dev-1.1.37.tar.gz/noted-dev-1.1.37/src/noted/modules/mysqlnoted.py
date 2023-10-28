import os
import yaml
import time
import pandas as pd
import mysql.connector
from datetime import datetime
from modules.tools import * # Tools functions

conn = mysql.connector.connect(
  host     = 'dbod-dbod-noted.cern.ch',
  port     = '5509',
  user     = 'script_w',
  password = 'spectrum-noted',
  database = 'noted'
)

# "{spectrum_start.strftime('%Y-%m-%d %H:%M:%S')}", 

def generate_noted_mysql_insert_query(alarmn_name, noted_start, noted_version, description):
  """Function to generate the MySQL query to export a NOTED alarm to MONIT Grafana.

  Args:
      alarmn_name (str): name of the NOTED alarm.
      noted_start (datetime): start of the NOTED alarm.
      noted_version (str): LHCOPN/LHCONE NOTED version.
      description (str): NOTED description.
  """
  return f"""
      INSERT INTO noted_alarms(alarm_name, noted_start, noted_version, description) 
      VALUES (
          "{alarmn_name}", 
          "{noted_start.strftime('%Y-%m-%d %H:%M:%S')}", 
          "{noted_version}",
          "{description}")
  """

def generate_noted_mysql_update_query(column_name, data, id):
  """Function to generate the MySQL query to export a NOTED alarm to MONIT Grafana.

  Args:
      column_name (str): name of the column to update.
      data (str): data to update field in MySQL.
      id (int): alarm ID as defined in MySQL row.
  """
  return f"""
      UPDATE noted_alarms 
      SET {column_name} = "{data}"
      WHERE alarm_id = {id}   
  """

def generate_noted_mysql_get_query(column_name, id):
  """Function to generate the MySQL query to get a NOTED alarm from MONIT Grafana.

  Args:
      column_name (str): name of the column to get.
      id (int): alarm ID as defined in MySQL row.
  """
  return f"""
    SELECT {column_name}
    FROM noted_alarms
    WHERE alarm_id = {id}
  """

def noted_mysql_entry_alarm(alarmn_name, noted_start, noted_version, description):
  """Function to enter a new entry alarm in MONIT Grafana.

  Args:
      alarmn_name (str): name of the NOTED alarm.
      noted_start (datetime): start of the NOTED alarm.
      noted_version (str): LHCOPN/LHCONE NOTED version.
      description (str): NOTED description.

  Returns:
      int: alarm ID in MONIT Grafana.
  """
  query_noted_alarms = generate_noted_mysql_insert_query(alarmn_name, noted_start, noted_version, description)
  conn.reconnect()
  cursor = conn.cursor()
  cursor.execute(query_noted_alarms)
  conn.commit()
  return cursor.lastrowid

def noted_mysql_update_alarm(column_name, data, id):
  """Function to enter a new entry alarm in MONIT Grafana.

  Args:
      column_name (str): name of the column to update.
      data (str): data to update field in MySQL.
      id (int): alarm ID as defined in MySQL row.
  """
  query_noted_alarms = generate_noted_mysql_update_query(column_name, data, id)
  cursor = conn.cursor()
  cursor.execute(query_noted_alarms)
  conn.commit()

def noted_mysql_get_alarm(column_name, id):
  """Function to get an alarm from MONIT Grafana.

  Args:
      column_name (str): name of the column to get.
      id (int): alarm ID as defined in MySQL row.
  """
  query_noted_alarms = generate_noted_mysql_get_query(column_name, id)
  cursor = conn.cursor(buffered = True)
  cursor.execute(query_noted_alarms)
  conn.commit()
  df_data = pd.DataFrame(cursor.fetchall(), columns = ['sense_status'])
  return df_data

def export_noted_alarm_to_monit(params, alarm_info):
    """Function to export the NOTED alarms to MONIT Grafana.

    Args:
        params (configparser): parameters file.
        alarm_info (str): alarm information.
    """
    print('\tExported alarm from NOTED to MONIT.')
    # datetime.now().replace(microsecond = 0) - timedelta(hours = 2) # Needed for my personal laptop but not for VMs
    config = load_yaml_file(''.join([os.getcwd(), '/', params.get('FILENAME PARAMETERS', 'filename_config_spectrum')]))
    alarm_id = noted_mysql_entry_alarm(config['source'][0] + ' to ' + config['destination'][0], datetime.now().replace(microsecond = 0), alarm_info.split('_')[4], 'Spectrum generated an alarm: NOTED is inspecting FTS.')
    noted_mysql_update_alarm('alarm_start', datetime.fromtimestamp(int(alarm_info.split('_')[0])).strftime('%Y-%m-%d %H:%M:%S'), alarm_id)
    noted_mysql_update_alarm('interface', alarm_info.split('_')[2] + '_' + alarm_info.split('_')[3], alarm_id) 
    config['alarm_id'] = alarm_id
    config['alarm_timestamp'] = alarm_info.split('_')[0]
    with open(''.join([os.getcwd(), '/', params.get('FILENAME PARAMETERS', 'filename_config_spectrum')]), 'w') as f: yaml.dump(config, f, default_flow_style = None) # Write config spectrum file
    cmd = os.popen('python3 ' + ''.join([os.getcwd(), '/noted/src/noted/main.py ' + params.get('FILENAME PARAMETERS', 'filename_config_spectrum')]) + ' &')
    time.sleep(10) # Wait 10 sec
