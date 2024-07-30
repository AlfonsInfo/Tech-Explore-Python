class User:
    def __init__(self,id, username):
        print("new user created!!")
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers+=1
        self.following+=1

user_1 = User(id="1001", username="alfonsus")
user_2 = User(id="1001", username="budi")
user_1.follow(user_2)
print(user_1.username)
print(user_1.following)
print(user_2.followers)

