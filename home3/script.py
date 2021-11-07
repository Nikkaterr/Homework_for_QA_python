import json
import csv
from collections import OrderedDict

with open("users.json", "r") as f:
    users = json.loads(f.read())
    f.close()

with open('books.csv', newline='') as r:
    reader = csv.reader(r)
    header = next(reader)

    books = []

    for row in reader:
        books.append(row)
    r.close()

for i in range(len(books)):
    books[i][3] = int(books[i][3])
    books[i].pop(4)
    books[i][2], books[i][3] = books[i][3], books[i][2]

sort = []
for i in range(len(header)):
    header[i] = header[i].lower()
    if header[i] == "title":
        sort.insert(0, header[i])
    elif header[i] == "author":
        sort.insert(1, header[i])
    elif header[i] == "height":
        header[i] = "pages"
        sort.insert(2, header[i])
    elif header[i] == "genre":
        sort.insert(3, header[i])
    elif header[i] == "publisher":
        header.pop(i)

header = sort

keys_users = ["name", "gender", "address", "age"]
user_and_books = users
for i in range(len(user_and_books)):
    user_and_books[i] = {key: value for key, value in user_and_books[i].items() if key in keys_users}
    change_order = OrderedDict(user_and_books[i])
    change_order.move_to_end("age")
    user_and_books[i] = dict(change_order)

for i in range(len(user_and_books)):
    list_books = []
    j = 0
    while i + j < (len(books)):
        list_books.append(books[i + j])
        j = j + len(user_and_books)
    for w in range(len(list_books)):
        user_and_books[i].setdefault("books", []).append(dict(zip(header, list_books[w])))
    list_books.clear()

with open("result.json", "w") as f:
    s = json.dumps(user_and_books, indent=4)
    f.write(s)
    f.close()
