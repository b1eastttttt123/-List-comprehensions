
L = [int(x) for x in input().split()]

a,b = int(input()),int(input())

print(L[:a]+L[b+1:])
