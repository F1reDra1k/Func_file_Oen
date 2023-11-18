# Написати клас та реалізувати його методи: (основа – ДЗ № 10)
#
# 1. Ініціалізація класу з одним параметром – ім'я файлу.
class FileProcessing:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_content = []

    def read_file(self):
        with open(self.file_name, 'r') as file:
            self.file_content = file.readlines()

    def read_domains_from_file(self):
        data_from_file = self.read_file(file_content)
        domain = [line.strip().replace('.', '') for line in data_from_file]
        return domain


file_processor = FileProcessing("domains.txt")
# file_processor.read_file()
file_processor.read_domains_from_file()
print(file_processor.file_content)
# 2. Написати метод екземпляра класу, який створює атрибут екземпляра класу
# у вигляді списку рядків (назви повертати без крапки)
#
# 2. Написати метод екземпляра класу, який повертає список усіх прізвищ із файлу.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"
#
# 3. Написати метод екземпляра класу, який повертає список
# словників виду {"date": date} у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
#
# 4* (*здавати не обов'язково).
# Написати метод екземпляра класу, отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date_original": date_original, "date_modified": date_modified}
# у яких date_original - це дата з рядка (якщо є),
# а date_modified - ця ж дата, представлена у форматі "dd/mm/yyyy" (d-день, m-місяць, y-рік)
# Наприклад [{"date_original": "8th February 1828", "date_modified": 08/02/1828}, ...]
