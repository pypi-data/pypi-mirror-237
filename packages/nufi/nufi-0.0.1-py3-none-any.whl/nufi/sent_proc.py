
# df_processed = nufi_examples_df.applymap(lambda x: x.replace("*","").split(":"))
# Nufi_ = df_processed.applymap(lambda x: x[0])


def word_end_with(Nufi,end_character = "b"):    
  sentences_containing_words_ending_with_ = []
  for k in range(len(Nufi)):    
    sentence_nufi = Nufi[k].strip()
    # sentence_nufi
    words_nufi = sentence_nufi.split()
    
    for i in words_nufi:
      if i.lower().endswith(end_character):
        sentences_containing_words_ending_with_.append(sentence_nufi)
        break  
        print(True)
  return sentences_containing_words_ending_with_

def word_start_with(Nufi,start_character = "b"):    
  sentences_containing_words_starting_with_ = []
  for k in range(len(Nufi)):    
    sentence_nufi = Nufi[k].strip()
    # sentence_nufi
    words_nufi = sentence_nufi.split()
    
    for i in words_nufi:
      if i.lower().startswith(start_character.lower()):
        sentences_containing_words_starting_with_.append(sentence_nufi)
        break  
        print(True)
  return sentences_containing_words_starting_with_

def word_start_with_at_least_n(Nufi,start_character = "b",n = 2):    
  sentences_containing_words_starting_with_ = []

  
  for k in range(len(Nufi)):    
    sentence_nufi = Nufi[k].strip()
    # sentence_nufi
    words_nufi = sentence_nufi.split()
    count = 0
    for i in words_nufi:
      if i.lower().startswith(start_character.lower()):
        
        count += 1
        
        if count >= n:
          sentences_containing_words_starting_with_.append(sentence_nufi)
          # break
    # print(count)   
  return sentences_containing_words_starting_with_

def word_end_with_at_least_n(Nufi,end_character = "b",n = 2):    
  sentences_containing_words_ending_with_ = []

  
  for k in range(len(Nufi)):    
    sentence_nufi = Nufi[k].strip()
    # sentence_nufi
    words_nufi = sentence_nufi.split()
    count = 0
    for i in words_nufi:
      if i.lower().endswith(end_character.lower()):
        
        count += 1
        
        if count >= n:
          sentences_containing_words_ending_with_.append(sentence_nufi)
          # break
    # print(count)   
  return sentences_containing_words_ending_with_



def sent_end_with(Nufi,end_character = "b"):    
  sentences_ending_with_ = []
  for k in range(len(Nufi)):    
    sentence_nufi = Nufi[k].strip()
    # sentence_nufi 
    if sentence_nufi.endswith(end_character):
      sentences_ending_with_.append(sentence_nufi)
      # break 
      # print(True)
  return sentences_ending_with_

def sent_start_with(Nufi,start_character = "b"):    
  sentences_starting_with_ = []
  for k in range(len(Nufi)):    
    sentence_nufi = Nufi[k].strip()
    # sentence_nufi 
    if sentence_nufi.startswith(start_character):
      sentences_starting_with_.append(sentence_nufi)
      # break 
      # print(True)
  return sentences_starting_with_


def sent_contain(Nufi,contain_character = "nàh"):    
  sentences_containing_words_containing_ = []
  for k in range(len(Nufi)):    
    sentence_nufi = Nufi[k].strip()
    # sentence_nufi
    words_nufi = sentence_nufi.split()
    
    for i in words_nufi:
      if contain_character in i:
        sentences_containing_words_containing_.append(sentence_nufi)
        break  
        print(True)
  return sentences_containing_words_containing_


# word_end_with(Nufi_,"e")
# nah = sent_contain(nufi_examples_df,"nàh")
# nah