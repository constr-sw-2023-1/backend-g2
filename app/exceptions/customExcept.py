class BadRequest(Exception):
    "400 - Bad Request"

class Unauthorized(Exception):
    "401 - Unauthorized"

class Forbidden(Exception):
    "403 - Forbidden"

class NotFound(Exception):
    "404 - Not Found"

class MethodNotAllowed(Exception):
    "405 - Method Not Allowed"

class NotAcceptable(Exception):
    "406 - Not Acceptable"

class InternalServerError(Exception):
    "500 - Internal Server Error"

class NotImplemented(Exception):
    "501 - Not Implemented"

class ServiceUnavailable(Exception):
    "503 - Service Unavailable"

class HTTPVersionNotSupported(Exception):
    "505 - HTTP Version Not Supported"

class CustomExpection(Exception):
    def __init__(self, errors, mensagem: str):
        self.mensagem = mensagem
        self.errors = errors
        super().__init__(self.mensagem)