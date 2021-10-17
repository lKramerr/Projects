def manprint(int_lives):
	
	if int_lives == 6:
		print(
			"""    
		______
		I   l
		I   l
		I   
		I  
		I  
		I 
		---------
			"""
		)
	elif int_lives == 5:
		print(
			"""    
		______
		I   l
		I   l
		I   O
		I  
		I  
		I 
		---------
			"""
		)
	elif int_lives == 4:
		print(
			"""    
		______
		I   l
		I   l
		I   O
		I  /
		I  
		I 
		---------
			"""
		)
	elif int_lives == 3:
		print(
			"""    
		______
		I   l
		I   l
		I   O
		I  /I
		I  
		I 
		---------
			"""
		)
	elif int_lives == 2:
		print(
			"""    
		______
		I   l
		I   l
		I   O
		I  /I\\
		I  
		I 
		---------
			"""
		)
	elif int_lives == 1:
		print(
			"""    
		______
		I   l
		I   l
		I   O
		I  /I\\
		I  / 
		I 
		---------
			"""
		)
		
	elif int_lives == 0:
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
