#Speech to Text Translation Project
___
#We will be searching for movie ratings and movie trailer by speaking to the Computer
___
####I used the *SpeechRecognition* package in python for this project.


###Installing SpeechRecognition:
To install the ***SpeechRecognition*** package; open Pycharm and type the following command: 

    $ pip install speechrecognition

##The Recognizer class
All of the magic in SpeechRecognition happens with the Recognizer class.

The primary purpose of a Recognizer instance is, of course, to recognize speech. Each instance comes with a variety of settings and functionality for recognizing speech from an audio source.

Creating a Recognizer instance is easy, open up your pycharm project, and type:
    
    ```python
    import speech_recognition as sr
    r = sr.Recognizer()
    ```
    

Each Recognizer instance has seven methods for recognizing speech from an audio source using various APIs. These are:

- recognize_bing() [Microsoft Bing Search](https://azure.microsoft.com/en-us/services/cognitive-services/speech/)
- recognize_google() [Google Web Search API](https://w3c.github.io/speech-api/speechapi.html)
- recognize_google_cloud() [Google Cloud Speech](https://cloud.google.com/speech/)
- recognize_houndify() [Houndify](https://www.houndify.com/)
- recognize_ibm() [IBM Speech to Text](https://www.ibm.com/watson/services/speech-to-text/)
- recognize_sphinx() [CMU Sphinx](https://cmusphinx.github.io/)
- recognize_wit() [Wit.ai](https://wit.ai/)

Of the seven, only recognize_sphinx() works offline with the CMU Sphinx engine. The other six all require an internet connection.

A full discussion of the features and benefits of each API is beyond the scope of this tutorial. Since SpeechRecognition ships with a default API key for the Google Web Speech API, you can get started with it right away. For this reason, we’ll use the Web Speech API in this guide. The other six APIs all require authentication with either an API key or a username/password combination. For more information, consult the SpeechRecognition [docs](https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst).

All seven recognize_*() methods of the Recognizer class require an audio_data argument. In each case, audio_data must be an instance of SpeechRecognition’s AudioData class.

There are two ways to create an AudioData instance: from an audio file or audio recorded by a microphone.
We will look into recording by a microphone.

##Working with microphones
To access the microphone with SpeechRecognizer, we’ll have to install the Pyaudio package.

###Installing Pyaudio: 
To work with microphones we need to install the [Pyaudio](https://people.csail.mit.edu/hubert/pyaudio/) package:

    $ sudo apt-get update
    $ sudo apt-get install python3-dev
    $ sudo apt-get install portaudio19-dev
    
    $ pip install pyaudio
    
###The Microphone Class
Open up Pycharm and create an instance of the recognizer class.

    ```python
    import speech_recognition as sr
    r = sr.Recogizer()
    ```
    
We will use the audio from the microphone as source. We can access the microphone by creating an instance of the Microphone class.

    mic = sr.Microphone()
    
###Using listen() to Capture Microphone Input
We can capture input from the microphone using the listen() method of the Recognizer class inside of the with block. This method takes an audio source as its first argument and records input from the source until silence is detected.

    with mic as source:
        audio = r.listen()
        
###Converting audio to text
We can now invoke recognize_google() to attempt to recognize any speech in the audio.
recognize_google() takes the audio as its first argument and converts it to text.

    with mic as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        
##Covering up all
Let us convert some speech to text.

    import speech_recognition as sr
    r = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        audio = r.listen(source)  
        text = r.recognize_google(audio)
        print(text)
        
Try speaking 'hello world' to the microphone. It prints out: 
    
    hello world
    
##Opening the Web Browser
Opening of the web browser can be done with the help of ***WebBrowser*** package.

    import webbrowser as wb
    wb.get().open_new(url)

We will get the url from the speech.