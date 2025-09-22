#Caesar Cipher
#The Caesar cipher moves each letter forward in the alphabet by
#the key.  The resulting message has all the letters advanced by 'key'
#letters.
#To run the code, run the main() function

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    for letter in message:
        if (alpha.find(letter) >= 0): #check to see if the letter is actually a letter
            spot = (alpha.find(letter) + key) % 26
            secret = secret + alpha[spot]
        else: # letter must have been a number, symbol, or punctuation.
            secret = secret + letter

    return secret

def decode(message, key):
    #We will want to decode the message here.
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    for l in message:
        if (alpha.find(l) >= 0): #check to see if the letter is actually a letter
            spot = (alpha.find(l) - key) % 26
            secret = secret + alpha[spot]
        else: # letter must have been a number, symbol, or punctuation.
            secret = secret + l

    return secret


def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))

    secret = encode(message, key)
    print ("Encrypted:", secret)
    encoded_msg = input("Enter encoded message: ")
    msgkey = int(input("Enter key: "))
    plaintext = decode(encoded_msg, msgkey)
    print("Decrypted:", plaintext)


if __name__ == '__main__':
  main()
