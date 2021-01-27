import adClient
import csv


class MassBot:

    def create(self):
        with open('MOCK_DATA.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                username = row['username']
                employee_id = row['employee_id']
                official_name = row['official_name']
                print(username, employee_id, official_name)
                adClient.create_user(username, employee_id, official_name)

    def manage(self):
        with open('MOCK_DATA.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # mode = print(input())
            for row in csv_reader:
                username = row['username']
                employee_id = row['employee_id']
                official_name = row['official_name']
                print(username, employee_id, official_name)
                adClient.manage_user(username, mode=mode)


"""
MassBot Calling
# MassBot.create()
# MassBot.manage()
"""

MassBot.create(None)

