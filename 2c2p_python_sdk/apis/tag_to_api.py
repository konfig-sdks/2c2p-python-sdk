import typing_extensions

from 2c2p_python_sdk.apis.tags import TagValues
from 2c2p_python_sdk.apis.tags.exchange_rate_api import ExchangeRateApi
from 2c2p_python_sdk.apis.tags.apple_pay_api import ApplePayApi
from 2c2p_python_sdk.apis.tags.cache_api import CacheApi
from 2c2p_python_sdk.apis.tags.cancel_transaction_api import CancelTransactionApi
from 2c2p_python_sdk.apis.tags.card_installment_plan_info_api import CardInstallmentPlanInfoApi
from 2c2p_python_sdk.apis.tags.card_token_info_api import CardTokenInfoApi
from 2c2p_python_sdk.apis.tags.initialization_api import InitializationApi
from 2c2p_python_sdk.apis.tags.loyalty_point_info_api import LoyaltyPointInfoApi
from 2c2p_python_sdk.apis.tags.payment_api import PaymentApi
from 2c2p_python_sdk.apis.tags.payment_inquiry_api import PaymentInquiryApi
from 2c2p_python_sdk.apis.tags.payment_instruction_api import PaymentInstructionApi
from 2c2p_python_sdk.apis.tags.payment_notification_api import PaymentNotificationApi
from 2c2p_python_sdk.apis.tags.payment_option_api import PaymentOptionApi
from 2c2p_python_sdk.apis.tags.payment_option_details_api import PaymentOptionDetailsApi
from 2c2p_python_sdk.apis.tags.payment_simulate_api import PaymentSimulateApi
from 2c2p_python_sdk.apis.tags.payment_token_api import PaymentTokenApi
from 2c2p_python_sdk.apis.tags.redirect_back_end_api import RedirectBackEndApi
from 2c2p_python_sdk.apis.tags.redirect_front_end_api import RedirectFrontEndApi
from 2c2p_python_sdk.apis.tags.transaction_status_api import TransactionStatusApi
from 2c2p_python_sdk.apis.tags.user_preference_api import UserPreferenceApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EXCHANGE_RATE: ExchangeRateApi,
        TagValues.APPLE_PAY: ApplePayApi,
        TagValues.CACHE: CacheApi,
        TagValues.CANCEL_TRANSACTION: CancelTransactionApi,
        TagValues.CARD_INSTALLMENT_PLAN_INFO: CardInstallmentPlanInfoApi,
        TagValues.CARD_TOKEN_INFO: CardTokenInfoApi,
        TagValues.INITIALIZATION: InitializationApi,
        TagValues.LOYALTY_POINT_INFO: LoyaltyPointInfoApi,
        TagValues.PAYMENT: PaymentApi,
        TagValues.PAYMENT_INQUIRY: PaymentInquiryApi,
        TagValues.PAYMENT_INSTRUCTION: PaymentInstructionApi,
        TagValues.PAYMENT_NOTIFICATION: PaymentNotificationApi,
        TagValues.PAYMENT_OPTION: PaymentOptionApi,
        TagValues.PAYMENT_OPTION_DETAILS: PaymentOptionDetailsApi,
        TagValues.PAYMENT_SIMULATE: PaymentSimulateApi,
        TagValues.PAYMENT_TOKEN: PaymentTokenApi,
        TagValues.REDIRECT_BACK_END: RedirectBackEndApi,
        TagValues.REDIRECT_FRONT_END: RedirectFrontEndApi,
        TagValues.TRANSACTION_STATUS: TransactionStatusApi,
        TagValues.USER_PREFERENCE: UserPreferenceApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EXCHANGE_RATE: ExchangeRateApi,
        TagValues.APPLE_PAY: ApplePayApi,
        TagValues.CACHE: CacheApi,
        TagValues.CANCEL_TRANSACTION: CancelTransactionApi,
        TagValues.CARD_INSTALLMENT_PLAN_INFO: CardInstallmentPlanInfoApi,
        TagValues.CARD_TOKEN_INFO: CardTokenInfoApi,
        TagValues.INITIALIZATION: InitializationApi,
        TagValues.LOYALTY_POINT_INFO: LoyaltyPointInfoApi,
        TagValues.PAYMENT: PaymentApi,
        TagValues.PAYMENT_INQUIRY: PaymentInquiryApi,
        TagValues.PAYMENT_INSTRUCTION: PaymentInstructionApi,
        TagValues.PAYMENT_NOTIFICATION: PaymentNotificationApi,
        TagValues.PAYMENT_OPTION: PaymentOptionApi,
        TagValues.PAYMENT_OPTION_DETAILS: PaymentOptionDetailsApi,
        TagValues.PAYMENT_SIMULATE: PaymentSimulateApi,
        TagValues.PAYMENT_TOKEN: PaymentTokenApi,
        TagValues.REDIRECT_BACK_END: RedirectBackEndApi,
        TagValues.REDIRECT_FRONT_END: RedirectFrontEndApi,
        TagValues.TRANSACTION_STATUS: TransactionStatusApi,
        TagValues.USER_PREFERENCE: UserPreferenceApi,
    }
)
