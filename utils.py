from datetime import datetime
from functools import wraps


# Logging Decorator
def track_access(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Method: {func.__name__}")
        print(f"Arguments: {args[1:]}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper


# Permission Closure
def permission_check(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if getattr(user, "role", None) == required_role:
                return func(user, *args, **kwargs)
            else:
                print("Access denied. Permission required:", required_role)
        return wrapper
    return decorator