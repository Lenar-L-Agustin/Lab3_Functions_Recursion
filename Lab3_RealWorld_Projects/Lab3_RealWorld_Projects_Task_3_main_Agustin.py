import Lab3_RealWorld_Projects_Task_3_processor_Agustin, Student_Configuration_Agustin

processor = Lab3_RealWorld_Projects_Task_3_processor_Agustin
configuration = Student_Configuration_Agustin
SEED_DIGIT = int(configuration.STUDENT_ID[-1])
NAME_LENGTH = len(configuration.LAST_NAME)
ARTIST_LENGTH = len(configuration.FAVORITE_ARTIST)

telemetry = [
    SEED_DIGIT * 10,
    NAME_LENGTH * 7,
    "INVALID_SENSOR_READING",
    ARTIST_LENGTH * 8,
    -15
]

def telemetry_generator(data_list):
    for item in data_list:
        yield item

square_transform = lambda x: x ** 2

processed_count = 0
valid_count = 0
invalid_count = 0
valid_readings = []
transformed_readings = []

print("=" * 50)
print("EXECUTION LOG:")
print("=" * 50)

gen = telemetry_generator(telemetry)
for item in gen:
    processed_count += 1
    status = processor.validate_reading(item)
    if status == "VALID":
        valid_count += 1
        valid_readings.append(item)
        transformed_readings.append(square_transform(item))
    else:
        invalid_count += 1

if valid_readings:
    avg_reading = sum(valid_readings) / len(valid_readings)
    overall_status = processor.get_equipment_status(avg_reading)
else:
    avg_reading = 0
    overall_status = "UNKNOWN"

abnormal_detected = invalid_count
fault_trace_score = processor.analyze_fault(abnormal_detected)

print("=" * 50)
print("ASSESSMENT DATA:")
print("=" * 50)
print("Student-Specific Inputs:", f"LAST_NAME={configuration.LAST_NAME}, SEED_NUM={SEED_DIGIT}, FAVORITE_ARTIST={configuration.FAVORITE_ARTIST}")
print("Generated Telemetry Data:", telemetry)
print("Valid/Invalid Results:", f"Valid={valid_count}, Invalid={invalid_count}")
print("Processed Results:", f"Total Processed={processed_count}, Transformed Squared Valid Readings={transformed_readings}")
print("Recursive Analysis:", f"Fault Severity Level={abnormal_detected}, Trace Result={fault_trace_score}")
print("Final Diagnostic Summary:", f"Average Valid Telemetry={round(avg_reading, 2)}, Equipment Status={overall_status}")
print("=" * 50)
print("Final Output: PIPELINE EXECUTION COMPLETE")
print("=" * 50)