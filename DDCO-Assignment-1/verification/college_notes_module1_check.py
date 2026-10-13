"""Checks every worked K-map answer printed in the college Module 1 notes.
Run:  python3 college_notes_module1_check.py
"""
N = lambda x: 1 - x
def bits(m, n): return [(m >> (n - 1 - i)) & 1 for i in range(n)]
def check(ones, dc, f, n):
    bad = []
    for m in range(2 ** n):
        v = f(*bits(m, n))
        if m in ones and not v: bad.append(f"misses {m}")
        if m not in ones and m not in dc and v: bad.append(f"extra {m}")
    return "correct" if not bad else "WRONG: " + ", ".join(bad)

rows = [
 ("2.1 y=A'B'+BC            S(0,1,3,6,7)", [0,1,3,6,7], [], lambda a,b,c:(N(a)&N(b))|(b&c), 3),
 ("2.1 fixed A'B'+A'C+AB    S(0,1,3,6,7)", [0,1,3,6,7], [], lambda a,b,c:(N(a)&N(b))|(N(a)&c)|(a&b), 3),
 ("2.2 y=AB'+AC             S(4,5,7)", [4,5,7], [], lambda a,b,c:(a&N(b))|(a&c), 3),
 ("2.3 F=A'C+A'B+BC         S(1,2,3,7)", [1,2,3,7], [], lambda a,b,c:(N(a)&c)|(N(a)&b)|(b&c), 3),
 ("2.4 F=A'B'D+AC'D'+B'C    S(1,2,3,5,8,10,11,12)", [1,2,3,5,8,10,11,12], [], lambda a,b,c,d:(N(a)&N(b)&d)|(a&N(c)&N(d))|(N(b)&c), 4),
 ("2.4 fixed B'C+A'C'D+AC'D'", [1,2,3,5,8,10,11,12], [], lambda a,b,c,d:(N(b)&c)|(N(a)&N(c)&d)|(a&N(c)&N(d)), 4),
 ("2.5 f=B'C'+A'C'D'+AB'D'  S(0,1,4,8,9,10)", [0,1,4,8,9,10], [], lambda a,b,c,d:(N(b)&N(c))|(N(a)&N(c)&N(d))|(a&N(b)&N(d)), 4),
 ("2.8 F=BD'+B'C            S(2,3,4,6,11,12)+d(10,13,14)", [2,3,4,6,11,12], [10,13,14], lambda a,b,c,d:(b&N(d))|(N(b)&c), 4),
 ("2.9 f=A'C'+B'C+A'D'+BC'D S(0,1,4,5,6,10,13)+d(2,3)", [0,1,4,5,6,10,13], [2,3], lambda a,b,c,d:(N(a)&N(c))|(N(b)&c)|(N(a)&N(d))|(b&N(c)&d), 4),
 ("2.9 fixed A'B'+A'D'+BC'D+B'CD'", [0,1,4,5,6,10,13], [2,3], lambda a,b,c,d:(N(a)&N(b))|(N(a)&N(d))|(b&N(c)&d)|(N(b)&c&N(d)), 4),
 ("2.10 f=AC'D'+A'D+A'C+AB  S(1,2,6,7,8,13,14,15)+d(0,3,5,12)", [1,2,6,7,8,13,14,15], [0,3,5,12], lambda a,b,c,d:(a&N(c)&N(d))|(N(a)&d)|(N(a)&c)|(a&b), 4),
]
for name, ones, dc, f, n in rows:
    print(f"{name:62s} {check(ones, dc, f, n)}")
