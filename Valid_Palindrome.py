class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == " ":
            return True

        else:
            #change the characters to their ascii value
            self.ascii_lst = list()
            for char in s:
                if 65 <=ord(char) <= 90:
                    self.ascii_lst.append(ord(char) + 32)
                else:
                    self.ascii_lst.append(ord(char))

            #loop through the ascii list and add alphanumeric values to a new list,
            self.ascii_reduced_lst = list()
            for index in range(len(self.ascii_lst)):

                if (48 > self.ascii_lst[index] > 57) or (97 > self.ascii_lst[index] > 122):
                    self.ascii_lst.pop(index)
                    #self.ascii_reduced_lst.append(self.ascii_lst[index])

            #convert the ascii list into string list
            self.reduced_lst = list()
            for index in range(len(self.ascii_reduced_lst)):
                #self.reduced_lst.append(chr(self.ascii_reduced_lst[index]))
                self.reduced_lst.append(chr(self.ascii_lst[index]))

            #reverse the string list
            self.reversed_lst = [None]* len(self.reduced_lst)
            for i in range((len(self.reduced_lst)-1),-1, -1):
                j = (len(self.reduced_lst)-1) - i
                self.reversed_lst[j]= self.reduced_lst[i]

            if self.reduced_lst == self.reversed_lst:
                return True

            else:
                return False
        
