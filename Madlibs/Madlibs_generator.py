with open('story.txt', 'r') as f:
    story = f.read()
    
target_start = '<'
target_end = '>'
words = set()
Word_start = -1

for i, char in enumerate(story):
    if char == target_start:
        Word_start = i

    if char == target_end and Word_start != -1:
        word = story[Word_start:i+1]
        words.add(word)
        Word_start = -1

answers = {}
for word in words:
    answer = input("Enter a word for" + word + ":")
    answers[word] = answer

for word in words:
    story.replace(word, answers[word])

print(story)  
