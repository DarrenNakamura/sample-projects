####################################################################################################
# Program: pyramidpuzzlesolver.py                                                                  #
# Author:  Darren Nakamura                                                                         #
# Notes:   This program was hand-coded by the author without any use of artificial intelligence.   #
#          It was created as an exercise in an application for a Software Engineer I position with #
#          Art of Problem Solving. Given a pyramid descent puzzle, this program will print all     #
#          solutions to the puzzle. If the puzzle has no solution, it will print nothing. Since it #
#          uses recursion, it will check every possible path from the top of the pyramid to the    #
#          bottom. As a result of this, its time efficiency is not great, taking O(2^n) time,      #
#          where n is the number of levels in the pyramid.                                         #
####################################################################################################

# Open the file
file = open('pyramid_sample_input.txt', 'r')

# Get the target integer
targetStr = file.readline()
targetStr = targetStr[8:]
targetInt = int(targetStr)

# Get the rest of the input file as integers
pyramidList = file.readlines()
numLevels = len(pyramidList)
for i in range(numLevels):
    pyramidList[i] = pyramidList[i].rstrip('\n')     # Strip newline
    pyramidList[i] = pyramidList[i].split(',')       # Split each line into an array
    for j in range(len(pyramidList[i])):
        pyramidList[i][j] = int(pyramidList[i][j])   # Convert strings to integers

# Close the file
file.close()

# Recursive function to check each path down the pyramid
def PyramidRecursion(product, depth, index, outStr):
    # Multiply the factor in the current position
    product *= pyramidList[depth][index]

    # If we've reached the maximum depth, print solution or just go back
    if (depth == numLevels - 1):
        if (product == targetInt):
            print(outStr)
            return
        else:
            return
    # Otherwise, check the left and right branches from where you are
    else:
        # Check the left branch recursively
        outStr += "L"
        depth += 1
        PyramidRecursion(product, depth, index, outStr)
        outStr = outStr[:-1]

        # Check the right branch recursively
        outStr += "R"
        index += 1
        PyramidRecursion(product, depth, index, outStr)

# Call the function with the given data
startProduct = 1
startDepth = 0
startIndex = 0
startResult = ""
PyramidRecursion(startProduct, startDepth, startIndex, startResult)