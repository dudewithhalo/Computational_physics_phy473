# Tower of Hanoi

def tower_of_hanoi(n, source, to, intermediate):
    if (n==1):
        print("transfer disk ", source, "to ", to)
    else:
        tower_of_hanoi(n-1,source,intermediate,to)
        print("transfer disk ", source,"to ", to)
        tower_of_hanoi(n-1, intermediate, to ,source)

n = int(input("Enter numer of disks: "))
tower_of_hanoi(n,"a","b","c")
