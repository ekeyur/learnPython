word = raw_input("Please enter a word: ")
word += " "
new_word = ''
for i in xrange(len(word)-1):
    if(word[i] == word[i+1]):
        new_word+= word[i] * 5
    else:
        new_word+= word[i]
print ''.join(new_word)
