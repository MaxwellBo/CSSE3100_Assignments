EMPTY = None

def pretty(i, j, k, r, D):
    print(i, j, k, r, [ i for i in D if i != EMPTY ])

A = list(range(1, 12, 2)); print(f"The length of A is {len(A)}")
B = list(range(5, 17, 1)); print(f"The length of B is {len(B)}")
C = list(range(6, 19, 3)); print(f"The length of C is {len(C)}")
# A = list(range(1, 10))
# B = list(range(1, 10))
# C = list(range(1, 10))
D = [EMPTY] * max(len(A), len(B), len(C))

i, j, k, r = 0, 0, 0, 0; print("\nKEY"); pretty("i", "j", "k", "r", D); print()

while ((i != len(A)) or (j != len(B)) or (k != len(C))):
    assert set(D[0:r]) == set(A[0:i]) & set(B[0:j]) & set(C[0:k])
    pretty(i, j, k, r, D)

    if   (A[i] > B[j]): 
        print(f"A[{i}]:{A[i]} > B[{j}]:{B[j]}")
        j = j + 1; 
    elif (B[j] > C[k]):
        print(f"B[{j}]:{A[j]} > C[{k}]:{C[k]}")
        k = k + 1;
    elif (C[k] > A[i]): 
        print(f"C[{k}]:{C[k]} > A[{i}]:{A[i]}")
        i = i + 1; 
    elif ((A[i] == B[j]) and (B[j] == C[k])):
        print(f"At A[{i}], B[{j}], and C[{k}], they had the value {A[i]}")
        i, j, k, D[r], r = i + 1, j + 1, k + 1, A[i], r + 1

assert set( i for i in D if i != EMPTY) == set(A) & set(B) & set(C)
pretty(i, j, k, r, D)
