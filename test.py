import csv
from datetime import datetime, timedelta

import pandas as pd
# Specify the folder path containing the CSV files


df = pd.read_csv('2.csv')
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
    df.to_csv('2.csv', index=False)

target=input("enter your date   ")
target_date = datetime.strptime(target, '%Y-%m-%d-%H:%M')
with open('2.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Get the header row
    header = next(reader)

    # Get the data rows
    data_rows = list(reader)

# Get the column index of the value column
date_column_index = header.index('Time')
#
# Get the last value in the column
last_date_str= data_rows[-1][date_column_index]
current_date = datetime.strptime(last_date_str, '%Y-%m-%d-%H:%M')
while current_date < target_date:
    # Get the last value in the column


    # Increment the last value by 15
    new_date = current_date + timedelta(minutes=15)

    # Format the new date as a string
    new_date_str = new_date.strftime('%Y-%m-%d-%H:%M')

    # Append the new date to the last row

    # Append the new value to a new row
    data_rows.append([new_date_str])

    # Write the modified data back to the CSV file
    with open('2.csv', 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(header)

        # Write the modified data rows
        writer.writerows(data_rows)

    # Update the current date
    last_date_str = data_rows[-1][date_column_index]
    current_date = datetime.strptime(last_date_str, '%Y-%m-%d-%H:%M')