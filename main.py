
blarghFile = open("ospd.txt","r")
newDict = blarghFile.readlines()


userLetters = raw_input("Enter your available letters: ")


"""Trying to hash out a functino for matching all two letter words"""
def twoLetterWords(lettersFromUser):
    indexOfLetters = 0
    #for x in range(0,len(lettersFromUser)):
        #for word in 
        #if (lettersFromUser[indexOfLetters] + lettersFromUser[x]) ==
        
"""One time use function for making separate dictionaries for each length of words"""
def sortDictionary(wordList):
    twoWordDictionary = open("2 Word Dictionary.txt","w")
    threeWordDictionary = open("3 Word Dictionary.txt","w")
    fourWordDictionary = open("4 Word Dictionary.txt","w")
    fiveWordDictionary = open("5 Word Dictionary.txt","w")
    sixWordDictionary = open("6 Word Dictionary.txt","w")
    sevenWordDictionary = open("7 Word Dictionary.txt","w")
    eightWordDictionary = open("8 Word Dictionary.txt","w")
    
    for x in range(0, len(wordList)):
        if len(wordList[x]) == 2:
            twoWordDictionary.write(wordList[x] + "\n")
        elif len(wordList[x]) == 3:
            threeWordDictionary.write(wordList[x] + "\n")
        elif len(wordList[x]) == 4:
            fourWordDictionary.write(wordList[x] + "\n")
        elif len(wordList[x]) == 5:
            fiveWordDictionary.write(wordList[x] + "\n")
        elif len(wordList[x]) == 6:
            sixWordDictionary.write(wordList[x] + "\n")
        elif len(wordList[x]) == 7:
            sevenWordDictionary.write(wordList[x] + "\n")
        elif len(wordList[x]) == 8:
            eightWordDictionary.write(wordList[x] + "\n")
        else:
            pass


#for i in range(0, len(newDict)):
    #newDict[i] = newDict[i].rstrip()

#for x in range(x,len(userLetters)):
    #tempWord = 
    
        




'''
for x in range(0,len(newDict)):
    if userLetters == newDict[x]:
        print newDict[x]
    else:
        print "No words"
        '''
            
