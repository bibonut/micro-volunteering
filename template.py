import csv
import datetime
"""
This script simplifies the process of filling the monthly template.
Creates an Excel sheet of each student:
- student number
- first name
- last name
- start date
- end date
- hours

Please input data into the 'data' file as tab separated values in the format:
date	studentnumber	firstname	lastname	hours

An example line (may not look tab separated but it is!):
04-Jul-24	00000001	foo	bar	10
"""
year = datetime.date.today().year

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
        if line[0] not in my_db.keys():
            my_db[line[1]] = [line[2], line[3]]
    
    return my_db


def start_end(data, my_db):
    '''
    Calculates volunteer start and end period
    '''
    period = {}

    for person in my_db:
        start = -1
        end = -1
        entries = []

        for line in data:
            if line[1] == person:
                entries.append(line)
        
        date = entries[0][0].split('-')
        start = date[0]
        date = entries[-1][0].split('-')
        end = date[0]

        period[person] = [start, end]

    return period


def template_maker(data, month, my_db):
    '''
    Outputs template of volunteers with volunteer period and sum of hours within that period
    '''
    months = dict(January=1, February=2, March=3, April=4, May=5, June=6, July=7, August=8, September=9, October=10, November=11, December=12)
    mnth = months[month]
    data_out  = []
    hours = {}

    # period[student] -> [start, end]
    period = start_end(data, my_db)

    for line in data:
        hours[line[1]] = hours.get(line[1], 0) + int(line[4])

    # sort hours descending
    my_list = sorted(hours.items(), key=lambda kv: kv[1])

    data_out.append(["Student Number","First Name","Last Name",None,"Description","Start Date","End Date","Hours"])
    for person in my_list:
        # student no, firstname, lastname, , description, start, end, hours
        data_out.append([person[0], my_db[person[0]][0], my_db[person[0]][1], None, 'Micro', period[person[0]][0]+f"/{mnth}/24", period[person[0]][1]+f"/{mnth}/24", hours[person[0]]])

    with open(f'Monthly Template Raw/Micro Volunteering {month} {year} Template Hours.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data_out)


def main():
    print('\n================================================================================')
    month = input('> What month is it?\n')

    my_data = get_data("data")
    my_db = db(my_data)
    template_maker(my_data, month, my_db)
    print('\n================================================================================')
    print(f"Successfuly created file:\n\t\'Micro Volunteering {month} {year} Template Hours.csv\'\nin the \'Monthly Template Raw\' folder!")
    print('\n================================================================================')

        
if __name__ == "__main__":
    main()