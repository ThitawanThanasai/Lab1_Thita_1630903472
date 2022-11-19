# diamond pattern with *
n= 5
for i in range(n):
    print(' '*(n-i-1)+'*'*(2*i+1))
for i in range(n-2,-1,-1):
    print(' '*(n-i-1)+'*'*(2*i+1))

# - Adjustable of width and depth
# - Can draw multiple diamonds
# - Error input handle

def diamond(n,width, depth):
    # recursion version
    if n==0:
        return
    else:
        for i in range(depth):
            print(' '*(depth-i-1)+'*'*(2*i+1))
        for i in range(depth-2,-1,-1):
            print(' '*(depth-i-1)+'*'*(2*i+1))
        diamond(n-1,width, depth)
def main():
    while True:
        try:
            n = int(input("Enter the amount of diamond: "))
            width = int(input("Enter width of diamond: "))
            depth = int(input("Enter depth of diamond: "))
            diamond(n,width, depth)
        except ValueError:
            print("Invalid input. Please enter an integer.")
        else:
            break
if __name__ == "__main__":
    main()