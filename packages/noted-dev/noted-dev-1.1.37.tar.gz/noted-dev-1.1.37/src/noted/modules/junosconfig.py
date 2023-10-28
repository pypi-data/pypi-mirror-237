# © Copyright 2022 CERN. This software is distributed under the terms of
# the GNU General Public Licence version 3 (GPL Version 3), copied verbatim
# in the file 'LICENCE.txt'. In applying this licence, CERN does not waive
# the privileges and immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.

import ipaddress
import pandas as pd
from jnpr.junos import Device
from modules.query import * # Query functions
from modules.tools import * # Tools functions
from modules.mysqlnoted import *    # MySQL NOTED functions
from modules.mysqlspectrum import * # Mysql functions

# Lab router: R1000-B-RJUXS-1. Production router: l513-v-rjuxl-12

def execute_cmd_junos(cmd, user, password, hostname):
    """Function to get interfaces configuration in Juniper routers.

    Args:
        user (str): username to access the router.
        password (str): password to access the router.
        hostname (str): hostname of the router.

    Returns:
        str: interfaces description of the router.
    """
    try:
        with Device(host = hostname, user = user, password = password) as dev:
            return dev.cli(cmd, warning = False)
    except Exception as err: 
        print('Cannot connect to device: {0}'.format(err))
        exit()

def get_list_next_hop(ip_address, next_hop_description):
    """Function to get next hops of LHCONE.

    Args:
        ip_address (str): IPv4/IPv6 address of the next hop.
        next_hop_description (dataframe): list of potential next-hop.

    Returns:
        dataframe: list of next hops.
    """
    df = pd.DataFrame(next_hop_description, columns = ['Nexthop'])['Nexthop'].str.split('*', expand = True)[0].to_frame(name = 'Nexthop')
    df_query = df.query('Nexthop.str.contains("/|>") & Nexthop.str.contains(":|.")', engine = 'python').reset_index(drop = True)
    df_next_hop = pd.concat([df_query.iloc[0:-2:2].reset_index(drop = True), df_query.iloc[1:-1:2].reset_index(drop = True)], axis = 1, ignore_index = True)
    if df_next_hop.empty: df_next_hop = pd.concat([df_query.iloc[0].reset_index(drop = True), df_query.iloc[1].reset_index(drop = True)], axis = 1, ignore_index = True)
    df_next_hop[1] = df_next_hop[1].str.split('to').str[1].str.split('via').str[0].str.strip()
    df_next_hop.rename(columns = {0: 'Interface', 1: 'Nexthop'}, inplace = True)
    df_next_hop['Interface'] = df_next_hop['Interface'].str.strip()
    list_next_hop = df_next_hop.query('Nexthop.str.contains(@ip_address)', engine = 'python').reset_index(drop = True)['Interface'].tolist()
    return [item.split('/', 1)[0] for item in list_next_hop] # remove the network mask

def get_router_interfaces_terse_description(params, df_data):
    """Function to get interfaces terse description of the router.

    Args:
        params (configparser): parameters file.
        df_data (dataframe): spectrum alarms in a dataframe structure.

    Returns: 
        str: router interfaces terse description.
    """
    return execute_cmd_junos('show interfaces ' + df_data['Interface'] + ' terse', params.get('JUNOS PARAMETERS', 'junos_user'), params.get('JUNOS PARAMETERS', 'junos_passwd'), df_data['Device'])

def get_router_next_hop_description(params, df_data, terse_description):
    """Function to get next hop description of the router.

    Args:
        params (configparser): parameters file.
        df_data (dataframe): spectrum alarms in a dataframe structure.
        terse_description (str): interfaces terse description of the router.

    Returns:
        str: next hop IP address.
        str: router next hop description.
    """
    try:
        ip_addr = terse_description.split('inet6')[1].strip().split(' ')[0].strip()    
        # By definition CERN is ::1 and the next hop ::2
        if int(ip_addr.split('::')[1].split('/')[0]) % 2 == 1: ip_next_hop = str(ipaddress.IPv6Address(ip_addr.split('/')[0]) + 1) # Odd number (impar) -> +1
        else: ip_next_hop = str(ipaddress.IPv6Address(ip_addr.split('/')[0]) - 1) # Even number (par) -> -1
        description = execute_cmd_junos('show route next-hop ' + ip_next_hop + ' protocol bgp active-path table inet6.0', params.get('JUNOS PARAMETERS', 'junos_user'), params.get('JUNOS PARAMETERS', 'junos_passwd'), df_data['Device']).split('Both')[1].strip().split('\n')
        return [ip_next_hop, description]        
    except (Exception, IndexError):
        ip_addr = terse_description.split('inet')[1].strip().split('/')[0].strip()    
        # By definition CERN is odd and the next hop even
        if int(ip_addr.split('.')[3].split('/')[0]) % 2 == 1: ip_next_hop = str(ipaddress.IPv4Address(ip_addr.split('/')[0]) + 1) # Odd number (impar) -> +1
        else: ip_next_hop = str(ipaddress.IPv4Address(ip_addr.split('/')[0]) - 1) # Even number (par) -> -1
        description = execute_cmd_junos('show route next-hop ' + ip_next_hop + ' protocol bgp active-path table inet', params.get('JUNOS PARAMETERS', 'junos_user'), params.get('JUNOS PARAMETERS', 'junos_passwd'), df_data['Device']).split('Both')[1].strip().split('\n')
        return [ip_next_hop, description] 
