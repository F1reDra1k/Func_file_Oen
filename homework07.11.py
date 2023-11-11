# Всі пункти є частиною одного завдання, тому можна використовувати функції кілька разів та не дублювати код.
# Якщо хочете, можете використовувати дефолтні значення та анотацію типів.
#
# 1. Написати функцію, яка отримує один параметр - ім'я директорії та повертає словник виду
# {'filenames': [список файлів у папці], 'dirnames': [список усіх підпапок у папці]}.
# Підпапки враховувати лише першого рівня вкладення. Папка в папці в папці - таке не брати))
import os


def analyze_directory(dire_name: str) -> dict:
    if not os.path.exists(dire_name):
        return {'filenames': [], 'dirnames': []}

    items = os.listdir(directory_name)

    files = [item for item in items if os.path.isfile(os.path.join(directory_name, item))]
    directories = [item for item in items if os.path.isdir(os.path.join(directory_name, item))]

    return {'filenames': files, 'dirnames': directories}


directory_name = '/Volumes/Python/Lessons'
result = analyze_directory(directory_name)
# print(result)


# 2. Написати функцію, яка отримує два параметри – словник, описаний у пункті 1
# і значення булю (True/False) - можна зробити за замовчуванням.
# Функція повертає той самий словник, але з відсортованими іменами файлів та папок у відповідних списках.
# Булеве значення True означає, що порядок сортування алфавітний, False – зворотний порядок.

def sort_directory(dictionary: dict, reverse: bool = False) -> dict:
    dictionary['filenames'] = sorted(dictionary['filenames'], reverse=reverse)
    dictionary['dirnames'] = sorted(dictionary['dirnames'], reverse=reverse)

    return dictionary


directory_info = analyze_directory(directory_name)
sorted_directory = sort_directory(directory_info, reverse=False)
# print(sorted_directory)


# 3. Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та рядок, який може бути
# або ім'ям файлу, або ім'ям папки. (У імені файлу має бути точка).
# Залежно від того, що функція отримала (ім'я файлу або ім'я папки) – записати його у відповідний список
# та повернути оновлений словник.

def add_item_to_directory(dictionary: dict, item_name: str) -> dict:
    if '.' in item_name:
        dictionary['filenames'].append(item_name)
    else:
        dictionary['dirnames'].append(item_name)

    return dictionary


directory_info = analyze_directory(directory_name)
new_item_name = 'Hello_world'
updated_directory = add_item_to_directory(directory_info, new_item_name)
# print(updated_directory)


# 4* (*здавати не обов'язково).
# Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та ім'я директорії.
# Функція перевіряє відповідність отриманого словника та реальної файлової системи в отриманій папці та,
# якщо треба, створює потрібні папки та порожні файли, відповідно до структури словника.

def synchron_with_filesystem(dictionary: dict, base_directory: str):
    for dirname in dictionary['dirnames']:
        directory_path = os.path.join(base_directory, dirname)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    for filename in dictionary['filenames']:
        file_path = os.path.join(base_directory, filename)
        if not os.path.exists(file_path):
            open(file_path, 'w').close()


dir_info = analyze_directory(directory_name)
base_dir = '/Volumes/Python/Lessons/Test'

synchron_with_filesystem(dir_info, base_dir)
# print(synchron_with_filesystem)

