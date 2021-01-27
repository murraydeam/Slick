import adClient
import csv


class Bulk:

    def add_user(self):

        with open('MOCK_DATA.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                username = row['username']
                employee_id = row['employee_id']
                official_name = row['official_name']
                print(username, employee_id, official_name)
                adClient.create_user(username, employee_id, official_name, active=True)

    def del_user(self):

        with open('MOCK_DATA.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                username = row['username']
                employee_id = row['employee_id']
                official_name = row['official_name']
                print(username, employee_id, official_name)
                adClient.manage_user(username, mode='delete')

    def user_info(self):

        with open('MOCK_DATA.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                username = row['username']
                print(username)
                adClient.user_info(username)



