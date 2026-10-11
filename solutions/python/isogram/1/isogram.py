"""Determine if a word or phrase is an isogram."""

def is_isogram(phrase):

    phrase = phrase.lower()
    
    for letter_before in range(len(phrase)):
        
        for letter_after in range(letter_before + 1, len(phrase)):
            
            if phrase[letter_before] == phrase[letter_after] and phrase[letter_before] != " " and phrase[letter_before] != "-":
                
                return False
                
    return True