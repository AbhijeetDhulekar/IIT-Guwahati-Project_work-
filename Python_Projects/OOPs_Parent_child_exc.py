## Q1 = Create a file class for reading data from respective file with a method name read and write.
## Q2 = Try to inheriet read and write mwthod from parent class to child class to perform read and write operation.

class readFile:
    def __init__(self, fileObj, lines):
        self.file = fileObj
        self.lines = lines

    def readFile(self):
        file2 = open(self.file, 'r')
        line = file2.readline()
        while (line != ""):
            print(line)
            line = file2.readline()

    def writeFile(self):
        content_write = open(self.file, 'w')
        content_write.writelines(lines)
        content_write.close()


class readFile1(readFile):
    def readFile(self):
        print("Inheritance pf readFile class")


file1 = r'test.txt'
lines = 'Inserted Lines....'

read_write = readFile1(file1, lines)
read_write.writeFile()
read_write.readFile()