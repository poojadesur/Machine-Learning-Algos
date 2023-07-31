import sys


## STATES
# f = open("./states.txt",'+w')

# for ai in range(2):
#     for aj in range(4):
#         for ti in range(2):
#             for tj in range(4):
#                 for call in range(2):

#                     if(call == 0):
#                         var = ((ai,aj),(ti,tj),"off")
#                     if(call == 1):
#                         var = ((ai,aj),(ti,tj),"on")

#                     f.write(str('s' + str(var).replace(' ','')))
#                     f.write(" ")


# f.close()

## OBSERVATION O1
# basic = "O: * : s"

# for i in range(2):
#     for j in range(4):
#         end = ([i,j],[i,j],'on')
#         final = basic + str(end).replace(' ','')
#         print(final)
#         print("1.0 0.0 0.0 0.0 0.0 0.0")
#         end = ([i,j],[i,j],'off')
#         final = basic + str(end).replace(' ','')
#         print(final)
#         print("1.0 0.0 0.0 0.0 0.0 0.0")

# # OBSERVATION O2
# basic = "O: * : s"

# for i in range(2):
#     for j in range(3):
#         end = ([i,j],[i,j+1],'on')
#         final = basic + str(end).replace(' ','')
#         print(final)
#         print("0.0 1.0 0.0 0.0 0.0 0.0")
#         end = ([i,j],[i,j+1],'off')
#         final = basic + str(end).replace(' ','')
#         print(final)
#         print("0.0 1.0 0.0 0.0 0.0 0.0")


# OBSERVATION O4
# basic = "O: * : s"

# for i in range(2):
#     for j in range(1,4):
#         end = ([i,j],[i,j-1],'on')
#         final = basic + str(end).replace(' ','')
#         print(final)
#         print("0.0 0.0 0.0 1.0 0.0 0.0")
#         end = ([i,j],[i,j-1],'off')
#         final = basic + str(end).replace(' ','')
#         print(final)
#         print("0.0 0.0 0.0 1.0 0.0 0.0")


#OBSERVATION 5
# basic = "O: * : s"

# for i in range(1,2):
#     for j in range(4):
#         end = ([i,j],[i-1,j],'on')
#         final = basic + str(end).replace(' ','')
#         print(final)
#         print("0.0 0.0 0.0 0.0 1.0 0.0")
#         end = ([i,j],[i-1,j],'off')
#         final = basic + str(end).replace(' ','')
#         print(final)
#         print("0.0 0.0 0.0 0.0 1.0 0.0")b

# OBSERVATION 3
basic = "O: * : s"


# for i in range(1):
#     for j in range(4):
#         end = ([i,j],[i+1,j],'on')
#         final = basic + str(end).replace(' ','')
#         print(final)
#         print("0.0 0.0 1.0 0.0 0.0 0.0")
#         end = ([i,j],[i-1,j],'off')
#         final = basic + str(end).replace(' ','')
#         print(final)
#         print("0.0 0.0 1.0 0.0 0.0 0.0")

# REWARD

basic = "R: STAY : * : * "

for i in range(2):
    for j in range(4):
        end = ((i,j),(i,j),'on')
        reward = " : o1 82"
        final = basic + str(end).replace(' ','') + reward
        print(final)


# basic = "R: * : * : "


# for i in range(2):
#     for j in range(4):
#         end = ((i,j),(i,j),'on')
#         reward = " : o1 81"
#         final = basic + str(end).replace(' ','') + reward
#         print(final)







# R: * : * : 0-0-0-0-on : * 71
# R: * : * : 0-1-0-1-on : * 71
# R: * : * : 0-2-0-2-on : * 71
# R: * : * : 0-3-0-3-on : * 71
# R: * : * : 1-0-1-0-on : * 71
# R: * : * : 1-1-1-1-on : * 71
# R: * : * : 1-2-1-2-on : * 71
# R: * : * : 1-3-1-3-on : * 71



