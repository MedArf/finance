import pandas as pd
import chardet
import os
import numpy
import yaml

current_dir=os.path.dirname(__file__)
relative_path='resources/export_25_11_2024_09_50_28.xls'
file_path=os.path.join(current_dir, relative_path)
file_encoding=''

with open(file_path,'rb') as file:
    file_encoding=chardet.detect(file.read())

print(file_encoding)
statement=pd.read_excel(file_path,header=2)

print(statement)
print(statement.describe())
