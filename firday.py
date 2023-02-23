import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia




listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
machine.runAndWait()


def input_instruction():
    global instruction
    try:
        with sr.Microphone() as origin:
            print("listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "friday" in instruction:
                print(instruction)
    except:
        pass
    finally:
        print("exit")
    return instruction

def play_friday():
    instruction = input_instruction()
    print(instruction)
    if 'play' in instruction:
        song = instruction.replace('play'," ")
        talk("playing" + song)
        pywhatkit.playsonyt(song)

    elif 'time' in instruction:
        time =  datetime.datetime.now().strftime('%I:%M%p')
        talk('currenttime'+time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Todays date"+ date )
    elif 'how are you' in instruction:
        talk('Im fine What about you??')
    elif 'explain' in instruction:
        human = instruction.replace('explain'," ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
play_friday()

