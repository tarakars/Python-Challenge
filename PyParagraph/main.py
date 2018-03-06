import os
import re

paragraph_path = os.path.join("raw_data", "paragraph_2.txt")


with open(paragraph_path,'r') as text:
    paragraph = text.read()
    words = paragraph.split(" ")
    print(str(len(words)))
    sentence = paragraph.split(".")
    print(str(len(sentence)))
    print(sentence)
    average_sentence_length = (len(words)/len(sentence))
    print(average_sentence_length)
    average_letter_count = (len(paragraph)/len(words))
    print(average_letter_count)



