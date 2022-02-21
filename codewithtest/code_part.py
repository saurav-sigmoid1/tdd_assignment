import sys
class oddTimeNumberOccurance:
    def getOddOccurrence(self,arr, arr_size):
        for i in range(0, arr_size):
            count = 0
            for j in range(0, arr_size):
                if arr[i] == arr[j]:
                    count += 1

            if (count % 2 != 0):
                return arr[i]

        return -1

    # def readFromfile(self,filename):
    #     sys.stdin = open('test.txt', 'r')
    #     line = infile.readline()
    #     return line
#
#
# # driver code
if __name__ == "__main__":
    arr=[]
    inputs=[]

    # print(sys.stdin)
    for i in range(2):
        inputs = input()
        for val in inputs:
            if val!=' ' and val!='\n':
                arr.append(int(val))
        n = len(arr)
        obj = oddTimeNumberOccurance()
        print(obj.getOddOccurrence(arr, n))
        arr=[]