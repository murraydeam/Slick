"""


"""
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
            mode = "delete"
            for row in csv_reader:
                username = row['username']
                employee_id = row['employee_id']
                official_name = row['official_name']
                print(username, employee_id, official_name)
                adClient.manage_user(username, mode=mode)

    def pword(self):
        with open('MOCK_DATA.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                username = row['username']
                employee_id = row['employee_id']
                official_name = row['official_name']
                pword = row['pword']
                print(username, employee_id, official_name)
                adClient.pword_change(username, pword)

    def group(self):
        with open('MOCK_DATA.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            mode = "add"
            for row in csv_reader:
                username = row['username']
                employee_id = row['employee_id']
                official_name = row['official_name']
                print(username, employee_id, official_name)
                adClient.manage_user(username, mode=mode)


"""
MassBot Calling
# MassBot.create(MassBot)
# MassBot.manage(MassBot)
"""

MassBot.manage(MassBot)

