from sympy import factorint

"""
first we reduce the problem modulo prime powers
"""
def isogeny_graph(N,S):
    L = [[p, v] for p, v in factorint(N).items()]
    output=[]
    for p, v in L:
        R = Integers(p**v)
        Sp = [A.change_ring(R) for A in S]
        output.append(p_isogeny_graph(p, v, Sp))
    return output
    
"""a helper for smith normal form manipulations"""
def clear_entry(r1, r2, i, p, v):
    R = Integers(p**v)
    r1 = vector(R, r1)
    r2 = vector(R, r2)

    x = r1[i]
    y = r2[i]

    if y == 0:
        return r2

    vx = (x.lift()+p**v).valuation(p)
    vy = (y.lift()+p**v).valuation(p)
    

    if vx > vy:
  
        raise ValueError("Need vp(r1[i]) <= vp(r2[i])")
           
    # x = p^vx * u, y = p^vx * w
    u = x.lift() // (p**vx)
    w = y.lift() // (p**vx)

    # solve lambda*u = w mod p^(v-vx)
    lam = (w * inverse_mod(u, p**(v-vx)))%(p**v)
   
  
    return r2 - R(lam)*r1
    
    
"""a helper for finding pivot in smith normal form"""

def find_pivot_row_col(mat, p, cols):
    """
    Find pivot position (row, col) with smallest p-adic valuation.
    Ties are broken according to the order of cols.
    """
    best_row = None
    best_col = None
    best_val = Infinity

    for j in cols:
        for i in range(mat.nrows()):
            if mat[i,j] != 0:
                v = mat[i,j].valuation(p)
                if v < best_val:
                    best_val = v
                    best_row = i
                    best_col = j
    if best_row == None:
        best_row = 0
    if best_col == None:
        best_col = 0
    return best_row, best_col

"""a helper that moves the pivot row to the top"""
def move_pivot_to_top(mat, p, cols):
    # columns 1,3,2 in human notation
    pivot_row, pivot_col = find_pivot_row_col(mat, p, cols)

    mat.swap_rows(0, pivot_row)

    return pivot_row, pivot_col

    
"""
quadratic equation solver, A,B,C are coefficients of AX^2+BX+C we're trying to solve, p is our prime, v is our maximal precision (A,B,C are hence given mod p^v)
 output is a tuple (i, u, L) where i is the maximum precision to which we can solve, u is the smallest vp among A,B,C and L is a list of x modulo p^{i-u} which are solutions
  the set of solutions modulo p^i of our equation is the set of all x+k*p^{i-u} where x varies through L and k varies through integers mod p^u
 u is the minimum vp among A,B,C, and L is a list of a
"""

