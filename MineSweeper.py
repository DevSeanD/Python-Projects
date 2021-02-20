from random import random
"""
Author: Sean Dever
Date: 2/13/2021
Description - MineSweeper CLI Implementation Using BFTS                algorithm 

"""
# Constant Values
UNVISITED = 0
INQUEUE = 1
VISITED = 2
BOMB = 9

GRID_OFF_SETS = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1],
                 [-1, -1]]


class dataCell:
	def __init__(self, row, col, flag, data):
		self.r = row
		self.c = col
		self.f = flag
		self.d = data


class Queue:
	def __init__(self):
		self.queue = []

	def clear(self):
		self.queue = []

	def enqueue(self, elm):
		self.queue.append(elm)

	def dequeue(self):
		return self.queue.pop(len(self.queue) - 1)

	def isEmpty(self):
		return len(self.queue) == 0  # Boolean value

	def returnQueue(self):
		allElm = []

		for elm in self.queue:
			allElm.append(elm)

		return allElm


def testQueue():
	queueTest = Queue()

	print(queueTest.isEmpty())

	queueTest.enqueue("test")
	print(queueTest.returnQueue())

	queueTest.enqueue("second elm")
	queueTest.dequeue()
	print(queueTest.returnQueue())


# Testint dataCell and Queue
# x = dataCell(3,3,UNVISITED,1)
# print(x.d)
# testQueue()


def initGameBoard(numRow, numCol, default):
	gameBoard = [[0] * numRow for i in range(numCol)]
	for row in range(0, numRow):
		for col in range(0, numCol):
			gameBoard[row][col] = dataCell(
			    row, col, UNVISITED, default)  # default values for a dataCell
	return gameBoard


def isOnBoard(row, col, numRow, numCol):
	if (row >= 0 and row < numRow and col >= 0 and col < numCol):
		return True
	else:
		return False


def printGameBoard(board):
	for r in range(0, len(board)):
		for c in range(0, len(board)):
			print("[", board[r][c].d, "]", end="\t")
		print()
		print()


def addBombs(board, numRow, numCol, percent, rSkip, cSkip):
	numOfBombs = 0
	for r in range(0, numRow):
		for c in range(0, numCol):
			if (
			    percent >= random()
			):  # with no perameters the radom function genereated from 0 to 1.0
				if (r == rSkip and c == cSkip):
					pass
				else:
					board[r][c].d = BOMB
					numOfBombs += 1

	return numOfBombs


def updateNeighbors(board, numRow, numCol):
	for r in range(0, numRow):
		for c in range(0, numCol):
			if board[r][c].d == BOMB:
				for ni in range(0, 8):  # update all 8 neighbors
					nr = r + GRID_OFF_SETS[ni][0]
					nc = c + GRID_OFF_SETS[ni][1]

					if (isOnBoard(nr, nc, numRow, numCol)
					    and board[nr][nc].d != BOMB):
						if (board[nr][nc].d == '?'):
							board[nr][nc].d = 0
						board[nr][nc].d = int(board[nr][nc].d + 1)


def floodFill(gameBoard, showBoard, inRow, inCol, numOfRow, numOfCol,
              numOfCells):

	cellQueue = Queue()
	gameBoard[inRow][inCol].f = INQUEUE
	cellQueue.enqueue(gameBoard[inRow][inCol])

	while (cellQueue.isEmpty() == False):
		current = cellQueue.dequeue()
		current.f = VISITED

		showBoard[current.r][current.c].d = gameBoard[current.r][current.c].d

		numOfCells -= 1

		if (current.d == 0):
			for ni in range(0, 8):
				nr = current.r + GRID_OFF_SETS[ni][0]
				nc = current.c + GRID_OFF_SETS[ni][1]

				if (isOnBoard(nr, nc, numOfRow, numOfCol)
				    and gameBoard[nr][nc] != BOMB
				    and gameBoard[nr][nc].f == UNVISITED):
					cellQueue.enqueue(gameBoard[nr][nc])
					gameBoard[nr][nc].f = INQUEUE

	return numOfCells


# Entrypoint
qValidate = Queue()  # Queue Validate
print("#############################")
print("# Welcome to MineSweeper.py #")
print("#############################")
print()
print()
print("Difficulty Selection")
print("1 - Easy")
print("2 - Normal")
print("3 - Hard")
print()
difficulty = input()

while (int(difficulty) < 1 or int(difficulty) > 3):
	print("Invalid selection")
	print("Enter again")
	difficulty = input()

if (difficulty == '1'):
	percent = 0.10
if (difficulty == '2'):
	percent = 0.14
if (difficulty == '3'):
	percent = 0.18

numOfRow = int(input("How many rows? : "))
numOfCol = int(input("How many cols? : "))
while (numOfRow < 2 or numOfCol < 1 and numOfRow != numOfCol):
	if (numOfRow != numOfCol):
		print("number of rows and columns must be the same")
	print("Invalid selection")
	numOfRow = int(input("How many rows? : "))
	numOfCol = int(input("How many cols? : "))

numOfCells = numOfRow * numOfCol

gameBoard = initGameBoard(numOfRow, numOfCol, 0)

showBoard = initGameBoard(numOfRow, numOfCol, '?')
loopGame = True

printGameBoard(showBoard)

inRow = int(input("Select a row: "))
inCol = int(input("Select a col: "))
while ((inRow < 0 or inRow > numOfRow - 1 or inCol < 0 or inCol > numOfCol)):
	inRow = int(input("Select a row: "))
	inCol = int(input("Select a col: "))

numOfBombs = addBombs(gameBoard, numOfRow, numOfCol, percent, inRow, inCol)

updateNeighbors(gameBoard, numOfRow, numOfCol)

numOfCells = floodFill(gameBoard, showBoard, inRow, inCol, numOfRow, numOfCol,
                       numOfCells)

showBoard[inRow][inCol].d = gameBoard[inRow][inCol].d

print()
print("Number of bombs: ", numOfBombs)
print()
printGameBoard(showBoard)

while (loopGame == True):
	inRow = int(input("Select a row: "))
	inCol = int(input("Select a col: "))

	while (inRow < 0 or inRow > numOfRow - 1 or inCol < 0 or inCol > numOfCol):
		print("Invalid selection")
		inRow = int(input("Select a row: "))
		inCol = int(input("Select a col: "))

	print()
	print()

	showBoard[inRow][inCol].d = gameBoard[inRow][inCol].d

	if (showBoard[inRow][inCol].d == BOMB):
		showBoard[inRow][inCol].d = "☢"
		print()
		print("Number of bombs", numOfBombs)
		print()
		printGameBoard(showBoard)
		print()
		print("############################")
		print("# You have selected a bomb #")
		print("#  Thank you for playing   #")
		print("#       Game Over          #")
		print("############################")
		loopGame = False

	else:
		numOfCells = floodFill(gameBoard, showBoard, inRow, inCol, numOfRow,
		                       numOfCol, numOfCells)

		print()
		print("Number of bombs", numOfBombs)
		print()
		printGameBoard(showBoard)
		print()

		if (numOfCells == numOfBombs):
			print()
			print("#########################")
			print("#       You Win!        #")
			print("# Thank you for playing #")
			print("#########################")
			loopGame = False
      
