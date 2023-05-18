class BadRequest(Exception):
    "400 - Bad Request"

class Unauthorized(Exception):
    "401 - Bad Request"

class Forbidden(Exception):
    "403 - Bad Request"

class NotFound(Exception):
    "404 - Bad Request"

class MethodNotAllowed(Exception):
    "405 - Bad Request"

class NotAcceptable(Exception):
    "406 - Bad Request"

class InternalServerError(Exception):
    "500 - Bad Request"

class NotImplemented(Exception):
    "501 - Bad Request"

class ServiceUnavailable(Exception):
    "503 - Bad Request"

class HTTPVersionNotSupported(Exception):
    "505 - Bad Request"


class CustomExpection(Exception):
    def __init__(self, message, errors):
        super(CustomExpection, self).__init__(message)
        self.errors = errors