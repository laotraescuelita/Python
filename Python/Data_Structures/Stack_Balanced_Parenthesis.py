def is_correct( opened,  closed ): 
	if opened =="(" and closed ==")":
		return True
	elif opened =="[" and closed =="]":
		return True
	elif opened =="{" and closed =="}":
		return True
	else: 
		return False

def is_balanced( string ):
	s = []
	balanced = True
	index = 0 

	while index < len( string ) and balanced: 
		item = string[index]
		print( item )
		if item in "([{" : 
			s.append( item )
		else: 
			if len( s ) == 0:
				balanced = False
			else:
				last = s.pop()
				if not is_correct(last, item):
					balanced = False
		index += 1

	if len(s) == 0 and balanced:
		return True 
	else: 
		return False

string =  "({[]})"
print( is_balanced( string ) )





