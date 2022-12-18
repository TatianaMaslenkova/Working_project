import csv
import interface as ie

def Read_csvfile(datacsv): 
    """чтение cvs файла и вывод на экран"""
    with open(datacsv, encoding='utf-8') as data:
        file_reader = csv.reader(data, delimiter = "|")
        count = 0
        ie.top_line()
        for row in file_reader:
            print(f' {"|".join(row)}')
            count += 1