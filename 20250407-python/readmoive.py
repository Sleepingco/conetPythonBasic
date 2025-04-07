import sys

with open('movies.csv','r',encoding='utf-8') as file:
    for line in file.readlines():
        data = line.split(',')
        (title, genre, year) = data
        print('%-15s %-10s %-10s'%(title,genre,year))
    
    
with open('movies.csv','r',encoding='utf-8') as file:
    while True:
        line = file.readline()
        if not line:
            break
        text = line.strip().split(',')
        print(text, end='')
