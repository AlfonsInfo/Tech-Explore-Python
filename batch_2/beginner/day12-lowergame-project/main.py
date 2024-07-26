question_banks = [
    {"Who has more followers, Ronaldo(A) or Messi(B)?" : "A"},
    {"Who has more followers, Instagram(A) or Facebook(B)?" : "A"},
    {"Who has more followers, Youtube(A) or Twitter(B)?" : "B"},
    {"Who has more followers, Tiktok(A) or Snapchat(B)?" : "B"},
    {"Who has more followers, Netflix(A) or Amazon Prime(B)?" : "A"},
]
isPlaying = True
while isPlaying:
    score = 0
    for question in question_banks:
        for q, a in question.items():
            print(q)
            answer = input("Enter A or B: ").upper()
            if answer == a:
                score += 1
    print(f"Your score is {score}")
    isPlaying = False
    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again == "Y":
        isPlaying = True