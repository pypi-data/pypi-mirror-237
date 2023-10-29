ron = {
	'I':1,
	'V':5,
	'X':10,
	'L':50,
	'C':100,
	'D':500,
	'M':1000,
}

def r2d(romanNumeral):
	sum = 0
	for i in range(len(romanNumeral) - 1):
		left = romanNumeral[i]
		right = romanNumeral[i + 1]
		if ron[left] < ron[right]:
			sum -=ron[left]
		else:
			sum += ron[left]
	sum += ron[romanNumeral[-1]]
	return
	 sum