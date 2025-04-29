#The EARS of Spot: When activated, listens to commands given by voice from a user, then translates it to strings.
import speech_recognition as sr

RECOGNIZER = sr.Recognizer()  #creates a Recognizer instance
SECONDS = 5 #how long Spot should listen in for with every call...
VERBOSE = False

def listen(VERBOSE, SECONDS):
    '''When activated, listens in on a user's command (and a boolean specifying whether you want Spot to Speak back), then returns the command as a text string.'''
    if VERBOSE: 
        with sr.Microphone() as source:
            #read the audio data from the default microphone
            print("I am listening for ", SECONDS ," seconds. Please speak now!")
            audio_data = RECOGNIZER.record(source, duration=SECONDS)
            #convert speech to text
            print("I am thinking... give me a second to transcribe!")
            try:
                text = RECOGNIZER.recognize_google(audio_data)
                print("I think you said the following:")
                print(text)
                return text  
            except sr.exceptions.UnknownValueError: #if the audio file is empty, simply return no text
                text = ""
                return text
    if not VERBOSE:
        with sr.Microphone() as source:
            audio_data = RECOGNIZER.record(source, duration=SECONDS)
            try:
                text = RECOGNIZER.recognize_google(audio_data)
                return text 
            except sr.exceptions.UnknownValueError: #if the audio file is empty, simply return no text
                text = ""
                return text
    
if __name__ == "__main__":
    print("I want to hear what you have to say...")
    VERBOSE = True #Set True for verbal feedback, False for silence!
    text = listen(VERBOSE, 10)       
