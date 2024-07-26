total_person = int(input("Enter the number of people: "))
total_height = 0
for i in range(total_person):
    height = int(input(f"Enter the height of person {i+1}: "))
    total_height += height
average_height = total_height // total_person
print(f"The average height is {average_height}")