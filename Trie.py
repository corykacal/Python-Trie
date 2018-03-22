class _TrieNode(object):

        def __init__(self,char):
            global children
            self.word = False
            self.end = True
            self.char = char
            self.children = {}

        def contains(self, char):
            return self.children.get(char)!=None

        def add(self, char):
            self.end = False
            newChild = self.__class__(char)
            self.children[char] = newChild

        def remove(self, char):
            self.end = True
            self.children[char] = None

        def get(self, char):
            if(not self.contains(char)):
                return -1
            return self.children[char]

        def isEnd(self):
            return self.end

        def setWord(self,status):
            self.word = status

        def isWord(self):
            return self.word

        def childCnt(self):
            return len(self.children)

        def getChar(self):
            return self.char

        def remove(self, char):
            child_to_delete = self.get(char)
            child_to_delete.setWord(False)
            self.children.pop(char)
            del child_to_delete

        def getChildren(self):
            return self.children


class Trie(object):

	def __init__(self):
            self.root = _TrieNode('')
            global size
            self.size = 0
        '''
        recursively adds a word to the tree
        '''
	def add(self, word):
            word = word.upper()
            if(word!=""):
                self.size+=1
                self.__recursiveAdd(self.root, word)

	def __recursiveAdd(self, node, word):
            if(len(word)!=0):
                char = word[0]
                if(not node.contains(char)):
                    node.add(char)
                self.__recursiveAdd(node.get(char), word[1:len(word)])
            else:
                node.setWord(True)


        '''
        removes a word and its all its nodes from the tree unless its nodes are used by another word.
        If another word uses its nodes then the node's status will be adjusted.
        ex:
            Words added are 'apple' and 'app'
            the nodes will have status as shown below
            a = !isWord, !isEnd
            p = !isWord, !isEnd
            p = isWord, !isEnd
            l = !isWord, !isEnd
            e = isWord, isEnd
            After 'app' is removed then all the nodes will still exist but the status will change
            a = !isWord, !isEnd
            p = !isWord, !isEnd
            p = !isWord, !isEnd     previous = isWord, !isEnd
            l = !isWord, !isEnd
            e = isWord, isEnd
        '''
        def remove(self, word):
            word = word.upper()
            if(word!=""):
                self.size-=1
                self.__recursiveRemove(self.root,word)

        def __recursiveRemove(self, node, word):
            if(len(word)!=0):
                char = word[0]
                if(not node.contains(char)):
                    return False
                remove = self.__recursiveRemove(node.get(char),word[1:len(word)])
                if(remove):
                    node.remove(char)
            else:
                if(node.childCnt()!=0):
                    node.setWord(False)
            if(node.childCnt()==0):
                return True
            else:
                return False


        '''
        return a list of all words with the given prefix
        '''
        def wordsWithPrefix(self, prefix):
            prefix = prefix.upper()
            return self.__wordsWithPrefix(self.root, [], prefix, prefix)

        def __wordsWithPrefix(self, node, words, prefix, originalPrefix):
            if(len(prefix)==0):
                return self.__wordsFromNode(node, [], originalPrefix)
            char = prefix[0]
            if(not node.contains(char)):
                return words
            return self.__wordsWithPrefix(node.get(char), words, prefix[1:len(prefix)], originalPrefix)

        '''
        prints all the words in the trie as a list
        '''
        def asList(self):
            return self.__wordsFromNode(self.root, [], "")

        '''
        prints all words from a given node in the tree as they were inserted, is not in order
        '''
        def __wordsFromNode(self, node, words, currentWord):
            if(node.isWord()):
                words.append(currentWord)
            for child in node.getChildren():
                nextWord = currentWord + child
                nextNode = node.get(child)
                self.__wordsFromNode(nextNode,words,nextWord)
            return words


        '''
        Sees if a given string is in the tree
        '''
	def contains(self, word):
            word = word.upper()
            if(word==""):
                return True
            return self.__recursiveContains(self.root,word)

	def __recursiveContains(self, node, word):
            if(len(word)==0):
                    return True
            char = word[0]
            if(not node.contains(char)):
                    return False
            return self.__recursiveContains(node.get(char), word[1:len(word)])

        #see if a given string is a word in the tree
        def isWord(self, word):
            word = word.upper()
            return self.__isWord(self.root,word)

        def __isWord(self, node, word):
            if(len(word)==0):
                return node.isWord()
            else:
                char = word[0]
                if(not node.contains(char)):
                    return False
                return self.__isWord(node.get(char), word[1:len(word)])


        '''
        Returns the current state/status of a string
        0 means it is not a word and it will never be a word
        1 means not a word but is a substring of one
        2 means it is a word but also a substring of a bigger word
        3 means it is a word and it is not a substring of a bigger word
        '''
	def wordStatus(self, word):
            word = word.upper()
            if(len(word)!=0):
                char = word[0]
                return self.__wordStatus(self.root,word)
            else:
                return 1

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
                #not word or potential word
                return 0
            return self.__wordStatus(node.get(char), word[1:len(word)])


        '''
        prints all the nodes and what they point at with their respective layer

        example of what it looks like with the contents: birp, bike, bikes, bi, mad
        layer 1: Root node
        r o o t => {'B': <Trie._TrieNode object at 0x7fb87dfeb410>, 'M': <Trie._TrieNode object at 0x7fb87dfebe50>}
        layer 2:
        B => {'I': <Trie._TrieNode object at 0x7fb87dfeb950>}
        layer 3:
        I => {'K': <Trie._TrieNode object at 0x7fb87dfebf10>, 'R': <Trie._TrieNode object at 0x7fb87dfebdd0>}
        layer 4:
        K => {'E': <Trie._TrieNode object at 0x7fb87dfebd50>}
        layer 5:
        E => {'S': <Trie._TrieNode object at 0x7fb87dfebd90>}
        layer 4:
        R => {'P': <Trie._TrieNode object at 0x7fb87dfebe10>}
        layer 2:
        M => {'A': <Trie._TrieNode object at 0x7fb87dfebe90>}
        layer 3:
        A => {'D': <Trie._TrieNode object at 0x7fb87dfebed0>}
        '''
        def printTree(self):
            print "layer 1: Root node"
            print '         r o o t','=>',self.root.children
            self.__printTree(self.root,1)


        def __printTree(self,node,layer):
            layer+=1
            for child in node.getChildren():
                child = node.get(child)
                if(child.childCnt()!=0):
                    print "layer",str(layer)+":"
                    print '        ',child.getChar(),'=>',child.children
                    self.__printTree(child,layer)
