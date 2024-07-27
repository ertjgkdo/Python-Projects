
#read the file with the story
with open("story.txt", "r") as f:

    story = f.read()
# characters that surrounds the missing word in order to search for it    
target_start = '<'
target_end = '>'
words = []

# in order to check if the word is
Word_start = -1

for i, char in enumerate(story):
    if char == target_start:
        # the starting word is found and put it as a value in the variable 
        Word_start = i
    # if the word start is found and has a variable diff than -1, to search for end word
    if char == target_end and Word_start != -1:
        # a new variable having characters from the start to the current+1 index inorder to include current char
        word = story[Word_start:i+1]
        words.append(word)
        Word_start = -1

#dictionary where words are keys and input answer is value
answers = {}
for word in words:
    answer = input("Enter a word for" + word + ":")
    answers[word] = answer
print(answers)
for word in words:
    story = story.replace(word, answers[word])

print(story)  
