class BinaryCode:
	"""
	Let's say you have a binary string such as the following:
	011100011
	One way to encrypt this string is to add to each digit the sum of its adjacent digits. For example, the above string would become:
	123210122
	In particular, if P is the original string, and Q is the encrypted string, then Q[i] = P[i-1] + P[i] + P[i+1] for all digit positions i. Characters off the left and right edges of the string are treated as zeroes.
	An encrypted string given to you in this format can be decoded as follows (using 123210122 as an example):
	Assume P[0] = 0.
	Because Q[0] = P[0] + P[1] = 0 + P[1] = 1, we know that P[1] = 1.
	Because Q[1] = P[0] + P[1] + P[2] = 0 + 1 + P[2] = 2, we know that P[2] = 1.
	Because Q[2] = P[1] + P[2] + P[3] = 1 + 1 + P[3] = 3, we know that P[3] = 1.
	Repeating these steps gives us P[4] = 0, P[5] = 0, P[6] = 0, P[7] = 1, and P[8] = 1.
	We check our work by noting that Q[8] = P[7] + P[8] = 1 + 1 = 2. Since this equation works out, we are finished, and we have recovered one possible original string.
	Now we repeat the process, assuming the opposite about P[0]:
	Assume P[0] = 1.
	Because Q[0] = P[0] + P[1] = 1 + P[1] = 1, we know that P[1] = 0.
	Because Q[1] = P[0] + P[1] + P[2] = 1 + 0 + P[2] = 2, we know that P[2] = 1.
	Now note that Q[2] = P[1] + P[2] + P[3] = 0 + 1 + P[3] = 3, which leads us to the conclusion that P[3] = 2. However, this violates the fact that each character in the original string must be '0' or '1'. Therefore, there exists no such original string P where the first digit is '1'.
	Note that this algorithm produces at most two decodings for any given encrypted string. There can never be more than one possible way to decode a string once the first binary digit is set.
	Given a string message, containing the encrypted string, return a tuple (string) with exactly two elements. The first element should contain the decrypted string assuming the first character is '0'; the second element should assume the first character is '1'. If one of the tests fails, return the string "NONE" in its place. For the above example, you should return {"011100011", "NONE"}

	"""

	def iterate_over(self, string, p_zero):
		"""assume p[0] = 0"""
		count, result = 0, ''
		for c in string:
			q = int(string[count])

			if (count - 1 < 0):
				pminus1 = 0
				p = p_zero

			if (count == len(string)):
				pplus1 = 0
			else:
				pplus1 = q - p - pminus1

			if 	(pplus1 != 0 and pplus1 != 1) or \
				(pplus1 == 1 and count == len(string)-1):	
				#this happens if p and pminus1 are 0
				return 'NONE'
			result = result + str(p)
			pminus1, p, count = p, pplus1, count + 1

		return result
	
	def decode(self, message):
		"""
		>>> a = BinaryCode()
		>>> a.decode("123210122")
		('011100011', 'NONE')
		>>> a.decode("11")
		('01', '10')
		>>> a.decode("22111")
		('NONE', '11001')
		>>> a.decode("123210120")
		('NONE', 'NONE')
		>>> a.decode("3")
		('NONE', 'NONE')
		>>> a.decode("12221112222221112221111111112221111")
		('01101001101101001101001001001101001', '10110010110110010110010010010110010')
		>>> a.decode("2")
		('NONE', 'NONE')
		>>> a.decode("1")
		('NONE', '1')

		"""
		return self.iterate_over(message, 0), self.iterate_over(message, 1)

if __name__ == '__main__':
    import doctest
    
    doctest.run_docstring_examples(BinaryCode.decode, globals(), True, __name__)