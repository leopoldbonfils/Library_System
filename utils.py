from datetime import datetime
from functools import wraps


def track_access(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] '{func.__name__}' called with args: {args[1:]}")
        return func(*args, **kwargs)
    return wrapper


def permission_check(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(self, user, *args, **kwargs):
            if getattr(user, "role", None) == required_role:
                return func(self, user, *args, **kwargs)
            print(f"Access denied for '{user.name}'. You need the '{required_role}' role.")
        return wrapper
    return decorator