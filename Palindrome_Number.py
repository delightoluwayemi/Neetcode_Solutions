#This class receives an input int x and returns
#true if it is a Palindrome and false otherwise
#constraint: ((-2)^31) <= x <= ((2^31) - 1)
class Solution:
    # the method converts the int into a string and then the reverse of the
    #string is copied into another string
    # returns true, if the two strings are equal and false otherwise
    def isPalindrome(self, x: int) -> bool:

        self.lst = list(str(x))
        self.new_lst = [None]* len(self.lst)

        #reverse the list
        for lst_index in range((len(self.lst)-1),-1, -1):
            new_lst_index = (len(self.lst)-1) - lst_index
            self.new_lst[new_lst_index]= self.lst[lst_index]

        #check if its a palindrome
        if self.lst == self.new_lst:
            return True
        else:
            return False
