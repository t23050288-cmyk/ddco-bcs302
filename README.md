# Digital Design and Computer Organization (BCS302) — VTU

Exam-ready notes for VTU 3rd semester "Digital Design and Computer Organization" (BCS302), written in easy student language.

Sources: the college Module 1 notes PDF, the handwritten Module 1 and Module 2 note PDFs, and the Assignment 1 sheet (Oct 2026). Answers are written in simple words, enough for full marks at 3rd sem level, and not copied word-for-word from any source.

## Contents

### Assignment 1 (10 questions x 5 marks = 50)

| File | Covers |
|---|---|
| [DDCO-Assignment-1/DDCO-Assignment-1.md](DDCO-Assignment-1/DDCO-Assignment-1.md) | Q1 Boolean minimization, Q2 basic gates with truth tables, Q3 K-map simplification (2 functions), Q4 gates using NAND and NOR, Q5 4-bit carry look ahead adder, Q6 4x1 multiplexer, Q7 latch vs flip-flop, Q8 SR latch using NOR gates, Q9 basic operation concepts of a computer, Q10 functional units of a digital computer |

Every numeric answer was machine-verified before writing (see below).

### Notes

| File | Covers |
|---|---|
| [College-Notes-Module1-Checked.md](College-Notes-Module1-Checked.md) | **Start here for the college notes.** Follows the college Module 1 PDF section by section (laws, gates, canonical forms, K-map, NAND/NOR). Every worked answer was checked, and the mistakes found in the PDF are marked and corrected |
| [Module1-Notes.md](Module1-Notes.md) | Binary logic, theorems and postulates, De Morgan, Boolean functions, all gates, NAND/NOR implementation, SOP/POS, minterms and maxterms, canonical forms, K-map rules, don't cares, worked examples |
| [Module2-Notes.md](Module2-Notes.md) | Half and full adder, ripple carry adder, CLA, decoder, encoder, MUX, DEMUX, latches and flip-flops, master-slave, edge triggering, excitation tables |

### Verification scripts

| File | What it checks |
|---|---|
| [DDCO-Assignment-1/verification/q1_q3_boolean_kmap_check.py](DDCO-Assignment-1/verification/q1_q3_boolean_kmap_check.py) | Q1 truth tables, Q3 K-map answers (prime implicants and minimum cover) |
| [DDCO-Assignment-1/verification/q4_q5_q8_cla_latch_nandnor_check.py](DDCO-Assignment-1/verification/q4_q5_q8_cla_latch_nandnor_check.py) | Q4 NAND/NOR constructions, Q5 CLA expressions vs real addition (all 512 cases), Q8 SR NOR latch behaviour |

Run them with `python3 <file>`; they print OK lines and no dependencies are needed.
