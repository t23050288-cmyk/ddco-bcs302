"""Checks used for Q4 (NAND/NOR constructions), Q5 (carry look ahead) and Q8 (SR NOR latch)."""
nand=lambda a,b:1-(a&b); nor=lambda a,b:1-(a|b)
ok=True
for x in (0,1):
    for y in (0,1):
        ok&= nand(x,x)==1-x and nor(x,x)==1-x
        ok&= nand(nand(x,y),nand(x,y))==(x&y)
        ok&= nand(nand(x,x), nand(y,y))==(x|y)
        ok&= nor(nor(x,y),nor(x,y))==(x|y)
        ok&= nor(nor(x,x),nor(y,y))==(x&y)
        m=nand(x,y); ok&= nand(nand(x,m),nand(y,m))==(x^y)
print("Q4 NAND/NOR constructions OK:",ok)

ok=True
for a in range(16):
    for b in range(16):
        for c0 in (0,1):
            A=[(a>>i)&1 for i in range(4)]; B=[(b>>i)&1 for i in range(4)]
            g=[A[i]&B[i] for i in range(4)]; p=[A[i]|B[i] for i in range(4)]
            c1=g[0]|(p[0]&c0)
            c2=g[1]|(p[1]&g[0])|(p[1]&p[0]&c0)
            c3=g[2]|(p[2]&g[1])|(p[2]&p[1]&g[0])|(p[2]&p[1]&p[0]&c0)
            c4=g[3]|(p[3]&g[2])|(p[3]&p[2]&g[1])|(p[3]&p[2]&p[1]&g[0])|(p[3]&p[2]&p[1]&p[0]&c0)
            C=[c0,c1,c2,c3]
            s=sum((A[i]^B[i]^C[i])<<i for i in range(4))+(c4<<4)
            ok&= s==a+b+c0
print("Q5 CLA equations match real addition (512 cases):",ok)

def settle(S,R,Q,Qb):
    for _ in range(10):
        Qn=nor(R,Qb); Qbn=nor(S,Q)
        if (Qn,Qbn)==(Q,Qb): break
        Q,Qb=Qn,Qbn
    return Q,Qb
print("Q8 SR latch with NOR gates (S R Qprev -> Q Qbar):")
for S,R in [(0,0),(0,1),(1,0),(1,1)]:
    for Qp in (0,1):
        print(" ",S,R,Qp,"->",settle(S,R,Qp,1-Qp))
