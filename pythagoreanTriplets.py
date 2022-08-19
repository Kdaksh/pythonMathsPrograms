def if_Pythagoren(triplets):
    grtrSq = max(triplets)**2
    triplets.remove(max(triplets))
    n1Sq = triplets[0]**2
    n2Sq = triplets[1]**2

    if(grtrSq == n1Sq+n2Sq):
        return True
    return False

nthArr = [0,0,0]
nthArr[0] = int(input("Enter 1st Number : "))
nthArr[1] = int(input("Enter 2nd Number : "))
nthArr[2] = int(input("Enter 3rd Number : "))

print(if_Pythagoren(nthArr)) 