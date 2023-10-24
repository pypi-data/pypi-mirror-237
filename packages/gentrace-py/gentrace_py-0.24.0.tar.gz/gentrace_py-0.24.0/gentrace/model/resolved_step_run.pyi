# coding: utf-8

"""
    Gentrace API

    These API routes are designed to ingest events from clients.  # noqa: E501

    The version of the OpenAPI document: 0.18.0
    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401

from gentrace import schemas  # noqa: F401

class ResolvedStepRun(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            organizationId = schemas.UUIDSchema
            providerName = schemas.StrSchema
            invocation = schemas.StrSchema
            
            
            class modelParams(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.AnyTypeSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                ) -> 'modelParams':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class inputs(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.AnyTypeSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                ) -> 'inputs':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class outputs(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.AnyTypeSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                ) -> 'outputs':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            startTime = schemas.StrSchema
            endTime = schemas.StrSchema
            pipelineRunId = schemas.UUIDSchema
            __annotations__ = {
                "id": id,
                "organizationId": organizationId,
                "providerName": providerName,
                "invocation": invocation,
                "modelParams": modelParams,
                "inputs": inputs,
                "outputs": outputs,
                "startTime": startTime,
                "endTime": endTime,
                "pipelineRunId": pipelineRunId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationId"]) -> MetaOapg.properties.organizationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerName"]) -> MetaOapg.properties.providerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invocation"]) -> MetaOapg.properties.invocation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modelParams"]) -> MetaOapg.properties.modelParams: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inputs"]) -> MetaOapg.properties.inputs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outputs"]) -> MetaOapg.properties.outputs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTime"]) -> MetaOapg.properties.startTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endTime"]) -> MetaOapg.properties.endTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pipelineRunId"]) -> MetaOapg.properties.pipelineRunId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "organizationId", "providerName", "invocation", "modelParams", "inputs", "outputs", "startTime", "endTime", "pipelineRunId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationId"]) -> typing.Union[MetaOapg.properties.organizationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerName"]) -> typing.Union[MetaOapg.properties.providerName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invocation"]) -> typing.Union[MetaOapg.properties.invocation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modelParams"]) -> typing.Union[MetaOapg.properties.modelParams, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inputs"]) -> typing.Union[MetaOapg.properties.inputs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outputs"]) -> typing.Union[MetaOapg.properties.outputs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTime"]) -> typing.Union[MetaOapg.properties.startTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endTime"]) -> typing.Union[MetaOapg.properties.endTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pipelineRunId"]) -> typing.Union[MetaOapg.properties.pipelineRunId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "organizationId", "providerName", "invocation", "modelParams", "inputs", "outputs", "startTime", "endTime", "pipelineRunId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        organizationId: typing.Union[MetaOapg.properties.organizationId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        providerName: typing.Union[MetaOapg.properties.providerName, str, schemas.Unset] = schemas.unset,
        invocation: typing.Union[MetaOapg.properties.invocation, str, schemas.Unset] = schemas.unset,
        modelParams: typing.Union[MetaOapg.properties.modelParams, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        inputs: typing.Union[MetaOapg.properties.inputs, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        outputs: typing.Union[MetaOapg.properties.outputs, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        startTime: typing.Union[MetaOapg.properties.startTime, str, schemas.Unset] = schemas.unset,
        endTime: typing.Union[MetaOapg.properties.endTime, str, schemas.Unset] = schemas.unset,
        pipelineRunId: typing.Union[MetaOapg.properties.pipelineRunId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ResolvedStepRun':
        return super().__new__(
            cls,
            *_args,
            id=id,
            organizationId=organizationId,
            providerName=providerName,
            invocation=invocation,
            modelParams=modelParams,
            inputs=inputs,
            outputs=outputs,
            startTime=startTime,
            endTime=endTime,
            pipelineRunId=pipelineRunId,
            _configuration=_configuration,
            **kwargs,
        )
