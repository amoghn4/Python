# Python Read in file
# import csv 

# GLOBAL VARIABLES
FILENAME = 'small_triangle.txt'
NUMBERWIDTH = 2
lines = []

def extract_data(filename):
    # infile = open(filename, 'r')
    # infile.readline() # skip the first line
    with open(filename) as infile:
        for line in infile:
            lines.append(line.strip().split(' '))
            
    return lines


def display():
    lines = extract_data(FILENAME)
    maxLength = len(max(lines, key=len))
    count = 0
    for line in lines:
        # print count
        lineSpace = maxLength/2-NUMBERWIDTH/2-NUMBERWIDTH/2*count+NUMBERWIDTH
        for i in range(lineSpace):
            print(' '),
        for number in line:
            print number, # print
        print # println
        count = count+1
        # print(*line) # print all elements in line list


        
def main():
    
    extract_data(FILENAME)
    display()

if __name__ == '__main__':
    main()