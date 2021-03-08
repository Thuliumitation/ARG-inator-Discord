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

def brute_force(str_to_brute_with, str_to_crack):
    complete_list = []
    for current in range(2, 3):
        a = [i for i in str_to_crack]
        for y in range(current):
            a = [x + i for i in str_to_brute_with for x in a]
        complete_list += a
    return complete_list

#Just to get the modinverse for affine cipher, gave it here cuz i mean its a resource tho
def invmod(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x

