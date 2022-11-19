def main():
    n = int(input("Enter max number: "))
    choice = input("Enter O/E/B (Odd/Even/Both): ")
    sure = input("Enter Y/N (OnlyPrime?): ")
    prime_and_odd(n,choice,sure)
def prime_and_odd(n,choice,sure):
    # recursion version
    if n==0:
        return
    if n==1 and sure=="Y" and (choice=="O" or choice=="B"):
        print(n,"is prime number")
    else:
        if sure == "Y":
            if is_prime(n):
                if choice == "O":
                    if is_odd(n):
                        print(n,"is prime number")
                elif choice == "E":
                    if not is_odd(n):
                        print(n,"is prime number")
                elif choice == "B":
                    print(n,"is prime number")
        else:
            if is_prime(n):
                if choice == "O":
                    if is_odd(n):
                        print(n,"is prime number")
                elif choice == "E":
                    if not is_odd(n):
                        print(n,"is prime number")
                elif choice == "B":
                    print(n,"is prime number")
            else:
                if choice == "O":
                    if is_odd(n):
                        print(n,"is not prime number")
                elif choice == "E":
                    if not is_odd(n):
                        print(n,"is not prime number")
                elif choice == "B":
                    print(n,"is not prime number")
        prime_and_odd(n-1,choice,sure)
def is_prime(n):
    # recursion version
    if n==1:
        return False
    elif n==2:
        return True
    else:
        return is_prime_helper(n,n-1)
def is_prime_helper(n,i):
    # recursion version
    if i==1:
        return True
    else:
        if n%i==0:
            return False
        else:
            return is_prime_helper(n,i-1)
def is_odd(n):
    # recursion version
    if n==0:
        return False
    elif n==1:
        return True
    else:
        return is_odd(n-2)
if __name__ == "__main__":
    main()