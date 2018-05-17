# Roman Bond
# reading files
def main():
    # read the file here
    file = open("yesno.txt", "r")
    lines = file.readlines() # use readlines bc we need to process each line seperatelely
    file.close()
    # find patterns
    countY  = 0
    countN  = 0
    for line in lines:
        # need to clean the line when read
        line = line.strip()
        # "print( line )" then you'd see each Y/N seperated by a blank line
        if line.find( "YES" ) != -1 and len(line) == 3:
            countY = countY + 1
        if line.find( "NO" ) != -1 and len(line) == 3:
            countN = countN + 1
    # display the result here
    print( "Yes: ", countY)
    print( "No: ", countN)
main()