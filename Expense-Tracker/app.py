import csv
from collections.abc import Iterator
from datetime import datetime

class tracker_app:

    def __init__(self) -> None:
        self.date: datetime = datetime.now()
        self.file: str = 'dat.csv'

    def read_file(self) -> Iterator[list[str]] :
        with open(self.file, mode='r', newline='') as file:
            yield from csv.reader(file)

    def write_file(self, mode: str , data) -> None:
        with open(self.file, mode=mode, newline='') as file:
            writer = csv.writer(file)

            if mode == 'w':
                writer.writerows(data)
            else:
                writer.writerow(data)

    def re_index(self) -> None:
        reader = self.read_file()

        rows = [row for row in reader]
        for i, row in enumerate(rows):
            rows[i][0] = str(i+1)

        self.write_file('w', rows)

    def next_id(self) -> int:
        last_id = 0
        for row in self.read_file():
            last_id = int(row[0])

        return last_id +1

    def add(self, description: str, amount: float) -> None:
        new_data: list[str] = [
            self.next_id() ,
            self.date.strftime('%d-%m-%Y'),
            description,
            amount
        ]
        self.write_file('a', new_data)

    def list(self) -> None:
        print("ID\tDate\t\t\tDescription\t\t\t\tAmount")
        for row in self.read_file():
            print(f" {row[0]:5}  {row[1]}  \t{row[2]:30}  \t${row[3]} ")

    def delete(self, id: int) -> None:
        temp = []
        for row in self.read_file():
            if int(row[0]) != id:
                temp.append(row)

        self.write_file('w', temp)
        self.re_index()
        print("Expense deleted succesfully")

    def sum(self, by_month: str | None = None) -> None:
        count = 0
        for row in self.read_file():
            month = row[1].split("-")[1].lstrip("0")

            if not by_month or month == by_month:
                count += int(row[3])

        print(f"Total expenses: ${count}")
