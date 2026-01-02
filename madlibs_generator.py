with open("story.txt","r") as f:
    story = f.read()  
   # enumerate will give access to the position 
   # set gives unique words no repettion
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"
# this block of code will look all characters of story
for i, char in enumerate(story):
   if char == target_start:
       start_of_word = i
            
   if char == target_end and start_of_word != -1 :
        word = story[start_of_word: i + 1] 
        words.add(word)
        start_of_word = -1
            
answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer
    
for word in words:
    story = story.replace(word,answers[word])
print(story)      