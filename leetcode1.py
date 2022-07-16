"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

# Solution 1
""" 
def input(a,b,c,t):
    list = [a,b,c]
    ind = 0
    if list[0] + list[1] != t and list[0] + list[2] != t:
        ind += 1
    if list[0] + list[1] == t:
        print(str(ind)  + ", " +  str(ind + 1))
    if list[0] + list[2] == t:
        print(str(ind)  + ", " +  str(ind + 2))
    if list[1] + list[2] == t:
        print(str(ind) + ", " + str(ind + 1))


def main():
    input(4, 2, 3,7)


if __name__ == '__main__':
    main()

"""
def input(a,b,c,t):
    list = [a,b,c]
    for n in range(0, len(list)):
        for m in range(0, len(list)):
            if list[n] + list[m] == t:
                print(str(n) + ", " + str(m))


def main():
    input(2, 4, 1,5)


if __name__ == '__main__':
    main()

        

