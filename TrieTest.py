from Trie import Trie

def testContains(word, correct_result):
    print "Testing if Trie contains ",word,". Expecting ",correct_result
    if(words.contains(word)):
        print "Passed test: ",correct_result
    else:
        print "Passed test: ", not correct_result





global words;
words = Trie()

words.add("Bird")

testContains("bird",True);
