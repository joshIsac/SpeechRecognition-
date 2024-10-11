import speech_recognition as sr

def listen():
    recognizer=sr.Recognizer()
    #recording the audio using a microphone
    with sr.Microphone() as source:
        print("Speak Anything...")
        recognizer.adjust_for_ambient_noise(source,duration=2)
        audio=recognizer.listen(source)
        return audio
    
def recognize_speech():
    recognizer = sr.Recognizer()
    audio = listen()
    try:
        print("Say Something...")
        text=recognizer.recognize_google(audio)
        print(f"Speech recognized: '{text}'")
        return f"Speech successfully converted to text: {text}"

    except sr.UnknownValueError:
            return "Sorry, could not understand what you said."
        
    except sr.RequestError:
            return "Sorry, could not connect to the speech recognition service."
        

#execute
if __name__=="__main__":
    result=recognize_speech()
    print(result)