import random
import string
import numpy
import itertools


count = numpy.zeros((5, 5))
count[0][0] = 0
count[1][0] = 1
count[2][0] = 2
count[3][0] = 3
count[4][0] = 4
count[0][1] = 5
count[1][1] = 6
count[2][1] = 7
count[0][2] = 8
count[1][2] = 9
count[2][2] = 10
count[0][3] = 11
count[1][3] = 12
count[0][4] = 13

def makenum():
	num = ''.join(random.sample(['1','2','3','4','5','6','7','8','9','0'], 4))
	return num

def compare(input, ans):
	count_a = 0
	count_b = 0
	for i in range(0, 4):
		if(input[i] == ans[i]):
			count_a += 1
		elif(input[i] in ans):
			count_b += 1
	return count[count_a][count_b]

def result(input):
	if input == count[0][0]: return '0A0B'
	elif input == count[1][0]: return '1A0B'
	elif input == count[2][0]: return '2A0B'
	elif input == count[3][0]: return '3A0B'
	elif input == count[4][0]: return '4A0B'
	elif input == count[0][1]: return '0A1B'
	elif input == count[1][1]: return '1A1B'
	elif input == count[2][1]: return '2A1B'
	elif input == count[0][2]: return '0A2B'
	elif input == count[1][2]: return '1A2B'
	elif input == count[2][2]: return '2A2B'
	elif input == count[0][3]: return '0A3B'
	elif input == count[1][3]: return '1A3B'
	elif input == count[0][4]: return '0A4B'

def guess():
	ans = makenum()
	print('Game start!')

	while(1):
		time = 1
		guess = input("pick a number:")
		comp = compare(guess, ans)

		print('guess %d:' % time, result(comp))
		if comp == count[4][0]:
			print('Congradulations! got the number in %d times' % time)
			return
		time += 1

class aiguess():
	
	possibleList = []
	round = 0

	def __init__(self):
		self.possibleList = list(map(''.join, itertools.permutations('1234567890', 4)))
		self.round = 1
	
	def guess(self):
		if self.round == 1:
			return '1234'
		elif self.round == 2:
			return '5678'
		else:
			allBest = 10000
			bestNum = ''
			for num in self.possibleList:
				tempList = list(self.possibleList)
				tempBest = 0
				tempLen = len(tempList)
				for res in ['0A0B', '1A0B', '2A0B', '3A0B', '0A1B', '1A1B', '2A1B', '0A2B', '1A2B', '2A2B', '0A3B', '1A3B', '0A4B']:
					tempList[:] = itertools.filterfalse(lambda x:result(compare(x, num)) == res, tempList)
					diff = tempLen - len(tempList)
					if diff > allBest:
						tempBest = diff
						break
					elif diff > tempBest:
						tempBest = diff
					tempLen -= diff
				
				if tempBest < allBest:
					allBest = tempBest
					bestNum = num

			return bestNum

	def guessResult(self, num, res):
		self.possibleList[:] = itertools.filterfalse(lambda x:result(compare(x, num)) != res, self.possibleList)
		self.round += 1



			


def aigame(ans):
	ai = aiguess()
	round = 1
	while(1):
		guessnum = ai.guess()
		comp = compare(guessnum, ans)
		ai.guessResult(guessnum, result(comp))
		#print('%d round guess %s:' % (round, guessnum), result(comp))
		if comp == count[4][0]:
			print(' got %s in %d times' % (ans, round))
			return
		round += 1

for num in list(map(''.join, itertools.permutations('1234567890', 4))):
	aigame(num)
