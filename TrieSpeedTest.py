
import time
import numpy as np
from trie import Trie

def wordStatus(word):
    return words.wordStatus(word)

def inBounds(x,y):
        if(x>3 or x<0):
                return False
        if(y>3 or y<0):
                return False
        return True

def solve(array,visited,word,x,y):
        moves = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1]]
        isAWord = wordStatus(word)
        if(isAWord == 0):
        		return
        if(isAWord == 3):

                return
        if(isAWord==1 or isAWord==2):
                for i in moves:
                        newX = x+i[0]
                        newY = y+i[1]
                        if(inBounds(newX,newY) and not visited[newX][newY]):
                                visited[newX][newY] = True
                                newWord = word + array[newX][newY]
                                solve(array,visited,newWord,newX,newY)
                                visited[newX][newY] = False

def analyzeMatrix(letterArray):
	visited = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
        for x in range(0,4):
                for y in range(0,4):
                        word = letterArray[x][y]
                        visited[x][y] = True
                        solve(letterArray,visited,word,x,y)
			visited[x][y] = False


def addToTrie(wordslin):
    result = Trie()
    for word in wordslin:
        result.add(word)
    print("Added to Trie")
    return result


def main():
        letterArray = [['E','I','J','L'],['P','R','S','V'],['X','Y','O','T'],['E','O','S','S']]
        with open('dictionary.txt', 'r') as f:
                 wordslin = [line.strip() for line in f]
        print("dictionary list is made")
        global words
        words = addToTrie(wordslin)
        average = 0;
        i = 1000
        for x in range(0,i):
        	start = time.time()
        	analyzeMatrix(letterArray)
        	end = time.time()
        	average += end-start
        print(average/i)
	


if __name__ == '__main__':
    main()
