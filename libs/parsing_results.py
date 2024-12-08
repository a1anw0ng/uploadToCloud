# Define a function to process the log lines
def analyze_test_results(log_lines):
    total_runs = 0
    passed_tests = 0
    failed_tests = 0

    # Analyze each line for test run start and test results
    for line in log_lines:
        if "================= Run:" in line:
            total_runs += 1
        elif "Final Status: SUCCEEDED" in line:
            passed_tests += 1

    # If there's logic to detect failed tests, it would adjust failed_tests accordingly
    # Assuming all runs that didn't explicitly succeed are failed (not applicable here as all succeeded)
    failed_tests = total_runs - passed_tests

    return total_runs, passed_tests, failed_tests

# Example usage with a list of log lines (you could replace this with reading from a file)
log_lines = [
    "02-09 22:00 INFO     ================= Run: 1 -> 1 ====================",
    "02-09 22:04 INFO     Final Status: SUCCEEDED",
    "02-09 22:05 INFO     ================= Run: 2 -> 1 ====================",
    "02-09 22:08 INFO     Final Status: SUCCEEDED",
    "02-09 22:09 INFO     ================= Run: 3 -> 1 ====================",
    "02-09 22:12 INFO     Final Status: SUCCEEDED",
    "02-09 22:13 INFO     ================= Run: 4 -> 1 ====================",
    "02-09 22:16 INFO     Final Status: SUCCEEDED",
]

# Call the function with the log lines
total_runs, passed_tests, failed_tests = analyze_test_results(log_lines)

# Print out the results
print(f"Total number of test cases executed: {total_runs}")
print(f"Number of tests passed: {passed_tests}")
print(f"Number of tests failed: {failed_tests}")
