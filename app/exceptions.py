class BootstrapError(Exception):
    """Application initialization error"""


class RequestError(RuntimeError):
    detail = None
    orig = None

    def __init__(self, detail, orig=None):
        self.detail = detail
        self.orig = orig


class PayloadDecodeError(RequestError):
    """Error decoding the request JSON body"""


class PayloadValidationError(RequestError):
    """Payload of a POST request failed validation"""
