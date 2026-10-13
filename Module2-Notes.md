# Module 2: Combinational & Sequential Circuits (BCS302)

Short exam notes. Each topic has a definition, easy points, the key expressions and small tables.

---

## 1. Half adder

**Definition:** A half adder adds two single bits and gives a sum and a carry.

- Sum S = A ⊕ B
- Carry C = A.B

| A | B | S | C |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Made with one XOR gate and one AND gate.

## 2. Full adder

**Definition:** A full adder adds three bits (two inputs plus the carry from the previous stage) and gives sum and carry out.

- Sum S = A ⊕ B ⊕ Cin
- Carry Cout = AB + BCin + ACin = AB + Cin(A ⊕ B)

| A | B | Cin | S | Cout |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

Can be built from two half adders and one OR gate.

## 3. Ripple carry adder (4-bit)

1. Four full adders joined in series; carry of each stage goes into the next.
2. Simple, but slow: the carry must **ripple** through all stages.
3. Total delay grows with the number of bits: for n bits, roughly 2n gate delays.
4. For big word sizes it becomes too slow, which is why the CLA is used.

## 4. Carry look ahead adder (CLA)

**Definition:** A fast adder where each carry is computed directly from the inputs using generate and propagate signals, so all carries come at almost the same time.

- Generate: Gi = Ai.Bi (the stage itself makes a carry)
- Propagate: Pi = Ai + Bi (a carry passes through)
- C1 = G0 + P0C0
- C2 = G1 + P1G0 + P1P0C0
- C3 = G2 + P2G1 + P2P1G0 + P2P1P0C0
- C4 = G3 + P3G2 + P3P2G1 + P3P2P1G0 + P3P2P1P0C0

Delay is constant (2 levels of gates) instead of growing with n. Costs more gates than ripple carry.

## 5. Decoder

**Definition:** A decoder converts coded binary input into a single output line. An n-to-2^n decoder has n inputs and 2^n outputs; exactly one output is 1 for each input combination.

Example: 2x4 decoder with enable E: D0 = E.A'.B', D1 = E.A'.B, D2 = E.A.B', D3 = E.A.B.

## 6. Encoder

**Definition:** An encoder is the opposite of a decoder. It has 2^n input lines and n output lines; the output is the binary code of the line that is active.

Example: 4x2 encoder: when input I1 is 1, output is A1A0 = 01; when I2 is 1, output is 10, and so on.

## 7. Multiplexer (MUX)

**Definition:** A multiplexer selects one of many inputs and sends it to a single output line. It works like a digitally controlled switch.

1. A 2^n x 1 MUX has 2^n inputs, n select lines and one output.
2. A 4x1 MUX: inputs I0 to I3, select lines S1 S0. Output Y = S1'S0'I0 + S1'S0I1 + S1S0'I2 + S1S0I3.
3. Uses: data routing, function realization (any n-variable function fits in a 2^n x 1 MUX).

## 8. Demultiplexer (DEMUX)

**Definition:** A demultiplexer takes one input and sends it to one of many outputs selected by select lines. It is the reverse of a MUX.

A 1x4 DEMUX has 1 input, 2 select lines and 4 outputs; only the selected output follows the input.

## 9. Latch vs flip-flop

| Latch | Flip-flop |
|---|---|
| Level triggered | Edge triggered |
| Output follows the input while the enable is active | Output changes only at the clock edge |
| Built from gates only | Latch + clock control |
| Faster, used inside ICs | Used for registers, counters |

## 10. SR latch

**NOR version:** S = R = 0 keeps the state, S = 1 sets Q = 1, R = 1 resets Q = 0, and S = R = 1 is not used (both outputs go to 0, so Q and Q' are not complements).

**NAND version (S'R' latch):** the control inputs are active low; S' = R' = 1 keeps the state, S' = 0 sets, R' = 0 resets, S' = R' = 0 invalid.

Characteristic equation: **Qn+1 = S + R'Qn**, with the restriction SR = 0.

## 11. Flip-flop types

**D flip-flop:** output copies the input at the clock edge. Qn+1 = D. One input, no invalid state. Used for data storage.

**JK flip-flop:** like SR but J = K = 1 **toggles** the output instead of being invalid. Qn+1 = JQn' + K'Qn. Most flexible flip-flop.

**T flip-flop:** JK with J and K joined. T = 1 toggles, T = 0 holds. Qn+1 = T⊕Qn. Used in counters.

| Type | Characteristic equation |
|---|---|
| SR | Qn+1 = S + R'Qn (SR = 0) |
| D | Qn+1 = D |
| JK | Qn+1 = JQn' + K'Qn |
| T | Qn+1 = T⊕Qn |

## 12. Master-slave JK and edge triggering

1. The race problem: with J = K = 1 and a level-triggered JK, the output toggles again and again while the clock stays 1.
2. **Master-slave:** two flip-flops in series. The master is enabled when clock = 1, the slave when clock = 0, so the output changes only once per clock cycle.
3. **Edge triggering** solves it more simply: the output changes only at the rising (or falling) edge of the clock, and is blocked the rest of the time. Modern ICs use this.

## 13. Excitation tables (used when designing counters)

Present state Qn, next state Qn+1, what inputs are needed:

| Qn | Qn+1 | S R | J K | D | T |
|---|---|---|---|---|---|
| 0 | 0 | 0 X | 0 X | 0 | 0 |
| 0 | 1 | 1 0 | 1 X | 1 | 1 |
| 1 | 0 | 0 1 | X 1 | 0 | 1 |
| 1 | 1 | X 0 | X 0 | 1 | 0 |
