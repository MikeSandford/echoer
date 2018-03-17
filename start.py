
import sys
import pyttsx3
import argparse


def echo_stuff(stuff):
    engine = pyttsx3.init()
    engine.say(stuff)
    engine.runAndWait()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Say something out loud')
    parser.add_argument('words', type=str, nargs='+',
                        help='Words to be spoken')

    args = parser.parse_args()
    print(args.words)
    word_string = " ".join(args.words)
    print(word_string)
    echo_stuff(word_string)
