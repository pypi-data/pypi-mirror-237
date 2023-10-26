from enum import Enum


class Status(Enum):
    CONTINUE_100 = "100 Continue"
    Continue = CONTINUE_100

    SWITCHING_PROTOCOLS_101 = "101 Switching Protocols"
    SwitchingProtocols = SWITCHING_PROTOCOLS_101

    OK_200 = "200 OK"
    Ok = OK_200

    CREATED_201 = "201 Created"
    Created = CREATED_201

    ACCEPTED_202 = "202 Accepted"
    Accepted = ACCEPTED_202

    NON_AUTHORITATIVE_INFORMATION_203 = "203 Non-Authoritative Information"
    NonAuthoritativeInformation = NON_AUTHORITATIVE_INFORMATION_203

    NO_CONTENT_204 = "204 No Content"
    NoContent = NO_CONTENT_204

    RESET_CONTENT_205 = "205 Reset Content"
    ResetContent = RESET_CONTENT_205

    PARTIAL_CONTENT_206 = "206 Partial Content"
    PartialContent = PARTIAL_CONTENT_206

    MULTIPLE_CHOICES_300 = "300 Multiple Choices"
    MultipleChoices = MULTIPLE_CHOICES_300

    MOVED_PERMANENTLY_301 = "301 Moved Permanently"
    MovedPermanently = MOVED_PERMANENTLY_301

    FOUND_302 = "302 Found"
    Found = FOUND_302

    SEE_OTHER_303 = "303 See Other"
    SeeOther = SEE_OTHER_303

    NOT_MODIFIED_304 = "304 Not Modified"
    NotModified = NOT_MODIFIED_304

    USE_PROXY_305 = "305 Use Proxy"
    UseProxy = USE_PROXY_305

    TEMPORARY_REDIRECT_307 = "307 Temporary Redirect"
    TemporaryRedirect = TEMPORARY_REDIRECT_307

    BAD_REQUEST_400 = "400 Bad Request"
    BadRequest = BAD_REQUEST_400

    UNAUTHORIZED_401 = "401 Unauthorized"
    Unauthorized = UNAUTHORIZED_401

    PAYMENT_REQUIRED_402 = "402 Payment Required"
    PaymentRequired = PAYMENT_REQUIRED_402

    FORBIDDEN_403 = "403 Forbidden"
    Forbidden = FORBIDDEN_403

    NOT_FOUND_404 = "404 Not Found"
    NotFound = NOT_FOUND_404

    METHOD_NOT_ALLOWED_405 = "405 Method Not Allowed"
    MethodNotAllowed = METHOD_NOT_ALLOWED_405

    NOT_ACCEPTABLE_406 = "406 Not Acceptable"
    NotAcceptable = NOT_ACCEPTABLE_406

    PROXY_AUTHENTICATION_REQUIRED_407 = "407 Proxy Authentication Required"
    ProxyAuthenticationRequired = PROXY_AUTHENTICATION_REQUIRED_407

    REQUEST_TIMEOUT_408 = "408 Request Timeout"
    RequestTimeout = REQUEST_TIMEOUT_408

    CONFLICT_409 = "409 Conflict"
    Conflict = CONFLICT_409

    GONE_410 = "410 Gone"
    Gone = GONE_410

    LENGTH_REQUIRED_411 = "411 Length Required"
    LengthRequired = LENGTH_REQUIRED_411

    PRECONDITION_FAILED_412 = "412 Precondition Failed"
    PreconditionFailed = PRECONDITION_FAILED_412

    REQUEST_ENTITY_TOO_LARGE_413 = "413 Request Entity Too Large"
    RequestEntityTooLarge = REQUEST_ENTITY_TOO_LARGE_413

    REQUEST_URI_TOO_LONG_414 = "414 Request-URI Too Long"
    RequestUriTooLong = REQUEST_URI_TOO_LONG_414

    UNSUPPORTED_MEDIA_TYPE_415 = "415 Unsupported Media Type"
    UnsupportedMediaType = UNSUPPORTED_MEDIA_TYPE_415

    REQUESTED_RANGE_NOT_SATISFIABLE_416 = "416 Requested Range Not Satisfiable"
    RequestedRangeNotSatisfiable = REQUESTED_RANGE_NOT_SATISFIABLE_416

    EXPECTATION_FAILED_417 = "417 Expectation Failed"
    ExpectationFailed = EXPECTATION_FAILED_417

    INTERNAL_SERVER_ERROR_500 = "500 Internal Server Error"
    InternalServerError = INTERNAL_SERVER_ERROR_500

    NOT_IMPLEMENTED_501 = "501 Not Implemented"
    NotImplemented = NOT_IMPLEMENTED_501

    BAD_GATEWAY_502 = "502 Bad Gateway"
    BadGateway = BAD_GATEWAY_502

    SERVICE_UNAVAILABLE_503 = "503 Service Unavailable"
    ServiceUnavailable = SERVICE_UNAVAILABLE_503

    GATEWAY_TIMEOUT_504 = "504 Gateway Timeout"
    GatewayTimeout = GATEWAY_TIMEOUT_504

    HTTP_VERSION_NOT_SUPPORTED_505 = "505 HTTP Version Not Supported"
    HttpVersionNotSupported = HTTP_VERSION_NOT_SUPPORTED_505

    def __str__(self) -> str:
        return self.value


class Method(Enum):
    get = "GET"
    post = "POST"
    put = "PUT"
    delete = "DELETE"
    patch = "PATCH"
    options = "OPTIONS"

    def __str__(self) -> str:
        return self.value
