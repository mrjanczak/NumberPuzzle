
import copy
import numpy as np
import collections
import sys

n = 4
# allowable indexies in columns & rows
c_ = np.repeat(np.arange(n), n).reshape((4,4)).transpose().tolist()
r_ = copy.deepcopy(c_)

# required elements in diagonals
d_ = np.arange(n).tolist()

# initial matrix of unit digits adders indexies
u_ = [[],[],[],[]]

num_R = {
    11:11,
    16:91,
    18:81,
    19:61,
    61:19,
    66:99,
    68:89,
    69:69,
    81:18,
    86:98,
    88:88,
    89:68,
    91:16,
    96:96,
    98:86,
    99:66,
}

base = 6
adder = [-5,0,2,3]
sum = 264

U = []
S = []

# sorting of U to find proper order of unit and ten digit adder indexies
sort_options = []
for r in range(n-1):
    for c in range(n):
        r__ = []
        if c != r:
            if r == 0:
                r0 = 1
            else:
                r0 = r
            for rr in range(r0, n):
                if c != rr:
                    r__.append(rr)
        if len(r__) > 1:
            dict = {'c' : c, 'r' : r, 'r_' : r__}
            sort_options.append(dict)             

def next_cell(c, r, n = n):
    last = False
    r += 1
    if r > n-1:
        r = 0
        c +=1
    if r == n-1 and c == n-1:
        last = True
    return c, r, last

def fill_U(u_, c, r, c_, r_, last = False):
    i_ = np.intersect1d(c_[c], r_[r])             
    for i in i_:
        u__ = copy.deepcopy(u_)
        c__ = copy.deepcopy(c_)    
        r__ = copy.deepcopy(r_)   

        # print(c,r,u__, c__, r__)

        u__[c].append(i)
        c__[c].remove(i)
        r__[r].remove(i) 


        if last:
            check_diagonals(u__)   
        else:     
            c_next, r_next, last = next_cell(c, r)
            fill_U(u__, c_next, r_next, c__, r__, last)

def check_diagonals(u, n = n):
    global U
    u_ = np.array(u)
    u_T = np.rot90(u_)

    d1 = np.diag(u_)
    d2 = np.diag(u_T)   

    if collections.Counter(d1) == collections.Counter(d_) and collections.Counter(d2) == collections.Counter(d_):
        U.append(u_T)

def sort_U(u_, t_, sort_i = 0):
    global sort_options
    c = sort_options[sort_i]['c']
    r = r0 = sort_options[sort_i]['r']
    r1_ = sort_options[sort_i]['r_']

    for r1 in r1_:
        u__ = copy.deepcopy(u_)
        t__ = copy.deepcopy(t_)
        u__[r0][c], u__[r1][c] = u__[r1][c], u__[r0][c]
        t__[r0][c], t__[r1][c] = t__[r1][c], t__[r0][c]

        if u__[r][c] not in u__[r][:c] and u__[r][c] not in u__[r][:c]:
            if sort_i < len(sort_options) - 1:
                sort_U(u__, t__, sort_i + 1)
            else:
                fill_S(u__, t__)

def fill_S(u_, t_):
    global S

    # check if adder indexes are complete in rows & diagonals
    correct = True
    for u in u_.tolist():
        if collections.Counter(u) != collections.Counter(d_):
            correct = False
            break

    for t in t_.tolist():
        if collections.Counter(t) != collections.Counter(d_):
            correct = False
            break

    t_T = np.rot90(t_)
    d2 = np.diag(t_T)   
    if collections.Counter(d2) != collections.Counter(d_):
        correct = False

    if not correct:
        return

    # Calculate solutions
    s_ = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            num = 10 * (base + adder[t_[i][j]]) + (base + adder[u_[i][j]])
            s_[i][j] = num


    # calculate rotated matrix (with rotated digits)
    s_R = np.zeros((n,n))
    for i in range(n):
        for j in range(n):                
            s_R[i][j] = num_R[s_[i][j]]
    s_R = np.rot90(s_R, 2)


    # check if sum of cols, rows & diagonals is correct (also after rotation by 180deg)
    for s in s_.tolist():
        if np.array(s).sum() != sum:
            correct = False
            break

    for s in s_.transpose().tolist():
        if np.array(s).sum() != sum:
            correct = False
            break

    for s in s_R.tolist():
        if np.array(s).sum() != sum:
            correct = False
            break

    d1_sum = np.diag(s_).sum()
    d2_sum = np.diag(np.rot90(s_)).sum()   
    if d1_sum != sum  or d2_sum != sum:
        correct = False
        
    if correct:    
        S.append(s_)
        print(s_,'\n---------------')

c, r = (0, 0)
fill_U(u_, c, r, c_, r_)

for u_ in U:
    t_ = np.repeat(np.arange(n), n).reshape((4,4))
    sort_U(u_, t_ )

print('S size',len(S))
