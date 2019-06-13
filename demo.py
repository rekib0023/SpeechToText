import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[search ratings: search trailer]')
    print('speak now')
    audio = r3.listen(source)
    get1=""
    try:
        get1 = r2.recognize_google(audio)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))

if 'ratings' == get1:
    r2 = sr.Recognizer()
    url = 'https://www.rottentomatoes.com/m/'
    with sr.Microphone() as source:
        print('search your query')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            get=get.replace(" ", "_")
            print('Showing ' + get1 + ' of ' + get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))

if 'trailer' == get1:
    r1 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('search your query')
        audio = r1.listen(source)

        try:
            get = r1.recognize_google(audio)
            print('Showing ' + get1 + ' of ' + get)
            wb.get().open_new(url+get+'+trailer')
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))
