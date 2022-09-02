from operator import truediv
from speak import speak
from listener import listener
import os


def lock():
    p = "jarvis"
    speak("plese enter your password")
    g = input("enter your password = ")
    if p == g :
        speak("access granted, welcome back boss")

    else:
        exit()

if __name__ == "__main__":
    lock()
    while True:
        permission = listener().lower()
        if "hey jarvis" in permission:
            while True:
                query = listener().lower()
                if 'hello jarvis' in query:
                    speak("hello boss")
                elif 'go to sleep' in query:
                    speak("ok boss")
                    break
                elif "shutdown system" in query:
                    speak("shutdown system under 3 second")
                    os.system("shutdown /s /t 3")
                elif "restart system" in query:
                    speak("shutdown system under 3 second")
                    os.system("shutdown /r")
                elif "logout system" in query:
                    speak("shutdown system under 3 second")
                    os.system("shutdown /l")

        elif "go to sleep" in permission:
            exit()
        elif "shutdown system" in permission:
            speak("shutdown system under 3 second")
            os.system("shutdown /s /t 3")
