class BaseAPIException(Exception):
    """
    Base class for exceptions related to API errors.

    This class serves as a custom exception for handling API-related errors, allowing for a message and
    a status code to be specified. It extends the built-in Exception class to provide additional context
    for API exceptions.

    Args:
        message (str): A descriptive message for the exception.
        status_code (int): The HTTP status code associated with the exception (default is 500).
    """
    def __init__(self, message: str = "", status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class PokeAPIException(BaseAPIException):
    """
    Exception raised for errors related to the PokeAPI.

    This class extends the BaseAPIException to provide a specific exception type for handling errors
    that occur when interacting with the PokeAPI. It allows for a custom message and status code to be
    specified, defaulting to a general error message and a status code of 500.

    Args:
        message (str): A descriptive message for the exception (default is "Error with PokeAPI").
        status_code (int): The HTTP status code associated with the exception (default is 500).
    """
    def __init__(self, message: str = "Error with PokeAPI", status_code: int = 500):
        super().__init__(message, status_code)


class ValidationException(BaseAPIException):
    """
    Exception raised for validation errors.

    This class extends the BaseAPIException to provide a specific exception type for handling validation
    errors that occur within the application. It allows for a custom message and status code to be specified,
    defaulting to a general validation error message and a status code of 400.

    Args:
        message (str): A descriptive message for the exception (default is "Validation error").
        status_code (int): The HTTP status code associated with the exception (default is 400).
    """
    def __init__(self, message: str = "Validation error", status_code: int = 400):
        super().__init__(message, status_code)


class NotFoundError(BaseAPIException):
    """
    Exception raised when a requested resource is not found.

    This class extends the BaseAPIException to provide a specific exception type for handling cases
    where a resource cannot be located. It allows for a custom message and status code to be specified,
    defaulting to a general resource not found message and a status code of 404.

    Args:
        message (str): A descriptive message for the exception (default is "Resource not found").
        status_code (int): The HTTP status code associated with the exception (default is 404).
    """
    def __init__(self, message: str = "Resource not found", status_code: int = 404):
        super().__init__(message, status_code)


class ConfigError(BaseAPIException):
    """
    Exception raised for configuration errors.

    This class extends the BaseAPIException to provide a specific exception type for handling configuration
    errors that occur within the application. It allows for a custom message and status code to be specified,
    defaulting to a general configuration error message and a status code of 500.

    Args:
        message (str): A descriptive message for the exception (default is "Configuration error").
        status_code (int): The HTTP status code associated with the exception (default is 500).
    """
    def __init__(self, message: str = "Configuration error", status_code: int = 500):
        super().__init__(message, status_code)


class ServiceError(BaseAPIException):
    """
    Exception raised for general service errors.

    This class extends the BaseAPIException to provide a specific exception type for handling errors
    that occur within the service layer of the application. It allows for a custom message and status code
    to be specified, defaulting to a general service error message and a status code of 500.

    Args:
        message (str): A descriptive message for the exception (default is "Service error").
        status_code (int): The HTTP status code associated with the exception (default is 500).
    """
    def __init__(self, message: str = "Service error", status_code: int = 500):
        super().__init__(message, status_code)
