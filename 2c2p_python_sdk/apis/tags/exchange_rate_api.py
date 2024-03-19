# coding: utf-8

"""
    PGW Payment API 4.3

    Rest API for PGW payment purpose - LATEST

    The version of the OpenAPI document: 4.3
    Generated by: https://konfigthis.com
"""

from 2c2p_python_sdk.paths.payment_4_3_exchangerate_apmmccexchangerate.post import ApmMcc
from 2c2p_python_sdk.paths.payment_4_3_exchangerate.post import GetRate
from 2c2p_python_sdk.paths.payment_4_3_exchangerate_secure.post import RequestEndpoint
from 2c2p_python_sdk.apis.tags.exchange_rate_api_raw import ExchangeRateApiRaw


class ExchangeRateApi(
    ApmMcc,
    GetRate,
    RequestEndpoint,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ExchangeRateApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ExchangeRateApiRaw(api_client)