#using random module
# winning rules as follows:
# Rock vs paper->paper wins
# Rock vs scissor->Rock wins
# paper vs scissor->scissor win

import random
choices = ["rock", "scissor", "paper"]

while True:
    ccount = 0  # Computer score
    ucount = 0  # User score

    
    try:
        user_choice = int(input('''
🎮 Game Start...
1️⃣ - Yes
2️⃣ - No (Exit)
Your choice: '''))

        if user_choice != 1:
            print("👋 Thanks for playing! See you next time!")
            break  

        for _ in range(5): 
            try:
                userInput = int(input('''
🪨 1 - Rock
✂️ 2 - Scissor
📄 3 - Paper
Your choice: '''))

                if userInput not in [1, 2, 3]:
                    print("❌ Invalid choice! Please enter 1️⃣, 2️⃣, or 3️⃣.")
                    continue  

                
                uchoice = choices[userInput - 1]
                Cchoice = random.choice(choices)

                print(f"\n🖥️ Computer chose: {Cchoice}")
                print(f"🙋‍♂️ You chose: {uchoice}")

                # Game logic
                if Cchoice == uchoice:
                    print("🤝 It's a Draw!")
                elif (uchoice == "rock" and Cchoice == "scissor") or \
                     (uchoice == "paper" and Cchoice == "rock") or \
                     (uchoice == "scissor" and Cchoice == "paper"):
                    print("🎉 You Win!")
                    ucount += 1
                else:
                    print("💻 Computer Wins!")
                    ccount += 1

            except ValueError:
                print("❌ Invalid input! Please enter a number (1️⃣, 2️⃣, or 3️⃣).")

        # Display Final Result
        print("\n---- 🏆 Final Score 🏆 ----")
        print(f"🙋‍♂️ User Score: {ucount}")
        print(f"🖥️ Computer Score: {ccount}")

        if ucount > ccount:
            print("🎉🥳 You Won the Game! 🏆🎊")
        elif ucount < ccount:
            print("💻😈 Computer Wins the Game! 🏆💻")
        else:
            print("🤝 It's a Draw! 🤝")

    except ValueError:
        print("❌ Invalid input! Please enter a number (1️⃣ or 2️⃣).")  
