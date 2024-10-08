def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    str_num = 0
    str_start_bytes = file.seek(0)

    for string in strings:
        file.write(string +'\n')
        str_num +=1
        key = (str_num, str_start_bytes)
        strings_positions[key] = string
        str_start_bytes = file.tell()
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)