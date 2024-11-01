from multiprocessing import Pool
from datetime import datetime
from threading import Thread

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            line = file.readline()
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# time_start = datetime.now()
# for name in filenames:
#     read_info(name)
# time_end = datetime.now()
# time_res = time_end - time_start
# print(time_res)


if __name__ == '__main__':
    time_start = datetime.now()
    with Pool(4) as pool:
        res = pool.map(read_info, filenames)
    time_end = datetime.now()
    time_res = time_end - time_start
    print(time_res)


