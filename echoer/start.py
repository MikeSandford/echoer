
import sys
import pyttsx3
import argparse


def echo_stuff(stuff):
    engine = pyttsx3.init()
    engine.say(stuff)
    engine.runAndWait()

def main():
    parser = argparse.ArgumentParser(description='Say something out loud')
    parser.add_argument('words', type=str, nargs='+',
                        help='Words to be spoken')

    args = parser.parse_args()
    word_string = " ".join(args.words)
    echo_stuff(word_string)

if __name__ == "__main__":

    main()
