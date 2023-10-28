class NotLoggedInException(Exception):
    def __init__(self, message="Usuário precisa fazer login"):
        super().__init__(message)


class NotAuthorisedException(Exception):
    def __init__(self, message="Usuário não autorizado"):
        super().__init__(message)


class AuthenticationFailed(Exception):
    def __init__(self, message="Autenticação falhou"):
        super().__init__(message)


class NotFoundException(Exception):
    def __init__(self, message="Registro não encontrado"):
        super().__init__(message)


class ApiException(Exception):
    def __init__(self, message="Erro desconhecido na API"):
        super().__init__(message)


class ValidationException(Exception):
    def __init__(self, message="Erro de validação"):
        super().__init__(message)
