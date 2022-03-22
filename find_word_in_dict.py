!pip install textdistance
import pandas as pd
import numpy as np
import textdistance
import re
from collections import Counter
words = ['']
filename='file'
mylist=[]
for i in range(1,6):
  with open(filename,'r') as file1:
    file_name_data = file1.read()
    file_name_data=file_name_data.lower()
    words+=re.findall('\w+',file_name_data)
    
V=set(words)

word_freq_dict = {}  
word_freq_dict = Counter(words)

def my_autocorrect(input_word):
  input_word = input_word.lower()
  if input_word in V:
    return('Your word seems to be correct')
  else:
    tmp_sim=0
    word=''
    for v in word_freq_dict.keys():
      similarities = 1-(textdistance.Jaccard(qval=2).distance(v,input_word)) 
      if similarities  > tmp_sim:
        tmp_sim=similarities
        word=v
        return v

my_autocorrect('dadammmmmm')
