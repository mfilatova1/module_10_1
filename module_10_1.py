from time import sleep
from datetime import datetime
from threading import Thread


time_start = datetime.now()
def write_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i+1}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

time_start = datetime.now()
first = Thread(target=write_words, args=(10, "xample5.txt"))
second = Thread(target=write_words, args=(30, "example6.txt"))
third = Thread(target=write_words, args=(200, "example7.txt"))
forth = Thread(target=write_words, args=(100, "example8.txt"))

first.start()
second.start()
third.start()
forth.start()

first.join()
second.join()
third.join()
forth.join()

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)


