Всі пункти зробити як окремі функції та їх виклики.

1. Написати функцію, яка отримує як параметр ім'я файлу назви інтернет доменів (domains.txt)
та повертає їх у вигляді списку рядків (назви повертати без крапки).

2. Написати функцію, яка отримує як параметр ім'я файла (names.txt)
і повертає список усіх прізвищ із нього.
Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
Розділювач - символ табуляції "t"

3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
словників виду {"date": date}
у яких date - це дата з рядка (якщо є),
Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

4* (*здавати не обов'язково).
Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
словників виду {"date_original": date_original, "date_modified": date_modified}
у яких date_original - це дата з рядка (якщо є),
а date_modified - ця ж дата, представлена у форматі "dd/mm/yyyy" (d-день, m-місяць, y-рік)
Наприклад [{"date_original": "8th February 1828", "date_modified": 08/02/1828}, ...]