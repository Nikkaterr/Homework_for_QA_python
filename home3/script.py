import json
import csv


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


keys_users = ["name", "gender", "address", "age"]
user_and_books = users
for i in range(len(user_and_books)):
    user_and_books[i] = {key: value for key, value in user_and_books[i].items() if key in keys_users}

for i in range(len(user_and_books)):
    list_books = []
    j = 0
    while i+j < (len(books)):
        list_books.append(books[i+j])
        j = j+29
    for w in range(len(list_books)):
        user_and_books[i].setdefault("Books", []).append(dict(zip(header, list_books[w])))
    list_books.clear()

with open("result.json", "w") as f:
    s = json.dumps(user_and_books, indent=4)
    f.write(s)
    f.close()




