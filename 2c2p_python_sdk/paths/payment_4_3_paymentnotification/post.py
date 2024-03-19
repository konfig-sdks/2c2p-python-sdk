# coding: utf-8

"""
    PGW Payment API 4.3

    Rest API for PGW payment purpose - LATEST

    The version of the OpenAPI document: 4.3
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from 2c2p_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from 2c2p_python_sdk.api_response import AsyncGeneratorResponse
from 2c2p_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from 2c2p_python_sdk import schemas  # noqa: F401

from 2c2p_python_sdk.model.payment_response_base import PaymentResponseBase as PaymentResponseBaseSchema
from 2c2p_python_sdk.model.payment_notification_request import PaymentNotificationRequest as PaymentNotificationRequestSchema
from 2c2p_python_sdk.model.browser_details import BrowserDetails as BrowserDetailsSchema

from 2c2p_python_sdk.type.browser_details import BrowserDetails
from 2c2p_python_sdk.type.payment_notification_request import PaymentNotificationRequest
from 2c2p_python_sdk.type.payment_response_base import PaymentResponseBase

from ...api_client import Dictionary
from 2c2p_python_sdk.pydantic.payment_response_base import PaymentResponseBase as PaymentResponseBasePydantic
from 2c2p_python_sdk.pydantic.browser_details import BrowserDetails as BrowserDetailsPydantic
from 2c2p_python_sdk.pydantic.payment_notification_request import PaymentNotificationRequest as PaymentNotificationRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = PaymentNotificationRequestSchema
SchemaForRequestBodyTextJson = PaymentNotificationRequestSchema
SchemaForRequestBodyApplicationJsonPatchjson = PaymentNotificationRequestSchema
SchemaForRequestBodyApplicationJson = PaymentNotificationRequestSchema


request_body_payment_notification_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaForRequestBodyTextJson),
        'application/json-patch+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonPatchjson),
        'application/*+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = PaymentResponseBaseSchema
SchemaFor200ResponseBodyTextJson = PaymentResponseBaseSchema
SchemaFor200ResponseBodyTextPlain = PaymentResponseBaseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaymentResponseBase


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaymentResponseBase


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextPlain),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
    'text/json',
    'text/plain',
)


class BaseApi(api_client.Api):

    def _process_notification_mapped_args(
        self,
        payment_token: str,
        plateform: typing.Optional[typing.Optional[str]] = None,
        recipient_id: typing.Optional[typing.Optional[str]] = None,
        recipient_name: typing.Optional[typing.Optional[str]] = None,
        locale: typing.Optional[typing.Optional[str]] = None,
        client_id: typing.Optional[str] = None,
        browser_details: typing.Optional[BrowserDetails] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if plateform is not None:
            _body["plateform"] = plateform
        if recipient_id is not None:
            _body["recipientID"] = recipient_id
        if recipient_name is not None:
            _body["recipientName"] = recipient_name
        if payment_token is not None:
            _body["paymentToken"] = payment_token
        if locale is not None:
            _body["locale"] = locale
        if client_id is not None:
            _body["clientID"] = client_id
        if browser_details is not None:
            _body["browserDetails"] = browser_details
        args.body = _body
        return args

    async def _aprocess_notification_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/payment/4.3/paymentnotification',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_payment_notification_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _process_notification_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/payment/4.3/paymentnotification',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_payment_notification_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ProcessNotificationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aprocess_notification(
        self,
        payment_token: str,
        plateform: typing.Optional[typing.Optional[str]] = None,
        recipient_id: typing.Optional[typing.Optional[str]] = None,
        recipient_name: typing.Optional[typing.Optional[str]] = None,
        locale: typing.Optional[typing.Optional[str]] = None,
        client_id: typing.Optional[str] = None,
        browser_details: typing.Optional[BrowserDetails] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._process_notification_mapped_args(
            payment_token=payment_token,
            plateform=plateform,
            recipient_id=recipient_id,
            recipient_name=recipient_name,
            locale=locale,
            client_id=client_id,
            browser_details=browser_details,
        )
        return await self._aprocess_notification_oapg(
            body=args.body,
            **kwargs,
        )
    
    def process_notification(
        self,
        payment_token: str,
        plateform: typing.Optional[typing.Optional[str]] = None,
        recipient_id: typing.Optional[typing.Optional[str]] = None,
        recipient_name: typing.Optional[typing.Optional[str]] = None,
        locale: typing.Optional[typing.Optional[str]] = None,
        client_id: typing.Optional[str] = None,
        browser_details: typing.Optional[BrowserDetails] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._process_notification_mapped_args(
            payment_token=payment_token,
            plateform=plateform,
            recipient_id=recipient_id,
            recipient_name=recipient_name,
            locale=locale,
            client_id=client_id,
            browser_details=browser_details,
        )
        return self._process_notification_oapg(
            body=args.body,
        )

class ProcessNotification(BaseApi):

    async def aprocess_notification(
        self,
        payment_token: str,
        plateform: typing.Optional[typing.Optional[str]] = None,
        recipient_id: typing.Optional[typing.Optional[str]] = None,
        recipient_name: typing.Optional[typing.Optional[str]] = None,
        locale: typing.Optional[typing.Optional[str]] = None,
        client_id: typing.Optional[str] = None,
        browser_details: typing.Optional[BrowserDetails] = None,
        validate: bool = False,
        **kwargs,
    ) -> PaymentResponseBasePydantic:
        raw_response = await self.raw.aprocess_notification(
            payment_token=payment_token,
            plateform=plateform,
            recipient_id=recipient_id,
            recipient_name=recipient_name,
            locale=locale,
            client_id=client_id,
            browser_details=browser_details,
            **kwargs,
        )
        if validate:
            return PaymentResponseBasePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaymentResponseBasePydantic, raw_response.body)
    
    
    def process_notification(
        self,
        payment_token: str,
        plateform: typing.Optional[typing.Optional[str]] = None,
        recipient_id: typing.Optional[typing.Optional[str]] = None,
        recipient_name: typing.Optional[typing.Optional[str]] = None,
        locale: typing.Optional[typing.Optional[str]] = None,
        client_id: typing.Optional[str] = None,
        browser_details: typing.Optional[BrowserDetails] = None,
        validate: bool = False,
    ) -> PaymentResponseBasePydantic:
        raw_response = self.raw.process_notification(
            payment_token=payment_token,
            plateform=plateform,
            recipient_id=recipient_id,
            recipient_name=recipient_name,
            locale=locale,
            client_id=client_id,
            browser_details=browser_details,
        )
        if validate:
            return PaymentResponseBasePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaymentResponseBasePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        payment_token: str,
        plateform: typing.Optional[typing.Optional[str]] = None,
        recipient_id: typing.Optional[typing.Optional[str]] = None,
        recipient_name: typing.Optional[typing.Optional[str]] = None,
        locale: typing.Optional[typing.Optional[str]] = None,
        client_id: typing.Optional[str] = None,
        browser_details: typing.Optional[BrowserDetails] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._process_notification_mapped_args(
            payment_token=payment_token,
            plateform=plateform,
            recipient_id=recipient_id,
            recipient_name=recipient_name,
            locale=locale,
            client_id=client_id,
            browser_details=browser_details,
        )
        return await self._aprocess_notification_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        payment_token: str,
        plateform: typing.Optional[typing.Optional[str]] = None,
        recipient_id: typing.Optional[typing.Optional[str]] = None,
        recipient_name: typing.Optional[typing.Optional[str]] = None,
        locale: typing.Optional[typing.Optional[str]] = None,
        client_id: typing.Optional[str] = None,
        browser_details: typing.Optional[BrowserDetails] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._process_notification_mapped_args(
            payment_token=payment_token,
            plateform=plateform,
            recipient_id=recipient_id,
            recipient_name=recipient_name,
            locale=locale,
            client_id=client_id,
            browser_details=browser_details,
        )
        return self._process_notification_oapg(
            body=args.body,
        )

