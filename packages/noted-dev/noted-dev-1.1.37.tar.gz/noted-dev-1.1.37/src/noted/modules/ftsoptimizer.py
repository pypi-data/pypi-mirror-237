# © Copyright 2022 CERN. This software is distributed under the terms of
# the GNU General Public Licence version 3 (GPL Version 3), copied verbatim
# in the file "LICENCE.txt". In applying this licence, CERN does not waive
# the privileges and immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.

class FtsOptimizer():
    """Class for FTS optimizer attributes."""

    def __init__(self):
        """Function to initialize the attributes."""
        self._timestamp = '0'
        self._data_gigabytes = 0.0
        self._throughput_gigabits = 0.0
        self._parallel_transfers = 0
        self._queued_transfers = 0

    def get_timestamp(self):
        """Function to get timestamp attribute."""
        return self._timestamp

    def set_timestamp(self, timestamp):
        """Function to set timestamp attribute."""
        self._timestamp = timestamp

    def get_data_gigabytes(self):
        """Function to get data_gigabytes attribute."""
        return self._data_gigabytes

    def set_data_gigabytes(self, data_gigabytes):
        """Function to set data_gigabytes attribute."""
        self._data_gigabytes = data_gigabytes

    def get_throughput_gigabits(self):
        """Function to get throughput_gigabits attribute."""
        return self._throughput_gigabits

    def set_throughput_gigabits(self, throughput_gigabits):
        """Function to set throughput_gigabits attribute."""
        self._throughput_gigabits = throughput_gigabits

    def get_parallel_transfers(self):
        """Function to get parallel_transfers attribute."""
        return self._parallel_transfers

    def set_parallel_transfers(self, parallel_transfers):
        """Function to set parallel_transfers attribute."""
        self._parallel_transfers = parallel_transfers

    def get_queued_transfers(self):
        """Function to get queued_transfers attribute."""
        return self._queued_transfers

    def set_queued_transfers(self, queued_transfers):
        """Function to set queued_transfers attribute."""
        self._queued_transfers = queued_transfers

    def set_zero(self):
        """Function to set queued_transfers attribute."""
        self._timestamp = '0'
        self._data_gigabytes = 0.0
        self._throughput_gigabits = 0.0
        self._parallel_transfers = 0
        self._queued_transfers = 0
