class Error(Exception):
   """Base class for other exceptions"""
   pass

class IncorrectLogin(Error):
   """Raised when incorrect login informatio is entered"""
   pass

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass
