import csv
from collections.abc import Iterator
from datetime import datetime

class tracker_app:

    def __init__(self) -> None:

        self.date: datetime = datetime.now()
        self.fields: list = ['Id','Date', 'Description', 'Amount']
        self.file: str = 'data.csv'

    def read_file(self) -> Iterator[list[str]] :
        with open(self.file, mode='r') as file:
            csv_read = csv.reader(file)

            data = (row for row in csv_read)

            for row in data:
                yield row

    def write_file(self, mode: str, data) -> None:
        with open(self.file, mode=mode, newline='') as file:

            writer = csv.writer(file)

            if mode == 'w':
                writer.writerows(data)
            elif mode == 'a':
                writer.writerow(data)

    def re_index(self) -> None:
        reader = self.read_file()

        data = [index for index in reader]

        for i, row in enumerate(data):
            data[i][0] = str(i+1)

        self.write_file('w', data)

    def add(self, description: str, amount: float) -> None:
        reader = self.read_file()

        ids: list[int] = [int(row[0]) for row in reader]

        last_id: int = ids[-1]+1 if ids else 1

        new_data: list[str] = [
            last_id ,
            self.date.strftime('%d-%m-%Y %I:%M %p'),
            description,
            amount
        ]

        self.write_file('a', new_data)

    def list(self) -> None:
        reader = self.read_file()

        print("ID\tDate\t\t\tDescription\t\t\t\tAmount")
        for row in reader:
            print(f" {row[0]:5}  {row[1]}  \t{row[2]:30}  \t${row[3]} ")

    def delete(self, id: int) -> None:
        reader = self.read_file()
        temp = []

        for row in reader:
            if int(row[0]) != id:
                temp.append(row)

        self.write_file('w', temp)

        self.re_index()
        print("Expense deleted succesfully")

    def sum(self):
        reader = self.read_file()
        count = 0

        for row in reader:
            count += int(row[3])

        print(f"Total expenses: ${count}")

