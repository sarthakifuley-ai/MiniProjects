def attendance_percentage(attended, total):
    return (attended / total) * 100
attended = int(input("Classes Attended: "))
total = int(input("Total Classes Conducted: "))
percentage = attendance_percentage(attended, total)
print(f"Attendance Percentage = {percentage:.2f}%")
if percentage >= 75:
    print("Eligible")
else:
    target = 75
    extra = 0
    while ((attended + extra) / (total + extra)) * 100 < target:
        extra += 1
    print("Not Eligible")
    print(f"Attend at least {extra} more classes to reach 75%")