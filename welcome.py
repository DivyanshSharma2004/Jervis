import pyttsx3

def read_todo_list(file_path):
    try:
        with open(file_path, 'r') as file:
            todo_items = file.readlines()
        return [item.strip() for item in todo_items]
    except FileNotFoundError:
        return ["Your to-do list file is missing. Please create a file named todo_list.txt."]

def welcome_message():
    engine = pyttsx3.init()
    engine.say("        what is goody gang Welcome back! Have a great day code maxxing!")

    todo_items = read_todo_list("C:/Users/divme/OneDrive/Desktop/Welcome/todo_list.txt")
    if todo_items:
        engine.say("Here are your to-do items for today:")
        for item in todo_items:
            engine.say(item)
    else:
        engine.say("You have no items on your to-do list.")
    
    engine.runAndWait()

if __name__ == "__main__":
    welcome_message()