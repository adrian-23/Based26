import math

"""
Given an index 0<= i <= k,
find the corresponding letter it maps to on the letter list.
if it goes over the length of the list, find it's appropriate 
combination.

"""
class NumberLetterConverter:

    def __init__(self):
        self.letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    def getLetter(self,index:int):
        
        index+=1
        letter = ""
        letter_indexes = []
        
        if(index < 26):
            return self.letter_list[index]
        else:
            self.calculateIndices(index,letter_indexes)
        
        
        # convert indexes in 0 - 25 format
        self.convertIndexes(letter_indexes)
       
        
        #go through each index for letter processing.
        for i,number in enumerate(letter_indexes):
            if(i == 0 and number == 0):
                continue
            else:
                letter += self.letter_list[number - 1]
        
        return letter

        
    def calculateIndices(self,index,letter_indexes):
        remainder = index % 26
        whole_num = index // 26

        letter_indexes.insert(0, remainder)
        
        

        #we add the last number into our index list when it is no longer divisible
        if(whole_num < 26):
            letter_indexes.insert(0,whole_num)
            
            return letter_indexes
        
        else:
            
            return self.calculateIndices(whole_num,letter_indexes)


    def convertIndexes(self,letter_indexes):
        previousIsZero = False
        for i in range(len(letter_indexes)-1,-1,-1):
            if(previousIsZero):
                
                letter_indexes[i] -= 1
            if(letter_indexes[i] == 0):
                if(i != 0):
                    letter_indexes[i] = 26
                previousIsZero = True
            else:
                previousIsZero = False







