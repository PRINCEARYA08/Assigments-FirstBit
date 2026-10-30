D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter amount: "))
count = 0

for note in D:
    notes = amount // note    
    
    amount = amount % note
    count += notes

    if notes > 0:
        print(f"₹{note} notes = {notes}")

print("Minimum number of notes:", count)