# transposition.py
# Kelly Neiling
# CYB210
# November 30, 2021

import math

def main():
    print("This program will encrypt or decrypt a file of your choice using the Transposition Cipher.")
    input_file = input("What is the name of the file? ")
    crypto_act = input("Would you like the file encrypted ('e') or decrypted ('d')? ")
    crypto_key = int(input("What is the key? "))
    output_file = input("What filename would you like the final draft saved to? ")

    #read the file
    text = open(input_file, mode='r')
    raw_text = text.read() 
    text.close()

    #send to correct function
    if crypto_act == 'e' or crypto_act == 'E':
        final_text = encryptTransposition(crypto_key, raw_text)
        print("Encrypted file has been written.")
    elif crypto_act == 'd' or crypto_act == 'D':
        final_text = decryptTransposition(crypto_key, raw_text)
        print("Decrypted file has been written.")
    
    #write to output file
    out_text = open(output_file, "w+")
    out_text.write(final_text)
    out_text.close()

def encryptTransposition(key, message):
    cipherText = ['']*key
    
    for column in range(key):
        currentIndex = column #for use in messages index
        while currentIndex < len(message):
            cipherText[column] += message[currentIndex]
            currentIndex += key #shifts message index to next possible position; stops while loop when next key position >= len(message)

    return ''.join(cipherText) #converts list into a string

def decryptTransposition(key, message):
    numColumns = int(math.ceil(len(message) / float(key)))
    numRows = key

    plainText = ['']*numColumns
    shadowBoxes = (numColumns*numRows) - len(message)
    col = 0
    row = 0
    for ch in message:
        plainText[col] += ch
        col += 1
        if (col == numColumns) or (col == numColumns -1 and row >= numRows - shadowBoxes):
            col = 0
            row += 1

    return ''.join(plainText)

main()