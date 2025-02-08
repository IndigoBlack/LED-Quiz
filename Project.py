import requests
import random
from gpiozero import LED
from time import sleep




def main():
    green = LED(21)
    red = LED(16)
    green.off()
    red.off()
    answer = questions()
    if answer == True:
        green.on()
        sleep(2)
        green.off()
    else:
        red.on()
        sleep(2)
        red.off()

def questions():
    url = "https://opentdb.com/api.php?amount=5&category=9&type=multiple"
    response = requests.get(url)
    try:
        data = response.json()
        question = data['results'][0]['question']
        correct = data['results'][0]['correct_answer']
        incorrect = data['results'][0]['incorrect_answers']
        choose = incorrect + [correct]
        random.shuffle(choose)
        print(question)
        letters = "ABCD"
        for i, j in enumerate(choose):
            print(f"{letters[i]}: {j}")
        s = input("Choose the correct letter: ").upper().strip()
        while validate(s) == False:
            s = input("Choose the correct letter: ").upper().strip()
        index = letters.index(s)
        user_choice = choose[index]
        if user_choice == correct:
            print("Correct")
            return True
        else:
            print(f"Incorrect\nThe corrected answer is {correct}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error, couldn't get question because of {e}")
        return False


def validate(s):
    let = ['A', 'B', 'C', 'D']
    if len(s) != 1:
        print("Answer should be 1 letter")
        return False
    elif s not in let:
        print("Answer should be a letter from A to D")
        return False
    else:
        return True


if __name__ == "__main__":
    main()
