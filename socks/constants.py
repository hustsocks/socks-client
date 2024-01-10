BUFFER_SIZE = 8192
PUBLIC_KEY = "FUXLOG"


class General:
    VERSION = 5
    AUTHENTICATION_VERSION = 1
    REGISTER_VERSION = 2
    MODIFIED_VERSION = 3


class Method:
    NO_AUTHENTICATION_REQUIRED = 0
    GSSAPI = 1
    USERNAME_PASSWORD = 2
    NO_ACCEPTABLE_METHOD = 255


class Command:
    CONNECT = 1
    BIND = 2
    UDP_ASSOCIATED = 3


class AddressType:
    IPV4 = 1
    DOMAINNAME = 3
    IPV6 = 4


class AuthenticationStatus:
    SUCCESS = 0
    FAILURE = 1


class RegisterStatus:
    SUCCESS = 0
    USERNAME_IS_EXISTED = 1
    INVALID_USERNAME_PASSWORD = 2


class ReplyStatus:
    SUCCEEDED = 0
    GENERAL_SOCKS_SERVER_FAILURE = 1
    CONNECTION_NOT_ALLOWED_BY_RULESET = 2
    NETWORK_UNREACHABLE = 3
    HOST_UNREACHABLE = 4
    CONNECTION_REFUSED = 5
    TTL_EXPIRED = 6
    COMMAND_NOT_SUPPORTED = 7
    ADDRESS_TYPE_NOT_SUPPORTED = 8
