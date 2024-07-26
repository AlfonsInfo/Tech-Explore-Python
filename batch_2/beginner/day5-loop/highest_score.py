total_person = int(input("Enter the number of people: "))
highest_score = 0
for i in range(total_person):
    score = int(input(f"Enter the score of person {i+1}: "))
    if(score > highest_score):
        highest_score = score

print(f"The highest score is {highest_score}")