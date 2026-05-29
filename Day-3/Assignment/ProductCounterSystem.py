import random
target = int(input("Enter target units: "))
workers = int(input("Enter workers per shift: "))
defect_rate = int(input("Enter defect rate percentage: "))
total = 0
for shift in range(1, 4):
    produced = 0
    defects = 0
    print("\nShift", shift)
    for cycle in range(1, 21):
        if total >= target:
            break
        chance = random.randint(1, 100)
        if chance <= defect_rate:
            defects += 1
            print("Cycle", cycle, "- Defective Item")
            continue
        produced += 1
        total += 1
        print("Cycle", cycle, "- Item Produced")
    productivity = produced / workers
    print("Produced :", produced)
    print("Defects  :", defects)
    print("Productivity :", productivity)
    if total >= target:
        print("\nTarget Reached")
        break
print("\nTotal Items Produced =", total)