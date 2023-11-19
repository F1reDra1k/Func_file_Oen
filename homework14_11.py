# Написати клас та реалізувати його методи: (основа – ДЗ № 10)
#
# 1. Ініціалізація класу з одним параметром – ім'я файлу.
class FileProcessing:
    def __init__(self, filename):
        self.filename = filename

    def readlines_file(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        return lines

 # 2. Написати метод екземпляра класу, який створює атрибут екземпляра класу
 # у вигляді списку рядків (назви повертати без крапки)

    def read_domains_from_file(self):
        data_from_file = self.readlines_file()
        domains = [line.strip().replace('.', '') for line in data_from_file]
        return domains

# 2. Написати метод екземпляра класу, який повертає список усіх прізвищ із файлу.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"

    def get_last_names_from_file(self):
        data_from_file = self.readlines_file()
        ln_list = [line.split('\t')[1] for line in data_from_file if line]
        return ln_list

# 3. Написати метод екземпляра класу, який повертає список
# словників виду {"date": date} у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]

    def get_date_dict_from_file(self):
        data_from_file = self.readlines_file()
        new_data = []
        for line in data_from_file:
            if line and '-' in line:
                new_data.append({'date': line.split(' - ')[0]})

        return new_data


file_processor = FileProcessing("../Func_file_Open/domains.txt")
domains_list = file_processor.read_domains_from_file()
print(domains_list)

file_processor = FileProcessing("../Func_file_Open/names.txt")
last_names_list = file_processor.get_last_names_from_file()
print(last_names_list)

file_processor = FileProcessing("../Func_file_Open/authors.txt")
date_list = file_processor.get_date_dict_from_file()
print(date_list)

