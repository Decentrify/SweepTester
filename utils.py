__author__ = 'alidar'


def escape_quotes(str):
    return str.replace("\'", '"')


def get_webservice_call_result(returned_data):

    status_key = "status"
    reason_key = "reason"

    if status_key in returned_data:
        status = returned_data[status_key]
        if status == "success":
            return True, returned_data[reason_key]
        else:
            return False, returned_data[reason_key]

    return True, ""

