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
                result = list()
                result.append(f'Request Method: {method}')
                status = re.search("status=\w*", text)
                if status is not None:
                    try:
                        status_code = int(status.group().strip("status="))
                    except ValueError:
                        status_code = 200
                    name_status = HTTPStatus(status_code).phrase
                    result.append(f'Request Status: {status_code} {name_status}')
                    status_line = f'HTTP/1.1 {status_code} {name_status}'
                else:
                    result.append(f'Request Status: 200 OK')
                    status_line = f'HTTP/1.1 200 OK'
                headers_http = text.split("\r\n")
                del headers_http[0]
                result.append(f'Request Source: {raddr}')
                for i in range(len(headers_http)):
                    result.append(f"{headers_http[i]}")
                result_str = str()
                for i in range(len(result)):
                    result_str = result_str+f"{result[i]}\r\n"
                header = '\r\n'.join((
                    status_line,
                    f'Content-Length: {len(result_str)}',
                    f'Content-Type: text',
                    ))
                resp = '\r\n\r\n'.join([
                    header,
                    result_str
                ])
                sent_bytes = conn.send(resp.encode('utf-8'))
            else:
                print(f'no data from {raddr}')
                break
        conn.close()
