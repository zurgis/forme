import csv

text = ['Tom', 'Jerry']
#text = input('Введите текст: ')
#text2 = input('Введите текст: ')

with open('csvfile.csv', 'w', newline='') as f:
    fieldnames = ['name']
    csv_writer = csv.writer(f)  
    #csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    #csv_writer.writeheader()
    csv_writer.writerow(text)
    
    

with open('csvfile.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)