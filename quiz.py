import pgzrun
import random

WIDTH = 1280
HEIGHT = 720


def make_question():
    number_1 = random.randint(1, 20)
    number_2 = random.randint(1, 20)

    operation = random.randint(1, 3)
    if operation == 1:
        a = number_1 + number_2
        qs = f"What is {number_1} + {number_2}?"
    elif operation == 2:
        a = number_1 - number_2
        qs = f"What is {number_1} - {number_2}?"
    else:
        a = number_1 * number_2
        qs = f"What is {number_1} * {number_2}?"

    answers = []
    s = 0
    for i in range(4):
        s += random.randint(1, 10)
        answers.append(s)

    pos = random.randint(0, 3)
    d = answers[pos]
    answers = [x - d + a  for x in answers]
    
    q = [qs]
    for x in answers:
        q.append(str(x))
    q.append(pos + 1)

    return q   


main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10
g = False

question = make_question()


def draw():
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index += 1
    

def game_over():
    global question, time_left, g
    g = True
    message = "Game over. You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0


def correct_answer():
    global question, score, time_left

    score += 1
    question = make_question()
    time_left = 10


def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):           
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print ("You got it correct!")
                correct_answer()
            else:
                game_over()
        index += 1


def update_time_left():
    global time_left

    if time_left:
        time_left -= 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)


def on_key_up(key):
    global g, score, time_left, question
    if g and key == keys.SPACE:
        print('space')
        question = make_question()
        score = 0
        time_left = 10
        g = False



pgzrun.go()