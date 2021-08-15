from survey import AnonymousSurvey

question = "Which language did you learn first?"

mysurvey = AnonymousSurvey(question)

mysurvey.display_question()
print("Enter 'q' to quit")
while True:
    answer = input("Language: ")
    if (answer == 'q'):
        break
    else:
        mysurvey.store_response(answer)

print("Thank you all for participating. Here are the results of the survey")
mysurvey.show_result()