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

from .resource import Resource


class Experiment(Resource):
    """Defines the properties of an Experiment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param description: The description of the details or intents of the
     Experiment
    :type description: str
    :param endpoint_a: The endpoint A of an experiment
    :type endpoint_a: ~azure.mgmt.frontdoor.models.Endpoint
    :param endpoint_b: The endpoint B of an experiment
    :type endpoint_b: ~azure.mgmt.frontdoor.models.Endpoint
    :param enabled_state: The state of the Experiment. Possible values
     include: 'Enabled', 'Disabled'
    :type enabled_state: str or ~azure.mgmt.frontdoor.models.State
    :param resource_state: Resource status. Possible values include:
     'Creating', 'Enabling', 'Enabled', 'Disabling', 'Disabled', 'Deleting'
    :type resource_state: str or
     ~azure.mgmt.frontdoor.models.NetworkExperimentResourceState
    :ivar status: The description of Experiment status from the server side
    :vartype status: str
    :ivar script_file_uri: The uri to the Script used in the Experiment
    :vartype script_file_uri: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'status': {'readonly': True},
        'script_file_uri': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'endpoint_a': {'key': 'properties.endpointA', 'type': 'Endpoint'},
        'endpoint_b': {'key': 'properties.endpointB', 'type': 'Endpoint'},
        'enabled_state': {'key': 'properties.enabledState', 'type': 'str'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'script_file_uri': {'key': 'properties.scriptFileUri', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Experiment, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.endpoint_a = kwargs.get('endpoint_a', None)
        self.endpoint_b = kwargs.get('endpoint_b', None)
        self.enabled_state = kwargs.get('enabled_state', None)
        self.resource_state = kwargs.get('resource_state', None)
        self.status = None
        self.script_file_uri = None
