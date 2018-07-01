# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Find all strobogrammatic numbers that are of length = n.

# n = 0:   none

# n = 1:   0, 1, 8

# n = 2:   11, 69, 88, 96

# n = 3:   101, 609, 808, 906, 111, 619, 818, 916, 181, 689, 888, 986

# n = 4:   1001, 6009, 8008, 9006, 1111, 6119, 8118, 9116, 1691, 6699, 8698, 9696, 1881, 6889, 8888, 9886, 1961, 6969, 8968, 9966

def findStrobogrammatic(n):




 	if n == 0:
 		return ""
 	if n == 1:
 		return 0,1,8
 	if n > 1:
 		result = []
 		middles = [0,1,8,69,96]
 		middles2 = [mid for item in middles for mid in repeat(item, n-2)]
 		for mid in middles2:
 			print('mid is ' + str(mid))
 			result.append('1' + str(mid) + '1')
 			result.append('6' + str(mid) + '9')
 			result.append('8' + str(mid) + '8')
 			result.append('9' + str(mid) + '6')

 		# mid = 'x','y'
 		# t = '1' + str(mid) + '1'
 		# t = '6' + str(mid) + '9'
 		# len(mid) == n - 2
 	return result

findStrobogrammatic(5)

from itertools import repeat
l = [0,1,8,69,96]
[x for item in l for x in repeat(item, 3)]



def gen_strobogrammatic(n):
    """
    :type n: int
    :rtype: List[str]
    """
    #
    result = helper(n, n)
    return result


def helper(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = helper(n-2, length)
    print('middles are ' + str(middles))  # n= 5  3,5    
    result = []
    for middle in middles:
        if n != length:
            result.append("0" + middle + "0")  #010 
        result.append("8" + middle + "8")     #818
        result.append("1" + middle + "1")     #111
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
    return result

#print("n = 2: \n",gen_strobogrammatic(2))
print("n = 3: \n",gen_strobogrammatic(3))
print("n = 4: \n",gen_strobogrammatic(4))
print("n = 5: \n",gen_strobogrammatic(5))
print("n = 6: \n",gen_strobogrammatic(6))


