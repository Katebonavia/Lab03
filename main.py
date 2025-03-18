import spellchecker
from datetime import datetime

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input().lower()
        print("Using contains")
        start_time = datetime.now()
        sc.handleSentence(txtIn,"italian")
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        print("Using Linear search")
        start_time = datetime.now()
        sc.handleSentenceLinear(txtIn, "italian")
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input().lower()
        print("Using contains")
        start_time = datetime.now()
        sc.handleSentence(txtIn,"english")
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        print("Using Linear search")
        start_time = datetime.now()
        sc.handleSentenceLinear(txtIn, "english")
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input().lower()
        print("Using contains")
        start_time = datetime.now()
        sc.handleSentence(txtIn,"spanish")
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        print("Using Linear search")
        start_time = datetime.now()
        sc.handleSentenceLinear(txtIn, "spanish")
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        continue

    if int(txtIn) == 4:
        break


