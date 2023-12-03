def findFirstDigit(line):
    allPossibleNums =["one","two","three","four","five","six","seven","eight","nine"]
    numMap= [1,2,3,4,5,6,7,8,9]
    
    for i in range(len(line)):          
        if line[i].isdigit():
            return int(line[i])
        #check if everything beforehand contains a number
        currStr= line[0:i+1] 
        for j in range(0,len(allPossibleNums)):      
            if currStr.find(allPossibleNums[j])!=-1:
                return numMap[j]
    return -1
def findLastDigit(line):
    allPossibleNums =["one","two","three","four","five","six","seven","eight","nine"]
    numMap= [1,2,3,4,5,6,7,8,9]

    for i in range(len(line)-1,0,-1):
        if line[i].isdigit():
            return int(line[i])
        #check if everything beforehand contains a number
        currStr= line[i-1:len(line)] 
        for j in range(0,len(allPossibleNums)):      
            if currStr.find(allPossibleNums[j])!=-1:
                return numMap[j]
    return -1

# Read the lines from Day1.txt into an array
lines = []
with open('Day1.txt', 'r') as file:
    for line in file:
        lines.append(line.strip())
sum=0
for line in lines:
    first=findFirstDigit(line)
    last=findLastDigit(line)
    if first!=-1 and last!=-1:
        sum+=first*10+last
print(sum)