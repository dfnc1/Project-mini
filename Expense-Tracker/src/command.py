import argparse
from src import Service

class Command:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Expense Tracker CLI")
        self.subparser = self.parser.add_subparsers(dest="command", required=True)
        self.service = Service()
        self.register_command()

    def register_command(self) -> None:
        add_parser = self.subparser.add_parser("add", help="Add an entry")
        add_parser.add_argument("--description", type=str, help="Add an description", required=True)
        add_parser.add_argument("--amount", type=int, help="Add an amount", required=True)
        add_parser.set_defaults(func=lambda args: self.service.add(args.description, args.amount))

        list_parser = self.subparser.add_parser("list", help="List all entries")
        list_parser.set_defaults(func=lambda args: self.service.list())

        sum_parser = self.subparser.add_parser("summary", help="Show summary")
        sum_parser.add_argument("--month", type=str, help="Show summary by month")
        sum_parser.set_defaults(func=lambda args: self.service.sum(args.month))

        del_parser = self.subparser.add_parser("delete", help="Delete an entry")
        del_parser.add_argument("--id", type=int, help="Delete by id", required=True)
        del_parser.set_defaults(func=lambda args: self.service.delete(args.id))

    def run(self) -> None:
        args = self.parser.parse_args()
        args.func(args)