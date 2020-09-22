import math

"""
Given an index 0<= i <= k,
find the corresponding letter it maps to on the letter list.
if it goes over the length of the list, find it's appropriate 
combination.
"""
class NumberLetterConverter:

    def __init__(self):
        self.letter_list = ['','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    def getLetter(self,index:int):
        if index < 27:
            return self.letter_list[index]

        else:
            build_string = ""

            while(index != 0):
                
                if index % 26 == 0:
                    build_string = 'Z' + build_string
                    index-=1
                else:
                    
                    build_string = self.letter_list[index % 26] + build_string
                index //=26
                    

        return build_string




