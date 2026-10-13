# DDCO Assignment 1

Subject: Digital Design and Computer Organization (BCS302) | Semester III | VTU

Answers are based on the Module 1 and Module 2 class notes. The Boolean results, K-map groups, carry look ahead equations and the SR latch table were all checked by running a small program (see the `verification` folder).

---

## 1. Minimize the following Boolean function. (i) F = X(X' + Y) + X'Y  (ii) F = AB + A'B + AB'

**Definition:** Minimizing a Boolean function means writing the same function with fewer terms and fewer literals, so that it needs fewer gates. We use the Boolean postulates and theorems for this.

**Laws used:**

| Law | Form |
|---|---|
| Distributive | X(Y + Z) = XY + XZ |
| Complement | X + X' = 1 and X . X' = 0 |
| Identity | X + 0 = X and X . 1 = X |
| Idempotent | X + X = X |
| Absorption | X + XY = X |

### (i) F = X(X' + Y) + X'Y

**Step 1:** Open the bracket using the distributive law.

F = X.X' + X.Y + X'Y

**Step 2:** X.X' = 0 (complement law).

F = 0 + XY + X'Y = XY + X'Y

**Step 3:** Take Y common.

F = Y(X + X')

**Step 4:** X + X' = 1.

F = Y . 1

**F = Y**

**Check by truth table:**

| X | Y | X' | X' + Y | X(X' + Y) | X'Y | F |
|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 | 1 |

The F column is the same as Y, so the answer is correct.

### (ii) F = AB + A'B + AB'

**Method 1 (algebra):**

**Step 1:** Take B common from the first two terms.

F = B(A + A') + AB'

**Step 2:** A + A' = 1.

F = B + AB'

**Step 3:** Use the rule X + X'Y = X + Y. Our expression is B + AB'. Treat B as X and A as Y, so the second term is Y.X' = AB'.

B + AB' = (B + A)(B + B')   [distributive law: X + YZ = (X + Y)(X + Z)]
        = (B + A) . 1       [B + B' = 1]
        = A + B

**F = A + B**

**Method 2 (using the idempotent law, the quick way):**

AB is repeated, so use AB = AB + AB.

F = AB + A'B + AB' + AB = B(A + A') + A(B + B') = B + A

**F = A + B**

**Check by truth table:**

| A | B | AB | A'B | AB' | F | A + B |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 1 | 1 |

The F column matches A + B in all four rows.

**Gates saved:** (i) needed 2 AND, 1 OR and 1 NOT gate before. Now it is just a wire (F = Y). (ii) needed 3 AND, 2 NOT and 1 OR. Now it is one OR gate.

---

## 2. Explain Basic logic gates with truth table.

**Definition:** A logic gate is an electronic circuit that takes one or more binary inputs (0 or 1) and gives one binary output, according to a logical rule. Gates are the building blocks of every digital circuit.

**Points:**

1. In a digital system, voltages are treated as only two values: logic 1 (high) and logic 0 (low).
2. The three basic gates are AND, OR and NOT. Every other gate can be made from them.
3. NAND and NOR are called universal gates, because any circuit can be built using only one of them.
4. XOR and XNOR are special gates, mainly used in adders and comparators.
5. The truth table lists the output for every input combination. For n inputs, it has 2^n rows.

### 1. AND gate
Output is 1 only when **all** inputs are 1. Expression: Z = X . Y

| X | Y | Z = X.Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### 2. OR gate
Output is 1 when **at least one** input is 1. Expression: Z = X + Y

| X | Y | Z = X+Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### 3. NOT gate (inverter)
One input. Output is the **complement** of the input. Expression: Z = X'

| X | Z = X' |
|---|---|
| 0 | 1 |
| 1 | 0 |

### 4. NAND gate
AND followed by NOT. Output is 0 only when all inputs are 1. Expression: Z = (X.Y)'

| X | Y | Z = (XY)' |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### 5. NOR gate
OR followed by NOT. Output is 1 only when all inputs are 0. Expression: Z = (X + Y)'

| X | Y | Z = (X+Y)' |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

### 6. XOR gate (exclusive OR)
Output is 1 when the inputs are **different**. Expression: Z = X'Y + XY' = X ⊕ Y

| X | Y | Z = X⊕Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### 7. XNOR gate (equivalence)
Output is 1 when the inputs are **same**. Expression: Z = XY + X'Y' = (X ⊕ Y)'

| X | Y | Z = (X⊕Y)' |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### 8. Buffer
Output is the same as the input. It is used to strengthen a weak signal. Expression: Z = X.

### Symbols

```
AND:   X --|‾‾\            OR:   X --)‾‾\
           |   )-- Z               )    )-- Z
       Y --|__/                Y --)__/

NOT:   X --|>o-- Z         NAND: AND symbol with a small circle at the output
NOR:   OR symbol with a small circle at the output
XOR:   OR symbol with an extra curved line at the input
XNOR:  XOR symbol with a small circle at the output
```

Draw the standard gate symbols in the Blue Book. A small circle (bubble) at the output means the output is inverted.

### Summary table

| Gate | Expression | Output is 1 when |
|---|---|---|
| AND | X.Y | all inputs are 1 |
| OR | X + Y | any input is 1 |
| NOT | X' | input is 0 |
| NAND | (XY)' | any input is 0 |
| NOR | (X+Y)' | all inputs are 0 |
| XOR | X⊕Y | inputs are different |
| XNOR | (X⊕Y)' | inputs are same |

---

## 3. Simplify the given functions using a 4-variable K-map. (i) F(W,X,Y,Z) = Σm(0,1,2,4,6,7,9,12,14)  (ii) F(A,B,C,D) = Σm(5,6,7,12,14,15) + d(9,11,13)

**Definition:** A Karnaugh map (K-map) is a diagram made of squares, where each square is one minterm. It gives a systematic way to simplify Boolean expressions. A 4-variable map has 2^4 = 16 squares. The rows and columns follow Gray code (00, 01, 11, 10), so neighbouring squares differ by only one bit.

**Rules for grouping:**

1. Group only 1s (and don't cares if they help), in powers of 2: 1, 2, 4, 8, 16.
2. Make groups as big as possible.
3. Every 1 must be covered at least once.
4. Groups can overlap. Edges wrap around (left and right edge are neighbours, top and bottom edge are neighbours).
5. No diagonal groups.
6. A don't care (X or d) can be taken as 1 only if it makes a group bigger. Do not need to cover all don't cares.
7. A pair removes 1 variable, a quad removes 2, an octet removes 3.

### (i) F(W,X,Y,Z) = Σm(0,1,2,4,6,7,9,12,14)

**K-map** (rows WX, columns YZ; the small number is the minterm number):

```
          YZ
 WX     00     01     11     10
 00    [1]0   [1]1    0 3   [1]2
 01    [1]4    0 5   [1]7   [1]6
 11    [1]12   0 13   0 15  [1]14
 10     0 8   [1]9    0 11   0 10
```

**Groups:**

| Group | Cells | Type | Term |
|---|---|---|---|
| G1 | 0, 2, 4, 6 | Quad (W = 0, Z = 0) | W'Z' |
| G2 | 4, 6, 12, 14 | Quad (X = 1, Z = 0) | XZ' |
| G3 | 6, 7 | Pair (W = 0, X = 1, Y = 1) | W'XY |
| G4 | 1, 9 | Pair (X = 0, Y = 0, Z = 1) | X'Y'Z |

**How each term is written:** in a group, a variable that stays the same is kept; a variable that changes is removed. For G1 (cells 0,2,4,6): W is 0 in all, Z is 0 in all, X and Y change. So the term is W'Z'.

**Check that every 1 is covered:** 0 (G1), 1 (G4), 2 (G1), 4 (G1, G2), 6 (G1, G2, G3), 7 (G3), 9 (G4), 12 (G2), 14 (G2). All nine are covered.

**F(W,X,Y,Z) = W'Z' + XZ' + W'XY + X'Y'Z**

This is the minimum form: 4 terms and 10 literals. The pair 0,1 (W'X'Y') is a valid group too, but it is not needed since 0 and 1 are already covered.

### (ii) F(A,B,C,D) = Σm(5,6,7,12,14,15) + d(9,11,13)

**K-map** (rows AB, columns CD; d = don't care):

```
          CD
 AB     00     01     11     10
 00     0 0    0 1    0 3    0 2
 01     0 4   [1]5   [1]7   [1]6
 11    [1]12  [d]13  [1]15  [1]14
 10     0 8   [d]9   [d]11   0 10
```

**Groups:**

| Group | Cells | Type | Term |
|---|---|---|---|
| G1 | 5, 7, 13, 15 | Quad (B = 1, D = 1), uses d13 | BD |
| G2 | 6, 7, 14, 15 | Quad (B = 1, C = 1) | BC |
| G3 | 12, 13, 14, 15 | Quad (A = 1, B = 1), uses d13 | AB |

Here only the don't care 13 is useful (it joins the quads). The don't cares 9 and 11 are left as 0, so they are not used and need not be covered.

**Check:** 5 (G1), 6 (G2), 7 (G1, G2), 12 (G3), 14 (G2, G3), 15 (all). All covered.

**F(A,B,C,D) = BD + BC + AB**

Another way to write it: F = B(A + C + D).

---

## 4. Implement Basic Logic gates by using Nand and Nor Gates.

**Definition:** NAND and NOR are called **universal gates**, because AND, OR and NOT (and so every logic circuit) can be built using only NAND gates or only NOR gates. They are also easier to build with transistors, so IC families use them as the basic gate.

**Basic fact used:** If both inputs of a NAND (or NOR) are joined together, it works as a NOT gate.
- NAND with inputs tied: (X.X)' = X'
- NOR with inputs tied: (X + X)' = X'

### A. Using NAND gates only

| Gate | Implementation | Working |
|---|---|---|
| NOT | one NAND, both inputs tied to X | (X.X)' = X' |
| AND | NAND followed by a NAND used as NOT | ((X.Y)')' = XY |
| OR | NOT on each input, then one NAND | (X'.Y')' = X + Y (De Morgan) |
| NOR | OR (as above) followed by a NAND-NOT | ((X + Y))' |
| XOR | four NAND gates | see below |

**NOT:**
```
X --+--|‾‾\
    |  |   )o-- X'
    +--|__/
```

**AND:**
```
X --|‾‾\      |‾‾\
Y --|   )o----|   )o-- XY      (first NAND gives (XY)', second NAND inverts it)
    |__/      |__/
```

**OR:**
```
X --|>o--|‾‾\
         |   )o-- X + Y      (X' and Y' go into a NAND)
Y --|>o--|__/
```
(each `|>o` is a NAND with tied inputs, i.e. a NOT)

**XOR with 4 NAND gates:** Let M = (X.Y)'. Then Z = (X.M)' . (Y.M)' passed through a NAND.

Check: Z = [(X.M)' . (Y.M)']' = X.M + Y.M = X(XY)' + Y(XY)' = X(X' + Y') + Y(X' + Y') = XY' + X'Y. This is X⊕Y.

### B. Using NOR gates only

| Gate | Implementation | Working |
|---|---|---|
| NOT | one NOR, both inputs tied to X | (X + X)' = X' |
| OR | NOR followed by a NOR used as NOT | ((X + Y)')' = X + Y |
| AND | NOT on each input, then one NOR | (X' + Y')' = XY (De Morgan) |
| NAND | AND (as above) followed by a NOR-NOT | (XY)' |
| XNOR | four NOR gates | similar to XOR with NAND |

**NOT:**
```
X --+--)‾‾\
    |  )   )o-- X'
    +--)__/
```

**OR:**
```
X --)‾‾\      )‾‾\
Y --)   )o----)   )o-- X + Y
    )__/      )__/
```

**AND:**
```
X --|>o--)‾‾\
          )   )o-- XY       (X' and Y' go into a NOR)
Y --|>o--)__/
```
(each `|>o` is a NOR with tied inputs)

### C. Implementing a Boolean function (example from class notes)

**NAND-NAND form of f = AB + BC:**

The normal AND-OR form uses two AND gates and one OR gate. Replace every gate with a NAND gate:

```
A --|‾‾\
B --|   )o---+
    |__/     |   |‾‾\
             +---|   )o-- f = AB + BC
    |‾‾\     |   |__/
B --|   )o---+
C --|__/
```

Proof: f = [(AB)' . (BC)']' = AB + BC (De Morgan).

**NOR-NOR form of f = (A + B)(B + C):**

The OR-AND form uses two OR gates and one AND gate. Replace every gate with a NOR gate.

Proof: f = [(A + B)' + (B + C)']' = (A + B)(B + C).

### Summary

| To make | Using NAND | Using NOR |
|---|---|---|
| NOT | 1 gate (inputs tied) | 1 gate (inputs tied) |
| AND | 2 gates | 3 gates |
| OR | 3 gates | 2 gates |
| SOP function | NAND-NAND | - |
| POS function | - | NOR-NOR |


---

## 5. Explain 4-bit carry look ahead adder with neat diagram and relevant expressions.

**Definition:** A carry look ahead adder (CLA) is a fast parallel adder. It finds all the carries directly from the inputs at the same time, so it does not wait for the carry to travel from one stage to the next.

### Why we need it: the problem with the ripple carry adder

1. A normal parallel adder is made by joining full adders in a chain. The carry out of each stage goes to the carry in of the next stage.
2. So it is also called a **ripple carry adder**.
3. The sum and carry of any stage cannot be produced until the carry of the previous stage arrives.
4. This waiting is called **carry propagation delay**. For more bits, the delay becomes bigger.
5. The look ahead method removes this delay by computing the carries in advance.

### Carry generate and carry propagate

For one full adder at stage i, with inputs Ai, Bi and carry in Ci:

Sum: **Si = Ai ⊕ Bi ⊕ Ci**

Carry: **Ci+1 = AiBi + AiCi + BiCi = AiBi + Ci(Ai + Bi)**

Define two functions:

| Function | Expression | Meaning |
|---|---|---|
| Carry generate | **Gi = Ai . Bi** | stage i makes a carry by itself, whatever Ci is |
| Carry propagate | **Pi = Ai + Bi** | stage i passes the incoming carry Ci to the next stage |

(Some books use Pi = Ai ⊕ Bi. Both work. We use Ai + Bi as in the class notes.)

So the carry equation becomes:

**Ci+1 = Gi + Pi.Ci**

### Carry equations for the 4-bit adder

Take C0 as the input carry. Put i = 0, 1, 2, 3 one by one and substitute the earlier carry:

**C1 = G0 + P0C0**

**C2 = G1 + P1C1**
= G1 + P1(G0 + P0C0)
**C2 = G1 + P1G0 + P1P0C0**

**C3 = G2 + P2C2**
= G2 + P2(G1 + P1G0 + P1P0C0)
**C3 = G2 + P2G1 + P2P1G0 + P2P1P0C0**

**C4 = G3 + P3C3**
= G3 + P3(G2 + P2G1 + P2P1G0 + P2P1P0C0)
**C4 = G3 + P3G2 + P3P2G1 + P3P2P1G0 + P3P2P1P0C0**

**Important point:** C1, C2, C3 and C4 now depend only on the inputs A, B and C0. They do not depend on the earlier carry outputs. So all four carries can be made at the same time by AND-OR gates, and the delay is just two gate levels (one AND level and one OR level).

### Block diagram

```
        A3 B3        A2 B2        A1 B1        A0 B0
         |  |         |  |         |  |         |  |
      +--v--v--+   +--v--v--+   +--v--v--+   +--v--v--+
      |  PG    |   |  PG    |   |  PG    |   |  PG    |     PG = generates
      | block  |   | block  |   | block  |   | block  |     Pi and Gi
      +-P3-G3--+   +-P2-G2--+   +-P1-G1--+   +-P0-G0--+
         |  |         |  |         |  |         |  |
         v  v         v  v         v  v         v  v
      +----------------------------------------------------+
      |           CARRY LOOK AHEAD GENERATOR               |<-- C0
      |   C1 = G0 + P0C0                                   |
      |   C2 = G1 + P1G0 + P1P0C0                          |
      |   C3 = G2 + P2G1 + P2P1G0 + P2P1P0C0               |
      |   C4 = G3 + P3G2 + P3P2G1 + P3P2P1G0 + P3P2P1P0C0  |
      +--C4-----C3---------C2---------C1-------------------+
         |       |          |          |
         |       v          v          v
         |    +--------+ +--------+ +--------+ +--------+
         |    |   S3   | |   S2   | |   S1   | |   S0   |
         |    | A3^B3^C3| |A2^B2^C2| |A1^B1^C1| |A0^B0^C0|
         |    +---+----+ +---+----+ +---+----+ +---+----+
         v        v          v          v          v
        C4       S3         S2         S1         S0
```

Each sum bit is made by XOR gates: Si = Ai ⊕ Bi ⊕ Ci, where Ci comes from the look ahead generator.

### Step by step working

1. Give inputs A3A2A1A0, B3B2B1B0 and C0.
2. The PG blocks make Gi = AiBi and Pi = Ai + Bi for all four bits at once.
3. The look ahead generator makes C1, C2, C3, C4 directly from G, P and C0 using the equations above.
4. The sum bits are made as Si = Ai ⊕ Bi ⊕ Ci.
5. C4 is the final carry out.

### Example

Add A = 1011 (11) and B = 0110 (6), C0 = 0.

| Bit | A | B | G = AB | P = A + B |
|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |
| 2 | 0 | 1 | 0 | 1 |
| 3 | 1 | 0 | 0 | 1 |

C1 = G0 + P0C0 = 0 + 1.0 = 0
C2 = G1 + P1G0 + P1P0C0 = 1 + 0 + 0 = 1
C3 = G2 + P2G1 + ... = 0 + 1.1 + ... = 1
C4 = G3 + P3G2 + P3P2G1 + ... = 0 + 0 + 1.1.1 = 1

Sum bits: S0 = 1⊕0⊕0 = 1, S1 = 1⊕1⊕C1(0) = 0, S2 = 0⊕1⊕C2(1) = 0, S3 = 1⊕0⊕C3(1) = 0.

Result: C4 S3 S2 S1 S0 = 1 0 0 0 1 = 17, which is 11 + 6. Correct.

### Advantages and disadvantages

| Advantages | Disadvantages |
|---|---|
| Much faster than ripple carry adder | More gates needed, circuit is more complex |
| Delay does not grow with each stage | Equations get very large for more bits (8, 16 bits) |
| Used in the ALU of fast processors | For large adders, it is built in groups of 4 bits |

---

## 6. What is Multiplexer. Explain 4X1 multiplexer with neat diagram.

**Definition:** A multiplexer (MUX) is a combinational circuit that selects binary information from one of many input lines and sends it to a single output line. The selection is controlled by a set of select lines. A multiplexer is also called a **data selector**.

**Points:**

1. A MUX has 2^n data input lines, n select lines and 1 output line.
2. The binary number on the select lines decides which input goes to the output.
3. It is a combinational circuit, so it has no memory.
4. Internally it is a group of AND gates whose outputs go to one OR gate.
5. Common sizes: 2x1, 4x1, 8x1, 16x1.

**Block diagram of 2^n x 1 MUX:**

```
      D0 ----+
      D1 ----|
      D2 ----|  2^n x 1        
      .      |   MUX  ------------- Y (output)
      .      |
  D(2^n-1) --+
                ^  ^  ^
                |  |  |
               n select lines
```

### 4 x 1 multiplexer

It has 4 data inputs (D0, D1, D2, D3), 2 select lines (S1, S0) and 1 output Y.

**Logic symbol:**

```
        +-----------+
   D0 --|           |
   D1 --|   4 x 1   |
   D2 --|    MUX    |---- Y
   D3 --|           |
        +--^-----^--+
           |     |
           S1    S0
```

**Function table:**

| S1 | S0 | Y |
|---|---|---|
| 0 | 0 | D0 |
| 0 | 1 | D1 |
| 1 | 0 | D2 |
| 1 | 1 | D3 |

**Output expression** (from the function table):

**Y = S1' S0' D0 + S1' S0 D1 + S1 S0' D2 + S1 S0 D3**

**Working:** When S1S0 = 00, only the term S1'S0'D0 can be 1, so Y = D0. When S1S0 = 01, only S1'S0D1 is active, so Y = D1. In the same way for 10 and 11.

**Logic diagram:**

```
 S1 ----+--------+-------------+--------------+
        |        |             |              |
       NOT       |            NOT             |
        |        |             |              |
 S0 ----|--+-----|--+----------|--+-----------|--+
        |  |     |  |         |  |           |  |
       NOT |    NOT |          |  |           |  |
        |  |     |  |          |  |           |  |
   +----v--v-+ +-v--v--+   +--v--v--+      +--v--v--+
D0-|  AND3   | |  AND3 |-D1| AND3   |-D2   | AND3   |-D3
   |S1' S0' D0| |S1' S0 D1| |S1 S0' D2|     |S1 S0 D3|
   +----+----+ +---+---+   +---+----+      +---+----+
        |          |           |               |
        +----------+-----+-----+---------------+
                         |
                      +--v--+
                      | OR4 |---------- Y
                      +-----+
```

(In the Blue Book, draw 2 NOT gates to make S1' and S0', four 3-input AND gates, each one taking one data input, and one 4-input OR gate at the output. Label each AND gate output as S1'S0'D0, S1'S0D1, S1S0'D2, S1S0D3.)

**Truth table (with data inputs):**

| S1 | S0 | D0 | D1 | D2 | D3 | Y |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | x | x | x | 0 |
| 0 | 0 | 1 | x | x | x | 1 |
| 0 | 1 | x | 0 | x | x | 0 |
| 0 | 1 | x | 1 | x | x | 1 |
| 1 | 0 | x | x | 0 | x | 0 |
| 1 | 0 | x | x | 1 | x | 1 |
| 1 | 1 | x | x | x | 0 | 0 |
| 1 | 1 | x | x | x | 1 | 1 |

(x = don't care)

### Using a MUX to build a Boolean function (from class notes)

Because a MUX is a set of AND gates feeding an OR gate, each AND gate acts as one minterm. If the minterm is in the function, connect that data input to 1. Otherwise connect it to 0.

**Example:** F(x,y,z) = Σm(0,2,6,7) using an 8x1 MUX. Connect D0, D2, D6, D7 to 1 and D1, D3, D4, D5 to 0. Connect x, y, z to select lines S2, S1, S0.

### Applications

1. Data routing: select one of many sources to go to one destination.
2. Parallel to serial conversion.
3. Implementing Boolean functions.
4. Selecting registers in the CPU.

---

## 7. Differentiate Latches and Flip-Flops.

**Definition:**
- A **latch** is a basic memory element that stores 1 bit. It is **level triggered**, which means it responds to the inputs as long as the enable signal is at its active level.
- A **flip-flop** is a memory element that stores 1 bit. It is **edge triggered**, which means it responds to the inputs only at the rising or falling edge of the clock pulse.

**Common points:**

1. Both are bistable circuits with two stable states (Q = 1 and Q = 0).
2. Both store one bit of information.
3. Both have outputs Q and Q' (complement).
4. Both are sequential circuits, because the output depends on the present inputs and the past state.

### Difference table

| Point | Latch | Flip-flop |
|---|---|---|
| Triggering | **Level triggered** (works while enable is active) | **Edge triggered** (works only at clock edge) |
| Control signal | Enable (EN) | Clock pulse (CP) |
| Output change | Output can change many times while enable is active | Output changes only once per clock edge |
| Clock | Not clocked (or gated by enable) | Clocked |
| Edge detector circuit | Not needed | Needed (positive or negative edge detector) |
| Speed | Faster, simple circuit | Slightly slower, more gates |
| Number of gates | Fewer gates | More gates |
| Timing control | Poor, output may change at unwanted times | Good, easy to synchronise the whole system |
| Race condition | Can occur while enable is high | Avoided by edge triggering or master-slave |
| Transparency | Transparent when enable is high (D latch) | Not transparent |
| Types | SR latch, gated SR latch, D latch | SR, D, JK, T flip-flops |
| Use | Simple storage, temporary hold of data | Registers, counters, synchronous circuits |

### Working difference (example with D)

- **D latch:** When EN = 1, Q follows D at every moment. If D changes three times while EN = 1, Q also changes three times. When EN = 0, Q holds its value.
- **D flip-flop:** Q takes the value of D only at the clock edge (for example, the positive edge). Even if D changes between two edges, Q does not change.

### Waveform idea

```
 EN/CP   __|‾‾‾‾‾‾‾‾|______|‾‾‾‾‾‾‾‾|____
 D       __|‾‾|__|‾‾‾|________|‾‾|_______
 Latch Q follows D while EN = 1 (several changes)
 FF Q    changes only at the rising edge of CP (one change)
```

---

## 8. Explain the working of an SR latch using NOR gates.

**Definition:** An SR latch is a basic 1-bit memory element. It has two inputs, S (Set) and R (Reset), and two outputs, Q and Q' (complement). It is made by cross-coupling two gates, so that the output of each gate goes to the input of the other gate.

### Circuit (using two NOR gates)

```
        R ----------)‾‾\
                    )    )o--------+------------ Q
              +-----)__/ (NOR 1)   |
              |                    |
              |    +---------------+
              |    |
              +----|---------------+
                   |               |
                   +-----)‾‾\      |
                         )    )o---+------------ Q'
        S ----------)__/ (NOR 2)
```

In words (to draw in the Blue Book):
- NOR gate 1 has inputs R and Q'. Its output is Q.
- NOR gate 2 has inputs S and Q. Its output is Q'.
- The output of each gate is fed back to the input of the other gate (cross coupled).

**Equations:**

**Q = (R + Q')'**

**Q' = (S + Q)'**

### Operation (case by case)

The NOR gate gives 1 only when both inputs are 0. If any input is 1, the output is 0.

**Case 1: S = 0, R = 0 (No change / memory state)**

Both external inputs are 0, so they do not matter. NOR 1 becomes Q = (0 + Q')' = Q'' = Q, and NOR 2 becomes Q' = (0 + Q)' = Q'. The circuit **holds its previous state**.
- If Q was 0 (Q' = 1): NOR 1 has inputs 0, 1, output 0. NOR 2 has inputs 0, 0, output 1. Stays Q = 0.
- If Q was 1 (Q' = 0): NOR 1 has inputs 0, 0, output 1. NOR 2 has inputs 0, 1, output 0. Stays Q = 1.

**Case 2: S = 0, R = 1 (Reset)**

R = 1 forces the output of NOR 1 to 0, so **Q = 0**. Now NOR 2 has inputs S = 0 and Q = 0, so **Q' = 1**. The latch is in the **reset state** (Q = 0).

**Case 3: S = 1, R = 0 (Set)**

S = 1 forces the output of NOR 2 to 0, so **Q' = 0**. Now NOR 1 has inputs R = 0 and Q' = 0, so **Q = 1**. The latch is in the **set state** (Q = 1).

**Case 4: S = 1, R = 1 (Invalid)**

Both gates have a 1 at an input, so both outputs go to 0: **Q = 0 and Q' = 0**. This breaks the rule that Q and Q' must be complements. Also, when S and R both go back to 0 together, both gates try to change at once, and the final state depends on which gate is faster. It cannot be predicted. So S = R = 1 is **not allowed**.

### Truth table

| S | R | Qn (present) | Qn+1 (next) | State |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | No change |
| 0 | 0 | 1 | 1 | No change |
| 0 | 1 | 0 | 0 | Reset |
| 0 | 1 | 1 | 0 | Reset |
| 1 | 0 | 0 | 1 | Set |
| 1 | 0 | 1 | 1 | Set |
| 1 | 1 | 0 | x | Invalid |
| 1 | 1 | 1 | x | Invalid |

### Characteristic equation

From the K-map of Qn+1 with variables S, R, Qn (treating S = R = 1 as don't care):

```
        R Qn
 S      00   01   11   10
 0       0    1    0    0
 1       1    1    x    x
```

Make two groups:
- The whole bottom row (S = 1, including the two don't cares) gives **S**.
- The pair of cells with Qn = 1 and R = 0 (top row, column 01, and bottom row, column 01) gives **R'Qn**.

**Qn+1 = S + R' Qn**

(with the condition S.R = 0)

### Logic symbol

```
        +---------+
   S ---|  SR     |--- Q
        |  Latch  |
   R ---|         |--- Q'
        +---------+
```

### Points to remember

1. The NOR SR latch is an **active high** latch: S = 1 sets it and R = 1 resets it.
2. The NAND SR latch (in your notes) is the opposite: it is active low in its basic form, and S = R = 0 is the invalid case there.
3. Output changes immediately when the input changes, because there is no clock. The latch is sensitive to the inputs at all times.
4. To control when the latch responds, an enable input is added. This gives the **gated SR latch**.
5. The invalid condition can be removed by using a D latch (D and D' feed S and R, so S and R are never both 1).
6. Uses: simple 1-bit storage, switch debouncing, building blocks of flip-flops.

---

## 9. Explain the basic operation concepts of the computer with a neat diagram.

**Definition:** The basic operation of a computer is the way the processor fetches an instruction from memory, executes it, and stores the result. A computer works by running a stored program, which is a list of instructions kept in the main memory.

**Points:**

1. A program is a sequence of instructions stored in memory. The processor takes them one by one.
2. The processor has special registers: PC, IR, MAR, MDR, general purpose registers and a few more.
3. Instructions and data are kept in main memory. The processor reads them using the address and data buses.
4. Every instruction goes through two main phases: **fetch** and **execute**.
5. The time taken for one memory access is much longer than a processor operation, so registers are used to hold data inside the processor.

### Important registers

| Register | Full name | Work |
|---|---|---|
| PC | Program Counter | holds the address of the next instruction to be fetched. After each fetch, PC is increased to point to the next instruction |
| IR | Instruction Register | holds the instruction that is being executed. The control unit decodes the instruction from IR |
| MAR | Memory Address Register | holds the address of the memory location to be read or written |
| MDR | Memory Data Register | holds the data being written into or read from memory |
| R0 to Rn-1 | General purpose registers | hold data and intermediate results |

### Block diagram

```
             +---------------------------------------------------+
             |                    PROCESSOR                      |
             |                                                   |
             |   +----+      +-----+                             |
             |   | PC |      | IR  |      +--------------------+ |
             |   +-+--+      +--+--+      |  Control unit       | |
             |     |            |         +--------------------+ |
             |     |  +------+  |                                |
             |     +->| MAR  |  |   +-----------------+          |
             |        +--+---+  +-->| Instruction     |          |
             |           |         | decoder         |          |
             |        +--+---+     +-----------------+          |
             |        | MDR  |<-------+                         |
             |        +--+---+        |   +-------+             |
             |           |         +--+-->|  ALU  |             |
             |    R0 ... Rn-1 ----------->|       |             |
             |                            +-------+             |
             +-----------|--------------------|-----------------+
                  address bus            data bus
                         |                    |
                    +----v--------------------v----+
                    |        MAIN MEMORY           |
                    +------------------------------+
                         ^                    ^
                         |                    |
                  Input unit            Output unit
```

(Draw the processor box with PC, IR, MAR, MDR, general registers, ALU and control unit. Draw the memory box below it, joined by an address bus from MAR and a data bus to MDR.)

### Steps of instruction execution

**A. Instruction fetch phase**

1. The address of the next instruction is in the PC.
2. The contents of PC are moved to MAR. MAR sends the address to memory.
3. The control unit sends a **Read** signal to memory.
4. Memory reads the instruction at that address and puts it on the data bus. It is loaded into MDR.
5. The contents of MDR are moved to IR.
6. The PC is incremented by 1 word (for example by 4 in a 32-bit machine) so it points to the next instruction.

**B. Instruction execute phase**

1. The control unit decodes the instruction in IR to find out what operation to do and where the operands are.
2. If an operand is in memory, its address is sent through MAR, and the data comes into MDR.
3. The ALU does the operation (add, subtract, compare, etc.).
4. The result is stored in a register, or written back to memory (through MAR and MDR with a **Write** signal).

### Example: Add LOCA, R0

The instruction `Add LOCA, R0` means: add the number in memory location LOCA to the number in R0, and put the sum in R0.

1. Fetch the instruction (steps A1 to A6 above).
2. Send the address LOCA to memory (through MAR) and read the data (comes in MDR).
3. ALU adds the contents of MDR and R0.
4. The sum is stored in R0.

### Normal program flow and interrupts

1. Normally, the processor runs instructions one after another, in order of increasing address.
2. A **branch** instruction changes PC to a new address.
3. An **interrupt** is a request from an I/O device for the processor's attention.
   - The processor finishes the present instruction and saves the PC and status in a safe place (stack).
   - It runs the **interrupt service routine (ISR)** for the device.
   - After that, it restores the saved PC and goes back to the main program.
4. Interrupts avoid the processor wasting time waiting for slow I/O devices.

### Bus structure

1. The processor, memory and I/O devices are joined by a group of wires called a **bus**.
2. The bus has three parts: **address lines** (to say where), **data lines** (to carry the data), and **control lines** (to say what to do: read, write, etc.).
3. Only one device can send data on the bus at a time.

### Summary

**Fetch** (PC to MAR, read memory, MDR to IR, PC + 1) then **Decode** (control unit reads IR) then **Execute** (ALU works, result stored) and repeat.

---

## 10. Explain the functional units of a digital computer with the help of a neat block diagram. Explain the function of each unit.

**Definition:** A digital computer is made of five functional units: the **input unit**, the **memory unit**, the **arithmetic and logic unit (ALU)**, the **output unit** and the **control unit**. The ALU and the control unit together are called the **processor** (CPU).

### Block diagram

```
                         +---------------+
        Data/Programs    |               |   Results
   +----------+  ----->  |  MEMORY UNIT  |  ----->   +-----------+
   |  INPUT   |          |   (Main and   |           |  OUTPUT   |
   |   UNIT   |          |   Secondary)  |           |   UNIT    |
   +----------+          +-------+-------+           +-----------+
                                 ^
                                 |  instructions and data
                         +-------v-------+
                         |      ALU      |
                         | (Arithmetic & |
                         |  Logic Unit)  |
                         +-------^-------+
                                 |
                         +-------+-------+
                         |  CONTROL UNIT |   sends control signals to
                         |               |   all other units
                         +---------------+

         [ ALU + CONTROL UNIT = PROCESSOR (CPU) ]
```

**Another way to draw it (as in the textbook):** Input, Output, Memory and Arithmetic-Logic connect to each other through the Control unit. The processor has ALU and control. Arrows show data and control flow.

### 1. Input unit

1. It takes data and instructions from the outside world and gives them to the computer in binary form.
2. Each key pressed or each signal is converted into a binary code (for example ASCII).
3. The codes are sent to the processor, or stored in memory.
4. **Examples:** keyboard, mouse, scanner, microphone, touch screen, joystick, camera.

### 2. Memory unit

1. It stores programs and data.
2. It has two classes:
   - **Primary (main) memory:** fast, directly accessed by the processor. Made of semiconductor RAM and ROM. It is made of many storage cells, each with a unique address. It is volatile (RAM loses data when power is off). Access time is short.
   - **Secondary memory:** large, slower and cheaper per bit. Keeps data permanently (non-volatile). **Examples:** hard disk, SSD, optical disk, pen drive.
3. Memory is organised in words (for example 32 bits). The processor reads a word using its address.
4. Memory can be accessed in any order, so it is called **random access memory (RAM)**.
5. **Cache memory** is a very small and very fast memory kept between the processor and main memory. It holds the most used instructions and data to speed up the work.

### 3. Arithmetic and Logic Unit (ALU)

1. It does the actual calculation and decisions.
2. **Arithmetic operations:** add, subtract, multiply, divide.
3. **Logic operations:** AND, OR, NOT, XOR, compare.
4. The data to be operated is brought from memory into **registers** inside the processor. Registers are very fast storage cells.
5. After the operation, the result is kept in a register, or sent back to memory.
6. The ALU sets flag bits (such as zero, carry, sign, overflow) to show the result status.

### 4. Output unit

1. It is the opposite of the input unit. It gives the results of processing to the user in a form that people can understand.
2. It converts the binary result into characters, pictures or sound.
3. **Examples:** monitor (display), printer, speaker, plotter.
4. Some devices, such as a touch screen or a network card, work as both input and output.

### 5. Control unit

1. It is the **nerve centre** of the computer. It coordinates all the other units.
2. It reads each instruction from memory, decodes it, and sends the right **timing and control signals** to the other units, so that the instruction is carried out.
3. It decides: which data comes from where, what operation the ALU does, and where the result goes.
4. It controls the data transfer between processor, memory, and I/O devices.
5. Control is done by sending signals along **control lines**. The timing is based on the clock.
6. Internally it has the instruction register (IR), program counter (PC) and the instruction decoder.

### Processor (CPU)

The ALU and the control unit together form the **processor**. A modern processor chip is a microprocessor. Its main parts are the ALU, the control unit, the registers, and often the cache memory.

### How the units work together (steps)

1. A program and its data are entered through the **input unit** and stored in **memory**.
2. The **control unit** fetches the first instruction from memory.
3. The control unit decodes it and tells the **ALU** and other units what to do.
4. The **ALU** works on the data (taken from memory or registers).
5. The result is stored in a register or in memory.
6. The result is sent to the **output unit** to show to the user.
7. The control unit then fetches the next instruction and the process repeats.

### Summary table

| Unit | Main function | Examples |
|---|---|---|
| Input | brings data and instructions into the computer | keyboard, mouse, scanner |
| Memory | stores programs and data | RAM, ROM, hard disk, cache |
| ALU | does arithmetic and logic operations | adder, logic circuits, registers |
| Output | gives results to the user | monitor, printer, speaker |
| Control | controls and coordinates all units | PC, IR, decoder, timing circuits |
