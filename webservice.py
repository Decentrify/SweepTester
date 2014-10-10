__author__ = 'alidar'

import httplib
import json


def call(host, port, method, resource_path, body):
    headers = {"Content-type": "application/json"}
    conn = httplib.HTTPConnection(host, port)
    conn.request(method, resource_path, json.dumps(body), headers)
    response = conn.getresponse()
    data = response.read()

    return json.loads(data)

