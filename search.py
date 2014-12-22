__author__ = 'alidar'

import time
import json
import logging

import webservice
import utils


def do_search(host, port, total_request, interval, index_name, args, append_number_to_index_name=True):
    file_name_key = 'fileNamePattern'

    logging.info("Starting Search")

    for i in range(total_request):

        new_index_name = index_name
        if append_number_to_index_name:
            new_index_name += str(i)

        name_dict = {file_name_key: new_index_name, 'category': 'Video'}
        args_dict = {}

        if args is not None:
            args_dict = json.loads(utils.escape_quotes(args))

        body_dict = dict(name_dict.items() + args_dict.items())

        logging.info("Searching %s", body_dict[file_name_key])

        result = webservice.call(host, port, "PUT", "/search", body_dict)

        status = utils.get_webservice_call_result(result)

        if status[0]:
            logging.info("%d items Returned: %s", len(result), result)
        else:
            logging.info("FAILED with reason: %s", status[1])

        # don't sleep for the last iteration. All calls have been completed.
        if i != (total_request - 1):
            time.sleep(interval)

    logging.info("Ending Search")