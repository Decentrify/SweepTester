__author__ = 'alidar'

import json
import time
import logging

import webservice
import utils


def do_insert(host, port, total_request, interval, index_name, args):

    file_name_key = 'fileName'
    logging.info("Starting Insert")

    for i in range(total_request):

        new_index_name = index_name + str(i)

        add_dict = {'url': "Test URL", file_name_key: new_index_name, 'fileSize': 1, 'language': 'English',
                    'category': 'Video', 'description': 'Test Desc'}
        args_dict = {}

        if args is not None:
            args_dict = json.loads(utils.escape_quotes(args))

        body_dict = dict(add_dict.items() + args_dict.items())

        logging.info("Inserting %s", body_dict[file_name_key])

        result = webservice.call(host, port, "PUT", "/add", body_dict)

        status = utils.get_webservice_call_result(result)

        if status[0]:
            logging.info("Returned data: %s", result)
        else:
            logging.info("FAILED with reason: %s", status[1])

        # don't sleep for the last iteration. All calls have been completed.
        if i != (total_request - 1):
            time.sleep(interval)

    logging.info("Ending Insert")