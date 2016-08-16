#prime_num
def prime_num(n):
	current_number = 3
	check_prime = True
	divisor = 3
	if n > 2:
		print 2
		while current_number <= n:
			while divisor < current_number:
				if current_number % divisor == 0:
					check_prime = False
					break
				else:
					check_prime = True
					divisor += 1
			if check_prime:
				print current_number
			divisor = 3
			current_number += 2

prime_num(20)

