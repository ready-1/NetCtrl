# coding: utf-8

"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class SnoopingQueriersPost(BaseModel):
    """
    SnoopingQueriersPost
    """  # noqa: E501

    address: StrictStr = Field(description="Configured IP address of querier")
    admin_mode: StrictStr = Field(
        description="Enable or disable querier", alias="adminMode"
    )
    expiry_interval: Annotated[int, Field(le=300, strict=True, ge=60)] = Field(
        description="Expiry interval of a snoop instance in seconds",
        alias="expiryInterval",
    )
    query_interval: Annotated[int, Field(le=1800, strict=True, ge=1)] = Field(
        description="Snooping query interval in seconds", alias="queryInterval"
    )
    querier_version: Annotated[int, Field(le=2, strict=True, ge=1)] = Field(
        description="Configured version for the querier", alias="querierVersion"
    )
    vlan_address: StrictStr = Field(
        description="IP address configured for the querier", alias="vlanAddress"
    )
    __properties: ClassVar[List[str]] = [
        "address",
        "adminMode",
        "expiryInterval",
        "queryInterval",
        "querierVersion",
        "vlanAddress",
    ]

    @field_validator("admin_mode")
    def admin_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["enabled", "disabled"]):
            raise ValueError("must be one of enum values ('enabled', 'disabled')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SnoopingQueriersPost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SnoopingQueriersPost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "address": obj.get("address"),
                "adminMode": obj.get("adminMode"),
                "expiryInterval": obj.get("expiryInterval"),
                "queryInterval": obj.get("queryInterval"),
                "querierVersion": obj.get("querierVersion"),
                "vlanAddress": obj.get("vlanAddress"),
            }
        )
        return _obj
