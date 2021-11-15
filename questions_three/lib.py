# try_me test function
from random import randint

def try_me():
    print("What is your name?")
    name = input()
    print("What is your quest?")
    quest = input()
    question3_list = ["What is your favorite color?",
                      "What is the capital of Assyria?",
                      "What is the average airspeed velocity of an unladen swallow?"]
    q = randint(0, len(question3_list)-1)
    print(question3_list[q])
    answer = input()
    print("You may pass.\n")
    questions_three = {"Name": name, "Quest": quest, "Answer": answer}
    return questions_three

if __name__ == "__main__":
    print(try_me())
