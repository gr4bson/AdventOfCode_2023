class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_in_file = []
        self.numbers_in_lines = []

    def read_data_from_file(self):
        with open(self.file_name) as file:
            for line in file.readlines():
                self.data_in_file.append(line.strip())

    def search_for_numbers(self):
        first_number = None
        last_number = None
        for item in self.data_in_file:
            for symbol in item:
                if symbol.isdigit():
                    first_number = int(symbol)
                    break
            for symbol in reversed(item):
                if symbol.isdigit():
                    last_number = int(symbol)
                    break
            self.numbers_in_lines.append(first_number * 10 + last_number)
