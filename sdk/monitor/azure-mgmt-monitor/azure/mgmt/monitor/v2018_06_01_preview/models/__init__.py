# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import DataSource
    from ._models_py3 import DataSourceConfiguration
    from ._models_py3 import ErrorResponse
    from ._models_py3 import EtwEventConfiguration
    from ._models_py3 import EtwProviderConfiguration
    from ._models_py3 import EventLogConfiguration
    from ._models_py3 import GuestDiagnosticSettingsAssociationList
    from ._models_py3 import GuestDiagnosticSettingsAssociationResource
    from ._models_py3 import GuestDiagnosticSettingsAssociationResourcePatch
    from ._models_py3 import GuestDiagnosticSettingsList
    from ._models_py3 import GuestDiagnosticSettingsPatchResource
    from ._models_py3 import GuestDiagnosticSettingsResource
    from ._models_py3 import PerformanceCounterConfiguration
    from ._models_py3 import Resource
    from ._models_py3 import SinkConfiguration
except (SyntaxError, ImportError):
    from ._models import DataSource  # type: ignore
    from ._models import DataSourceConfiguration  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import EtwEventConfiguration  # type: ignore
    from ._models import EtwProviderConfiguration  # type: ignore
    from ._models import EventLogConfiguration  # type: ignore
    from ._models import GuestDiagnosticSettingsAssociationList  # type: ignore
    from ._models import GuestDiagnosticSettingsAssociationResource  # type: ignore
    from ._models import GuestDiagnosticSettingsAssociationResourcePatch  # type: ignore
    from ._models import GuestDiagnosticSettingsList  # type: ignore
    from ._models import GuestDiagnosticSettingsPatchResource  # type: ignore
    from ._models import GuestDiagnosticSettingsResource  # type: ignore
    from ._models import PerformanceCounterConfiguration  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import SinkConfiguration  # type: ignore

from ._monitor_management_client_enums import (
    DataSourceKind,
    GuestDiagnosticSettingsOsType,
    SinkConfigurationKind,
)

__all__ = [
    'DataSource',
    'DataSourceConfiguration',
    'ErrorResponse',
    'EtwEventConfiguration',
    'EtwProviderConfiguration',
    'EventLogConfiguration',
    'GuestDiagnosticSettingsAssociationList',
    'GuestDiagnosticSettingsAssociationResource',
    'GuestDiagnosticSettingsAssociationResourcePatch',
    'GuestDiagnosticSettingsList',
    'GuestDiagnosticSettingsPatchResource',
    'GuestDiagnosticSettingsResource',
    'PerformanceCounterConfiguration',
    'Resource',
    'SinkConfiguration',
    'DataSourceKind',
    'GuestDiagnosticSettingsOsType',
    'SinkConfigurationKind',
]
