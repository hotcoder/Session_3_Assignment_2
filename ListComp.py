'''
Created on Nov 15, 2017

@author: z002krv
'''
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

inputList_0 = [1,2,3]
inputList_1 = [1,2,3]

outPutList = [(i,j) for i in inputList_0 for j in inputList_1]

outPutList.sort(key=lambda x:x[1])

print(outPutList)

#################################
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']   

inputList_2 = ['x','y','z']

outputList_2 = [[x ,x*2 ,x*3 , x*4] for x in inputList_2]

outputList_2_1 = [item for group  in outputList_2 for item in group]

print(outputList_2_1)

outputList_2_1.sort(key=len)

print(outputList_2_1)


##############################
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

inputList_3 = [['x','y','z']]

outputList_2 = [[x ,x*2 ,x*3 , x*4] for group in inputList_3]

outputList_2_1 = [item for group  in outputList_2 for item in group]

#print(outputList_2_1)

##############################

# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]

input_nested_list = [[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]

print([[number + 1 for number in group] for group in input_nested_list])

##############################

# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]

l = [[2],[3],[4]]

rl = [[[k+i for k in j] for j in l ] for i in range(0,3)]

newL = sum(rl,[])

print(newL)

################################

# ['A', 'C', 'A', 'D', 'G', 'L', 'I', 'D']

name = 'ACADGLID'

print([letter for letter in name])







