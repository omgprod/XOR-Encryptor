import sys
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
KEY = "x"


def xor(data, key):
	key = str(key)
	l = len(key)
	output_str = ""
	for i in range(len(data)):
		current = data[i]
		current_key = key[i % len(key)]
		output_str += chr(ord(current) ^ ord(current_key))
	#print(output_str)
	return output_str


def printCiphertext(ciphertext):
	print('{ 0x' + ', 0x'.join(hex(ord(x))[2:] for x in ciphertext) + ' };')


# def test():
#     try:
# 	    plaintext = open(sys.argv[1], "rb").read()
#     except:
#     	print("File argument needed! %s " % sys.argv[0])
# 	    sys.exit()

#ciphertext = xor(plaintext, KEY)
#print(hex(ord(x))[2:] for x in ciphertext)

window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
