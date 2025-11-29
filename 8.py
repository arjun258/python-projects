months = {
    "january": 31, "february": 28, "march": 31, "april": 30,
    "may": 31, "june": 30, "july": 31, "august": 31,
    "september": 30, "october": 31, "november": 30, "december": 31
}

def get_days(item):
    return item[1]

# (a)
m = input("Enter month name: ")
print("Days:", months.get(m.lower(), "Invalid month"))

# (b)
print("\nMonths in alphabetical order:")
print(sorted(months.keys()))

# (c)
print("\nMonths with 31 days:")
for k, v in months.items():
    if v == 31:
        print(k)

# (d)
print("\nSorted by number of days:")
for k, v in sorted(months.items(), key=get_days):
    print(k, v)
