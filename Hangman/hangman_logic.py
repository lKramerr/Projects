def hangman():
	str_word = "restaurant"
	list_word_full = ["R", "E", "S", "T", "A", "U", "R", "A", "N", "T"]
	list_word_fill = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
	str_letter = ""
	int_counter = 0



	while list_word_fill != list_word_full:
		
		print(
		"""    
			______
			I   l
			I   l
			I   O
			I  /I\\
			I  / \\
			I 
		    ---------
		"""
		)
		for n in list_word_fill:
		    print(n, end=" ")

		print("")
		
		str_letter = str(input().upper())
		int_counter = 0
		
		while int_counter < len(list_word_full):
		    
		    if str_letter == list_word_full[int_counter]:        
		        list_word_fill[int_counter] = str_letter
		    
		    int_counter += 1
		    
	for n in list_word_fill:
		print(n, end=" ")

	print("")

def abc():	
	list_abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 				"L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 				"W", "X", "Y", "Z"]

	list_display_abc = list_abc

	def print_abc():

		int_for_counter = 0
		
		for n in list_display_abc:

			print(n + " ", end = " ")
			
			if int_for_counter == 7:
				print("")
				
			if int_for_counter == 15:
				print("")
				
			if int_for_counter == 23:
				print("")
			
			int_for_counter += 1
			
		print("")
				
				
	#int_while_counter = 0
	#int_lives = 5

	#while int_lives > 0:

		#int_while_counter = 0
		str_input = str(input("Letter: ").upper())

		for n in list_display_abc:
			if n == str_input:
				list_display_abc[int_while_counter] = "_"	
				
			int_while_counter += 1
		   
		print_abc()
		print("")
		#int_lives -= 1

hangman()
"""    
    ______
    I   l
    I   l
    I   O
    I  /I\\
    I  / \\
    I 
---------
"""
"R _ _ _ _ _ _ _ _ T"













