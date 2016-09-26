word = raw_input("Please enter a word: ")
new_word = ''
for i in xrange(len(word)):
    if(word[i] == word[i]):
        new_word+= word[i] * 5
    else:
        new_word+= word[i]
print ''.join(new_word)
