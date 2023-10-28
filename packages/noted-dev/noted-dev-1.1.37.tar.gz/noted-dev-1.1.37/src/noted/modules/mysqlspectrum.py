# © Copyright 2022 CERN. This software is distributed under the terms of
# the GNU General Public Licence version 3 (GPL Version 3), copied verbatim
# in the file 'LICENCE.txt'. In applying this licence, CERN does not waive
# the privileges and immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.

import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
  host     = 'dbod-netstat.cern.ch',
  port     = '5509',
  user     = 'spectrum_noted',
  password = 'spectrum_noted',
  database = 'monitoring'
)

# Columns of spectrum alarms: start_unix, end_unix, pcause_title, alarm name, address, mname, pcause_txt, mh, mtype, mclass, aid, severity, impact, pcause_id, ticket_id, start_date, end_date, ackd, landscape, occurences, status
# Show colums: SHOW COLUMNS FROM spectrum_alarms;

query_spectrum_alarms = """
    SELECT 
        start_unix, 
        end_unix,
        pcause_title, # alarm name
        mname,        # interface name uses slashes not underscores
        address,
        severity,
        ticket_id
    FROM 
        spectrum_alarms 
    WHERE 
        pcause_title = 'OUT LOAD THRESHOLD EXCEEDED' OR
        pcause_title = 'IN LOAD THRESHOLD EXCEEDED' 
    ORDER BY 
        start_unix DESC
    LIMIT 1000
"""

query_service_name = """
    SHOW OPEN TABLES;
"""

def get_spectrum_alarms():
    """Function to query netstat database to get the Spectrum alarms.

    Args:

    Returns:
        dataframe: spectrum alarms in a dataframe structure.
    """
    cursor = conn.cursor(buffered = True)
    cursor.execute(query_spectrum_alarms)
    conn.commit()
    df_data = pd.DataFrame(cursor.fetchall(), columns = ['Start', 'End', 'Alarm', 'Device', 'IP', 'Severity', 'Ticket_id'])
    df_data[['Device', 'Interface']] = df_data['Device'].str.split('_', expand = True)
    return df_data

def filter_spectrum_alarms(list_routers, df_data):
    """Function to filter the spectrum alarms by routers and irb interfaces.

    Args:
        list_routers (list): list of the routers.
        df_data (dataframe): spectrum alarms in a dataframe structure.
    
    Returns:
        dataframe: spectrum alarms in a dataframe structure filtered by list_routers.
    """
    df_query = df_data.query('Device in @list_routers & Interface.str.contains("irb")', engine = 'python').drop_duplicates(subset = ['Interface'], keep = 'first').reset_index(drop = True)
    return df_query.query('End.isna()', engine = 'python').drop_duplicates(subset = ['Interface'], keep = 'first').reset_index(drop = True)
