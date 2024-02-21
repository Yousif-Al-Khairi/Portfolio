from mood_interest import mood_interest_choices
from graph_creation import Vertex
from graph_creation import Graph
from graph_creation import activity_graph

#from graph_creation import *

choice_str = '\n'.join([f"{key}: {value}" for key, value in mood_interest_choices.items()])

list_lim = None
interest_list = None

def welcome_func():
    print("Welcome to the activity reccommender terminal application!!\n")

def explainer():
    print("Heres how it works, we'll give you a list of moods and interests that could interest you, and you pick as many (or as few) as you want. \nFrom that we'll do a search of our nice graph and find you the activities you could do in your boredom that would suit you best.")


def print_options():
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    if interest_list == None:
        print("You have not set any mood/interest preferences")
    else:
        print(f"You have set your interest/mood preference list as follows: {interest_list}")
    if list_lim == None:
        print("You have not set any limit for how many results you'd like returned to you")
    else:
        print(f"You have set your limit for the size of our reccommendation to be: {list_lim}")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Pick your options! Type the number corresponding to the option you want.\n")
    print("1. Set your preferences\n")
    print("2. Return a list of activities that match your preferences list\n")
    print("3. Get a re-explanation of how the program works\n")
    print("4. Reset your preferences\n")
    print("5. Exit the program.\n")
    

def pref_sub():
    choice = input("Type your preference or type 'end':\n")
    if choice.lower() != "end":
        if choice.lower() in list(mood_interest_choices.keys()):
            if mood_interest_choices[choice] not in interest_list:
                interest_list.append(mood_interest_choices[choice])
                print(f"Success! Added {mood_interest_choices[choice]} to your preference list, you can see the list on the bottom")
                print(str(interest_list))
                pref_sub()
            else:
                print(f"'{mood_interest_choices[choice]}' is already in your interest/mood list")
                pref_sub()
        else:
            pref_sub()
    else: 
        print(f"Great, your preferences have been set, your interests and moods have been given to us as the following:")
        for interest in interest_list:
            print(interest)
         
def pref_sub_2():
    global list_lim
    ans = input("\n")
    try:
        num = int(ans)
        if 1 <= num <= 100:
            list_lim = int(ans)
            print(f"Fantastic, you have set your list limit as {int(ans)}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        pref_sub_2()

def set_preferences():
    global interest_list
    global list_lim
    if interest_list == None:
        interest_list = []
    if len(interest_list) == len(list(mood_interest_choices.keys())):
        print("We've completely filled your list! All we can do now is let you change how large you want your list of suggestions to be.")
        pref_sub_2()
        return
    print("Wonderful, heres a list of the moods you could be in or your interests. Whichever applies to you, put in the letter, we'll save your perference and you will be asked to continue doing it until you type 'stop'.")
    print(choice_str)
    pref_sub()
    print("Great, now that you've picked your mood and interests, why don't you tell us how large you want your list of suggestions to be? Type a number between 1-100")
    pref_sub_2()
    
def find_activities():
    global interest_list
    global list_lim
    if interest_list == None or list_lim == None: 
        print("Please set your preferences before trying to generate a list!")
        return
    list, length = activity_graph.search(interest_list, list_lim)
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Based on your preferences regarding your interests and mood we think that the following activities would interest you: ")
    for activity in list:
        print(activity)
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def get_user_res():
    global interest_list
    global list_lim
    ans = input("Which choice would you like to make?\n")
    if int(ans) == 1:
        set_preferences()
    elif int(ans) == 2: 
        find_activities()
    elif int(ans) == 3: 
        explainer()
    elif int(ans) ==4:
        print("Resetting preferences!") 
        list_lim = None
        interest_list = None
    elif int(ans) == 5:
        print("Thanks for using the activity suggestion application, til next time!")
        exit()
    else: 
        print("Please type in either 1,2,3,4, or 5 to match the options we've given you ")
        get_user_res()

def appfunc():
    welcome_func()
    explainer()
    while True:
        print_options()
        get_user_res()

appfunc()