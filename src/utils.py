import json
import os
import csv
import pandas as pd

PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
data_path = os.path.join(PATH, "data")

def read_config():
    return json.load(open("config.json"))

def create_csv():
    filename = "historic.csv"
    assert(os.path.isdir(os.path.join(data_path, filename)) == False),"Historic already exists"  
    if not os.path.isdir(data_path): os.mkdir(data_path) 

    col_names = ["Date", "Cycle day", "Level"]
    df = pd.DataFrame(columns = col_names)
    df.to_csv(open(os.path.join(data_path, filename), 'x'))

def read_csv():
    with open(data_path, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)
        file.close()

create_csv()
