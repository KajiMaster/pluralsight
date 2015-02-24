import random

def main():
    # User enters question
    print("Ask the 8 ball your question!")
    question = input('--> ')
    print("You asked: {}".format(question))

    # 20 8 ball responses
    responses = ["Yes", "No", "All signs point to yes.", "Ask again later",
    			 "Very likely", "Future un-clear", "Very doubtful",
    			 "Concentrate, and ask again", "I'm trying to sleep", "Outlook not so good",
    			 "Possibly", "Sure", "Not a chance", "Are you kidding me?", "Quit asking me questions",
    			 "I'm getting annoyed", "Yes", "No", "I don't care", "Why are you asking me?"]

    # Display progress and choose answer
    print("Thinking...")
    print(" ")
    answer = responses[random.randint(0, 19)]
    print(answer)

    # Allow another question to be asked.
    print("Would you like to ask another question? y/n")
    again = input('--> ')
    if again == 'y':
        main()

if __name__ == '__main__':
    main()