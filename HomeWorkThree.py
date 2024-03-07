# Список файлов с известными именами
file_names = ['D:/Python Project/ExOne/1.txt', 'D:/Python Project/ExOne/2.txt']

# Словарь для хранения содержимого файлов
files_content = {}

# Чтение содержимого файлов
for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        files_content[file_name] = {
            'num_lines': len(lines),
            'content': lines
        }

# Вывод содержимого файлов для проверки
for file_name, file_data in files_content.items():
    print(f'File: {file_name}')
    print(f'Number of lines: {file_data["num_lines"]}')
    print('Content:')
    for line in file_data['content']:
        print(line)

# Сортировка файлов по количеству строк
sorted_files = sorted(files_content.items(), key=lambda x: x[1]['num_lines'])

# Запись отсортированного содержимого в новый файл
with open('result.txt', 'w') as result_file:
    for file_name, file_data in sorted_files:
        result_file.write(f'{file_name}\n{file_data["num_lines"]}\n')
        result_file.writelines(file_data['content'])
        result_file.write('\n')