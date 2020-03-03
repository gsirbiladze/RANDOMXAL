from pprint import pprint
from random import randint

def line_rotate_ccw(arr, n):
    n = n%len(arr)
    for _ in range(n):
        arr=arr[1:]+arr[:1]

    return arr

# M x N
M=300
N=300
R=30000

matrix=[ [ randint(0, 100) for _ in range(N) ] for _ in range(M) ]


levels=(M if M<N else N)//2
# print("Levels: %s " % levels)
# print("Matrix:")
# pprint(matrix)


for lvl in range(levels):
    top    = matrix[lvl][lvl:N-lvl]
    bottom = matrix[M-(lvl+1)][lvl:N-lvl]
    left   = []
    right  = []
    
    for row_idx in range(lvl+1, M-(lvl+1)):
        left.append(matrix[row_idx][lvl])
        right.append(matrix[row_idx][N-(lvl+1)])

    left.reverse()
    bottom.reverse()

    linead_up = top + right + bottom + left
    # Rotate
    linead_up = line_rotate_ccw(linead_up, R)

    # Chop-chop
    chop_top  = N-(lvl*2)
    chop_side = M-((lvl+1)*2)

    # print("linead_up %s" % linead_up)
    top    = linead_up[0:chop_top]
    # print("top %s" % top)
    right  = linead_up[chop_top: chop_top+chop_side]
    # print("right %s" % right)
    bottom = linead_up[chop_top+chop_side : chop_top+chop_side+chop_top]
    # print("bottom %s" % bottom)
    bottom.reverse()
    left   = linead_up[chop_top+chop_side+chop_top: chop_top+chop_side+chop_top+chop_side]
    # print("left %s" % left)
    left.reverse()

    matrix[lvl][lvl:N-lvl] = top
    matrix[M-(lvl+1)][lvl:N-lvl] = bottom

    for row_idx in range(lvl+1, M-(lvl+1)):
        # print(row_idx, lvl)
        matrix[row_idx][lvl] = left[row_idx-(lvl+1)]
        matrix[row_idx][N-(lvl+1)] = right[row_idx-(lvl+1)]

for m in range(0, M):
    for n in range(0, N):
        print("%s " % matrix[m][n], end='')
    print("")


def matrixRotation(matrix, r):
    def line_rotate_ccw(arr, n):
        n = n%len(arr)
        for _ in range(n):
            arr=arr[1:]+arr[:1]
        return arr

    # M x N
    M=len(matrix)
    N=len(matrix[0])
    R=r

    levels=(M if M<N else N)//2

    for lvl in range(levels):
        top    = matrix[lvl][lvl:N-lvl]
        bottom = matrix[M-(lvl+1)][lvl:N-lvl]
        left   = []
        right  = []
        
        for row_idx in range(lvl+1, M-(lvl+1)):
            left.append(matrix[row_idx][lvl])
            right.append(matrix[row_idx][N-(lvl+1)])

        left.reverse()
        bottom.reverse()

        linead_up = top + right + bottom + left
        # Rotate
        linead_up = line_rotate_ccw(linead_up, R)

        # Chop-chop
        chop_top  = N-(lvl*2)
        chop_side = M-((lvl+1)*2)

        top    = linead_up[0:chop_top]
        right  = linead_up[chop_top: chop_top+chop_side]
        bottom = linead_up[chop_top+chop_side : chop_top+chop_side+chop_top]
        bottom.reverse()
        left   = linead_up[chop_top+chop_side+chop_top: chop_top+chop_side+chop_top+chop_side]
        left.reverse()

        matrix[lvl][lvl:N-lvl] = top
        matrix[M-(lvl+1)][lvl:N-lvl] = bottom

        for row_idx in range(lvl+1, M-(lvl+1)):
            matrix[row_idx][lvl] = left[row_idx-(lvl+1)]
            matrix[row_idx][N-(lvl+1)] = right[row_idx-(lvl+1)]

    for m in range(0, M):
        for n in range(0, N):
            print("%s " % matrix[m][n], end='')
        print("")

