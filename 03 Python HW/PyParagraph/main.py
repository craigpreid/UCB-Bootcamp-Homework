import re
import os


#Create a function to use regex to find spaces
#Spaces will be an approximation of word count
def wordcount(value):
    # Find all non-whitespace patterns.
    list = re.findall("(\S+)", value)
    # Return length of resulting list.
    return len(list)


#Use regex to find all ANSCii characters
def charactercount(value2):
    # Find all characters
    list2 = re.findall("([a-z0-9A-Z])", value2)
    # Return length of resulting list.
    return len(list2)

#Attempt to to use regex to define sentences
def sentencesplit(value3):
    list3 = re.findall("(?<=[.!?]) +", value3)
    return len(list3)



#set variables that we will count with for loop
sentencecount = 0
lines, blanklines, countofwords, words = 0, 0, 0, 0

#Create path to .txt file
filepath = os.path.join('Resources','mcphee_short.txt')

#Open the .txt file we want to process
with open (filepath,'r') as f: 
    data = f.readlines()

    #Store text and use wordcount function
    value = str(data)
    countofwords = (wordcount(value))

    value2 = str(data)
    characters = (charactercount(value2))

    value3 = str(data)
    sentence2 = (sentencesplit(value3))
  
    for line in data:
      lines += 1
      
      if line.startswith('\n'):
        blanklines += 1
      else:
        # assume that each sentence ends with . or ! or ?
        # count these characters
        sentencecount += line.count('. ') + line.count('!') + line.count('?')
        
        # create a list of words
        # use None to split at any whitespace regardless of length
        # so for instance double space counts as one space
        tempwords = line.split(None)
               
        # a second method to get word count for fun
        words += len(tempwords)
        
#Print to terminal
print("Paragraph Analyis")
print("-----------------")
print("Approximate word count: " + str(countofwords) + " & calculated this way: " + str(words))
print("Approximate sentence count: " + str(sentencecount) + " & calculated this way: " + str(sentence2))
print("Average letter count: " +str(format(characters/countofwords,'.1f')))
print("Average sentence length: " +str(format(characters/sentencecount,'.1f')))

#print to txt file
fileout = os.path.join('Output','counter.txt')

with open(fileout,'w') as file:
    file.write("Paragraph Analyis" +'\n')
    file.write("-----------------" +'\n')
    file.write("Approximate word count: " + str(countofwords)+'\n')
    file.write("Approximate sentence count: " + str(sentencecount)+'\n')
    file.write("Average letter count: " +str(format(characters/countofwords,'.1f'))+ '\n')
    file.write("Average sentence length: " +str(format(characters/sentencecount,'.1f')))

file.close()
