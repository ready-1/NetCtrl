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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.fiber_optics import FiberOptics
from openapi_client.models.general_responses_code import GeneralResponsesCode
from typing import Optional, Set
from typing_extensions import Self


class FiberOpticsGet200Response(BaseModel):
    """
    FiberOpticsGet200Response
    """  # noqa: E501

    resp: Optional[GeneralResponsesCode] = None
    fiber_optics: Optional[FiberOptics] = None
    __properties: ClassVar[List[str]] = ["resp", "fiber_optics"]

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
        """Create an instance of FiberOpticsGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of resp
        if self.resp:
            _dict["resp"] = self.resp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fiber_optics
        if self.fiber_optics:
            _dict["fiber_optics"] = self.fiber_optics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FiberOpticsGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "resp": (
                    GeneralResponsesCode.from_dict(obj["resp"])
                    if obj.get("resp") is not None
                    else None
                ),
                "fiber_optics": (
                    FiberOptics.from_dict(obj["fiber_optics"])
                    if obj.get("fiber_optics") is not None
                    else None
                ),
            }
        )
        return _obj
