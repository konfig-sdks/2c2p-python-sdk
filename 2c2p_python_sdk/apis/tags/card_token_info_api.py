# coding: utf-8

"""
    PGW Payment API 4.3

    Rest API for PGW payment purpose - LATEST

    The version of the OpenAPI document: 4.3
    Generated by: https://konfigthis.com
"""

from 2c2p_python_sdk.paths.payment_4_3_cardtokeninfo.post import GetCardTokenInfo
from 2c2p_python_sdk.apis.tags.card_token_info_api_raw import CardTokenInfoApiRaw


class CardTokenInfoApi(
    GetCardTokenInfo,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CardTokenInfoApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CardTokenInfoApiRaw(api_client)
