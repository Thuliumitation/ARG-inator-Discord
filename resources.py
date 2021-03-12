#Like it says, a dictionary for the morse code translator
morse_dict = {' ': '/',', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-','A': '.-',
              'B': '-...','C': '-.-.', 'D': '-..',
              'E': '.', 'F': '..-.', 'G': '--.',
              'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--',
              'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...',
              'T': '-', 'U': '..-', 'V': '...-',
              'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..',
              '9': '----.','0': '-----'}

nato_dict = {'A' : "Alpha",'B' : "Bravo",'C' : "Charlie",
    'D' : "Delta",'E' : "Echo",'F' : "Foxtrot",
    'G' : "Golf",'H' : "Hotel",'I' : "India",
    'J' : "Juliet",'K' : "Kilo",'L' : "Lima",
    'M' : "Mike",'N' : "November",'O' : "Oscar",
    'P' : "Papa",'Q' : "Quebec",'R' : "Romeo",
    'S' : "Sierra",'T' : "Tango",'U' : "Uniform",
    'V' : "Victor",'W' : "Whisky",'X' : "X-Ray",
    'Y' : "Yankee",'Z' : "Zulu",'0' : "Zero",
    '1' : "One",'2' : "Two",'3' : "Three",
    '4' : "Four",'5' : "Five",'6' : "Six",
    '7': "Seven",'8' : "Eight",'9' : "Nine",
    ' ': "(space)"}

#Just to get the modinverse for affine cipher, gave it here cuz i mean its a resource tho
def invmod(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x

