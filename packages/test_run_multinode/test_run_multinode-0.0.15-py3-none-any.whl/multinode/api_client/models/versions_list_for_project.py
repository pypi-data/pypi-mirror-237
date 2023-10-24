# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from multinode.api_client.models.version_info_for_project import VersionInfoForProject

class VersionsListForProject(BaseModel):
    """
    VersionsListForProject
    """
    project_name: StrictStr = Field(...)
    versions: conlist(VersionInfoForProject) = Field(...)
    __properties = ["project_name", "versions"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> VersionsListForProject:
        """Create an instance of VersionsListForProject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in versions (list)
        _items = []
        if self.versions:
            for _item in self.versions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['versions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VersionsListForProject:
        """Create an instance of VersionsListForProject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VersionsListForProject.parse_obj(obj)

        _obj = VersionsListForProject.parse_obj({
            "project_name": obj.get("project_name"),
            "versions": [VersionInfoForProject.from_dict(_item) for _item in obj.get("versions")] if obj.get("versions") is not None else None
        })
        return _obj


