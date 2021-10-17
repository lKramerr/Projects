import random
import manprint

def hardmode():

	#Alphabet
	list_abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
				"L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
				"W", "X", "Y", "Z"]

	list_display_abc = list_abc

	#Words
	list_word1 = ["R", "E", "S", "T", "A", "U", "R", "A", "N", "T"]
	list_word2 = ["I", "N", "D", "E", "P", "E", "N", "D", "E", "N", "C", "E"]
	list_word3 = ["A", "U", "X", "I", "L", "I", "A", "R", "I", "E", "S"]

	list_words = [list_word1, list_word2, list_word3]
	list_word_fill = []

	int_word_full = random.choice(list_words)

	for n in int_word_full:
	    list_word_fill.append("_")

	#Extra Variables
	str_letter = ""

	#Counters
	int_lives = 6
	int_for_counter = 0
	int_while_counter = 0

	#Booleans
	bool_good = False

	def print_abc():
		"""
		A function to print the ABC
		"""
		int_for_counter = 0
		int_while_counter = 0

		for n in list_display_abc:
			if n == str_letter:
				list_display_abc[int_while_counter] = "_"

			int_while_counter += 1

		print(int_lives)
		print("\n")
		for n in list_display_abc:

			print(n + " ", end = " ")

			if int_for_counter == 7:
				print("")

			if int_for_counter == 15:
				print("")

			if int_for_counter == 23:
				print("")

			int_for_counter += 1


	while list_word_fill != int_word_full and int_lives > 0:

		bool_good = False

		#Print the Hangman
		manprint.manprint(int_lives)

		#Print the word to fill
		for n in list_word_fill:
			print(n, end=" ")

		#Print the ABC
		print("\n")
		print_abc()

		print("")

		#Input the Letter
		str_letter = str(input("\nLetter: ").upper())
		int_counter = 0

		while int_counter < len(int_word_full):

			if str_letter == int_word_full[int_counter]:
				list_word_fill[int_counter] = str_letter
				bool_good = True

			int_counter += 1

		if bool_good != True:
			int_lives -= 1


	if int_lives > 0:
		for n in list_word_fill:
			print(n, end=" ")
		print("\nYou win!")
	else:
		manprint.manprint(int_lives)
		print("\n")
		print("You lost!")


	print("")
