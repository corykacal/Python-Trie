import numpy as np

class _TrieNode(object):


		def __init__(self):
			global node
			self.word = False
			self.end = True
			self.node = np.empty(26, dtype=object)

		def contains(self, index):
			return self.node[index]!=None

		def add(self, index):
			self.end = False
			newNode = self.__class__()
			self.node[index] = newNode

		def get(self, index):
			return self.node[index]

		def isEnd(self):
			return self.end

		def setWord(self):
			self.word = True

		def isWord(self):
			return self.word

class Trie(object):

	def __init__(self):
		self.root = _TrieNode()


	def __recursiveAdd(self, node, word):
		if(len(word)!=0):
			index = ord(word[0])-65
			if(not node.contains(index)):
				if(len(word)==1):
					node.add(index)
				else:
					node.add(index)
			self.__recursiveAdd(node.get(index), word[1:len(word)])
		else:
			node.setWord()

	def add(self, word):
		if(word!=""):
			self.__recursiveAdd(self.root, word)


	def __recursiveContains(self, node,word):
		if(len(word)==0):
			return True
		index = ord(word[0])-65
		if(not node.contains(index)):
			return False
		return self.__recursiveContains(node.get(index), word[1:len(word)])



	def contains(self, word):
		if(word==""):
			return False
		return self.__recursiveContains(self.root,word)


	def wordStatus(self, word):
		return self.__wordStatus(self.root,word)


	def __wordStatus(self, node, word):
		if(len(word)==0):
			if(node.isEnd()):
				#end and word
				return 3
			if(node.isWord()):
				#continue but is word
				return 2
			else:
				#not word but possible
				return 1
		index = ord(word[0])-65
		if(not node.contains(index)):
			#do not cont7iue
			return 0
		return self.__wordStatus(node.get(index), word[1:len(word)])