def quadratic_equation_solver(A, B, C, p, v):
    from sage.all import ZZ, Zmod, PolynomialRing, legendre_symbol, inverse_mod

    # 1. Safely calculate the minimum valuation u, handling 0 coefficients
    A_int = ZZ(A.lift()) if hasattr(A, 'lift') else ZZ(A)
    B_int = ZZ(B.lift()) if hasattr(B, 'lift') else ZZ(B)
    C_int = ZZ(C.lift()) if hasattr(C, 'lift') else ZZ(C)
    
    u_a = v if A_int == 0 else min(v, A_int.valuation(p))
    u_b = v if B_int == 0 else min(v, B_int.valuation(p))
    u_c = v if C_int == 0 else min(v, C_int.valuation(p))
    u = int(min(u_a, u_b, u_c))
    
    # If the equation is identically 0 mod p^v
    if u >= v:
        return 1, 0, [0]
        
    # 2. Scale down the coefficients by p^u
    a = A_int // p**u
    b = B_int // p**u
    c = C_int // p**u
    
    # Target modular ring for the scaled system
    R = Zmod(p**(v-u))
    P.<x> = PolynomialRing(R)
    f = a * x**2 + b * x + c
    
    # --- ODD PRIME CASE ---
    if p > 2:
        if a % p != 0:
            # Calculate discriminant over ZZ to avoid ring truncation issues
            disc = ZZ(b*b - 4*a*c)
            vd = v if disc == 0 else disc.valuation(p)
            
            if vd >= v - u:
                x1=(-b * inverse_mod(2*a, p**(v-u)))
                if (v-u)%2!=0:
                    return 1, (v-u+1)//2, [int(x1)]
                else:
                    return 1, (v-u)//2, [int(x1)]         
                
            if vd % 2 != 0:
                return 0, -1, []
                
            else:
                """here we have two cases, depending on whether the discriminant is a square"""    
                """if the discriminant is not a square, there are no roots except modulo p^u"""
                """if it is a square, then there are solutions modulo p^{v-u}, and they are p-adic balls of the same radius"""

                sqfdisc = disc // (p**vd)
                
                
                if legendre_symbol(sqfdisc, p) == -1:
                    return 0, -1, []
                    
                else:
                        
                        R = Zmod(p**(v-u-vd))
                        P.<x> = PolynomialRing(R)
                        f = x**2-sqfdisc
                      
                        sqrtD=f.roots(multiplicities=False)
    
                        x1 = (((-b+int(sqrtD[0])* p**(vd // 2))* inverse_mod(2*a, p**(v-u))))%(p**(v-u-vd//2)) 
                        x2 = ((-b+int(sqrtD[1])* p**(vd // 2))* inverse_mod(2*a, p**(v-u)))%(p**(v-u-vd//2))
                        return 1, v - u - vd//2, [int(x1), int(x2)]
                    
        elif b % p != 0:
            print("lamp")
            """in this case, hensel's lemma holds, there will be a unique root"""
            L = f.roots(multiplicities=False)
            return 1, v - u, [int(r) for r in L]
            
        else:
            """in this case, only c is invertible so there is nothing to solve"""
            return 0, -1, []
            
    # --- EVEN PRIME CASE (p = 2) ---
    else:
        if a % p != 0:
            if b % p != 0:
                if c % p != 0:
                    """no solutions in this case"""
                    return 0, -1, []
                else:
                    """hensel's lemma holds, unique solution"""
                    L = f.roots(multiplicities=False)
                    return 1, v-u, [int(r) for r in L]
            else:
                b0 = int(b)//2
                print("lamp")
                disc = ZZ(b0*b0 - a*c)
                vd = v if disc == 0 else disc.valuation(p)
            
                if vd >= v - u:
                    x1=(-b0 * inverse_mod(a, p**(v-u)))
                    if (v-u)%2!=0:
                        return 1, (v-u+1)//2, [int(x1)]
                    else:
                        return 1, (v-u)//2, [int(x1)]         
                
                if vd % 2 != 0:
                    return 0, -1, []
                
                else:
                    """here we have two cases, depending on whether the discriminant is a square"""    
                    """if the discriminant is not a square, there are no roots except modulo p^u"""
                    """if it is a square, then there are solutions modulo p^{v-u}, and they are p-adic balls of the same radius"""
                    sqfdisc = disc // (p**vd)
                    R = Zmod(p**(v-u-vd))
                    P.<x> = PolynomialRing(R)
                    f = x**2-sqfdisc
                      
                    sqrtD=f.roots(multiplicities=False)
                    if len(sqrtD) == 0:
                        """no solutions in this case, discriminant not a square"""
                        return 0, -1, []
                    else:
                        """there are squareroots of the discriminant, possibly more than 2 in some cases, no more than 4"""
                        return 1, v-u-vd//2, [int((((-b0+int(t)* 2**(vd // 2))* inverse_mod(a, 2**(v-u))))%(2**(v-u-vd//2))) for t in sqrtD]
                        
                    
        elif b % p != 0:
            print("lamp")
            """in this case, hensel's lemma holds, there will be a unique root"""
            L = f.roots(multiplicities=False)
            return 1, v - u, [int(r) for r in L]
            
        else:
            """in this case, only c is invertible so there is nothing to solve"""
            return 0, -1, []

a, b, L= quadratic_equation_solver(1, 0, 2, 2, 2)
print(a)
print(b)
print(L)

def simultaneously_solvable(p, v, Mat):
    a0, r0, L0 = quadratic_equation_solver(Mat[0][0],   Mat[0][1], Mat[0][2], p, v)
    a1, r1, L1 = quadratic_equation_solver(Mat[1][0],   Mat[1][1], Mat[1][2], p, v)        
    a2, r2, L2 = quadratic_equation_solver(Mat[2][0],   Mat[2][1], Mat[2][2], p, v)
   
    if a0*a1*a2 == 0:
        return 0, 0, 0
        
    if r1 > r0:
        r0, r1 = r1, r0
        L0, L1 = L1, L0

    if r2 > r0:
        r0, r2 = r2, r0
        L0, L2 = L2, L0
        
    for i in [0, len(L0) - 1] :
        for j in [0, len(L1) - 1] :
            for k in [0, len(L2) - 1] :
                x0 = L0[i]
                x1 = L1[j]
                x2 = L2[k]
                """here we check if any of the balls intersect, since x0-ball has the least radius p^{-r0}, it has to be contained inside the larger ones"""
                d1 = ZZ(x0 - x1)
                d2 = ZZ(x0 - x2)
                if d1.valuation(p) >= r1 and d2.valuation(p) >= r2:
                    return 1, x0, 1
    
    a0, r0, L0 = quadratic_equation_solver(Mat[0][2],   Mat[0][1], Mat[0][0], p, v)
    a1, r1, L1 = quadratic_equation_solver(Mat[1][2],   Mat[1][1], Mat[1][0], p, v)        
    a2, r2, L2 = quadratic_equation_solver(Mat[2][2],   Mat[2][1], Mat[2][0], p, v)
    

    
    if r1 > r0:
        r0, r1 = r1, r0
        L0, L1 = L1, L0

    if r2 > r0:
        r0, r2 = r2, r0
        L0, L2 = L2, L0
    
    for i in [0, len(L0) - 1] :
        for j in [0, len(L1) - 1] :
             for k in [0, len(L2) - 1] :
                x0 = L0[i]
                x1 = L1[j]
                x2 = L2[k]
                """here we check if any of the balls intersect, since x0-ball has the least radius p^{-r0}, it has to be contained inside the larger ones"""
                d1 = ZZ(x0 - x1)
                d2 = ZZ(x0 - x2)
                if d1.valuation(p) >= r1 and d2.valuation(p) >= r2:
                    return 1, 1, x0
                    
    return 0, 0, 0
    
"""
our most important function
input is a prime p, a prime power s, and a list of matrices in GL2(Z/p^sZ)
output is a 5-tuple (p, k, r, dist, loc) 
"""

def p_isogeny_graph(p,v, Sp):    
    
    q=p**v
    R_q = Zmod(q)
    #step 1: find the largest r for which all elements of Sp can be conjugated simultaneously to be uppertriangular mod p^r. 
    rows = []
    for M in Sp:
        mat = M.matrix() if hasattr(M, 'matrix') else M
        rows.append([mat[0, 1], mat[1, 1] - mat[0, 0], -mat[1, 0]])
    

    
    BigMat = Matrix(R_q, rows)

    pivot_row, pivot_col=move_pivot_to_top(BigMat, p, [0,2,1])
 
    for i in range (BigMat.nrows()-1):

            BigMat[i+1]=clear_entry(BigMat[0], BigMat[i+1], pivot_col, p, v)
            
    
    print(BigMat)
    
    SubMat = matrix(R, [list(row) for row in BigMat[1:]])
    
    new_pivot_row, new_pivot_col = move_pivot_to_top(SubMat, p, [0,2,1])
 
    for i in range (SubMat.nrows()-1):
            SubMat[i+1]=clear_entry(SubMat[0], SubMat[i+1], new_pivot_col, p, v)
    
    for i in range(SubMat.nrows()):
        for j in range(SubMat.ncols()):
            BigMat[i+1,j] = SubMat[i,j]
    
    SubMat = matrix(R, [list(row) for row in BigMat[2:]])
    
    newer_pivot_row, newer_pivot_col=move_pivot_to_top(SubMat, p, [0,2,1])
 
    for i in range (SubMat.nrows()-1):
            SubMat[i+1]=clear_entry(SubMat[0], SubMat[i+1], newer_pivot_col, p, v)
    
    for i in range(SubMat.nrows()):
        for j in range(SubMat.ncols()):
            BigMat[i+2,j] = SubMat[i,j]
            
   
    """
    we've now reached a situation where at most 6 entries are nonzero, it remains to solve the three linear/quadratic equations, e.g. find the largest power of p mod which they are solvable
    """

    left = 0
    right = v
    best_x = 0
    best_y = 0
    i = 0
    while left < right:
        mid = (left + right - 1) // 2 + 1
        a, s, t =simultaneously_solvable(p, mid, BigMat)
        if a == 0:
            right = mid - 1
        else:
            left = mid
            i = mid
            best_x = s
            best_y = t
        
    print(i)
    print(best_x)
    print(best_y)
    
    if best_y % p != 0:
        g =  Matrix(R_q, [[1, 0],[best_x, best_y]])
    else:
        g = Matrix(R_q, [[1, 0],[best_x, best_y]])
    h = g.inverse_of_unit()    
    """we now conjugate each element of Sp by conjugating matrix"""
    
    for i in range (len(Sp)):
        Sp[i] = g * Sp[i] * h
        
    """this completes step 1 of the algorithm"""
    
    
R = Integers(3**4)

Sp = [
    Matrix(R, [[1,1 ],[9,1]]),
    Matrix(R, [[1,0],[0,1]]),
    Matrix(R, [[1,0],[0,1]])
]

p_isogeny_graph(3, 4, Sp)


