'''
Created on Oct 25, 2017

@author: z002krv
'''
def eg1_for(matrix):
    flat = []
    for row in matrix:
        for x in row:
            flat.append(x)
    return flat

def eg1_lc(matrix):
    return [x for row in matrix for x in row]

matrix = [ range(0,5), range(5,10), range(10,15) ]
print("Original Matrix: " + str(matrix))
print("FOR-loop result: " + str(eg1_for(matrix)))
print("LC result      : " + str(eg1_lc(matrix)))



def eg2_lc(sentence):
    vowels = 'aeiou'
    
    return ''.join([l for l in sentence if l not in vowels])


sentence = 'My name is Aarshay Jain!'
#print("FOR-loop result: " + eg2_for(sentence))
print ("LC result      : " + eg2_lc(sentence))



x = [[0]*2]*2

print(x)