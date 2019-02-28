import random

#class
class NameCreater:
    
    def __init__(self, filename, search_char):
        self.readFile = open(filename, "r")
        self.searchvar = search_char.lower()
        

    def namePrinter(self):
        arr = []
        for line in self.readFile:
            lowerCaseLine = line.lower()
            if lowerCaseLine.startswith(self.searchvar):
                arr.append(line)
            
        if not arr:
            print("no name found") 
        else:   
            print(random.choice(arr))

        self.readFile.close()

#main program
while True:
    readinput = input("\nPlease insert starting name character: ")

    Name = NameCreater("name.txt",readinput)
    Name.namePrinter()

    #exit program condition
    if "1" == input("type 1 to exit, else to continue: "):
        exit()
   



    
