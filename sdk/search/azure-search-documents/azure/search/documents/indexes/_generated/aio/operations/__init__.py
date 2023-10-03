# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.7, generator: @autorest/python@6.7.8)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._data_sources_operations import DataSourcesOperations
from ._indexers_operations import IndexersOperations
from ._skillsets_operations import SkillsetsOperations
from ._synonym_maps_operations import SynonymMapsOperations
from ._indexes_operations import IndexesOperations
from ._aliases_operations import AliasesOperations
from ._search_service_client_operations import SearchServiceClientOperationsMixin

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "DataSourcesOperations",
    "IndexersOperations",
    "SkillsetsOperations",
    "SynonymMapsOperations",
    "IndexesOperations",
    "AliasesOperations",
    "SearchServiceClientOperationsMixin",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
