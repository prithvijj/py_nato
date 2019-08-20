# File converts characters into NATO phonetic alphabets
import sys

def convert_str_to_nato(input_string):
	dict_nato = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf',"H":"Hotel", 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}
	nato = " ".join(map(dict_nato.get,input_string.replace(" ","").upper()))
	return nato

argument_number = len(sys.argv) - 1 

if (argument_number == 1):
	# input_string = raw_input('Enter a string:')
	input_string = sys.argv[1]
	converted_nato = convert_str_to_nato(input_string)
	print(converted_nato)

else:
	print("Enter a word as an argument.")


