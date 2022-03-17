import os
import socket
import re
from http import HTTPStatus

from helpers import get_open_port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    srv_addr = ('', get_open_port())
    print(f'starting on {srv_addr}, pid: {os.getpid()}')

    s.bind(srv_addr)
    s.listen(1)

    while True:
        conn, raddr = s.accept()
        print(conn)
        while True:
            data = conn.recv(1024)
            text = data.decode('utf-8')
            if text:
                method = re.search("(POST|GET|PUT|DELETE|HEAD|OPTIONS|CONNECT|TRACE|PATCH)", text).group()
                result_str = f'<p> Request Method: {method} </p>'
                status = re.search("status=\w*", text)
                if status is not None:
                    try:
                        status_code = int(status.group().strip("status="))
                    except ValueError:
                        status_code = 200
                    name_status = HTTPStatus(status_code).phrase
                    result_str = result_str + f'<p> Request Status: {status_code} {name_status} </p>'
                else:
                    result_str = result_str + f'<p> Request Status: 200 OK</p>'
                headers = text.split("\r\n")
                del headers[0]
                result_str = result_str + f'<p> Request Source: {raddr}</p>'
                status_line = 'HTTP/1.1 200 OK'
                for i in range(len(headers)):
                    result_str = result_str + f"<p> {headers[i]} </p>"
                resp = '\r\n\r\n'.join([
                    status_line,
                    result_str
                ])
                sent_bytes = conn.send(resp.encode('utf-8'))
            else:
                print(f'no data from {raddr}')
                break
        conn.close()
