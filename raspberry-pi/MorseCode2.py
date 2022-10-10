#type: ignore 
import digitalio
import time 
import board

greenled = digitalio.DigitalInOut(board.GP16)
greenled.direction = digitalio.Direction.OUTPUT
redled = digitalio.DigitalInOut(board.GP2)
redled.direction = digitalio.Direction.OUTPUT 

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

while True:
    Message = input("Type English Message: ")
    if Message == "-q": 
        break
    Message = Message.upper()
    Length = len(Message)
    print(Length)
    time.sleep(3)
    
    modifier = 0.25

    DotTime = 1 * modifier
    DashTime = 3  *modifier
    BetweenTaps = 1 * modifier
    BetweenLetters = 3 * modifier
    BetweenWords = 7 * modifier

    NewMessage = ""
    for Letter in Message:
        Letter = MORSE_CODE[Letter]
        for Symbol in Letter:
            redled.value = True 
            if Symbol == ".": 
                time.sleep(DotTime)
            if Symbol == "-":
                time.sleep(DashTime)
            redled.value = False
            time.sleep(BetweenTaps)
            if Symbol == " ": 
                time.sleep(BetweenLetters)
            if Symbol == "/":
                time.sleep(BetweenWords)
        NewMessage = NewMessage + Letter + " "
        print(NewMessage)
        






