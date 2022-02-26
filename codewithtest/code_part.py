import sys


class  OddOccuranceCheck:

    def Check(self, arr, arr_size):
        """iterate over the array to check the number count occur even or odd times if there is no number occure odd time return -1"""

        for idx1 in range(0, arr_size):
            count = 0
            for idx2 in range(0, arr_size):
                if arr[idx1] == arr[idx2]:
                    count += 1

            if (count % 2 != 0):
                return arr[idx1]
        return -1

    def readFromFile(self,filename):
        infile = open(filename,'r')
        line = infile.readlines()
        return line


# driver code

if __name__ == "__main__":
    arr = []
    inputs = []
    sys.stdin = open('test.txt', 'r')
    """reading the input from the file and call the function to perform on the array"""
    for i in range(5):
        inputs = input()
        for val in inputs:
            if val != ' ' and val != '\n':
                arr.append(int(val))
        n = len(arr)
        obj = oddTimeNumberOccurance()
        print(obj.getOddOccurrence(arr, n))
        arr = []
