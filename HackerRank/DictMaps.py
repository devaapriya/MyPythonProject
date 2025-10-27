import sys

num = int(input())

phone_book = {}
for n in range(num):
    phone_book_entry = input().strip().split()
    name, number = phone_book_entry[0], phone_book_entry[1]
    phone_book[name] = number

name_from_user = []
count = 0
for name in sys.stdin:
    name = name.strip()
    count += 1
    if len(name) <= 0:
        break
    name_from_user.insert(count, name)

# print(name_from_user)
for name in name_from_user:
    if name in phone_book:
        print(f"{name}={phone_book[name]}")
    else:
        print("Not found")