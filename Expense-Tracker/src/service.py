from datetime import datetime
from src import Utill

class Service:
    def __init__(self) -> None:
        self.date: datetime = datetime.now()
        self.utill = Utill()

    def add(self, description: str, amount: float) -> None:
        new_data: list[str] = [
            self.utill.next_id(),
            self.date.strftime('%d-%m-%Y'),
            description,
            amount
        ]
        self.utill.write_file('a', new_data)

    def list(self) -> None:
        print(f"{"ID":5}{"Date":15}{"Description":30}{"Amount"}")
        for row in self.utill.read_file():
            print(f"{row[0]:5}{row[1]:15}{row[2]:30}${row[3]}")

    def delete(self, id: int) -> None:
        temp = []
        for row in self.utill.read_file():
            if int(row[0]) != id:
                temp.append(row)

        self.utill.write_file('w', temp)
        self.utill.re_index()
        print("Expense deleted succesfully")

    def sum(self, by_month: str | None = None) -> None:
        count = 0
        for row in self.utill.read_file():
            month = row[1].split("-")[1].lstrip("0")

            if not by_month or month == by_month:
                count += int(row[3])

        print(f"Total expenses: ${count}")
