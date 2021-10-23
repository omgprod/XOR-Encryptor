import sys
import PySimpleGUI as sg
from itertools import cycle

sg.theme('Dark Teal')
layout = [
    [sg.Multiline('', size=(40, 10), key='-OUTPUT1-', disabled=True)],
    [sg.Text('Encrypt .txt bytes file')],
    [sg.Text('Filename to encrypt       :'), sg.InputText("raw.txt", size = (10, 2), key='path')],
    [sg.Text('Hard Hashing key          :'), sg.InputText("x", size = (10, 2), key='hash')],
    [sg.Text('Filename output.txt       :'), sg.InputText("raw_xor.txt", size = (10, 2), key='ouput')],
    [sg.Input(key='-IN-', disabled=True, visible=False)],
    [sg.OK("Load"), sg.OK("Crypt"), sg.Cancel("Close")]]
window = sg.Window('XOR Encryptor', layout)


def printCiphertext(ciphertext):
    print('{ 0x' + ', 0x'.join(hex(ord(x))[2:] for x in ciphertext) + ' };')


def xor(data, key):
    key = str(key)
    output_str = ""
    try:
        for i in range(len(data)):
            current = data[i]
            current_key = key[i % len(key)]
            output_str += chr(current ^ ord(current_key))
    except:
        return sg.popup('Error !', 'Something went wrong ..')

    return output_str


def get_file_data(filename):
    try:
        plaintext = open(filename, "rb").read()
        return plaintext
    except:
        return None


while True:
    event, values = window.read()
    #if event:
        #window['-OUTPUT1-'].update(values['-IN-'])
    if event in (sg.WIN_CLOSED, 'Close'):
        break
    if event in 'Crypt':

        bytes_file = values['path']
        hash_key = values["hash"]
        xor_file = values["ouput"]

        plaintext = get_file_data(bytes_file)

        if plaintext is None:
            sg.popup('Error !', 'Something went wrong on filename or path!')
        else:
            ciphertext = xor(plaintext, hash_key)
            if len(ciphertext) > 0:
                f = open(xor_file, "w+")
                f.write('{ 0x' + ', 0x'.join(hex(ord(x))[2:] for x in ciphertext) + ' };')
                f.close()
                window['-OUTPUT1-'].update('{ 0x' + ', 0x'.join(hex(ord(x))[2:] for x in ciphertext) + ' };')
                printCiphertext(ciphertext)
                sg.popup('Success !', 'DATA SUCCESSFULLY XORED !')
            else:
                sg.popup('Error !', 'Something went wrong ..')

window.close()
