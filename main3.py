import random

yourDict = {"w": -1, "s": 1, "g": 0}
reversDict = {1: "snake", -1: "water", 0: "gun"}

print("Welcome to Snake-Water-Gun Game!")
print("Type 'exit' anytime to quit game.\n")

while True:
    youstr = input("Enter your choice (w/s/g): ").lower()
    
    if youstr == "exit":
        break
    
    if youstr not in yourDict:
        print("❌ Invalid input! Please enter only 'w', 's', or 'g'.\n")
        continue

    you = yourDict[youstr]
    computer = random.choice([-1, 1, 0])

    print(f"\nYou chose     ➤ {reversDict[you]}")
    print(f"Computer chose ➤ {reversDict[computer]}")

    if you == computer:
        print("👉 It's a draw!\n")
    elif (computer == -1 and you == 1) or \
         (computer == 1 and you == 0) or \
         (computer == 0 and you == -1):
        print("🎉 You won!!\n")
    else:
        print("😞 You lose\n")


print(" Thanx for playing 😎")
