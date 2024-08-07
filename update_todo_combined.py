import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What do you want to add to your to-do list?")
        audio = recognizer.listen(source)

        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Could not request results; check your internet connection.")
            return None

def update_todo_list(item):
    with open("todo_list.txt", "a") as file:
        file.write(f"{item}\n")
    speak("To-do list updated.")

def main():
    speak("Do you want to add something to your to-do list? Type 'yes' or 'no'.")
    response = input("Do you want to add something to your to-do list? (yes/no): ").strip().lower()
    
    if response in ["yes", "y"]:
        speak("Would you like to use voice input? Type 'yes' or 'no'.")
        use_voice = input("Would you like to use voice input? (yes/no): ").strip().lower()
        
        if use_voice in ["yes", "y"]:
            item = get_voice_input()
        else:
            speak("What do you want to add to your to-do list?")
            item = input("Enter your to-do item: ").strip()
        
        if item:
            update_todo_list(item)
    else:
        speak("Okay, shutting down now. Goodbye!")

if __name__ == "__main__":
    main()