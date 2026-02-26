import csv
from datetime import datetime
from xxlimited_35 import Null


class tracker_app:

    def __init__(self) -> None:
        self.date: datetime = datetime.now()
        self.fields: list = ['Id','Date', 'Description', 'Amount']
        self.file: str = 'data.csv'

    def re_index(self) -> None:

        with open(self.file, mode='r') as file:
            reader = csv.DictReader(file, fieldnames=self.fields)
            data = [row for row in reader]
            new_id = [index for index in range(1, len(data) + 1)]

        with open(self.file, mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            new_data = [row|{"Id": new}  for row, new in zip(data, new_id) ]
            writer.writerows(new_data)

    def add(self, description: str, amount: float) -> None:

        with open(self.file, "r+") as file:
            reader = csv.DictReader(file, fieldnames=self.fields)
            writer = csv.DictWriter(file, fieldnames=self.fields)
            ids: list[int] = [int(row["Id"]) for row in reader]
            last_id: int = ids[-1]+1 if ids else 1
            new_data: dict = {
                'Id': last_id ,
                'Date': self.date.strftime('%d-%b-%Y %I:%M %p'),
                'Description': description,
                'Amount': amount
            }
            writer.writerow(new_data)


    def list(self) -> None:

        with open(self.file, mode='r') as file:
            reader = csv.DictReader(file, fieldnames=self.fields)
            data: list[list] = [list(row.values()) for row in [row for row in reader]]

            print("ID\tDate\t\t\tDescription\t\t\t\tAmount")
            for row in range(len(data)):
                print(f" {data[row][0]:5}  {data[row][1]}  \t{data[row][2]:30}  \t{data[row][3]} ")

    def delete(self, id: int) -> None:
        with open(self.file, mode='r+') as file:
            reader = csv.DictReader(file, fieldnames=self.fields)
            data: list[list] = [list(row.values()) for row in [row for row in reader]]

            for row in range(len(data)):
                if data[row][0] == id:
                    del data[row]
            print(data)




tracker_app().add("lunch", 20)