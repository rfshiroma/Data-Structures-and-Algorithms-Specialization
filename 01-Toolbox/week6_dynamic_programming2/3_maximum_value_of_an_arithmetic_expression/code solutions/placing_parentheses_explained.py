# Uses python3

# More about it:
  # https://www.geeksforgeeks.org/minimum-maximum-values-expression/
  # https://www.techiedelight.com/maximize-value-of-the-expression/
  # https://www.geeksforgeeks.org/all-ways-to-add-parenthesis-for-evaluation/

# Problem Statement:
# The task is to find the maximum value possible by adding parentheses to a given arithmetic expression to maximize its value.

# Approach idea with Dynamic Programming method:
  # Separate the operators and numbers from given expression;
  # Create two 2D-arrays for storing the intermediate result which are updated similar to "matrix chain multiplication" and different parenthesization are tried among the numbers but according to operators ocurring in between them.

# Utility method to check whether a character is operator or not
def isOperator(op):
    return (op == '+' or op == "*")


# Method prints minimum and maximum value obtainable from an expression
def printMinAndMaxValueOfExp(exp):
    num = []
    opr = []
    tmp = ""

    # store operator and numbers in different vectors
    for i in range(len(exp)):
        if (isOperator(exp[i])):
            opr.append(exp[i])
            num.append(int(tmp))
            tmp = ""
        else:
            tmp += exp[i]

    # storing last number in vector
    num.append(int(tmp))

    llen = len(num)
    minVal = [[ 0 for i in range(llen)] for i in range(llen)]
    maxVal = [[ 0 for i in range(llen)] for i in range(llen)]

    # initialising minVal and max_value 2D array
    for i in range(llen):
        for j in range(llen):
            minVal[i][j] = 10**9
            maxVal[i][j] = 0

            # initialising main diagonal by num values
            if (i == j):
                minVal[i][j] = maxVal[i][j] = num[i]

    # looping similar to matrix chain multiplication and updating both 2D arrays
    for L in range(2, llen + 1):
        for i in range(llen - L + 1):
            j = i + L - 1
            for k in range(i, j):
                minTmp = 0
                maxTmp = 0

                # if current operator is '+', updating tmp variable by addition
                if (opr[k] == '+'):
                    minTmp = minVal[i][k] + minVal[k+1][j]
                    maxTmp = maxVal[i][k] + maxVal[k+1][j]


                # if current operator is '*', updating tmp variable by multiplication
                elif (opr[k] == '*'):
                    minTmp = minVal[i][k] * minVal[k+1][j]
                    maxTmp = maxVal[i][k] * maxVal[k+1][j]

                # updating array values by tmp variables
                if (minTmp < minVal[i][j]):
                    minVal[i][j] = minTmp
                if (maxTmp > maxVal[i][j]):
                    maxVal[i][j] = maxTmp

    # last element of first row will store the result
    print("Mininum value: ", minVal[0][llen - 1], "\nMaximum value: ", maxVal[0][llen - 1])



if __name__ == "__main__":
    expression = "1+2*3+4*5"
    print(printMinAndMaxValueOfExp(expression))
