enemies =1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies are now {enemies}")

increase_enemies()
print(enemies)