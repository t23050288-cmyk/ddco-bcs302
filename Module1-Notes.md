# Module 1: Introduction to Digital Design (BCS302)

Short exam notes based on the Module 1 class notes. Each topic has a definition, easy points and the main formula or example.

---

## 1. Binary Logic

**Definition:** Binary logic deals with variables that take only two values, 1 and 0 (true/false, yes/no, high/low), and with operations that have a logical meaning. It is equal to an algebra called **Boolean algebra**.

**Points:**
1. Variables are written with letters like A, B, C, X, Y, Z.
2. Each variable has only two possible values, 0 or 1.
3. There are three basic logical operations: AND, OR and NOT.
4. Each operation gives one binary result, say Z.

| Operation | Symbol | Expression | Rule |
|---|---|---|---|
| AND | dot | Z = X.Y | 1 only if both are 1 |
| OR | plus | Z = X + Y | 1 if any one is 1 |
| NOT | prime or bar | Z = X' | complement of X |

---

## 2. Logic gates and signal levels

**Definition:** Logic gates are electronic circuits that work on one or more input signals to produce one output signal.

1. In a digital system, a voltage is read as only 0 or 1.
2. Each level has an acceptable range of voltage. The area in between is the transition region, and the signal passes through it quickly.
3. AND and OR gates can have more than two inputs, for example a 3-input AND (F = ABC) and a 4-input OR (F = A + B + C + D).

**Positive and negative logic:**
- **Positive logic:** the high level H represents logic 1 and the low level L represents logic 0.
- **Negative logic:** the low level L represents logic 1 and the high level H represents logic 0.
- An AND gate in positive logic works as an OR gate in negative logic, and an OR gate becomes an AND gate.

---

## 3. Basic theorems and postulates of Boolean algebra

**Duality:** Every Boolean equation stays valid if the operators and identity elements are interchanged. To get the dual: change AND to OR, OR to AND, 1 to 0 and 0 to 1.

