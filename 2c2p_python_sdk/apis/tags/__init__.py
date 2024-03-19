# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from 2c2p_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    EXCHANGE_RATE = "ExchangeRate"
    APPLE_PAY = "ApplePay"
    CACHE = "Cache"
    CANCEL_TRANSACTION = "CancelTransaction"
    CARD_INSTALLMENT_PLAN_INFO = "CardInstallmentPlanInfo"
    CARD_TOKEN_INFO = "CardTokenInfo"
    INITIALIZATION = "Initialization"
    LOYALTY_POINT_INFO = "LoyaltyPointInfo"
    PAYMENT = "Payment"
    PAYMENT_INQUIRY = "PaymentInquiry"
    PAYMENT_INSTRUCTION = "PaymentInstruction"
    PAYMENT_NOTIFICATION = "PaymentNotification"
    PAYMENT_OPTION = "PaymentOption"
    PAYMENT_OPTION_DETAILS = "PaymentOptionDetails"
    PAYMENT_SIMULATE = "PaymentSimulate"
    PAYMENT_TOKEN = "PaymentToken"
    REDIRECT_BACK_END = "RedirectBackEnd"
    REDIRECT_FRONT_END = "RedirectFrontEnd"
    TRANSACTION_STATUS = "TransactionStatus"
    USER_PREFERENCE = "UserPreference"
