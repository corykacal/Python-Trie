from Trie import Trie


def testRemove(word):
    print "Testing if Trie removes",word+'.',"\nExpecting ",True
    words.remove(word)
    if(not words.isWord(word)):
        print "Test passed: ",True,"\n"
    else:
        print "Test passed: ",False,"\n"

def testContains(word, correct_result):
    print "Testing if Trie contains",word+'.',"\nExpecting ",correct_result
    if(words.contains(word)):
        print "Test passed: ",correct_result,"\n"
    else:
        print "Test passed: ", not correct_result,"\n"

def wordStatus(word, expected_status):
    print "Testing the word status of",word+'.',"\nExpecting",expected_status
    actual_status = words.wordStatus(word)
    print "return status",actual_status,
    print "Test passed: ",expected_status==actual_status,'\n'





global words;
words = Trie()

words.add("bir")
words.add("birds")
words.add("23Apple!")
words.add("33")
words.add("%%%%%%")

print 'Testing the contains method\n'
#testing the contians/add method
testContains("bird",True)
testContains("23aPple!",True)
testContains("33",True)
testContains("",True)
testContains("&^%$%^#%^#",False)
testContains("%%%%%%",True)
testContains("%%%%%$",False)

print 'testing the remove method\n'
#testing the remove method
testRemove("bi")
testRemove("birds")
testRemove("zz")
testRemove("")
testRemove("21444443244453253253251")
testRemove("\n")


words = Trie()
words.add("BIRP")
words.add("mad")
words.add("bike")
words.add("bikes")
words.add("bi")

print 'testing the word status method\n'
#testing the word status method
wordStatus('bike',2)
wordStatus('bi',2)
wordStatus('birp',3)
wordStatus('birps',0)
wordStatus('ma',1)
wordStatus('zzzz',0)



words = Trie()
words.add("incel")
words.add("into")
words.add("intro")
words.add("introduction")
words.add("enter")
words.add("apple")
words.add("ape")

print words.asList()
print words.wordsWithPrefix("a")
print words.wordsWithPrefix("int")
print words.wordsWithPrefix("in")




