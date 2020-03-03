def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i<len(c):
        if (i+1 == n - 1) or (i+2 == n - 1):
            return jumps+1
        elif c[i+2] == 0:
            i+=2
        else:
            i+=1
        jumps+=1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    
    fptr.write(str(result) + '\n')
    fptr.close()
