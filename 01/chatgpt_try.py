def extract_calibration_values(calibration_document):
    total_sum = 0

    for line in calibration_document:
        # Find the first and last digits in the line
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        # If both digits are found, convert them to integers and add to the total sum
        if first_digit is not None and last_digit is not None:
            total_sum += int(first_digit + last_digit)

    return total_sum

def read_file_to_list(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines from the file and remove newline characters
            lines = [line.strip() for line in file.readlines()]
            return lines
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

# Example usage:
file_path = './input.txt'  # Replace with the actual path to your file
calibration_document = read_file_to_list(file_path)

# Calculate the sum of calibration values
result = extract_calibration_values(calibration_document)

# Print the result
print(result)