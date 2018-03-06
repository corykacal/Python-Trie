import numpy as np

class _TrieNode(object):


        def __init__(self):
            global node
            self.word = False
            self.end = True
            self.node = {}

        def contains(self, char):
            return self.node.get(char)!=None

        def add(self, char):
            self.end = False
            newNode = self.__class__()
            self.node[char] = newNode

        def get(self, char):
            if(not self.contains(char)):
                return -1
            return self.node[char]

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
                char = word[0]
                if(not node.contains(char)):
                    if(len(word)==1):
                        node.add(char)
                    else:
                        node.add(char)
                self.__recursiveAdd(node.get(char), word[1:len(word)])
            else:
                node.setWord()

	def add(self, word):
            word = word.upper()
            if(word!=""):
                self.__recursiveAdd(self.root, word)


	def __recursiveContains(self, node,word):
            if(len(word)==0):
                    return True
            char = word[0]
            if(not node.contains(char)):
                    return False
            return self.__recursiveContains(node.get(char), word[1:len(word)])



	def contains(self, word):
            word = word.upper()
            if(word==""):
                return False
            return self.__recursiveContains(self.root,word)


	def wordStatus(self, word):
            return self.__wordStatus(self.root,word)

        def isWord(self, word):
            return self.__isWord(self.root,word)

        def __isWord(self, node, word):
            char = word[0]
            if(not node.contains(char)):
                return False
            if(len(word)==0):
                return node.isWord()
            else:
                return self.__isWord(node.get(char), word[1:len(word)])

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
            char = word[0]
            if(not node.contains(char)):
                #do not cont7iue
                return 0
            return self.__wordStatus(node.get(char), word[1:len(word)])

