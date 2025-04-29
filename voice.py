#The VOICE of Spot: Communicates back generated comments to a user using physical audio.
import pyttsx3

ENGINE = pyttsx3.init()
voices = ENGINE.getProperty('voices') 
ENGINE.setProperty('voice', voices[1].id) #SETS VOICE PROPERTY AS FEMALE FOR DEFAULT!!

def set_voice(gender):
    ''' Decides the gender of the voice...'''
    voices = ENGINE.getProperty('voices') 
    if gender == "f":
        ENGINE.setProperty('voice', voices[1].id) #changing index, changes voices. 0 for male, 1 for female
    elif gender == "m":
        ENGINE.setProperty('voice', voices[0].id) #changing index, changes voices. 0 for male, 1 for female
    else: 
        raise RuntimeError("Gender can only be 'f' or 'm' for now. Please check your spelling.")
    ENGINE.say("This is a demonstration of my voice. Is it to your liking?")
    ENGINE.runAndWait()

def speak(string):
    '''Given a string, speaks it out loud! Make sure to turn your volume up...'''
    ENGINE.say(string)
    ENGINE.runAndWait()

if __name__ == "__main__":
    print("Spot is speaking....")
    text = '''TFriends, Romans, countrymen, lend me your ears;
            I come to bury Caesar, not to praise him.
            The evil that men do lives after them;
            The good is oft interred with their bones;
            So let it be with Caesar. The noble Brutus
            Hath told you Caesar was ambitious:
            If it were so, it was a grievous fault,
            And grievously hath Caesar answered it.'''
    ENGINE.say(text)
    ENGINE.runAndWait()