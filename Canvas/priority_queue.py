import sys

def doSomething(blob, pattern):
    #Write your code here

for line in sys.stdin:
    splitted_input = line.split(';')
    pattern = splitted_input[0]
    blobs = splitted_input[1].split('|')

    result = doSomething(blob, pattern)
    print(result)


bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32
