# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AuthorizationRule
    from ._models_py3 import CorrelationFilter
    from ._models_py3 import CreateQueueBody
    from ._models_py3 import CreateQueueBodyContent
    from ._models_py3 import CreateRuleBody
    from ._models_py3 import CreateRuleBodyContent
    from ._models_py3 import CreateSubscriptionBody
    from ._models_py3 import CreateSubscriptionBodyContent
    from ._models_py3 import CreateTopicBody
    from ._models_py3 import CreateTopicBodyContent
    from ._models_py3 import EmptyRuleAction
    from ._models_py3 import FalseFilter
    from ._models_py3 import KeyValue
    from ._models_py3 import MessageCountDetails
    from ._models_py3 import NamespaceProperties
    from ._models_py3 import NamespacePropertiesEntry
    from ._models_py3 import NamespacePropertiesEntryContent
    from ._models_py3 import QueueDescription
    from ._models_py3 import QueueDescriptionEntry
    from ._models_py3 import QueueDescriptionEntryContent
    from ._models_py3 import QueueDescriptionFeed
    from ._models_py3 import ResponseAuthor
    from ._models_py3 import ResponseLink
    from ._models_py3 import RuleAction
    from ._models_py3 import RuleDescription
    from ._models_py3 import RuleDescriptionEntry
    from ._models_py3 import RuleDescriptionEntryContent
    from ._models_py3 import RuleDescriptionFeed
    from ._models_py3 import RuleFilter
    from ._models_py3 import ServiceBusManagementError
    from ._models_py3 import SqlFilter
    from ._models_py3 import SqlRuleAction
    from ._models_py3 import SubscriptionDescription
    from ._models_py3 import SubscriptionDescriptionEntry
    from ._models_py3 import SubscriptionDescriptionEntryContent
    from ._models_py3 import SubscriptionDescriptionFeed
    from ._models_py3 import TopicDescription
    from ._models_py3 import TopicDescriptionEntry
    from ._models_py3 import TopicDescriptionEntryContent
    from ._models_py3 import TopicDescriptionFeed
    from ._models_py3 import TrueFilter
except (SyntaxError, ImportError):
    from ._models import AuthorizationRule  # type: ignore
    from ._models import CorrelationFilter  # type: ignore
    from ._models import CreateQueueBody  # type: ignore
    from ._models import CreateQueueBodyContent  # type: ignore
    from ._models import CreateRuleBody  # type: ignore
    from ._models import CreateRuleBodyContent  # type: ignore
    from ._models import CreateSubscriptionBody  # type: ignore
    from ._models import CreateSubscriptionBodyContent  # type: ignore
    from ._models import CreateTopicBody  # type: ignore
    from ._models import CreateTopicBodyContent  # type: ignore
    from ._models import EmptyRuleAction  # type: ignore
    from ._models import FalseFilter  # type: ignore
    from ._models import KeyValue  # type: ignore
    from ._models import MessageCountDetails  # type: ignore
    from ._models import NamespaceProperties  # type: ignore
    from ._models import NamespacePropertiesEntry  # type: ignore
    from ._models import NamespacePropertiesEntryContent  # type: ignore
    from ._models import QueueDescription  # type: ignore
    from ._models import QueueDescriptionEntry  # type: ignore
    from ._models import QueueDescriptionEntryContent  # type: ignore
    from ._models import QueueDescriptionFeed  # type: ignore
    from ._models import ResponseAuthor  # type: ignore
    from ._models import ResponseLink  # type: ignore
    from ._models import RuleAction  # type: ignore
    from ._models import RuleDescription  # type: ignore
    from ._models import RuleDescriptionEntry  # type: ignore
    from ._models import RuleDescriptionEntryContent  # type: ignore
    from ._models import RuleDescriptionFeed  # type: ignore
    from ._models import RuleFilter  # type: ignore
    from ._models import ServiceBusManagementError  # type: ignore
    from ._models import SqlFilter  # type: ignore
    from ._models import SqlRuleAction  # type: ignore
    from ._models import SubscriptionDescription  # type: ignore
    from ._models import SubscriptionDescriptionEntry  # type: ignore
    from ._models import SubscriptionDescriptionEntryContent  # type: ignore
    from ._models import SubscriptionDescriptionFeed  # type: ignore
    from ._models import TopicDescription  # type: ignore
    from ._models import TopicDescriptionEntry  # type: ignore
    from ._models import TopicDescriptionEntryContent  # type: ignore
    from ._models import TopicDescriptionFeed  # type: ignore
    from ._models import TrueFilter  # type: ignore

from ._service_bus_management_client_enums import (
    AccessRights,
    EntityAvailabilityStatus,
    EntityStatus,
    MessagingSku,
    NamespaceType,
)

__all__ = [
    'AuthorizationRule',
    'CorrelationFilter',
    'CreateQueueBody',
    'CreateQueueBodyContent',
    'CreateRuleBody',
    'CreateRuleBodyContent',
    'CreateSubscriptionBody',
    'CreateSubscriptionBodyContent',
    'CreateTopicBody',
    'CreateTopicBodyContent',
    'EmptyRuleAction',
    'FalseFilter',
    'KeyValue',
    'MessageCountDetails',
    'NamespaceProperties',
    'NamespacePropertiesEntry',
    'NamespacePropertiesEntryContent',
    'QueueDescription',
    'QueueDescriptionEntry',
    'QueueDescriptionEntryContent',
    'QueueDescriptionFeed',
    'ResponseAuthor',
    'ResponseLink',
    'RuleAction',
    'RuleDescription',
    'RuleDescriptionEntry',
    'RuleDescriptionEntryContent',
    'RuleDescriptionFeed',
    'RuleFilter',
    'ServiceBusManagementError',
    'SqlFilter',
    'SqlRuleAction',
    'SubscriptionDescription',
    'SubscriptionDescriptionEntry',
    'SubscriptionDescriptionEntryContent',
    'SubscriptionDescriptionFeed',
    'TopicDescription',
    'TopicDescriptionEntry',
    'TopicDescriptionEntryContent',
    'TopicDescriptionFeed',
    'TrueFilter',
    'AccessRights',
    'EntityAvailabilityStatus',
    'EntityStatus',
    'MessagingSku',
    'NamespaceType',
]
