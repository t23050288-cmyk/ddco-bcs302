# College Notes: Module 1 (checked and cleaned)

This file follows the college notes PDF (DDCO Module 1) section by section.
Every worked answer was checked on a computer against the full truth table.
Where the PDF has a mistake, it is marked **[NOTES ERROR]** and the correct answer is given.

---

## 1. Boolean algebra

- Boolean algebra is also called **switching algebra**. Switching circuits are called logic circuits, gate circuits or digital circuits.
- It is a system of mathematical logic with the set of elements {0, 1}, two binary operators (OR, AND) and one unary operator (NOT).
- Binary 1 is the high voltage level (+5 V) and binary 0 is the low level (0 V).

**Laws:**

| Law | AND form | OR form |
|---|---|---|
| Identity | A.1 = A | A + 0 = A |
| Null / Domination | A.0 = 0 | A + 1 = 1 |
| Idempotent | A.A = A | A + A = A |
| Complement | A.A' = 0 | A + A' = 1 |
| Commutative | A.B = B.A | A + B = B + A |
| Associative | (A.B).C = A.(B.C) | (A + B) + C = A + (B + C) |
| Distributive | A.(B + C) = A.B + A.C | A + (B.C) = (A + B)(A + C) |
| Absorption | A.(A + B) = A | A + (A.B) = A |
| De Morgan | (A.B)' = A' + B' | (A + B)' = A'.B' |

---

## 2. Basic logic gates

**Gate:** a device that performs a logical operation on one or more inputs and gives a single output.

**Logic gates:**
- are the building blocks of digital systems.
- give one output level for some input combinations and a different output level for other combinations.
- Inputs and outputs have only two levels: 1 or 0 (High or Low, True or False, On or Off).

**Truth table:** a table listing all possible input combinations and the matching outputs.

| Gate | Symbol | Expression | Key points |
|---|---|---|---|
| AND | dot | Y = A.B | two or more inputs, one output. Output is 1 only when **all** inputs are 1. Called the **all or nothing gate** |
| OR | plus | Y = A + B | output is 1 when **any one** input is 1. Called the **any or all gate** and **inclusive OR** |
| NOT | bar | Y = A' | one input, one output, output is the complement. Also called an **inverter** |

**Truth tables:**

| A | B | AND | OR | NAND | NOR | XOR | XNOR |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

**Universal gates:**
- **NAND** = AND followed by NOT. Output is 0 only when both inputs are 1. Y = (A.B)'
- **NOR** = OR followed by NOT. Output is 1 only when both inputs are 0. Y = (A + B)'

**XOR (exclusive OR):** Y = A ⊕ B = A'B + AB'. Output is 1 when the two inputs are **different**.
**XNOR:** Y = (A ⊕ B)' = AB + A'B'. Output is 1 when the two inputs are **same**.

> **[NOTES ERROR]** Page 3 of the PDF says "the output of XOR is 1 if both inputs are same and 0 if different". This is written the wrong way round. The truth table printed just below it on page 4 is correct (XOR is 1 for 01 and 10). Write it as above.

---

## 3. Combinational logic circuits

- A combinational circuit is made by combining different gates. Examples: encoder, decoder, multiplexer, demultiplexer.
- The output at any instant depends **only on the present inputs**.
- It has **no memory**. The earlier input has no effect on the present output.
- It can have n inputs and m outputs.
- Methods to analyse: truth table, Boolean algebra, Karnaugh map.

---

## 4. Canonical forms

