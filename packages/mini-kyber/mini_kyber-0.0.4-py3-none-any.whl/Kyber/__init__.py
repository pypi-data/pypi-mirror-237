import random
import numpy as np

q = 1664
mod = 2 * q + 1
N = 256

def addMod(a, b):
    val = (a + b) % mod
    if val > q:
        val -= mod
    elif val < -q:
        val += mod
    return val

def print_matrix(matrix):
    for row in matrix:
        print(", ".join(map(str, row)))
        print()

def mul(v1, v2):
    n = len(v1)
    ret = [0] * n
    for i in range(n):
        a = v2[i]
        for j in range(n):
            val = (a * v1[j]) % mod
            if val > q:
                val -= mod
            elif val < -q:
                val += mod

            ret[(i + j) % n] += val if i + j < n else -val
            ret[(i + j) % n] %= mod

            if ret[(i + j) % n] > q:
                ret[(i + j) % n] -= mod
            elif ret[(i + j) % n] < -q:
                ret[(i + j) % n] += mod

    return ret

def add(v1, v2):
    n = len(v1)
    ret = [0] * n
    for i in range(n):
        val = (v1[i] + v2[i]) % mod
        if val > q:
            val -= mod
        elif val < -q:
            val += mod
        ret[i] = val

    return ret

def subtract(v1, v2):
    n = len(v1)
    ret = [0] * n
    for i in range(n):
        val = (v1[i] - v2[i]) % mod
        if val > q:
            val -= mod
        elif val < -q:
            val += mod
        ret[i] = val

    return ret

def matrix_multiplication(matrix1, matrix2, e):
    m = len(matrix1)
    n = len(matrix1[0])
    t = len(matrix2[0])
    size = len(matrix1[0][0])

    ret = [[[0 for _ in range(size)] for _ in range(t)] for _ in range(m)]

    for i in range(m):
        for j in range(t):
            vec = e[i][j]
            for k in range(n):
                v = mul(matrix1[i][k], matrix2[k][j])
                for c in range(size):
                    vec[c] = addMod(vec[c], v[c])
            ret[i][j] = vec

    return ret

def create_random_vector(m1, m2, m3, range_val, neg):
    vec = []
    for i in range(m1):
        inner_vec = []
        for j in range(m2):
            inner_inner_vec = []
            for k in range(m3):
                val = random.randint(0, range_val - 1)
                r = random.randint(0, 1)
                if neg and r == 1:
                    val *= -1
                inner_inner_vec.append(val)
            inner_vec.append(inner_inner_vec)
        vec.append(inner_vec)
    return vec

def encrypt(A, t, m):
    r = create_random_vector(1, 2, N, 2, 1)
    e1 = create_random_vector(1, 2, N, 2, 1)
    e2 = create_random_vector(1, 2, N, 1, 0)

    u = matrix_multiplication(r, A, e1)
    V = matrix_multiplication(r, t, e2)

    v = []
    for i in range(len(m)):
        v1 = add(V[0][0], m[i])
        v.append(v1)

    return u, v

def decrypt(s, u, v):
    e0 = create_random_vector(1, 2, N, 1, 0)
    dv = matrix_multiplication(u, s, e0)

    d_e = []
    for i in range(len(v)):
        d_e1 = subtract(v[i], dv[0][0])
        d_e.append(d_e1)

    messages = []
    for i in range(len(v)):
        message1 = ""
        for j in range(len(d_e[i])):
            if d_e[i][j] < -q / 2 or d_e[i][j] > q / 2:
                message1 += '1'
            else:
                message1 += '0'
        messages.append(message1)

    return messages

def create_keys():
    A = create_random_vector(2, 2, N, q, 1)
    s = create_random_vector(2, 1, N, 2, 1)
    e = create_random_vector(2, 1, N, 2, 1)

    return A, s, e

def int_to_binary(n):
    return bin(n)[2:].zfill(8)

def convert_message_to_binary(str):
    vec = []
    ret = ""

    for i in range(len(str)):
        num = ord(str[i])
        s = int_to_binary(num)
        ret += s
        if len(ret) == N:
            vec.append(ret)
            ret = ""

    return vec

def convert_message_to_original(vec):
    ret = ""
    for s in vec:
        n = len(s)
        i = 0
        while i < n:
            binary_char = s[i:i + 8]
            i += 8
            num = int(binary_char, 2)
            ch = chr(num)
            if ch != '#':
                ret += ch

    return ret

def kyber(str):
    KeyComponents = create_keys()
    A, s, e = KeyComponents
    t = matrix_multiplication(A, s, e)
    ct = len(str) % N
    while ct > 0:
        str += '#'
        ct -= 1

    vec = convert_message_to_binary(str)

    m = []

    for i in range(len(vec)):
        ss = vec[i]
        mvec = []
        for c in ss:
            if c == '0':
                mvec.append(0)
            else:
                mvec.append(-q)
        m.append(mvec)

    u, v = encrypt(A, t, m)

    # print(u,v)
    return u, v
