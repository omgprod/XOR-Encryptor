import sys
import PySimpleGUI as sg
from itertools import cycle

sg.theme('Dark Teal')
layout = [  [sg.Text('Encrypt .txt bytes file')],
            [sg.Text('Path filename to encrypt  :'), sg.InputText("raw.txt")],
            [sg.Text('Hash key                    :'), sg.InputText("x")],
            [sg.Text('filename output.txt       :'), sg.InputText("raw_xor.txt")],
            [sg.OK(), sg.Cancel()]]
window = sg.Window('XOR Encryptor', layout)


def printCiphertext(ciphertext):
    print('{ 0x' + ', 0x'.join(hex(ord(x))[2:] for x in ciphertext) + ' };')


def xor(data, key):
    key = str(key)
    l = len(key)
    output_str = ""
    for i in range(len(data)):
        current = data[i]
        current_key = key[i % len(key)]
        output_str += chr(current ^ ord(current_key))
    return output_str


def get_file_data(filename):
    try:
        plaintext = open(filename, "rb").read()
        return plaintext
    except:
        print("Error! Check File Name ??")
    
#sg.theme_previewer()

while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event in ('OK'):
    
        bytes_file = values[0]
        hash_key = values[1]
        xor_file = values[2]
        
        plaintext = get_file_data(bytes_file)
        ciphertext = xor(plaintext, hash_key)
        if ciphertext:
            f = open(xor_file, "w+")
            f.write('{ 0x' + ', 0x'.join(hex(ord(x))[2:] for x in ciphertext) + ' };')
            f.close()
            printCiphertext(ciphertext)
            sg.popup('Success !', 'DATA SUCCESSFULLY XORED !')
        else:
            sg.popup('Error !', 'Something went wrong ..')


window.close()
