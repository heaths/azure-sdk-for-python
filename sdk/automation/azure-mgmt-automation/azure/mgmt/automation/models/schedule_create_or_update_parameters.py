# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ScheduleCreateOrUpdateParameters(Model):
    """The parameters supplied to the create or update schedule operation.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Gets or sets the name of the Schedule.
    :type name: str
    :param description: Gets or sets the description of the schedule.
    :type description: str
    :param start_time: Required. Gets or sets the start time of the schedule.
    :type start_time: datetime
    :param expiry_time: Gets or sets the end time of the schedule.
    :type expiry_time: datetime
    :param interval: Gets or sets the interval of the schedule.
    :type interval: object
    :param frequency: Required. Gets or sets the frequency of the schedule.
     Possible values include: 'OneTime', 'Day', 'Hour', 'Week', 'Month',
     'Minute'
    :type frequency: str or ~azure.mgmt.automation.models.ScheduleFrequency
    :param time_zone: Gets or sets the time zone of the schedule.
    :type time_zone: str
    :param advanced_schedule: Gets or sets the AdvancedSchedule.
    :type advanced_schedule: ~azure.mgmt.automation.models.AdvancedSchedule
    """

    _validation = {
        'name': {'required': True},
        'start_time': {'required': True},
        'frequency': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'expiry_time': {'key': 'properties.expiryTime', 'type': 'iso-8601'},
        'interval': {'key': 'properties.interval', 'type': 'object'},
        'frequency': {'key': 'properties.frequency', 'type': 'str'},
        'time_zone': {'key': 'properties.timeZone', 'type': 'str'},
        'advanced_schedule': {'key': 'properties.advancedSchedule', 'type': 'AdvancedSchedule'},
    }

    def __init__(self, **kwargs):
        super(ScheduleCreateOrUpdateParameters, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.start_time = kwargs.get('start_time', None)
        self.expiry_time = kwargs.get('expiry_time', None)
        self.interval = kwargs.get('interval', None)
        self.frequency = kwargs.get('frequency', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.advanced_schedule = kwargs.get('advanced_schedule', None)
