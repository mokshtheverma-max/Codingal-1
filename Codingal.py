print("Hi I Am an AI bot,whats your name")
name=input()
print(f"nice to meet you{name}")
print("How are you feeling today?good/bad")
mood=input().lower()
if mood=="good":
    print("I am glad to hear that!")
elif mood=="bad":
    print("I am Sorry to hear that,get better soon")
else:
    print("sorry i can understand")