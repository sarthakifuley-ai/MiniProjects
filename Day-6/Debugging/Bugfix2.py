# BUGGY CODE

# total = sum(marks)
# average = total / 4      # Wrong calculation
# print("Average:", average)

# FIXED CODE
marks = []
for i in range(5):
    mark = float(input(f"Enter marks for Student {i+1}: "))
    marks.append(mark)
total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)
print("\n----- RESULT -----")
print("Total Marks   :", total)
print("Average Marks :", average)
print("Highest Marks :", highest)
print("Lowest Marks  :", lowest)