| Form | Other names | Example |
|---|---|---|
| SOP | Disjunctive Normal Form (DNF) | f = A'B + BC |
| POS | Conjunctive Normal Form (CNF) | f = (A' + B)(B + C) |
| Canonical SOP | Expanded SOP, Disjunctive Canonical Form | every product term has all variables |
| Canonical POS | Expanded POS, Conjunctive Canonical Form | every sum term has all variables |

- **Minterm:** a product term containing all the variables (complemented or not). It is 1 for only one input combination. Written m0, m1, m2, ...
- **Maxterm:** a sum term containing all the variables. Written M0, M1, M2, ...

**Minterms and maxterms for 3 variables:**

| x y z | Minterm | Designation | Maxterm | Designation |
|---|---|---|---|---|
| 0 0 0 | x'y'z' | m0 | x + y + z | M0 |
| 0 0 1 | x'y'z | m1 | x + y + z' | M1 |
| 0 1 0 | x'yz' | m2 | x + y' + z | M2 |
| 0 1 1 | x'yz | m3 | x + y' + z' | M3 |
| 1 0 0 | xy'z' | m4 | x' + y + z | M4 |
| 1 0 1 | xy'z | m5 | x' + y + z' | M5 |
| 1 1 0 | xyz' | m6 | x' + y' + z | M6 |
| 1 1 1 | xyz | m7 | x' + y' + z' | M7 |

**From a truth table:** for SOP, write a minterm for each row with output 1. For POS, write a maxterm for each row with output 0.

**Worked example (from notes):**

| X | Y | Z | F |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

SOP: F = X'Y'Z' + X'Y'Z + XY'Z' + XYZ = Σm(0, 1, 4, 7)
Simplified: F = X'Y' + Y'Z' + XYZ

POS: F = (X + Y' + Z)(X + Y' + Z')(X' + Y + Z')(X' + Y' + Z) = ΠM(2, 3, 5, 6)
Simplified: F = (X + Y')(X' + Y + Z')(Y' + Z)

(Both simplified forms checked: they give 1 exactly at 0, 1, 4, 7.)

---

## 5. Problems on canonical forms (page 6 to 8 of the PDF)

**Problem 1: Express F = x + y'z in SOP and POS**

F = x(y + y') + y'z
 = xy + xy' + y'z
 = xy(z + z') + xy'(z + z') + (x + x')y'z
 = xyz + xyz' + xy'z + xy'z' + x'y'z (the repeated xy'z is written once)

Arranged: F = x'y'z + xy'z' + xy'z + xyz' + xyz = m1 + m4 + m5 + m6 + m7
**F = Σm(1, 4, 5, 6, 7) = ΠM(0, 2, 3)**

**Problem 2: Simplify F = A'B'C + A'BC + AB'C + ABC**

= A'C(B' + B) + AC(B' + B) = A'C + AC = C(A' + A) = **C**

**Problem 3: Convert F = A'B' + AC + B'C to canonical form**

F = A'B'(C + C') + A(B + B')C + (A + A')B'C
 = A'B'C + A'B'C' + ABC + AB'C + AB'C + A'B'C
Remove repeats: F = A'B'C' + A'B'C + AB'C + ABC
**F = Σm(0, 1, 5, 7)**

**Problem 4: Simplify Y = Σm(1, 3, 5, 6, 7)**

Y = A'B'C + A'BC + AB'C + ABC' + ABC
Group the three terms that have C in the first, second and third place with ABC:
A'B'C + A'BC + AB'C + ABC = C(A'B' + A'B + AB' + AB) = C
So Y = C + ABC' (the last term is ABC', which is left)
Use X + X'Y = X + Y with X = C: C + ABC' = C + AB
**Y = AB + C**

**Problem 5: Simplify F = Σm(0, 2, 4, 6)**

= B'C'(A' + A) + BC'(A' + A) = B'C' + BC' = C'(B' + B) = **C'**

**Problem 6: Convert to canonical POS**

(a) (A + C)(C + D), taking the variables as A, C, D:
(A + C) = (A + C + D)(A + C + D')
(C + D) = (A + C + D)(A' + C + D)
Product (repeats removed): **(A + C + D)(A + C + D')(A' + C + D)**
This matches the notes. If you write it in four variables A, B, C, D, it has six maxterms: ΠM(0, 1, 4, 5, 8, 12).

> **[NOTES ERROR] Problem 6(b)** The PDF expands only (B + C)(C' + D') and forgets the factor **A**. The factor A is a full sum term only for three variables, so for four variables A, B, C, D the correct canonical POS has 12 maxterms: ΠM(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15).
> If your teacher only wants the form, write **A . (B + C) . (C' + D')** and mention that it is zero for those 12 input combinations.

> **[NOTES ERROR] Problem 6(c)** (X + Y)(Y + Z)(X + Z). The PDF gives only three maxterms. The correct canonical POS has **four**:
> **(X + Y + Z)(X + Y + Z')(X + Y' + Z)(X' + Y + Z) = ΠM(0, 1, 2, 4)**
> Working: (X + Y) = (X + Y + Z)(X + Y + Z'); (Y + Z) = (X + Y + Z)(X' + Y + Z); (X + Z) = (X + Y + Z)(X + Y' + Z). Collect all different terms: M0, M1, M4, M2.

---

## 6. Karnaugh map

**Two variable K-map:** 2^2 = 4 cells. Each cell is one minterm: m0 = A'B', m1 = A'B, m2 = AB', m3 = AB (A is MSB).
- A **1** in a cell means that minterm is present in the output. A **0** or blank means it is not present.
- Example: f = A'B' + A'B + AB (minterms 0, 1, 3) = Σm(0, 1, 3). (The PDF writes this as Σm(0, 2, 3) with a matching map. Always write the minterm numbers that match the terms you wrote.)

**Mapping POS:** place **0** in the cell of each maxterm that is present, and **1** in all the other cells.

**Three variable K-map:** 2^3 = 8 cells. A is MSB, C is LSB. Column order is Gray code: BC = 00, 01, 11, 10.

**Four variable K-map:** 2^4 = 16 cells. Rows AB and columns CD both follow Gray code 00, 01, 11, 10 (so 01 is followed by 11, and 11 by 10: called **adjacency ordering**).

---

## 7. Worked K-map problems from the notes (all checked)

**Problem 1 (writing the expression from a truth table):**
1. A B Y: ones at 01 and 10, so Y = A'B + AB' (this is XOR).
2. x1 x2 f = 1, 1, 0, 1 so f = x1' + x2.
3. A B F = 0, 1, 1, 1 so F = A + B.
4. 3 variables, F = 1 for 0, 2, 3, 4, 5: **F = A'C' + A'B + AB'** (checked).
5. 4 variables, F = 1 for 1, 2, 3, 5, 6, 7, 8, 10, 13, 15: **F = A'D + A'C + BD + AB'D'** (checked).

**Problem 2 (reduce using K-map):**

| No. | Function | Answer in notes | Checked? |
|---|---|---|---|
| 1 | Σ(0,1,3,6,7) | y = A'B' + BC | **wrong** |
| 2 | Σ(4,5,7) | y = AB' + AC | correct |
| 3 | Σ(1,2,3,7) | F = A'C + A'B + BC | correct |
| 4 | Σ(1,2,3,5,8,10,11,12) | F = A'B'D + AC'D' + B'C | **wrong** |
| 5 | Σm(0,1,4,8,9,10) | f = B'C' + A'C'D' + AB'D' | correct |
| 6 | (A+B+C')(A+B'+C')(A'+B'+C') | y = (A + C')(B' + C') | correct |
| 7 | π(0,1,3,6,7) | f = (A + B)(B' + C')(A' + B') | correct |
| 8 | Σm(2,3,4,6,11,12) + d(10,13,14) | F = BD' + B'C | correct |
| 9 | Σm(0,1,4,5,6,10,13) + d(2,3) | f = A'C' + B'C + A'D' + BC'D | **wrong** |
| 10 | Σm(1,2,6,7,8,13,14,15) + d(0,3,5,12) | f = AC'D' + A'D + A'C + AB | correct |

> **[NOTES ERROR] No. 1.** The notes' answer leaves out cell 6 (ABC'). Correct: **y = A'B' + A'C + AB** (or A'B' + BC + AB, both are valid).
> **[NOTES ERROR] No. 4.** The notes' answer leaves out cell 5 (A'BC'D... i.e. 0101). Correct: **F = B'C + A'C'D + AC'D'**.
> **[NOTES ERROR] No. 9.** The notes' answer wrongly covers cell 11, which is neither a 1 nor a don't care. Correct: **f = A'B' + A'D' + BC'D + B'CD'**.

**Rules for K-map grouping (reminder):**
1. Group 1s in powers of 2: pair (2), quad (4), octet (8). Always take the biggest group.
2. Every 1 must be covered at least once.
3. Don't care cells can be used as 1 if they help to make a bigger group. They need not be covered.
4. Left and right edges are neighbours. Top and bottom edges are neighbours.
5. Diagonal groups and groups of odd size are illegal.

---

## 8. NAND and NOR implementation

**Using NAND gates:**
| Gate | How | Formula |
|---|---|---|
| NOT | join the two inputs | Q = NOT(A AND A) |
| AND | NAND followed by NAND as NOT | Q = NOT[NOT(A.B) AND NOT(A.B)] |
| OR | NAND on each input as NOT, then a NAND | Q = NOT[NOT(A.A) AND NOT(B.B)] |

**Using NOR gates:**
| Gate | How | Formula |
|---|---|---|
| NOT | join the two inputs | Output = NOT(A + A) |
| OR | NOR followed by NOR as NOT | Output = NOT[NOT(A + B) + NOT(A + B)] |
| AND | NOR with inverted inputs | invert A and B, then NOR them |

All of these were tested for the four input combinations and give the right truth tables.
