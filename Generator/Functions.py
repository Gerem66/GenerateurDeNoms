import os

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Align(text): return text.ljust(20)

def IsInt(text):
    try: return int(text) == int(text)
    except: return False

def UpperFirst(text):
    text_len = len(text)
    if text_len == 0: return ''
    elif text_len == 1: return text.upper()
    return text[0].upper() + text[1:].lower()
