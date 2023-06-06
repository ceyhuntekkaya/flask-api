class UnexpectedEntityException(BaseException):
    """
    This should be thrown when an attempt is made to persist an entity using the
    wrong repository.
    """
    pass