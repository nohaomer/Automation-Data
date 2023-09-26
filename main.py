import csv
from datetime import datetime, timedelta

# Open the CSV file in read mode
with open('1.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Get the header row
    header = next(reader)

    # Get the data rows
    data_rows = list(reader)

# Get the column index of the value column
date_column_index = header.index('Time')

# Get the last value in the column
last_date_str = data_rows[-1][date_column_index]
last_date = datetime.strptime(last_date_str, '%Y-%m-%d-%H:%M')
# Increment the last value by 15
new_date = last_date + timedelta(minutes=15)

# Format the new date as a string
new_date_str = new_date.strftime('%Y-%m-%d-%H:%M')

# Append the new date to the last row



# Append the new value to a new row
data_rows.append([new_date_str])

# Write the modified data back to the CSV file
with open('1.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(header)

    # Write the modified data rows
    writer.writerows(data_rows)