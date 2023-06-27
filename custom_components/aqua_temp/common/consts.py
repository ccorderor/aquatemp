from homeassistant.backports.enum import StrEnum
from homeassistant.components.climate.const import FAN_AUTO, FAN_LOW, HVACMode

from .account_types import AccountTypes
from .endpoints import Endpoints

DOMAIN = "aqua_temp"
DEFAULT_NAME = "Aqua Temp"
SIGNAL_AQUA_TEMP_DEVICE_NEW = f"signal_{DOMAIN}_device_new"

HTTP_HEADER_X_TOKEN = "x-token"

CONF_ACCOUNT_TYPE = "account-type"

SUPPORTED_ACCOUNT_TYPES = {
    AccountTypes.AquaTempAndroid: "https://cloud.linked-go.com/cloudservice/api",
    AccountTypes.AquaTempIOS: "https://cloud.linked-go.com:449/crmservice/api",
    AccountTypes.HiTemp: "https://cloud.linked-go.com/cloudservice/api",
}

PRODUCT_IDS = [
    "1132174963097280512",  # Aqua Temp
    "1245226668902080512",  # Hitemp
    "1186904563333062656",  # Aqua Temp
    "1158905952238313472",  # Aqua Temp
    "1442284873216843776",  # Aqua Temp
    "1548963836789501952",  # Aqua Temp
]

DEVICE_REQUEST_PRODUCT_IDS = "product_ids"
DEVICE_REQUEST_PAGE_INDEX = "page_index"
DEVICE_REQUEST_PAGE_SIZE = "page_size"
DEVICE_REQUEST_TO_USER = "to_user"

DEVICE_CODE = "device_code"
DEVICE_PRODUCT_ID = "product_id"
PROTOCAL_CODES = "protocal_codes"

DEVICE_CONTROL_PARAM = "param"

DEVICE_CONTROL_PROTOCOL_CODE = "protocol_code"
DEVICE_CONTROL_VALUE = "value"

DEVICE_REQUEST_PARAMETERS = {
    DEVICE_REQUEST_PRODUCT_IDS: PRODUCT_IDS,
    DEVICE_REQUEST_PAGE_INDEX: 1,
    DEVICE_REQUEST_PAGE_SIZE: 999,
}

DEVICE_LISTS = {
    Endpoints.LIST_REGISTERED_DEVICES: [
        DEVICE_REQUEST_PRODUCT_IDS,
        DEVICE_REQUEST_PAGE_INDEX,
        DEVICE_REQUEST_PAGE_SIZE,
    ],
    Endpoints.LIST_SHARED_TOBE_DEVICES: [
        DEVICE_REQUEST_PRODUCT_IDS,
        DEVICE_REQUEST_TO_USER,
    ],
    Endpoints.LIST_SHARED_APPECT_DEVICES: [
        DEVICE_REQUEST_PRODUCT_IDS,
        DEVICE_REQUEST_TO_USER,
        DEVICE_REQUEST_PAGE_INDEX,
        DEVICE_REQUEST_PAGE_SIZE,
    ],
}

MANUAL_MUTE_AUTO = "0"
MANUAL_MUTE_LOW = "1"

FAN_MODE_MAPPING = {FAN_AUTO: MANUAL_MUTE_AUTO, FAN_LOW: MANUAL_MUTE_LOW}

POWER_MODE_OFF = "0"
POWER_MODE_ON = "1"

HEADERS = {"Content-Type": "application/json; charset=utf-8"}

DATA_ITEM_DEVICES = "device"
DATA_ITEM_LOGIN_DETAILS = "login-details"
DATA_ITEM_CONFIG = "configuration"

CONFIG_SET_MODE = "mode"
CONFIG_SET_POWER = "power"
CONFIG_SET_TEMPERATURE = "temperature"
CONFIG_SET_FAN = "fan"
CONFIG_SET_CURRENT_TEMPERATURE = "current_temperature"

PRODUCT_ID_DEFAULT = "default"

CONFIG_HVAC_MODES = "hvac_modes"
CONFIG_HVAC_OFF = str(HVACMode.OFF)
CONFIG_HVAC_HEAT = str(HVACMode.HEAT)
CONFIG_HVAC_COOL = str(HVACMode.COOL)
CONFIG_HVAC_AUTO = str(HVACMode.AUTO)
CONFIG_HVAC_SET = "set"
CONFIG_HVAC_TARGET = "target"
CONFIG_HVAC_MINIMUM = "minimum"
CONFIG_HVAC_MAXIMUM = "maximum"

CONFIG_FAN_MODES = "fan_modes"
CONFIG_FAN_AUTO = "auto"
CONFIG_FAN_LOW = "low"


class ProductParameter(StrEnum):
    CONFIG = "config"
    ENTITY_DESCRIPTION = "ENTITY_DESCRIPTION"
