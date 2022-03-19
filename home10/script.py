from subprocess import (
    run, PIPE
)
import re
from collections import defaultdict
from datetime import datetime
from datetime import date

# By default, stdout and stderr are not captured, and those attributes will be None
result = run(["ps", "aux"], capture_output=True)
str_process = str(result.stdout)
str_process = str_process.split(r"\n")
del str_process[0]
str_process.remove("'")
idx = 0
dict_tasks = {"users": {}, "total_cpu": 0, "total_memory": 0}
dict_process = defaultdict(lambda: {"name": "", "cpu": 0, "memory": 0})
for line in str_process:
    idx += 1
    user = re.search("\w*", line).group()
    list_cpu_mem = re.findall("\d{1,3}\.\d{1,3}", line)
    cpu = list_cpu_mem[0]
    mem = list_cpu_mem[1]
    split_line = line.split(" ")
    name_process = split_line[len(split_line)-1]
    dict_process[idx]["name"] = name_process[0:20]
    dict_process[idx]["cpu"] = float(cpu)
    dict_process[idx]["memory"] = float(mem)
    dict_tasks["total_cpu"] += float(cpu)
    dict_tasks["total_memory"] += float(mem)
    if user in dict_tasks["users"].keys():
        dict_tasks["users"][user] += 1
    else:
        dict_tasks["users"][user] = 1
max_cpu = 0
max_mem = 0
for key in dict_process:
    if dict_process[key]['cpu'] > max_cpu:
        max_cpu = dict_process[key]['cpu']
    if dict_process[key]['memory'] > max_mem:
        max_mem = dict_process[key]['memory']
current_date = str(date.today())
current_time = f"{datetime.now().hour}:{datetime.now().minute}"

with open(f"{current_date}-{current_time}-scan.txt", "w") as f:
    f.write("Отчёт о состоянии системы:\n")
    f.write(f"Пользователи системы:{list(dict_tasks['users'].keys())}\n")
    f.write(f"Процессов запущено: {idx}\n")
    f.write("Пользовательских процессов:\n")
    for key in dict_tasks['users']:
        f.write(f"{key}: {dict_tasks['users'][key]}\n")
    f.write(f"Всего памяти используется: {dict_tasks['total_memory']}%\n")
    f.write(f"Всего CPU используется: {dict_tasks['total_cpu']}%\n")
    for key in dict_process:
        if dict_process[key]['memory'] == max_mem:
            f.write(f"Больше всего памяти использует: {dict_process[key]['name']} - {max_mem}%\n")
        if dict_process[key]['cpu'] == max_cpu:
            f.write(f"Больше всего CPU использует: {dict_process[key]['name']} - {max_cpu}%\n")

print("Отчёт о состоянии системы:\n")
print(f"Пользователи системы:{list(dict_tasks['users'].keys())}\n")
print(f"Процессов запущено: {idx}\n")
print("Пользовательских процессов:\n")
for key in dict_tasks['users']:
    print(f"{key}: {dict_tasks['users'][key]}\n")
print(f"Всего памяти используется: {dict_tasks['total_memory']}%\n")
print(f"Всего CPU используется: {dict_tasks['total_cpu']}%\n")
for key in dict_process:
    if dict_process[key]['memory'] == max_mem:
        print(f"Больше всего памяти использует: {dict_process[key]['name']} - {max_mem}%\n")
    if dict_process[key]['cpu'] == max_cpu:
        print(f"Больше всего CPU использует: {dict_process[key]['name']} - {max_cpu}%\n")

