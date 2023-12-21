from file_handler import FileHandler

calibration = FileHandler(file_name='values.txt')
calibration.read_data_from_file()
calibration.search_for_numbers()
sum_of_values = 0
for item in calibration.numbers_in_lines:
    sum_of_values += item
print(sum_of_values)
