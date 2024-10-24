import time
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f'Какое-то слово №  {i} + \n')
            time.sleep(0.1)
        return print(f'Завершилась запись в файл {file_name}')
time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

the_1 = Thread(target = write_words, args = (10, 'example5.txt'))
the_2 = Thread(target = write_words, args = (30, 'example6.txt'))
the_3 = Thread(target = write_words, args = (200, 'example7.txt'))
the_4 = Thread(target = write_words, args = (100, 'example8.txt'))

time_start2 = datetime.now()

the_1.start()
the_2.start()
the_3.start()
the_4.start()

the_1.join()
the_2.join()
the_3.join()
the_4.join()
time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(time_res2)