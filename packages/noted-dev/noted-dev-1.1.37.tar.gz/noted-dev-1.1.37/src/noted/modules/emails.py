# © Copyright 2022 CERN. This software is distributed under the terms of
# the GNU General Public Licence version 3 (GPL Version 3), copied verbatim
# in the file "LICENCE.txt". In applying this licence, CERN does not waive
# the privileges and immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.

import os
import logging

def write_content_email(params, message, class_transfer_broker_, class_fts_optimizer_, thread_name):
    """
    Function to write the content of the email for advertising the congestion of the link.

    Args:
        params (configparser): parameters file.
        message (str): message to stream
    """
    with open(''.join([os.getcwd(), '/', params.get('FILENAME PARAMETERS', 'filename_email')]), 'w') as f:
        f.write('From: ' + class_transfer_broker_.get_from_email_address() + '\n')
        f.write('To: '   + class_transfer_broker_.get_to_email_address()   + '\n')
        f.write('Subject: ' + class_transfer_broker_.get_subject_email()   + '\n')
        f.write(class_transfer_broker_.get_message_email() + '\n')
        f.write(message + '\n\n')
        if 'source' in thread_name:
            f.write('Source: '      + str(class_transfer_broker_.get_list_source()) + '\n')
            f.write('Destination: ' + str(class_transfer_broker_.get_list_destination()) + '\n\n')
        else:
            f.write('Source: '      + str(class_transfer_broker_.get_list_destination()) + '\n')
            f.write('Destination: ' + str(class_transfer_broker_.get_list_source()) + '\n\n')
        f.write('\tTimestamp: '            + str(class_fts_optimizer_.get_timestamp())            + '\n')
        f.write('\tAmount of data [GB]: '  + str(class_fts_optimizer_.get_data_gigabytes())       + '\n')
        f.write('\tNumber of parallel transfers: '  + str(class_fts_optimizer_.get_parallel_transfers()) + '\n')
        f.write('\tNumber of queued transfers: '     + str(class_fts_optimizer_.get_queued_transfers())     + '\n')
        f.write('\tThroughput [Gb/s]: '    + str(class_fts_optimizer_.get_throughput_gigabits())  + '\n\n')

def send_email(params, message, class_transfer_broker_, class_fts_optimizer_, thread_name):
    """
    Function to send an email for advertising the congestion of the link.

    Args:
        params (configparser): parameters file.
        message (str): message to stream
    """
    logging.warning('Sending email: LHCOPN Source: %s, LHCOPN Destination: %s, message: %s' % (class_transfer_broker_.get_list_source(), class_transfer_broker_.get_list_destination(), message))
    # inspect_transfers(params)
    # save_data_to_log_file(params, class_transfer_broker_.get_timestamp())
    write_content_email(params, message, class_transfer_broker_, class_fts_optimizer_, thread_name)
    cmd = os.popen('sendmail -vt < ' + ''.join([os.getcwd(), '/', params.get('FILENAME PARAMETERS', 'filename_email')]))
    