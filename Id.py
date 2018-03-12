import sys
class Id:


    def Include(self,text,index):
        id_list= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']


        for letters in id_list:

            if (id_list.__contains__(text[index])):
                #print(text[index])
                return True

            else:
                return False



