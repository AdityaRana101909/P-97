intro = input("Enter Your Introduction")
print(intro)
wordcount=1
charactercount=0

for character in intro :
    charactercount= charactercount+1
    if character == ' ':
        wordcount=wordcount+1

print(charactercount)
print('No. of words in the string')
print(wordcount)