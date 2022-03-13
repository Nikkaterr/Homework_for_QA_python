import argparse
import re
import json
from collections import defaultdict
from collections import Counter
import os


def pars_log(filename):
    dict_ip = defaultdict(
        lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
    )
    dict_time = defaultdict(
        lambda: {"time": "", "ip": "", "method": "", "url": "", "date": ""}
    )
    idx = 0
    with open(filename) as file:

        for line in file:
            ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            time_match = re.search(r"\d{1,5}$", line)
            date_match = re.search(r"\d{1,2}\S\w{3}\S\d{4}\S\d{2}\S\d{2}\S\d{2}", line)
            url_match = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                   line)
            if ip_match is not None:
                ip = ip_match.group()
                method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line)
                if method is not None:
                    dict_ip[ip][method.group(1)] += 1
            if time_match is not None:
                dict_time[idx]["time"] = time_match.group()
                if ip_match is not None:
                    dict_time[idx]["ip"] = ip
                else:
                    dict_time[idx]["ip"] = "-"
                if method is not None:
                    dict_time[idx]["method"] = method.group().replace('] \"', '')
                else:
                    dict_time[idx]["method"] = "-"
                if len(url_match) != 0:
                    dict_time[idx]["url"] = url_match[0]
                else:
                    dict_time[idx]["url"] = "-"
                dict_time[idx]["date"] = date_match.group()
            idx += 1

    top_ip = {}

    for key in dict_ip:
        count = 0
        ip = dict_ip[key]
        for method in ip:
            count += ip[method]
        top_ip[key] = count

    c_ip = Counter(top_ip)
    top_ip_list = c_ip.most_common(3)

    top_time_list = {}
    for key in dict_time:
        top_time_list[key] = int(dict_time[key]["time"])
    c_time = Counter(top_time_list)
    top_time_list = dict(c_time.most_common(3))

    if "\\" in filename:
        path_head = os.path.split(filename)[0]
        path_tail = os.path.split(filename)[1]
        result_json = f"{path_head}\\result_for_{path_tail}.json"
    else:
        result_json = f"result_for_{filename}.json"

    with open(result_json, "w") as f:
        f.write(f"Common counter of requests: {idx}\n")
        f.write("Top 3 IP addresses from which requests were made:\n")
        for key in dict(top_ip_list):
            f.write(f" - {key} : {dict(top_ip_list)[key]}\n")
        f.write("Top 3 long requests:\n")
        for key in top_time_list:
            f.write(json.dumps(dict_time[key], indent=4))
        f.write("\nCounter of HTTP-requests by ip addresses:\n")
        s = json.dumps(dict_ip, indent=4)
        f.write(s)
        f.close()

    print(f"For {filename}:\n")
    print(f"Common counter of requests: {idx}")
    print("Top 3 IP addresses from which requests were made:")
    for key in dict(top_ip_list):
        print(f" - {key} : {dict(top_ip_list)[key]}\n")
    print("Top 3 long requests:")
    for key in top_time_list:
        print(json.dumps(dict_time[key], indent=4))
    print("\nCounter of HTTP-requests by ip addresses:")
    print(json.dumps(dict_ip, indent=4))


parser = argparse.ArgumentParser(description='Process access.log')
parser.add_argument('-f', dest='file', action='store', help='Path to logfile')
args = parser.parse_args()
if os.path.exists(args.file):
    if os.path.isfile(args.file):
        if os.path.splitext(args.file)[1] == '.log':
            pars_log(args.file)
        else:
            print(f" File: {args.file} is not log")
    elif os.path.isdir(args.file):
        list_all_in_dir = os.listdir(args.file)
        count_log = 0
        for i in range(len(list_all_in_dir)):
            if '.log' in list_all_in_dir[i]:
                count_log += 1
                path_to_file = os.path.join(args.file, list_all_in_dir[i])
                pars_log(path_to_file)
        if count_log == 0:
            print(f" Directory {args.file} has not .log files")
else:
    print(f"{args.file} is not found")
