'''
Substitution Cipher
CIS 210 F17 Project 4, Part 1

Author: Nicholas Bonat

Credits: Based on code on p.106-107 Miller and Ranum text.

This project will use a substitution cipher algorithm to encrypt and decrypt
a plain text message.
'''
import doctest

def genKeyFromPass(psw):
    '''(str) -> str

    This function genKeyFromPass has one parameter: password, a string.
    The returned value is a key that will be used in other functions.
    
    >>> genKeyFromPass('ajax')
    'ajxyzbcdefghiklmnopqrstuvw'
    >>> genKeyFromPass('ayyx')
    'ayxzbcdefghijklmnopqrstuvw'
    '''
    key = 'abcdefghijklmnopqrstuvwxyz'
    psw = removeDupes(psw)
    lastChar = psw[-1]
    lastIdx = key.find(lastChar)
    afterString = removeMatches(key[lastIdx+1:], psw)
    beforeString = removeMatches(key[:lastIdx], psw)
    key = psw + afterString + beforeString
    return key

def removeDupes(myString):
    '''(str) -> str

    This function removeDupes has one parameter: myString, a string. This will
    remove duplicate letters from a string. The returned value is the new string.

    >>> removeDupes('hello')
    'helo'
    >>> removeDupes('sorry')
    'sory'
    '''
    newStr = ""
    for ch in myString:
        if ch not in newStr:
            newStr = newStr + ch
    return newStr

def removeMatches(myString, removeString):
    '''(str, str) -> str

    This function removeMatches has two parameters: myString and removeString,
    both strings. This will remove the characters from one string that are in
    another. The returned value is the new string(newStr).

    >>> removeMatches('hello','hi')
    'ello'
    >>> removeMatches('python','module')
    'pythn'
    '''
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch
    return newStr

def substitutionDecrypt(cipherText, psw):
    '''(str, str) -> str

    The function substitutionDecrypt has two parameters, ciperText and password.
    ciperText is the message encrypted by substitutionEncrypt and password is
    used to generate the encryption key. Both of these parameters are strings.
    This function returns the origianl message with spaces removed, which is
    also a string.

    >>> substitutionDecrypt('qdznrexgjoltkblu','ajax')
    'thequickbrownfox'
    >>> substitutionDecrypt('eaiqagekcamvqdlkxhapp','ajax')
    'iamtakingapythonclass'
    '''
    key = genKeyFromPass(psw)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipherText = cipherText.lower()
    plainText = ""
    for ch in cipherText:
        idx = key.find(ch)
        plainText = plainText + alphabet[idx]
    return plainText    


def substitutionEncrypt(plainText, psw):
    '''(str, str) -> str

    This function substitutionEncrypt has two parameters, plainText-a string
    and password-also a string. The returned value is an encrypted message,
    a string.

    >>> substitutionEncrypt('the quick brown fox','ajax')
    'qdznrexgjoltkblu'
    >>> substitutionEncrypt('i am taking a python class','ajax')
    'eaiqagekcamvqdlkxhapp'
    '''
    plainText = plainText.replace(' ', '')
    key = genKeyFromPass(psw)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plainText = plainText.lower()
    cipherText = "" 
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText


def main():
    text = input('Enter a string to encrypt: ')
    password = input('Enter a password: ')
    
    encrypt = substitutionEncrypt(text, password)
    print('Encryption: ' + encrypt)
    
    decrypt = substitutionDecrypt(encrypt, password)
    print('Decryption: ' + decrypt)
    
    
if __name__ == '__main__':
    doctest.testmod()
    
main()
