# © Copyright 2022 CERN. This software is distributed under the terms of
# the GNU General Public Licence version 3 (GPL Version 3), copied verbatim
# in the file "LICENCE.txt". In applying this licence, CERN does not waive
# the privileges and immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.

import os
import json
import logging
import pandas as pd

def query_monit_events(cmd):
    """Function to query MONIT to get events by using the curl command.

    Args:
        cmd (str): curl command to execute.

    Returns:
        dataframe: MONIT events in a dataframe structure.
    """
    try:
        response = json.loads(os.popen(cmd).read())['responses']
        df_hits  = pd.DataFrame(pd.DataFrame(response)['hits'][0]['hits'])
        df_items = pd.DataFrame(df_hits['_source'].values.tolist())
        df_data  = pd.DataFrame(df_items['data'].values.tolist())
    except (KeyError, ValueError): df_data = pd.DataFrame() # Return an empty dataframe because there are none MONIT Events
    return df_data

def query_cric_database(params, auth_token):
    """Query CRIC database.

    Args:
        params (configparser): parameters file.
        auth_token (str): authentication token.

    Returns:
        dataframe: CRIC database information in a dataframe structure.
    """
    logging.debug('Querying CRIC database.')
    with open(params.get('FILENAME PARAMETERS', 'filename_cric_query'), 'w') as f: f.write(params.get('CRIC PARAMETERS', 'query_1st_line') + '\n' + params.get('CRIC PARAMETERS', 'query_2nd_line_1') + params.get('CRIC PARAMETERS', 'query_2nd_line_3') + '\n')
    cmd = 'curl -s -X POST "' + params.get('FTS PARAMETERS', 'url_fts_raw_queue') + '" -H "Authorization: Bearer ' + auth_token + '" -H "Content-Type: application/json" --data-binary "@' + params.get('FILENAME PARAMETERS', 'filename_cric_query') + '"'
    df_data = query_monit_events(cmd)
    if df_data.empty: return pd.DataFrame(columns = ['status', 'experiment_site', 'endpoint', 'flavour', 'federation', 'official_site', 'country', 'institute_name', 'is_monitored', 'vo', 'state', 'country_code', 'in_report', 'tier', 'hostname', 'description']) # Return an empty dataframe because there are none CRIC items
    df_query = df_data.query('endpoint != "UNKNOWN"', engine = 'python').reset_index(drop = True)    # Discard UNKNOWN endpoints
    df_query = df_query.query('netroutes.str.len() > 0', engine = 'python').reset_index(drop = True) # Discard UNKNOWN network routes 
    df_query['tier']      = df_query['tier'].astype(str)
    df_query['endpoint']  = df_query['endpoint'].replace({r':\d+': ''}, regex = True)
    df_query['netroutes'] = df_query['netroutes']
    df_query = df_query.drop_duplicates(subset = ['endpoint'])
    logging.info('There are %d endpoints defined in CRIC database' % df_query.shape[0])
    return df_query[['endpoint', 'experiment_site', 'official_site', 'federation', 'country', 'country_code', 'tier', 'netroutes']]

def query_fts_optimizer(params, auth_token, name):
    """Function to get the FTS optimizer events.

    Args:
        params (configparser): parameters file.
        auth_token (str): authentication token.
        name (str): name of the thread.

    Returns:
        dataframe: FTS optimizers events in a dataframe structure.
    """
    logging.debug('Querying FTS optimizer.')
    # FTS Optimizer events:
    #   Connections:    gives the maximum number of transfers that can be held (optimizer decision)
    #   Rationale:      if 'Range fixes' means that connections is the limit value set by the organization, for example, by ATLAS
    #                   if 'Queue emptying' then connections is the maximum value set by the organization or maybe an optimizer value, for example, max = 100 but they assign 78
    #   Active_count:   gives the number of parallel transfers (TCP windows)
    #   Submitted_count gives the number of transfers in the queue
    if 'source' in name: filename = params.get('FILENAME PARAMETERS', 'filename_source_query')
    else: filename = params.get('FILENAME PARAMETERS', 'filename_destination_query')
    cmd = 'curl -s -X POST "' + params.get('FTS PARAMETERS', 'url_fts_raw_queue') + '" -H "Authorization: Bearer ' + auth_token + '" -H "Content-Type: application/json" --data-binary "@' + filename + '"'
    df_data  = query_monit_events(cmd)
    if df_data.empty: return pd.DataFrame(columns = ['source_se', 'dest_se', 'timestamp', 'throughput', 'throughput_ema', 'duration_avg', 'filesize_avg', 'filesize_stddev', 'success_rate', 'retry_count', 'active_count', 'submitted_count', 'connections', 'rationale', 'endpnt']) # Return an empty dataframe because there are none FTS Optimizer Events
    return df_data

