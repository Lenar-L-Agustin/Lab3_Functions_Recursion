import Student_Configuration_Agustin

SEED_DIGIT = int(Student_Configuration_Agustin.STUDENT_ID[-1])
NAME_LENGHT = len(Student_Configuration_Agustin.LAST_NAME)
ARTIST_LENGHT = len(Student_Configuration_Agustin.FAVORITE_ARTIST)

equipment_reading = [
    SEED_DIGIT * 10,
    NAME_LENGHT * 7,
    ARTIST_LENGHT * 7
]

def logger(func):
    def wrapper(*args, **kwargs):
        print("Executing:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logger
def validation(readings):
    try:
        for val in readings:
            if val < 0:
                return False
        return True
    except TypeError:
        return False

@logger
def calculation(readings):
    return sum(readings) / len(readings)

@logger
def classification(avg):
    if avg >= 80:
        return "NORMAL"
    elif avg >= 50:
        return "MAINTENANCE"
    else:
        return "REPLACEMENT"

print("=" * 40)
print("EQUIPMENT DIAGNOSTIC SYSTEM")
print("=" * 40)
if validation(equipment_reading):
    avg = calculation(equipment_reading)
    status = classification(avg)

    print("=" * 40)
    Student_Configuration_Agustin.print_student_configuration()
    print("Generated Readings:", equipment_reading)
    print("Validation Result:  PASSED")
    print("Average Value:", round(avg, 2))
    print("Diagnostic Result:", status)
    print("Final Output:", f"Equipment status:{status}, Average reading: {round(avg, 2)}")
    print("=" * 40)
else:
    print("-" * 40)
    print("Generated Readings:", equipment_reading)
    print("Validation Result:  FAILED")
    print("ERROR: Invalid readings detected!")
    print("Final Output: INVALID READINGS")
    print("=" * 40)