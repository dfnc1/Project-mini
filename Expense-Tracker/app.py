import argparse
import csv
from datetime import datetime

class tracker_app:
    def __init__(self, description: str, amount: float) -> None:
        self.date: datetime = datetime.now()
        self.fields: list = ['Id','Date', 'Description', 'Amount']
        self.file: str = 'data.csv'

        self.description: str = description
        self.amount: float = amount



    # def parse_args(self) -> argparse.Namespace:
    #
    #     parse = argparse.ArgumentParser(description="expense tracker")
    #
    #     parse.add_argument("add" )
    #
    #     return parse.parse_args()
    def list(self) -> None:
        with open(self.file, mode='r') as file:
            reader = csv.DictReader(file, fieldnames=self.fields)
            data: list[dict] = [row for row in reader]
            temp: list[list] = [list(row.values()) for row in data]
            print("ID\tDate\t\t\tDescription\t\t\t\tAmount")
            for row in range(len(temp)):
                print(f" {temp[row][0]:5}  {temp[row][1]}  \t{temp[row][2]:30}  \t{temp[row][3]} ")

    def re_index(self) -> None:
        with open(self.file, mode='r') as file:
            reader = csv.DictReader(file, fieldnames=self.fields)
            data = [row for row in reader]
            self.display(data)
            new_id = [index for index in range(1, len(data) + 1)]

        with open(self.file, mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            new_data = [row|{"Id": new}  for row, new in zip(data, new_id) ]
            writer.writerows(new_data)

    def add(self) -> None:
        with open(self.file, "r+") as file:
            reader = csv.DictReader(file, fieldnames=self.fields)
            writer = csv.DictWriter(file, fieldnames=self.fields)
            last_id = int([row["Id"] for row in reader][-1]) +1
            new_data = {
                'Id': last_id ,
                'Date': self.date.strftime('%d-%b-%Y %I:%M %p'),
                'Description': self.description,
                'Amount': self.amount
            }
            writer.writerow(new_data)

tracker_app("hari ini gacoan", 50).list()