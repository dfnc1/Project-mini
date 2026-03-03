import csv
from collections.abc import Iterator

class Utill:
    def __init__(self) -> None:
        self.file: str = 'src/data.csv'

    def read_file(self) -> Iterator[list[str]]:
        with open(self.file, mode='r', newline='') as file:
            yield from csv.reader(file)


    def write_file(self, mode: str, data) -> None:
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
            rows[i][0] = str(i + 1)

        self.write_file('w', rows)

    def next_id(self) -> int:
        last_id = 0
        for row in self.read_file():
            last_id = int(row[0])

        return last_id + 1
