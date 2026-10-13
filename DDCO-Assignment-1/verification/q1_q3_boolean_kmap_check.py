import itertools
# Q1
f1=lambda x,y: (x and ((not x) or y)) or ((not x) and y)
print("Q1(i) X(X'+Y)+X'Y :", [(x,y,int(bool(f1(x,y)))) for x in (0,1) for y in (0,1)], " vs X'Y+XY = Y ->", [(x,y,y) for x in (0,1) for y in (0,1)])
f2=lambda a,b: (a&b)|((1-a)&b)|(a&(1-b))
print("Q1(ii) AB+A'B+AB' :", [(a,b,f2(a,b)) for a in (0,1) for b in (0,1)], " = A+B")

# K-map solver (Quine-McCluskey) for Q3
def qm(ones, dc, n):
    minterms=sorted(set(ones)|set(dc))
    groups={}
    terms={(m,0) for m in minterms}   # (value, mask of dashes)
    primes=set()
    while terms:
        new=set(); used=set()
        tl=sorted(terms)
        for i in range(len(tl)):
            for j in range(i+1,len(tl)):
                (v1,m1),(v2,m2)=tl[i],tl[j]
                if m1==m2:
                    d=v1^v2
                    if d and (d&(d-1))==0:
                        new.add((v1&~d,m1|d)); used.add(tl[i]); used.add(tl[j])
        primes|=terms-used
        terms=new
    # cover
    def covers(p,m): return (m & ~p[1])==p[0]
    chosen=[]; left=set(ones)
    # essential
    while left:
        best=None
        for m in sorted(left):
            c=[p for p in primes if covers(p,m)]
            if len(c)==1: best=c[0]; break
        if best is None:
            best=max(primes,key=lambda p:sum(covers(p,m) for m in left))
        chosen.append(best); left={m for m in left if not covers(best,m)}
    return chosen
def term(p,names):
    v,mk=p; s=""
    for i,nm in enumerate(names):
        bit=3-i
        if mk>>bit &1: continue
        s+= nm if (v>>bit)&1 else nm+"'"
    return s or "1"
print("Q3(i):", " + ".join(term(p,"WXYZ") for p in qm([0,1,2,4,6,7,9,12,14],[],4)))
print("Q3(ii):", " + ".join(term(p,"ABCD") for p in qm([5,6,7,12,14,15],[9,11,13],4)))
