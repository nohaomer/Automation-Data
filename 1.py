import csv
import os
from datetime import datetime, timedelta

import pandas as pd
folder_path = r"D:/excel/GOV/"
os.chdir(folder_path)
# Get a list of CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
target = input("enter your date   ")
target_date = datetime.strptime(target, '%Y-%m-%d-%H:%M')
# Iterate over each CSV file
for csv_file in csv_files:
    print(csv_file)
    # Delete data from  files
    df = pd.read_csv(csv_file)
    df['Time'] = df['Time'].fillna('')
    
    # Find the index of the first occurrence that contains '20:22' in the Time column
    search_data=df[df['Time'].str.contains('2023-08-27')]
    if (len(search_data)==0):
          print("this word not found")
    else:
    
    
        idx = search_data.index[0]
    
        # Delete rows starting from the identified index
        df = df.iloc[:idx]
    
        # Write the modified DataFrame back to a CSV file
        df.to_csv(csv_file, index=False)
    
    ####################################################################
    # when excel stop add data (target_date =======>> is last date in excel sheet)

    
    # Read the CSV file into a list of dictionaries
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    
    # Get the column names
    columns = data[0].keys()
    c=list(columns)
    
    
    # Get the index of the columns
    time_column_index = list(columns).index(c[0])
    data_column_index = list(columns).index(c[1])
    
    # Get the last row's data
    last_row = data[-1]
    
    # Parse the last time value
    last_time = datetime.strptime(last_row[c[0]], '%Y-%m-%d-%H:%M')
    i = 1
    while last_time < target_date:
    
        # Add 15 minutes to the last time value
        new_time = last_time + timedelta(minutes=15)
    
        # Create a new row with updated time and data from previous rows
        new_row = {
            c[0]: new_time.strftime('%Y-%m-%d-%H:%M'),
            c[1]: data[i][c[1]] if last_row[c[1]] else data[i][c[1]]
        }
    
        # Append the new row to the data list
        data.append(new_row)
    
    # Write the updated data back to the CSV file
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            writer.writerows(data)
    
        last_row = data[-1]
    
        # Parse the last time value
        last_time = datetime.strptime(last_row[c[0]], '%Y-%m-%d-%H:%M')
        i+=1
