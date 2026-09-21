import Student_Configuration_Agustin

SEED_DIGIT = int(Student_Configuration_Agustin.STUDENT_ID[-1])
NAME_LENGTH = len(Student_Configuration_Agustin.LAST_NAME)
ARTIST_LENGTH = len(Student_Configuration_Agustin.FAVORITE_ARTIST)
fault_code = SEED_DIGIT + NAME_LENGTH + ARTIST_LENGTH

call_count = 0

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__} with input {args[0]}")
        return func(*args, **kwargs)
    return wrapper

@logger
def fault_trace(n):
    global call_count
    call_count = call_count + 1
    
    if n <= 1:
        return 1
    
    return n + fault_trace(n - 1)


print("=" * 40)
print("Execution Log:")
print("=" * 40)

final_result = fault_trace(fault_code)

print("=" * 40)
print("Assessment Data:")
print("Generated Fault Data:", fault_code)
print("Recursive Trace: Completed")
print("Number of Recursive Calls:", call_count)
print("Final Output:", final_result)
print("=" * 40)