def generate_query_fts_optimizer(config, params, type, df_cric_database, get_by):
    """Function to generate the queries for downloading the FTS raw queues.

    Args:
        config (dict): dictionary with the yaml configuration file.
        params (configparser): parameters file.
        type (str): direction of the link. It can take two values: source or destination.
        df_cric_database (DataFrame): CRIC database information in a dataframe structure.
        get_by (string): type of data select by the user to get by.

    Returns:
        list: list of endpoints for a defined link.
    """
    list_endpoints = df_cric_database.query('`{0}` in @config[@type]'.format(get_by)).reset_index(drop = True)['endpoint'].tolist()
    # list_endpoints = ['https://cmsnoted1.fnal.gov', 'https://eoscms.cern.ch', 'https://cmssense4.fnal.gov'] # @remove: just for @FNAL version. NOTE: remove also in query.py
    if 'source' in type: query_2nd_line_2 = '"data.source_se": ' + json.dumps(list_endpoints)
    else: query_2nd_line_2 = '"data.dest_se": ' + json.dumps(list_endpoints)
    with open(params.get('FILENAME PARAMETERS', 'filename_' + type.split('_')[0] + '_query'), 'w') as f: f.write(params.get('ELASTIC SEARCH PARAMETERS', 'query_1st_line') + '\n' + params.get('ELASTIC SEARCH PARAMETERS', 'query_2nd_line_1') + query_2nd_line_2 + params.get('ELASTIC SEARCH PARAMETERS', 'query_2nd_line_3') + '\n') # Write query into a file without extension
    logging.debug('Generating query for %s, number of endpoints: %d' % (type, len(list_endpoints)))
    return list_endpoints

def get_site_ip_addresses(df_data, ip_version):
    """Function to get IPv4/IPv6 addresses.

    Args:
        df_data (dataframe): CRIC database.
        ip_version (str): IPv4/IPv6 version.

    Returns:
        dataframe: columns 'IPv4' and 'IPv6' of CRIC database in a dataframe structure.
    """
    list_ip = []
    # Iterate over netroutes parameter
    for i in range(df_data.shape[0]):
        site = df_data['official_site'].values[i]
        df_networks = pd.DataFrame(df_data['netroutes'].values[i])['networks']
        df_ip = pd.DataFrame(df_networks.values.tolist())
        # Get IPv4/IPv6 addresses
        if ip_version in df_ip.columns: df_ip_version = pd.DataFrame(df_ip[ip_version].dropna().reset_index(drop = True))
        else: continue # There are none ip address
        for index, row in df_ip_version.iterrows():
            items = pd.DataFrame(row.values.tolist())
            for i in range(items.shape[1]):
                if items[i].values[0] not in list_ip: list_ip.append(items[i].values[0])
        # Fill dataframe with the data from query
        duplicated_index = df_data.query('official_site in @site').index # Note: can be more than one endpoints with the same rcsite
        if 'ipv4' in ip_version: df_data.loc[duplicated_index, 'IPv4'] = ', '.join(list_ip.copy())
        else: df_data.loc[duplicated_index, 'IPv6'] = ', '.join(list_ip.copy())
        # Clear the content of the list for the next iteration
        list_ip.clear()
    return

def get_cric_database_description(params, auth_token):
    """Function to get IPv4/IPv6 address of CRIC database.

    Args:
        params (configparser): parameters file.
        auth_token (str): authentication token.
    
    Returns:
        dataframe: CRIC database information in a dataframe structure.
    """
    df_data = query_cric_database(params, auth_token)
    get_site_ip_addresses(df_data, 'ipv4')
    get_site_ip_addresses(df_data, 'ipv6')
    return df_data

def get_cric_next_hop_federation(list_next_hop, df_data):
    """Function to get federations of the next hops based on the CRIC database.

    Args:
        list_next_hop (list): list of the next hop.
        df_data (dataframe): CRIC database information in a dataframe structure.
    
    Returns:
        dataframe: CRIC database federation of the next hop.
    """
    if ':' in list_next_hop[0]: df_query = df_data.dropna(subset = ['IPv6']).query('IPv6.str.contains("|".join(@list_next_hop))', engine = 'python').drop_duplicates(subset = ['IPv6']).reset_index(drop = True)
    else: df_query = df_data.dropna(subset = ['IPv4']).query('IPv4.str.contains("|".join(@list_next_hop))', engine = 'python').drop_duplicates(subset = ['IPv4']).reset_index(drop = True)
    return df_query.drop_duplicates(subset = ['federation']).reset_index(drop = True)['federation'].tolist()
