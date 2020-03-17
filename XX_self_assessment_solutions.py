# A possible solution to Ex. 0: Numpy
import numpy as np

# 1.
A = np.random.randn(5, 9) * 0.2 + 3.5 
print("shape of A:", A.shape)  # This should be (5, 9)

# 2.
b = A.reshape(-1)
print("shape of b:", b.shape)  # It should be equal to (49,) which is 5*9 
b_mean = b.mean()
print("mean of b:", b_mean)  # It should be approximately 1.5
b_var = b.var()
print("var of b:", b_var)  # It should be approximately 0.04 = 0.2**2 

# 3.
C = A.dot(A.T)

# 4.
C_diag = np.diag(C)
print("diag of C:", C_diag)  # They should all be roughly in between 100 and 120

# 5.
C_tr = C_diag.sum()
print("trace of C:", C_tr)

# 6.
C_det = np.linalg.det(C)
print("det of C:", C_det)

# 7.
eigval, eigvec = np.linalg.eigh(C)
lam = eigval

# 8. 
print("sum eigval:", lam.sum())  # It should be equal to C_tr

# 9. 
print("prod eigval:", lam.prod())  # It should be equal to C_det

# 10.
U = eigvec

# 11.
L = np.diag(lam)
D = U.dot(L).dot(U.T)
print("check D==C:", np.all(D == C))  # It may be not true, due to small approximation errors
print("check D approximately C:", np.allclose(D, C))  # This one is more appropriate to compare float numbers

