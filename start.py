
import sys
import pyttsx3

if __name__ == "__main__":

    words = sys.argv[1:]
    word_string = " ".join(words)

    engine = pyttsx3.init()
    engine.say(word_string)
    engine.runAndWait()
