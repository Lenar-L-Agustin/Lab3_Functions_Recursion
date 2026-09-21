def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[EXECUTION LOG] Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def validate_reading(val):
    try:
        if not isinstance(val, (int, float)):
            raise TypeError("Invalid data type")
        if val < 0:
            return "INVALID"
        return "VALID"
    except TypeError:
        return "INVALID"

@logger
def analyze_fault(level):
    if level <= 1:
        return 1
    return level + analyze_fault(level - 1)

@logger
def get_equipment_status(avg):
    if avg >= 80:
        return "NORMAL"
    elif avg >= 50:
        return "MAINTENANCE"
    else:
        return "REPLACEMENT"