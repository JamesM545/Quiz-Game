UserName = str(input("Enter your name: "))
print("Hello", UserName, ", let's play thq quiz!")


# defining a function to get questions
def play_quiz():
    # set score counter equal to 0
    global counter
    counter = 0
    # open file containing the questions in read mode
    questions = open("questions.txt", "r")
    # translate file contents into a list
    question_set = questions.readlines()
    for questions in question_set:
        # split all questions to to separate lines after each comma
        questions = questions.split(",")
        # Answer to each question is last number in list
        answer = int(questions[-1])
        # pop the last number in the list so it is not displayed to the user
        questions.pop(-1)
        # display each question to the user
        for questionLines in questions:
            print(questionLines)
        # prompt the user for an answer
        user_input = input("Enter your answer: ")
        # lowercase all letters of the user's answer and check against the correct answer in questions list.
        if user_input.lower() == questions[answer].lower():
            # if above statement is true, add 1 to counter
            counter = counter + 1
            # display answer correct message to user
            print("That's Correct, You have been awarded 1 point!")
        else:
            # if statement above is false, display message to user
            print("That's not quite right")
    # At the end of the quiz, show the user's score
    print("Thank you for completing the quiz. You got", counter, "questions correct!")


play_quiz()


def player_result():
    # import the date module
    import datetime
    # append the results of the quiz into a file named results.txt. If doesn't exist, create file.
    save_score = open("results.txt", "a+")
    player_score = str(counter)
    date = str(datetime.date.today())
    save_score.write("Name: " + UserName + "," + " Score: " + player_score + "," + " Date Completed: " + date + "\n")
    save_score.close()


player_result()


def leaderboard():
    print("+-------------------------------+")
    print("|----------LEADERBOARD----------|")
    print("+-------------------------------+")
    entries = open("results.txt", "r")
    entry = entries.readlines()
    for entries in entry:
        entries = entries.split(",")
        for user_entry in entries:
            print(user_entry)


leaderboard()
