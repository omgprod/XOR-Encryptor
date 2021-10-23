import sys

def iter_word_list(plaintext):
    hex = plaintext.split()
    output_str = ""
    c = 0
    for i in range(len(hex)):
        if hex[i] not in ["{", "};"]:
            #print(hex[i])
            if c <= 10:
                hexa = hex[i].replace(',', '')
                if i != 1:
                    output_str += ", " + hexa
                else:
                    output_str += '\n' + hexa
                c = c + 1
            else:
                hexa = hex[i].replace(',', '')
                output_str += ',\n' + hexa
                c = 0
    return 'char b[] = { ' + output_str + ' };'


def main():
    try:
        plaintext = open(sys.argv[1], "rb").read()
	if plaintext is not None:
	    print(iter_word_list(plaintext))
	    return
    except:
        sys.exit()


main()
