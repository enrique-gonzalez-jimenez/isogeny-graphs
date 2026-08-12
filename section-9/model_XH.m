////////////////////////////////////////////////////////////////////////////////////////////////
//
// Alexander J. Barrios, Enrique González-Jiménez, and Ivan Novak,
// Isogeny graphs of elliptic curves in characteristic zero
// arXiv:2608.02494 (2026).
//
// Magma V2.29-1
////////////////////////////////////////////////////////////////////////////////////////////////

// Modular-main (Zywina)
// https://github.com/davidzywina/Modular)
AttachSpec("Modular-main/Modular.spec");


function IsogGraphSubgroup(p,k,r)
/*
Input:
    p : a prime number.
    k : a positive integer.
    r : an integer satisfying 0 <= r <= Floor(k/2).

Output:
    The subgroup of GL(2,Z/p^k Z) consisting of the invertible
    upper-triangular matrices

        [ a  b ]
        [ 0  c ]

    such that

        c = a mod p^r.

    Equivalently, the output is the subgroup

        { [a,b;0,c] in GL(2,Z/p^k Z) : v_p(c-a) >= r }.

    The condition r <= Floor(k/2) is checked by an assertion.
*/

  assert r le Floor(k/2);
  R:=Integers(p^k);
  G:=GL(2,R);
  M22:=MatrixRing(R,2);
  ms:={G![a,b,0,c] : a,b,c in [0..p^k-1] | Valuation(c-a,p) ge r and IsInvertible(M22![a,b,0,c])};
  return sub<G|ms >;
end function;


function LiftGroups(G1,G2)
// Input: G1, G2 : subgroups of GL(2, Z/N1 Z) and GL(2, Z/N2 Z), respectively
// Output: The subgroup of GL(2, Z/(N1*N2)Z) consisting of the matrices whose reductions modulo N1 and modulo N2 belong to G1 and G2, respectively.
    N1 := #BaseRing(G1);
    N2 := #BaseRing(G2);
    N := N1*N2;
    GLN := GL(2,Integers(N));
    GLN1,mp1 := ChangeRing(GLN,Integers(N1));
    GLN2,mp2 := ChangeRing(GLN,Integers(N2));
    gens1 := [Inverse(mp1)(g): g in Generators(G1)];
    gens2 := [Inverse(mp2)(g): g in Generators(G2)];
    // Add generators of the kernels to obtain the full inverse images of G1 and G2 under the corresponding reduction maps.
    for g in Generators(Kernel(mp1)) do
        Append(~gens1,g);
    end for;
    for g in Generators(Kernel(mp2)) do
        Append(~gens2,g);
    end for;
    GL1 := sub<GLN | gens1>;
    GL2 := sub<GLN | gens2>;
    return GL1 meet GL2;
end function;


function SubgroupFiberProduct(s1,s2)
// Input: s1 = <p1,k1,r1>, s2 = <p2,k2,r2> : sequences of length three containing valid arguments for IsogGraphSubgroup where p1,p2 are primes.
// Output: The fiber product of IsogGraphSubgroup(p1,k1,r1) and IsogGraphSubgroup(p2,k2,r2), constructed inside the general linear group at the product of their levels.
  p1,k1,r1:=Explode(s1);
  G1:=IsogGraphSubgroup(p1,k1,r1);
  p2,k2,r2:=Explode(s2);
  G2:=IsogGraphSubgroup(p2,k2,r2);
  H:=LiftGroups(G1,G2);
  return H;  
end function;




H1_9:=IsogGraphSubgroup(3,2,1);
H2_16:=IsogGraphSubgroup(2,4,2);
H0_2xH1_9:=SubgroupFiberProduct([2,1,0],[3,2,1]);
H1_25:=IsogGraphSubgroup(5,2,1);
H1_27:=IsogGraphSubgroup(3,3,1);
H2_32:=IsogGraphSubgroup(2,5,2);
H1_36:=SubgroupFiberProduct([2,2,1],[3,2,1]);
H1_49:=IsogGraphSubgroup(7,2,1);


S:=<[3,2,1],[2,4,2],[[2,1,0],[3,2,1]],[5,2,1],[3,3,1],[2,5,2],[[2,2,1],[3,2,1]],[7,2,1]>;

function OurGroup(seq)
   case #seq:
     when 3: return IsogGraphSubgroup(seq[1],seq[2],seq[3]);
     when 2: return SubgroupFiberProduct(seq[1],seq[2]);
   end case;
end function;

// To obtain models for the modular curves X_0^r(p^k),
// we use the `FindModelOfXG` function from Zywina's "FindOpenImage" repository. 
// ChangeDirectory("../OpenImage-master");  
// load "main/GL2GroupTheory.m";
// load "main/ModularCurves.m";


function ModelXH(G) 
 X:=CreateModularCurveRec(G);
 K:=X`KG;
 AssignNames(~K, ["a"]);
 PK := Parent(DefiningPolynomial(K));
 AssignNames(~PK, ["t"]);

 printf "CPname=%o\n",X`CPname;
 printf "Genus of X_G = %o\n",X`genus;
 printf "K:G = %o\n",K;
 
 MFX:=FindModularForms(2,X);
 CFX:=FindCuspForms(MFX);
 modelX:=FindModelOfXG(CFX);
 printf "Model: %o\n",modelX`psi;
if X`genus eq 1 then
 P2<x,y,z>:=ProjectiveSpace(K,2);
 C:=Curve(P2,modelX`psi);
 printf "Model: %o\n",EllipticCurve(C);
 printf "j-invariant: %o\n",jInvariant(EllipticCurve(C));
end if;
  return X;
end function;



// for H in [H1_9,H2_16,H0_2xH1_9,H1_25,H2_32,H1_36,H1_49] do 
for seq in S do
    H:=OurGroup(seq); 
    printf "====================\n %o \n-- -- -- -- -- -- -- --\n",seq;
	S:=ModelXH(H);
end for;






