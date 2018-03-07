# Importing libraries we need
import os
import re # this library is not use but importe if needed we can use

paragraph_path = os.path.join("raw_data", "paragraph_2.txt") # creating a path for the data we need to read


with open(paragraph_path,'r') as text: #opening the text file in read only mode, 'r' represents read only mode
    paragraph = text.read() # reading the text file we have in to a variable which is a list
    words = paragraph.split(" ") # splitting the paragraph at each space and storing them in a new array
    print(str(len(words))) # we are counting number of words by using Len function and printing the count
    sentence = paragraph.split(".") #splitting the paragraph at each fullstop and storing them in a new array
    print(str(len(sentence)))  #we are counting number of sentences by using Len function and printing the count
    average_sentence_length = (len(words)/len(sentence)) # counting avergae sentence lenght in words and assiging them to an array
    print(average_sentence_length) #printing the avergae sentence lenght in words
    #by using the len(paragraph) we get number of letters in a paragraph, so we are calculating the average letter count for a word
    average_letter_count = (len(paragraph)/len(words)) 
    print(average_letter_count) # printing the average letter count