| Name | (a) | (b) |
|---|---|---|
| Postulate 2 (identity) | X + 0 = X | X . 1 = X |
| Postulate 5 (complement) | X + X' = 1 | X . X' = 0 |
| Theorem 1 (idempotent) | X + X = X | X . X = X |
| Theorem 2 | X + 1 = 1 | X . 0 = 0 |
| Theorem 3 (involution) | (X')' = X | |
| Postulate 3 (commutative) | X + Y = Y + X | XY = YX |
| Theorem 4 (associative) | X + (Y + Z) = (X + Y) + Z | X(YZ) = (XY)Z |
| Postulate 4 (distributive) | X(Y + Z) = XY + XZ | X + YZ = (X + Y)(X + Z) |
| Theorem 5 (De Morgan) | (X + Y)' = X'Y' | (XY)' = X' + Y' |
| Theorem 6 (absorption) | X + XY = X | X(X + Y) = X |

**Proof of Theorem 1(a): X + X = X**

X + X = (X + X).1 (identity)
= (X + X)(X + X') (complement)
= X + XX' (distributive)
= X + 0 (complement)
= X (identity)

**Proof of Theorem 6(a): X + XY = X**

X + XY = X.1 + XY = X(1 + Y) = X.1 = X

**De Morgan's theorem (proved by truth table):** (X + Y)' and X'Y' have the same output for all four input rows (1, 0, 0, 0).

**Complement of a function:** Use De Morgan again and again.
(A + B + C)' = A'(B + C)' = A'B'C'

---

## 4. Boolean functions

**Definition:** A Boolean function is an expression made of binary variables, the constants 0 and 1, and the logic operators. Example: F = X + Y'Z.

---

## 5. Digital logic gates (summary)

| Gate | Expression | Output 1 when |
|---|---|---|
| AND | F = XY | both inputs 1 |
| OR | F = X + Y | any input 1 |
| Inverter | F = X' | input 0 |
| Buffer | F = X | same as input |
| NAND | F = (XY)' | any input 0 |
| NOR | F = (X + Y)' | both inputs 0 |
| XOR | F = XY' + X'Y = X⊕Y | inputs different |
| XNOR | F = XY + X'Y' = (X⊕Y)' | inputs same |

---

## 6. NAND and NOR implementation

**Points:**
1. NAND and NOR are easier to make with electronic components, so IC families use them as the basic gate.
2. The NAND gate is a **universal gate**, because any logic circuit can be made with it. Same for NOR.
3. To use NAND: get the simplified Boolean function and change AND-OR logic to **NAND-NAND** logic.
4. To use NOR: change OR-AND logic to **NOR-NOR** logic.

**Examples from notes:**
- f = AB + BC (AND-OR) becomes NAND-NAND: f = [(AB)'(BC)']'. Use the K-map with minterms.
- f = (A + B)(B + C) (OR-AND) becomes NOR-NOR: f = [(A+B)' + (B+C)']'. Use the K-map with maxterms.

---

## 7. Principles of combinational logic

**Definition:** When logic gates are connected to produce a specified output for certain input combinations, with **no storage** involved, the circuit is called a combinational logic circuit.

1. It has n input variables, logic gates and m output variables.
2. The output depends only on the present inputs: **Y = F(X)**.
3. Block: inputs x0 to xn-1 go into a combinational logic circuit F, and it gives outputs y0 to ym-1.

**Terms:**

| Term | Meaning | Example |
|---|---|---|
| Literal | a variable, complemented or not | A, A' |
| Product term | literals ANDed together | A, AB', ABC |
| Sum term | literals ORed together | A, A + B, A' + B |
| SOP | product terms ORed | ABC + AB'C' + B'C |
| POS | sum terms ANDed | (P + Q')(R + S')(P + Q + R) |

---

## 8. Canonical forms

**Standard SOP (minterm form):** every product term has all the variables. Each term is a **minterm**.
Example: f(A,B,C) = AB'C' + ABC + A'BC'

**Standard POS (maxterm form):** every sum term has all the variables. Each term is a **maxterm**.
Example: f(A,B,C) = (A + B + C)(A + B' + C')(A' + B' + C')

**Minterms and maxterms for 3 variables:**

| A B C | Minterm mi | Maxterm Mi |
|---|---|---|
| 0 0 0 | A'B'C' = m0 | A + B + C = M0 |
| 0 0 1 | A'B'C = m1 | A + B + C' = M1 |
| 0 1 0 | A'BC' = m2 | A + B' + C = M2 |
| 0 1 1 | A'BC = m3 | A + B' + C' = M3 |
| 1 0 0 | AB'C' = m4 | A' + B + C = M4 |
| 1 0 1 | AB'C = m5 | A' + B + C' = M5 |
| 1 1 0 | ABC' = m6 | A' + B' + C = M6 |
| 1 1 1 | ABC = m7 | A' + B' + C' = M7 |

For n variables there are 2^n minterms and 2^n maxterms. Σm means sum of minterms. ΠM means product of maxterms.

**Converting SOP to standard SOP (steps):**
1. Find the missing literal in each product term.
2. AND the term with (missing literal + its complement).
3. Expand with the distributive law.
4. Remove repeated terms (A + A = A).

Example: f = AC + AB + BC becomes ABC + AB'C + ABC' + A'BC.

**Converting POS to standard POS:** find missing literals, OR each sum term with (literal . its complement), expand using A + BC = (A+B)(A+C), remove repeats.

**Truth table to equation:** take the rows with output 1 for SOP (write minterms), or the rows with output 0 for POS (write maxterms).
Example: if Y = 1 for rows 2, 3, 6, then f = Σm(2,3,6).

**Relation:** A function given as Σm(...) has the remaining rows as ΠM(...). Example: ΠM(2,5) = Σm(0,1,3,4,6,7).

---

## 9. Karnaugh map (K-map)

**Definition:** A K-map is a diagram made of squares, where each square is a minterm or maxterm. It is a systematic way to simplify Boolean expressions.

**Points:**
1. Number of squares = 2^n for n variables (2 var: 4, 3 var: 8, 4 var: 16, 5 var: 32).
2. Rows and columns follow **Gray code** (00, 01, 11, 10) so neighbouring cells differ by only one bit.
3. A cell is one row of the truth table. Place 1 for each minterm of the SOP.
4. For POS, place 0 for each maxterm.

**Rules for grouping:**
1. Group 1s in sizes 1, 2, 4, 8, 16 (powers of 2).
2. Always take the biggest possible group.
3. Every 1 must be covered at least once.
4. Don't cares (X) may be taken as 1 if they make a bigger group. They need not be covered.
5. Left and right edges are adjacent. Top and bottom edges are adjacent.
6. Diagonal groups and groups of odd size (3, 5, 6) are illegal.

| Group | Name | Variables removed |
|---|---|---|
| 2 cells | Pair | 1 |
| 4 cells | Quad | 2 |
| 8 cells | Octet | 3 |

**Essential prime implicant:** a group that covers a 1 which no other group covers. It must be in the answer.

**Don't care conditions:** some input combinations never occur (for example 10 to 15 in BCD). The output is not defined, written as X or d. The designer takes them as 0 or 1 to get the simplest expression. Example: f(A,B,C) = Σm(0,2,4) + d(1,5).

**Worked examples (from notes):**
1. Y = AB'C' + A'B'C' + A'B'C + A'BC' ... K-map gives Y = A'C + B'.
2. f(A,B,C,D) = Σm(0,1,4,8,9,10) gives f = A'C'D' + AB'D' + B'C'.
3. Σm(5,6,7,12,13) + d(4,9,14,15) gives Y = B.
4. Σm(7) + d(10,11,12,13,14,15) gives Y = BCD.
5. POS: ΠM(0,1,3,4,7) gives Y = (A + C')(B + C)(B' + C').
