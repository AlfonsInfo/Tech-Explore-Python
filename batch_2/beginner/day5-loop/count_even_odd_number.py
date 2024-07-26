total_input = int(input("Enter the number of people: "))
total_even = 0
total_odd = 0
for i in range(total_input):
    input = int(input(f"Enter the number of person {i+1}: "))
    if input % 2 == 0:
        total_even += 1
    else:
        total_odd += 1
print(f"Total even numbers: {total_even}")
print(f"Total odd numbers: {total_odd}")
