import csv
"""
This script counts number of hours volunteered by each person in the month and the grand total for that month.
Creates an Excel sheet of each student:
- student number
- first name
- last name
- hours

Please input data into the 'data' file as tab separated values in the format:
date	studentnumber	firstname	lastname	hours

An example line (may not look tab separated but it is!):
04-Jul-24	00000001	foo	bar	10
"""

def get_data(filename):
    """
    Takes in the parameter filename and retrieves data from the given file filename by returning
    the heading and every entry as a single list.
    """
    file = open(filename)
    data = []

    for line in file:
        data.append(line.split('\t'))

    file.close()

    return data


def db(data):
    """
    Creates a database (dict)
    mapping (student number) -> [firstname, lastname]
    """
    my_db = {}

    for line in data:
        if line[1] not in my_db.keys():
            my_db[line[1]] = [line[2], line[3]]
    
    return my_db


def calc(data, my_db, month):
    """
    Calculates monthly volunteered hours for each person and grand total
    Creates Excel sheet with volunteer hours descending
    """
    my_dict = {}
    data_out = []
    sum_hours = 0

    for line in data:
        print(line[4])
        my_dict[line[1]] = my_dict.get(line[1], 0) + int(line[4])
        sum_hours += int(line[4])

    # Sort hours descending
    my_list = sorted(my_dict.items(), key=lambda kv: kv[1], reverse=True)

    data_out.append(["Student Number","First Name","Last Name","Hours"])
    for person in my_list:
        data_out.append([person[0],my_db.get(person[0])[0],my_db.get(person[0])[1],my_dict.get(person[0])])
    data_out.append([None,None,"Grand Total",f"{sum_hours}"])

    with open(f'Monthly Hours/Micro Volunteering {month} 2025 Hours.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data_out)


def main():
    month = input('What month?\n')

    my_data = get_data("data")
    my_db = db(my_data)
    calc(my_data, my_db, month)
    print(f"Successfuly created file: 'Micro Volunteering {month} 2025 Hours.csv' in the 'Monthly Hours' folder")
        
if __name__ == "__main__":
    main()