# Всі пункти зробити як окремі функції та їх виклики.
#
# 1. Написати функцію, яка отримує як параметр ім'я файлу назви інтернет доменів (domains.txt)
# та повертає їх у вигляді списку рядків (назви повертати без крапки).

# def read_domains_from_file(file_name: str) -> list:
#     with open(file_name, 'r') as file:
#         domains = [line.strip().replace('.', '') for line in file.readlines()]
#     return domains
#
#
# name_file = "domains.txt"
# domain_list = read_domains_from_file(name_file)
# print(domain_list)

# 2. Написати функцію, яка отримує як параметр ім'я файла (names.txt)
# і повертає список усіх прізвищ із нього.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"

# def extract_last_names_from_file(file_name: str) -> list:
#     last_names =[]

#     with open(file_name, 'r') as file:
#         for line in file.readlines():
#             last_name = line.strip().split('\t')[1]
#             last_names.append(last_name)
#         return last_names
#
#
# name_file = "names.txt"
# last_names = extract_last_names_from_file(name_file)
# print(last_names)
#
# 3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date": date}
# у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]


# def extract_last_names_from_file(file_name: str) -> list:
#     result = []
#
#     with open(file_name, 'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             parts = line.split('-')
#             if len(parts) >= 2:
#                 date = parts[0]
#                 result.append({"date": date})
#     return result
#
#
# name_file = "authors.txt"
# last_names = extract_last_names_from_file(name_file)
# print(last_names)


# def get_dates(file_name: str) -> list:
#     result = []
#
#     with open(file_name, 'r') as file:
#         lines = file.readlines()
#     for s in lines:
#         if '-' in s:
#             result.append({'date': s.split('-')[0]})
#     return result
#
#
# name_file = "authors.txt"
# last_names = get_dates(name_file)
# print(last_names)

