# coding: utf-8

"""
    さくらのVPS APIドキュメント

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 5.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from sakura_vps_client_py.models.health_check_http import HealthCheckHttp
from sakura_vps_client_py.models.health_check_https import HealthCheckHttps
from sakura_vps_client_py.models.health_check_ping import HealthCheckPing
from sakura_vps_client_py.models.health_check_pop3 import HealthCheckPop3
from sakura_vps_client_py.models.health_check_smtp import HealthCheckSmtp
from sakura_vps_client_py.models.health_check_ssh import HealthCheckSsh
from sakura_vps_client_py.models.health_check_tcp import HealthCheckTcp
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

SERVERMONITORINGSETTINGSHEALTHCHECK_ONE_OF_SCHEMAS = ["HealthCheckHttp", "HealthCheckHttps", "HealthCheckPing", "HealthCheckPop3", "HealthCheckSmtp", "HealthCheckSsh", "HealthCheckTcp"]

class ServerMonitoringSettingsHealthCheck(BaseModel):
    """
    ServerMonitoringSettingsHealthCheck
    """
    # data type: HealthCheckPing
    oneof_schema_1_validator: Optional[HealthCheckPing] = None
    # data type: HealthCheckTcp
    oneof_schema_2_validator: Optional[HealthCheckTcp] = None
    # data type: HealthCheckSsh
    oneof_schema_3_validator: Optional[HealthCheckSsh] = None
    # data type: HealthCheckSmtp
    oneof_schema_4_validator: Optional[HealthCheckSmtp] = None
    # data type: HealthCheckPop3
    oneof_schema_5_validator: Optional[HealthCheckPop3] = None
    # data type: HealthCheckHttp
    oneof_schema_6_validator: Optional[HealthCheckHttp] = None
    # data type: HealthCheckHttps
    oneof_schema_7_validator: Optional[HealthCheckHttps] = None
    actual_instance: Optional[Union[HealthCheckHttp, HealthCheckHttps, HealthCheckPing, HealthCheckPop3, HealthCheckSmtp, HealthCheckSsh, HealthCheckTcp]] = None
    one_of_schemas: Set[str] = { "HealthCheckHttp", "HealthCheckHttps", "HealthCheckPing", "HealthCheckPop3", "HealthCheckSmtp", "HealthCheckSsh", "HealthCheckTcp" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ServerMonitoringSettingsHealthCheck.model_construct()
        error_messages = []
        match = 0
        # validate data type: HealthCheckPing
        if not isinstance(v, HealthCheckPing):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HealthCheckPing`")
        else:
            match += 1
        # validate data type: HealthCheckTcp
        if not isinstance(v, HealthCheckTcp):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HealthCheckTcp`")
        else:
            match += 1
        # validate data type: HealthCheckSsh
        if not isinstance(v, HealthCheckSsh):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HealthCheckSsh`")
        else:
            match += 1
        # validate data type: HealthCheckSmtp
        if not isinstance(v, HealthCheckSmtp):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HealthCheckSmtp`")
        else:
            match += 1
        # validate data type: HealthCheckPop3
        if not isinstance(v, HealthCheckPop3):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HealthCheckPop3`")
        else:
            match += 1
        # validate data type: HealthCheckHttp
        if not isinstance(v, HealthCheckHttp):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HealthCheckHttp`")
        else:
            match += 1
        # validate data type: HealthCheckHttps
        if not isinstance(v, HealthCheckHttps):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HealthCheckHttps`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ServerMonitoringSettingsHealthCheck with oneOf schemas: HealthCheckHttp, HealthCheckHttps, HealthCheckPing, HealthCheckPop3, HealthCheckSmtp, HealthCheckSsh, HealthCheckTcp. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ServerMonitoringSettingsHealthCheck with oneOf schemas: HealthCheckHttp, HealthCheckHttps, HealthCheckPing, HealthCheckPop3, HealthCheckSmtp, HealthCheckSsh, HealthCheckTcp. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into HealthCheckPing
        try:
            instance.actual_instance = HealthCheckPing.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HealthCheckTcp
        try:
            instance.actual_instance = HealthCheckTcp.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HealthCheckSsh
        try:
            instance.actual_instance = HealthCheckSsh.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HealthCheckSmtp
        try:
            instance.actual_instance = HealthCheckSmtp.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HealthCheckPop3
        try:
            instance.actual_instance = HealthCheckPop3.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HealthCheckHttp
        try:
            instance.actual_instance = HealthCheckHttp.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HealthCheckHttps
        try:
            instance.actual_instance = HealthCheckHttps.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ServerMonitoringSettingsHealthCheck with oneOf schemas: HealthCheckHttp, HealthCheckHttps, HealthCheckPing, HealthCheckPop3, HealthCheckSmtp, HealthCheckSsh, HealthCheckTcp. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ServerMonitoringSettingsHealthCheck with oneOf schemas: HealthCheckHttp, HealthCheckHttps, HealthCheckPing, HealthCheckPop3, HealthCheckSmtp, HealthCheckSsh, HealthCheckTcp. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], HealthCheckHttp, HealthCheckHttps, HealthCheckPing, HealthCheckPop3, HealthCheckSmtp, HealthCheckSsh, HealthCheckTcp]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


