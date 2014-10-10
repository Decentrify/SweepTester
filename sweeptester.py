__author__ = 'alidar'

import argparse
import traceback
import logging

import insert
import search


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("command", choices=["insert", "search"])
        parser.add_argument("host", help="Host address")
        parser.add_argument("port", help="Port on the host", type=int)
        parser.add_argument("total_requests", help="Total requests", type=int)
        parser.add_argument("interval", help="Interval in seconds between between requests", type=int)

        parser.add_argument("-n", "--name", help="Starting name of the index. If not given 'sweep' will be used",
                            default="sweep")
        parser.add_argument("-a", "--args", help="Other args in key value format e.g {'key':value, ...}", default=None)
        parser.add_argument("-o", "--output-file-path", help="Output file path", default=None)

        command = parser.parse_args()

        if command.output_file_path is not None:
            logging.basicConfig(filename=command.output_file_path, level=logging.INFO)
        else:
            logging.getLogger().setLevel(logging.INFO)

        if command.command == "insert":
            insert.do_insert(command.host, str(command.port), command.total_requests, command.interval, command.name,
                             command.args)
        else:
            command.command == "search"
            search.do_search(command.host, str(command.port), command.total_requests, command.interval, command.name,
                             command.args)
    except:
        traceback.print_exc()
        pass


if __name__ == "__main__":
    main()