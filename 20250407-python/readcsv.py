import csv
import pprint

with open('movies.csv') as file:
    reader = csv.reader(file)
    movies = list(reader)

for record in movies:
    genre = record[1]
    print(genre)
pprint.pprint(movies)