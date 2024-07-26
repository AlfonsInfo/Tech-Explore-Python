# if divisible by 3, print "fizz"
# if divisible by 5, print "buzz"
# if divisible by 3 and 5, print "fizzbuzz"
for i in range(1,101):
    isFizz = i % 3 == 0
    isBuzz = i % 5 == 0
    if(isFizz and isBuzz):
        print("fizzbuzz")
    elif(isFizz):
        print("fizz")
    elif(isBuzz):
        print("buzz")
    else:
        print(i)    
