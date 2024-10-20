import csv

with open('weather.csv', 'r') as file:
    data = list(csv.reader(file))

print(data)
city = input("Enter a city: ")

for row in data:
    if city == row[0]:
        print(row[1])