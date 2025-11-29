import pickle

all_emps = []

with open("empl.dat", "rb") as f:
    try:
        while True:
            rec = pickle.load(f)
            all_emps.append(rec)
    except EOFError:
        pass

# PRINT OLD RECORDS
print("Old records in file:")
for emp in all_emps:
    print(emp)

# ---------- Step 3: update salary of empno 1251 ----------
for emp in all_emps:
    if emp["empno"] == 1251:
        emp["salary"] += 2000

# ---------- Step 4: wipe file and write ALL records back ----------
with open("empl.dat", "wb") as f:
    for emp in all_emps:
        pickle.dump(emp, f)

# ---------- Step 5: print updated records ----------
print("\nUpdated records in file:")
with open("empl.dat","rb") as f:
    try:
        while True:
            rec_new = pickle.load(f)
            print(rec_new)
    except EOFError:
        pass

