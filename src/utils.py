import json
import os
import csv

def read_config():
    return json.load(open("config.json"))

def read_csv():
    path = 
    with open("students.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)
        file.close()

print(type(read_config()))
