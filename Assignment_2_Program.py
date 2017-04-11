EMPTY = None

def pretty(i, j, k, r, D):
    print(i, j, k, r, [ i for i in D if i != EMPTY ])

A = list(range(1, 12, 2)); print(f"The length of A is {len(A)}")
B = list(range(5, 17, 1)); print(f"The length of B is {len(B)}")
C = list(range(6, 19, 3)); print(f"The length of C is {len(C)}")
# A = [0]
# B = [1]
# C = [1]
D = [EMPTY] * max(len(A), len(B), len(C))

i, j, k, r = 0, 0, 0, 0; print("\nKEY"); pretty("i", "j", "k", "r", D); print()

VARIANT = min(len(A) - i, len(B) - j, len(C) - k)

while ((i != len(A)) and (j != len(B)) and (k != len(C))):

    D_IS_INTERSECTION_OF_ALL_SEEN = (set(D[0:r]) == set(A[0:i]) & set(B[0:j]) & set(C[0:k]))
    IS_BOUNDED = i in range(len(A))\
             and j in range(len(B))\
             and k in range(len(C))\
             and r in range(len(D))

    assert IS_BOUNDED
    assert D_IS_INTERSECTION_OF_ALL_SEEN
    assert VARIANT != 0

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

    # Technically gets executed at the top of the loop
    VARIANT = min(len(A) - i, len(B) - j, len(C) - k)


# POSTCONDITION
assert set( i for i in D if i != EMPTY) == set(A) & set(B) & set(C)
assert i in range(len(A) + 1) and j in range(len(B) + 1) and k in range(len(C) + 1) and r in range(len(D) + 1)
assert VARIANT == 0

pretty(i, j, k, r, D)
