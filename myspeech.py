import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone () as source:
        print(" I am listening..")
        audio = r.listen(source,phrase_time_limit = 5)
    data=""
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot understand")
    except sr.RequstError as e:
        print("Request Failed")
    return data    
listen()
