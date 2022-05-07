from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    name = text + ".mp3"
    filename = name
    tts.save(filename)


speak(str(input("Enter your text: ")))
