import re
import random

class Recognition():

    def __init__(self, gpio):
        self.gpio = gpio
        self.answered = False;
        self.last_funct = False;


    def answer(self, sentence):

        # Remote whitespaces at the end of the sentence
        sentence = sentence.rstrip()

        print("Question: " + sentence + " \n\rAnswer is: ")

        # Split sentence
        words = sentence.split()

        if re.search(r'\b(exit)\b', sentence, re.I):
            self.exit()

        if re.search(r'\b(yes)\b', sentence, re.I):
            self.say_yes()
        elif re.search(r'\b(no)\b', sentence, re.I):
            self.say_no()
        elif re.search(r'\b(verde)\b', sentence, re.I):
            self.say_yes()
        elif re.search(r'\b(giallo)\b', sentence, re.I):
            self.say_no()
        else:
            pass

        if re.search(r'\b(sicuro)\b', sentence, re.I):
            self.say_yes()

        if re.search(r'\b(tu)\b.*\b(macchina)\b', sentence, re.I):
            self.say_yes()
        if re.search(r'\b(tu)\b.*\b(umano)\b', sentence, re.I):
            self.say_no()
        if re.search(r'\b(io)\b.*\b(umano)\b', sentence, re.I):
            self.say_yes()
        if re.search(r'\b(io)\b.*\b(macchina)\b', sentence, re.I):
            self.say_no()

        if re.search(r'\b(tu)\b.*\b(olmo)\b', sentence, re.I):
            self.say_yes()

        if re.search(r'\b(io)\b.*\b(Fabio  )\b', sentence, re.I):
            self.say_yes()

        # Get question mark at the end of the string
        if not self.answered:
            qm = sentence[-1:]
            if not qm == "?":
                self.wtf()
            else:
                if re.search(r'\b(tu)\b.*\b(macchina)\b', sentence, re.I): self.say_yes()
                elif re.search(r'\b(tu)\b.*\b(umano)\b', sentence, re.I): self.say_no()
                elif re.search(r'\b(io)\b.*\b(umano)\b', sentence, re.I): self.say_yes()
                elif re.search(r'\b(io)\b.*\b(macchina)\b', sentence, re.I): self.say_no()
                elif re.search(r'\b(tu)\b.*\b(stanco)\b', sentence, re.I): self.say_no()
                elif re.search(r'\b(io)\b.*\b(continuare)\b', sentence, re.I): self.say_yes()
                else: self.wtf()

    def say_yes(self):
        self.gpio.say_yes()
        self.answered = True
        self.last_funct = self.say_yes
        print("yes")

    def say_no(self):
        self.gpio.say_no()
        self.answered = True
        self.last_funct = self.say_no
        print("no")

    def wtf(self):
        self.gpio.cant_understand()
        self.answered = True
        self.last_funct = False
        print("not known")

    def exit(self):
        print('Exiting...')
        self.gpio.blink_bye()
        exit()