from json import JSONDecodeError
from project.socket.response import Response
from setting import log_setting

resp = Response()


def validator(schema=None):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            request = args[0]
            if request.method == "GET":
                _in = dict(request.rel_url.query)
                valid, errors = await schema(_in)
                if not valid:
                    logger.error(
                        f"Method: {request.method}, Validation Error: {errors}"
                    )
                    return resp.invalid_input(message=errors)

            if request.method == "POST" or request.method == "PUT":
                try:
                    _in = await request.json()
                except JSONDecodeError:
                    print(request.method)
                    return resp.invalid_input(
                        message="Invalid JSON or no JSON content for this request."
                    )

                else:
                    valid, errors = await schema(_in)
                    if not valid:
                        logger.error(
                            f"Method: {request.method}, Validation Error: {errors}"
                        )
                        return resp.invalid_input(message=errors)

            return await func(*args, **kwargs)

        return wrapper

    return decorator
