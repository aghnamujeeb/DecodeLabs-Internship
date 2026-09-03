password=input("Enter your password:")

def check_strength(password):
	length_ok=len(password)>=8
	has_uppercase = any(char.isupper() for char in password)
	has_lowercase = any(char.islower() for char in password)
	has_digit = any(char.isdigit() for char in password)
	symbols = "!@#$%^&*()-_+=<>?"
	has_symbol = any(char in symbols for char in password)
	score= sum([length_ok, has_uppercase, has_lowercase, has_digit, has_symbol])
	if score<=2:
		result ="Weak"
	elif score<=4:
		result="Medium"
	else:
		result="Strong"
	return result

password_strength_checker = check_strength(password)
print(password_strength_checker)