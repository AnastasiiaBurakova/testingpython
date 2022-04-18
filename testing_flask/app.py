from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "Welcome Home"
    
    text = """It's a nice sunny day of your vacation. You come to a little village to visit your grandma. When you enter the house, you notice that something's off about your grandma."""

    choices = [
        ('talk_grandma',"Ask if she is feeling alright"),
        ('run_away',"Run away as fast as you can!!!")
    ]


    return render_template('home.html', title=title, text=text, choices=choices)



@app.route("/talk")
def talk_grandma():
    title = "You ask if grandma is okay..."
    
    text = """... and when she starts talking you notice that her ears are bigger than normal, her mouth is bigger, her hands don't look the same. Her teeth are like those of an animal but she says that she's just a bit tired and that you should come and give her a hug."""

    choices = [
        ('give_hug',"Go hug your grandma"),
        ('run_away',"Try to escape out the front door")
    ]

    return render_template('talk.html', title=title, text=text, choices=choices)

@app.route("/escape")
def run_away():
    title = "You run away!"
    
    text = """You safely escape and go back to the city. Who knows what could have happened. Those grandmas are unpredictable."""

    choices = []

    return render_template('escape.html', title=title, text=text, choices=choices)



@app.route("/hug")
def give_hug():
    title = "Deadly Hug!"
    
    text = """As you come and hug your grandma, she starts tearing you apart with her claws. First, she eats your legs and arms. Then, she feasts on your brain. It was never actually your grandma but a disguised wolf."""

    choices = []

    return render_template('hug.html', title=title, text=text, choices=choices)


@app.route("/fizzbuzz/<int:i>")
def FizzBuzz(i):
    l = []
    for i in range(1, i+1):

        if (i % 3 == 0 and i % 5 != 0):
            l.append ('Fizz')
        elif (i % 5 == 0 and i % 3 != 0):
            l.append ('Buzz')
        elif (i % 3 == 0 and i % 5 == 0):
            l.append ('FizzBuzz')
        else: 
            l.append (i)   
    return render_template('fizzbuzz.html', numbers=l)


@app.route("/words/<string:word>")
def words(word):
    f = open("words.txt")

    word_list = f.read().splitlines()

    is_real_word = word.upper() in word_list

    anagrams = []
    for w in word_list:
        if sorted(word.upper()) == sorted(w):
            anagrams.append(w)
    
    return render_template('words.html', word=word, is_real_word=is_real_word, anagrams=anagrams)
