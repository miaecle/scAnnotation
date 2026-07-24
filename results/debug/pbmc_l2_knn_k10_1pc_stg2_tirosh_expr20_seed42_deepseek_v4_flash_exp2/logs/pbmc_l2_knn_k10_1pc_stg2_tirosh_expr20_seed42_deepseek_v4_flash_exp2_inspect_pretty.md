# Inspect Traces

Total records: 9

## Record 1

- stage: stage1_annotation
- row_idx: 0
- cell_idx: 13748
- cell_barcode: L1_TTTGTTGCAGCGAGTA
- true_label: CD16 Mono

### prompt

```text
Tissue context: PBMC

Top genes (ranked by expression level):
    1. MALAT1 (5.910)
    2. FTL (5.449)
    3. TMSB4X (5.005)
    4. B2M (4.951)
    5. FTH1 (4.853)
    6. TMSB10 (4.308)
    7. ACTB (4.169)
    8. S100A4 (4.119)
    9. EEF1A1 (4.064)
   10. S100A6 (3.967)
   11. CST3 (3.890)
   12. AIF1 (3.799)
   13. TPT1 (3.720)
   14. LST1 (3.644)
   15. NEAT1 (3.577)
   16. CTSS (3.565)
   17. S100A11 (3.537)
   18. LYZ (3.486)
   19. SAT1 (3.477)
   20. PTMA (3.409)

Top expressed surface proteins / ADT markers (ranked by count):
    1. CD41 (3.942)
    2. CD62P (3.935)
    3. CD31 (3.822)
    4. CD4-1 (3.706)
    5. CD48 (3.094)
    6. CD18 (3.082)
    7. CD45-2 (3.014)
    8. CLEC2 (2.941)
    9. CD35 (2.829)
   10. CD93 (2.770)
   11. CD102 (2.720)
   12. CD63 (2.491)
   13. CD49d (2.477)
   14. CD43 (2.462)
   15. CD9 (2.437)
   16. CD61 (2.423)
   17. CD172a (2.415)
   18. CD16 (2.376)
   19. CD11b-1 (2.223)
   20. CD47 (2.180)

Choose the cell type from the following list (output exactly one of these names in the first line):
CD16 Mono, B memory, CD14 Mono

Based on the expression profile above, which cell type is this? Respond with the chosen cell type name (from the list above) in the first line, then in the second line provide very brief explanation (<100 words).
```

### output

```text
CD16 Mono
Top genes (LYZ, CST3, AIF1, CTSS, S100 family) and surface proteins (CD16, CD11b, CD18, CD45) are characteristic of monocytes, particularly non-classical CD16+ monocytes. Low CD14 expression and presence of CD16 confirm this subtype.
```

## Record 2

- stage: stage2_program_query
- row_idx: 0
- cell_idx: 13748
- cell_barcode: L1_TTTGTTGCAGCGAGTA
- true_label: CD16 Mono
- stage1_label: CD16 Mono

### stage1_reasoning

```text
Top genes (LYZ, CST3, AIF1, CTSS, S100 family) and surface proteins (CD16, CD11b, CD18, CD45) are characteristic of monocytes, particularly non-classical CD16+ monocytes. Low CD14 expression and presence of CD16 confirm this subtype.
```

### prompt_prefix

```text
This annotation may have minor inaccuracies, or may have been confused with a neighboring type.

Return a JSON object with gene programs for:
  1. The fine-grained subtypes of this cell type commonly found in PBMC.
  2. The most commonly confused neighboring cell types in PBMC.

Each key is a subtype/cell-type name; each value contains:
  "genes": list anywhere from 20 to 50 genes most specifically UPREGULATED in that subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)
  "description": one-sentence biological description

Include 3-5 subtypes total. Focus on subtypes commonly found in PBMC.
Return only the JSON.
```

### prompt

```text
A single cell in PBMC was annotated in a first pass as: "CD16 Mono"

```

### full_prompt

```text
This annotation may have minor inaccuracies, or may have been confused with a neighboring type.

Return a JSON object with gene programs for:
  1. The fine-grained subtypes of this cell type commonly found in PBMC.
  2. The most commonly confused neighboring cell types in PBMC.

Each key is a subtype/cell-type name; each value contains:
  "genes": list anywhere from 20 to 50 genes most specifically UPREGULATED in that subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)
  "description": one-sentence biological description

Include 3-5 subtypes total. Focus on subtypes commonly found in PBMC.
Return only the JSON.

A single cell in PBMC was annotated in a first pass as: "CD16 Mono"

```

### output

```text
{
  "CD16+ Monocyte (non-classical)": {
    "genes": [
      "FCGR3A",
      "LST1",
      "RHOC",
      "MS4A7",
      "LILRB2",
      "CDKN1C",
      "CX3CR1",
      "CFD",
      "HES4",
      "TCF7L2",
      "GTF2I",
      "MEF2C",
      "ZFP36L2",
      "IFITM3",
      "SERPINB1",
      "TMBIM1",
      "RBP7",
      "FES",
      "PTPRC",
      "ITGAL",
      "C5AR1",
      "FPR1",
      "S100A12",
      "CD36",
      "CLIC1"
    ],
    "description": "Patrolling monocytes that survey the endothelium and secrete pro-inflammatory cytokines such as TNF and IL-1β."
  },
  "Classical Monocyte": {
    "genes": [
      "CD14",
      "LYZ",
      "S100A8",
      "S100A9",
      "FCN1",
      "CST3",
      "CTSS",
      "PSAP",
      "NPC2",
      "TYMP",
      "VCAN",
      "TREM1",
      "IL1B",
      "CXCL8",
      "CCL3",
      "CCL4",
      "MNDA",
      "CSF1R",
      "IRF8",
      "MAFB",
      "CEBPA",
      "ETS2",
      "ETS1",
      "CTSD",
      "LIPA"
    ],
    "description": "Phagocytic monocytes that migrate to tissues and differentiate into macrophages or dendritic cells, key responders in infection and inflammation."
  },
  "Natural Killer (NK) cell": {
    "genes": [
      "NKG7",
      "GNLY",
      "PRF1",
      "GZMB",
      "GZMA",
      "GZMK",
      "KLRD1",
      "KLRB1",
      "KLRF1",
      "NCR1",
      "NCR3",
      "FCGR3A",
      "KLRK1",
      "KLRC1",
      "CST7",
      "CCL5",
      "XCL1",
      "XCL2",
      "ZEB2",
      "EOMES",
      "TBX21",
      "IL2RB",
      "IL18RAP",
      "CD247",
      "MYBL1"
    ],
    "description": "Cytotoxic innate lymphoid cells that kill infected or malignant cells without prior sensitization, characterized by expression of NKG7 and GNLY."
  }
}
```

## Record 3

- stage: stage2_refinement
- row_idx: 0
- cell_idx: 13748
- cell_barcode: L1_TTTGTTGCAGCGAGTA
- true_label: CD16 Mono
- stage1_label: CD16 Mono

### prompt

```text
Tissue context: PBMC

Stage-1 annotation: "CD16 Mono" — may have minor inaccuracies. Use the evidence below to confirm or correct it.

Stage-1 reasoning:
Top genes (LYZ, CST3, AIF1, CTSS, S100 family) and surface proteins (CD16, CD11b, CD18, CD45) are characteristic of monocytes, particularly non-classical CD16+ monocytes. Low CD14 expression and presence of CD16 confirm this subtype.

Top 30 genes by raw expression:
    1. MALAT1      (5.910)
    2. FTL         (5.449)
    3. TMSB4X      (5.005)
    4. B2M         (4.951)
    5. FTH1        (4.853)
    6. TMSB10      (4.308)
    7. ACTB        (4.169)
    8. S100A4      (4.119)
    9. EEF1A1      (4.064)
   10. S100A6      (3.967)
   11. CST3        (3.890)
   12. AIF1        (3.799)
   13. TPT1        (3.720)
   14. LST1        (3.644)
   15. NEAT1       (3.577)
   16. CTSS        (3.565)
   17. S100A11     (3.537)
   18. LYZ         (3.486)
   19. SAT1        (3.477)
   20. PTMA        (3.409)
   21. HLA-C       (3.389)
   22. OAZ1        (3.381)
   23. NACA        (3.350)
   24. TYROBP      (3.347)
   25. TXNIP       (3.303)
   26. HLA-DRA     (3.287)
   27. UBA52       (3.285)
   28. COTL1       (3.279)
   29. HLA-B       (3.274)
   30. FAU         (3.237)

Surface proteins (z-score vs. population):
    1. CD41             z=+3.94
    2. CD62P            z=+3.93
    3. CD31             z=+3.82
    4. CD4-1            z=+3.71
    5. CD48             z=+3.09
    6. CD18             z=+3.08
    7. CD45-2           z=+3.01
    8. CLEC2            z=+2.94
    9. CD35             z=+2.83
   10. CD93             z=+2.77
   11. CD102            z=+2.72
   12. CD63             z=+2.49
   13. CD49d            z=+2.48
   14. CD43             z=+2.46
   15. CD9              z=+2.44

Pathway scores (LLM-defined gene programs scored against this cell; higher = more active program):
  CD16+ Monocyte (non-classical): +1.127
  Classical Monocyte       : +0.332
  Natural Killer (NK) cell : -0.535

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
Top genes (LYZ, CST3, AIF1, CTSS, S100) and pathway scores indicate CD16+ monocyte. Surface proteins include CD18, CD45, CD35, CD49d, CD9, consistent with monocytes; the platelet markers (CD41, CD62P) likely reflect contamination or aggregates.
```

## Record 4

- stage: stage1_annotation
- row_idx: 1
- cell_idx: 48
- cell_barcode: L1_AAAGAACCACCTCTAC
- true_label: B memory

### prompt

```text
Tissue context: PBMC

Top genes (ranked by expression level):
    1. MALAT1 (6.431)
    2. EEF1A1 (4.733)
    3. IGKC (4.676)
    4. B2M (4.631)
    5. TPT1 (4.142)
    6. TMSB4X (4.073)
    7. HLA-DRA (3.950)
    8. CD74 (3.948)
    9. TMSB10 (3.923)
   10. FAU (3.716)
   11. PTMA (3.694)
   12. UBA52 (3.526)
   13. TXNIP (3.256)
   14. CD52 (3.241)
   15. ACTB (3.212)
   16. RACK1 (3.183)
   17. HLA-DPB1 (3.148)
   18. EEF1B2 (3.148)
   19. HLA-B (3.140)
   20. NACA (3.126)

Top expressed surface proteins / ADT markers (ranked by count):
    1. CD35 (4.648)
    2. CD73 (3.910)
    3. CD19 (3.654)
    4. CD22 (3.611)
    5. CD4-1 (3.102)
    6. CD48 (3.021)
    7. CD71 (2.492)
    8. CD45-2 (2.392)
    9. CD62P (2.384)
   10. CD21 (2.337)
   11. Integrin-7 (2.310)
   12. CD8a (2.215)
   13. CD18 (2.154)
   14. CD49d (2.066)
   15. CD27 (2.058)
   16. CD93 (2.015)
   17. CD102 (1.897)
   18. CD45RA (1.862)
   19. CD47 (1.831)
   20. CD268 (1.803)

Choose the cell type from the following list (output exactly one of these names in the first line):
CD16 Mono, B memory, CD14 Mono

Based on the expression profile above, which cell type is this? Respond with the chosen cell type name (from the list above) in the first line, then in the second line provide very brief explanation (<100 words).
```

### output

```text
B memory
High expression of B cell markers (CD19, CD22, IGKC) and memory-associated CD27 indicate a memory B cell. Monocyte markers (CD14, CD16) are absent.
```

## Record 5

- stage: stage2_program_query
- row_idx: 1
- cell_idx: 48
- cell_barcode: L1_AAAGAACCACCTCTAC
- true_label: B memory
- stage1_label: B memory

### stage1_reasoning

```text
High expression of B cell markers (CD19, CD22, IGKC) and memory-associated CD27 indicate a memory B cell. Monocyte markers (CD14, CD16) are absent.
```

### prompt_prefix

```text
This annotation may have minor inaccuracies, or may have been confused with a neighboring type.

Return a JSON object with gene programs for:
  1. The fine-grained subtypes of this cell type commonly found in PBMC.
  2. The most commonly confused neighboring cell types in PBMC.

Each key is a subtype/cell-type name; each value contains:
  "genes": list anywhere from 20 to 50 genes most specifically UPREGULATED in that subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)
  "description": one-sentence biological description

Include 3-5 subtypes total. Focus on subtypes commonly found in PBMC.
Return only the JSON.
```

### prompt

```text
A single cell in PBMC was annotated in a first pass as: "B memory"

```

### full_prompt

```text
This annotation may have minor inaccuracies, or may have been confused with a neighboring type.

Return a JSON object with gene programs for:
  1. The fine-grained subtypes of this cell type commonly found in PBMC.
  2. The most commonly confused neighboring cell types in PBMC.

Each key is a subtype/cell-type name; each value contains:
  "genes": list anywhere from 20 to 50 genes most specifically UPREGULATED in that subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)
  "description": one-sentence biological description

Include 3-5 subtypes total. Focus on subtypes commonly found in PBMC.
Return only the JSON.

A single cell in PBMC was annotated in a first pass as: "B memory"

```

### output

```text
{
  "Switched memory B": {
    "genes": [
      "CD27",
      "CR2",
      "CD40",
      "CXCR5",
      "IL4R",
      "BANK1",
      "MS4A1",
      "CD79A",
      "CD79B",
      "PAX5",
      "TNFRSF13B",
      "TNFRSF13C",
      "ZNF608",
      "P2RY8",
      "IGHG1",
      "IGHG3",
      "IGHA1",
      "IGHA2",
      "AICDA",
      "BCL6",
      "MEF2C",
      "POU2AF1",
      "SPIB",
      "IRF8",
      "NFATC1"
    ],
    "description": "Memory B cells that have undergone class switch recombination, typically expressing CD27 and lacking surface IgD."
  },
  "Unswitched memory B": {
    "genes": [
      "IGHD",
      "IGHM",
      "CD27",
      "CR2",
      "CXCR5",
      "MS4A1",
      "CD79A",
      "CD79B",
      "PAX5",
      "CD40",
      "IL4R",
      "TNFRSF13B",
      "TNFRSF13C",
      "CD1C",
      "CD1D",
      "CXCR4",
      "FCRL1",
      "FCRL2",
      "FCRL3",
      "BIRC3",
      "TCL1A",
      "IGHJ",
      "IGLC2",
      "IGKV1-39",
      "IGLV1-47"
    ],
    "description": "Memory B cells that have not undergone class switch recombination, co-expressing surface IgM and IgD along with CD27."
  },
  "Naive B": {
    "genes": [
      "IGHD",
      "IGHM",
      "TCL1A",
      "FCER2",
      "CD24",
      "CD38",
      "MS4A1",
      "CD79A",
      "CD79B",
      "PAX5",
      "CXCR4",
      "CXCR5",
      "IL4R",
      "TNFRSF13C",
      "P2RY8",
      "LRMP",
      "FCRLA",
      "FCRLB",
      "IGHJ",
      "IGLC2",
      "IGKV1-39",
      "IGLV1-47",
      "IGKC",
      "IGLC1",
      "IGHV1-18"
    ],
    "description": "Mature B cells that have not encountered antigen, expressing surface IgD and IgM, lacking CD27."
  },
  "Plasma cells": {
    "genes": [
      "SDC1",
      "MZB1",
      "XBP1",
      "PRDM1",
      "JCHAIN",
      "TNFRSF17",
      "CD38",
      "SLAMF7",
      "FKBP11",
      "SSB",
      "POU2AF1",
      "IRF4",
      "PTPRC",
      "HSP90B1",
      "PDIA6",
      "PDIA4",
      "CALR",
      "CANX",
      "GANAB",
      "SELENOM",
      "HYOU1",
      "KLRG1",
      "FCRL5",
      "CD28",
      "ITGA4"
    ],
    "description": "Antibody-secreting effector B cells characterized by high CD38 and surface or intracellular immunoglobulin."
  }
}
```

## Record 6

- stage: stage2_refinement
- row_idx: 1
- cell_idx: 48
- cell_barcode: L1_AAAGAACCACCTCTAC
- true_label: B memory
- stage1_label: B memory

### prompt

```text
Tissue context: PBMC

Stage-1 annotation: "B memory" — may have minor inaccuracies. Use the evidence below to confirm or correct it.

Stage-1 reasoning:
High expression of B cell markers (CD19, CD22, IGKC) and memory-associated CD27 indicate a memory B cell. Monocyte markers (CD14, CD16) are absent.

Top 30 genes by raw expression:
    1. MALAT1      (6.431)
    2. EEF1A1      (4.733)
    3. IGKC        (4.676)
    4. B2M         (4.631)
    5. TPT1        (4.142)
    6. TMSB4X      (4.073)
    7. HLA-DRA     (3.950)
    8. CD74        (3.948)
    9. TMSB10      (3.923)
   10. FAU         (3.716)
   11. PTMA        (3.694)
   12. UBA52       (3.526)
   13. TXNIP       (3.256)
   14. CD52        (3.241)
   15. ACTB        (3.212)
   16. RACK1       (3.183)
   17. HLA-DPB1    (3.148)
   18. EEF1B2      (3.148)
   19. HLA-B       (3.140)
   20. NACA        (3.126)
   21. FTL         (3.112)
   22. LTB         (3.057)
   23. HLA-DRB1    (3.033)
   24. HLA-DPA1    (2.981)
   25. HLA-C       (2.837)
   26. FTH1        (2.730)
   27. CD37        (2.700)
   28. EIF1        (2.664)
   29. H3F3A       (2.623)
   30. MS4A1       (2.585)

Surface proteins (z-score vs. population):
    1. CD35             z=+4.65
    2. CD73             z=+3.91
    3. CD19             z=+3.65
    4. CD22             z=+3.61
    5. CD4-1            z=+3.10
    6. CD48             z=+3.02
    7. CD71             z=+2.49
    8. CD45-2           z=+2.39
    9. CD62P            z=+2.38
   10. CD21             z=+2.34
   11. Integrin-7       z=+2.31
   12. CD8a             z=+2.21
   13. CD18             z=+2.15
   14. CD49d            z=+2.07
   15. CD27             z=+2.06

Pathway scores (LLM-defined gene programs scored against this cell; higher = more active program):
  Switched memory B        : +2.038
  Unswitched memory B      : +0.947
  Naive B                  : +0.852
  Plasma cells             : +0.132

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
B memory
High B cell markers (CD19, CD22, IGKC, MS4A1) and memory-associated CD27 confirm B memory. Monocyte markers CD14/CD16 are absent. Pathway scores strongly prefer switched memory B.
```

## Record 7

- stage: stage1_annotation
- row_idx: 2
- cell_idx: 6148
- cell_barcode: L1_CTGAATGAGGGCGAAG
- true_label: CD14 Mono

### prompt

```text
Tissue context: PBMC

Top genes (ranked by expression level):
    1. MALAT1 (5.713)
    2. FTL (4.947)
    3. B2M (4.799)
    4. TMSB4X (4.751)
    5. LYZ (4.707)
    6. EEF1A1 (4.372)
    7. TMSB10 (4.261)
    8. TPT1 (4.245)
    9. FTH1 (4.219)
   10. HLA-DRA (4.067)
   11. ACTB (3.992)
   12. CD74 (3.974)
   13. CST3 (3.834)
   14. NEAT1 (3.555)
   15. PTMA (3.520)
   16. S100A4 (3.491)
   17. FOS (3.474)
   18. UBA52 (3.419)
   19. HLA-DPA1 (3.379)
   20. HLA-DPB1 (3.311)

Top expressed surface proteins / ADT markers (ranked by count):
    1. CD62P (4.078)
    2. CD4-1 (4.014)
    3. CD41 (3.623)
    4. CD31 (3.441)
    5. CD93 (3.355)
    6. CD48 (3.062)
    7. CD35 (3.014)
    8. CD18 (2.911)
    9. CD45-2 (2.705)
   10. CLEC2 (2.580)
   11. CD11b-1 (2.482)
   12. CD102 (2.399)
   13. CD63 (2.372)
   14. CLEC12A (2.314)
   15. CD49d (2.156)
   16. CD9 (2.070)
   17. CD47 (2.035)
   18. CD305 (2.012)
   19. CD61 (1.996)
   20. CD172a (1.990)

Choose the cell type from the following list (output exactly one of these names in the first line):
CD16 Mono, B memory, CD14 Mono

Based on the expression profile above, which cell type is this? Respond with the chosen cell type name (from the list above) in the first line, then in the second line provide very brief explanation (<100 words).
```

### output

```text
CD14 Mono
```

## Record 8

- stage: stage2_program_query
- row_idx: 2
- cell_idx: 6148
- cell_barcode: L1_CTGAATGAGGGCGAAG
- true_label: CD14 Mono
- stage1_label: CD14 Mono

### stage1_reasoning

```text
None
```

### prompt_prefix

```text
This annotation may have minor inaccuracies, or may have been confused with a neighboring type.

Return a JSON object with gene programs for:
  1. The fine-grained subtypes of this cell type commonly found in PBMC.
  2. The most commonly confused neighboring cell types in PBMC.

Each key is a subtype/cell-type name; each value contains:
  "genes": list anywhere from 20 to 50 genes most specifically UPREGULATED in that subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)
  "description": one-sentence biological description

Include 3-5 subtypes total. Focus on subtypes commonly found in PBMC.
Return only the JSON.
```

### prompt

```text
A single cell in PBMC was annotated in a first pass as: "CD14 Mono"

```

### full_prompt

```text
This annotation may have minor inaccuracies, or may have been confused with a neighboring type.

Return a JSON object with gene programs for:
  1. The fine-grained subtypes of this cell type commonly found in PBMC.
  2. The most commonly confused neighboring cell types in PBMC.

Each key is a subtype/cell-type name; each value contains:
  "genes": list anywhere from 20 to 50 genes most specifically UPREGULATED in that subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)
  "description": one-sentence biological description

Include 3-5 subtypes total. Focus on subtypes commonly found in PBMC.
Return only the JSON.

A single cell in PBMC was annotated in a first pass as: "CD14 Mono"

```

### output

```text
{
  "Classical Monocyte": {
    "genes": [
      "CD14",
      "FCGR1A",
      "CSF1R",
      "CD33",
      "CTSS",
      "LYZ",
      "S100A8",
      "S100A9",
      "VCAN",
      "FGL2",
      "FCN1",
      "SERPINA1",
      "IL1B",
      "CCL2",
      "CLECT5A",
      "CD64",
      "CD11B",
      "CCR2",
      "CX3CR1",
      "S100A11",
      "TREM1",
      "CD4",
      "TLR2",
      "TLR4",
      "MYD88",
      "IRAK1",
      "NFKB1",
      "IL6R",
      "TNF",
      "IL1A",
      "IL1R1",
      "IL10",
      "IL18",
      "CD80",
      "CD86",
      "HLA-DRA",
      "HLA-DRB1",
      "CD40",
      "CD58",
      "CD97"
    ],
    "description": "Classical CD14++CD16- monocytes are the most abundant monocyte subset, responsible for phagocytosis, cytokine production, and inflammation."
  },
  "Non-classical Monocyte": {
    "genes": [
      "FCGR3A",
      "CX3CR1",
      "CD14",
      "CD16",
      "LST1",
      "RHOC",
      "S100A10",
      "S100A11",
      "AIF1",
      "COTL1",
      "MS4A7",
      "FCGR3B",
      "GPR183",
      "CSF1R",
      "ITGAL",
      "ITGAM",
      "CD11B",
      "CD11C",
      "CD18",
      "CCR5",
      "CX3CL1",
      "IL3RA",
      "IL4",
      "IL13",
      "IL1R1",
      "TNFRSF1B",
      "TLR4",
      "TLR7",
      "TLR8",
      "MYD88",
      "IRAK1",
      "NFKB1",
      "MAPK1",
      "MAPK3",
      "STAT1",
      "STAT3",
      "IRF8",
      "IRF5",
      "JAK1",
      "JAK2"
    ],
    "description": "Non-classical CD14+CD16++ monocytes patrol the endothelium, produce anti-inflammatory cytokines, and respond to viral and nucleic acid stimuli."
  },
  "Intermediate Monocyte": {
    "genes": [
      "CD14",
      "FCGR3A",
      "FCGR1A",
      "CD16",
      "CX3CR1",
      "CCR2",
      "HLA-DRA",
      "HLA-DRB1",
      "CD86",
      "CD40",
      "TNF",
      "IL1B",
      "IL6",
      "CCL3",
      "CCL4",
      "CXCL10",
      "CXCL9",
      "CD80",
      "CD58",
      "CD97",
      "TLR2",
      "TLR4",
      "TLR8",
      "MYD88",
      "IRAK1",
      "NFKB1",
      "MAPK1",
      "MAPK3",
      "STAT1",
      "STAT3",
      "IRF8",
      "IRF5",
      "JAK1",
      "JAK2",
      "S100A8",
      "S100A9",
      "S100A11",
      "CTSS",
      "LYZ",
      "VCAN",
      "FGL2",
      "FCN1",
      "SERPINA1"
    ],
    "description": "Intermediate CD14++CD16+ monocytes exhibit both classical and non-classical features, with high antigen-presenting and inflammatory cytokine production."
  },
  "CD1c+ Dendritic Cell": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "CCR7",
      "LAMP3",
      "CD83",
      "CD86",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPA1",
      "HLA-DPB1",
      "CD40",
      "CD80",
      "XCR1",
      "CADM1",
      "CLEC9A",
      "FLT3",
      "IL3RA",
      "ITGAX",
      "ITGAM",
      "CD11C",
      "IRF8",
      "IRF4",
      "ZEB2",
      "BATF3",
      "TCF4",
      "SPI1",
      "BCL6",
      "ID2",
      "E2-2",
      "TLR3",
      "TLR7",
      "TLR8",
      "MYD88",
      "IRAK1",
      "NFKB1",
      "MAPK1",
      "STAT1",
      "STAT3",
      "JAK1",
      "JAK2",
      "CLEC4C",
      "IL12A",
      "IL12B",
      "IFNAR1",
      "IFNAR2"
    ],
    "description": "CD1c+ myeloid dendritic cells (cDC2) are professional antigen-presenting cells that activate T cells and produce cytokines in response to pathogens."
  },
  "CD141+ Dendritic Cell": {
    "genes": [
      "CD141",
      "THBD",
      "XCR1",
      "CADM1",
      "CLEC9A",
      "CLEC10A",
      "CLEC4C",
      "FLT3",
      "IL3RA",
      "ITGAX",
      "ITGAM",
      "CD11C",
      "IRF8",
      "BATF3",
      "TCF4",
      "ID2",
      "E2-2",
      "TLR3",
      "TLR7",
      "TLR8",
      "MYD88",
      "IRAK1",
      "NFKB1",
      "MAPK1",
      "STAT1",
      "STAT3",
      "JAK1",
      "JAK2",
      "IL12A",
      "IL12B",
      "IFNAR1",
      "IFNAR2",
      "CCR7",
      "LAMP3",
      "CD83",
      "CD86",
      "HLA-DRA",
      "HLA-DRB1",
      "CD40",
      "CD80",
      "XCL1",
      "XCL2",
      "IL15",
      "IL18"
    ],
    "description": "CD141+ myeloid dendritic cells (cDC1) specialize in cross-presentation and are crucial for antiviral and antitumor immunity."
  }
}
```

## Record 9

- stage: stage2_refinement
- row_idx: 2
- cell_idx: 6148
- cell_barcode: L1_CTGAATGAGGGCGAAG
- true_label: CD14 Mono
- stage1_label: CD14 Mono

### prompt

```text
Tissue context: PBMC

Stage-1 annotation: "CD14 Mono" — may have minor inaccuracies. Use the evidence below to confirm or correct it.

Top 30 genes by raw expression:
    1. MALAT1      (5.713)
    2. FTL         (4.947)
    3. B2M         (4.799)
    4. TMSB4X      (4.751)
    5. LYZ         (4.707)
    6. EEF1A1      (4.372)
    7. TMSB10      (4.261)
    8. TPT1        (4.245)
    9. FTH1        (4.219)
   10. HLA-DRA     (4.067)
   11. ACTB        (3.992)
   12. CD74        (3.974)
   13. CST3        (3.834)
   14. NEAT1       (3.555)
   15. PTMA        (3.520)
   16. S100A4      (3.491)
   17. FOS         (3.474)
   18. UBA52       (3.419)
   19. HLA-DPA1    (3.379)
   20. HLA-DPB1    (3.311)
   21. FAU         (3.300)
   22. HLA-B       (3.295)
   23. TXNIP       (3.276)
   24. HLA-DRB1    (3.268)
   25. AIF1        (3.253)
   26. CTSS        (3.242)
   27. SAT1        (3.228)
   28. NACA        (3.164)
   29. JUNB        (3.163)
   30. EIF1        (3.117)

Surface proteins (z-score vs. population):
    1. CD62P            z=+4.08
    2. CD4-1            z=+4.01
    3. CD41             z=+3.62
    4. CD31             z=+3.44
    5. CD93             z=+3.36
    6. CD48             z=+3.06
    7. CD35             z=+3.01
    8. CD18             z=+2.91
    9. CD45-2           z=+2.70
   10. CLEC2            z=+2.58
   11. CD11b-1          z=+2.48
   12. CD102            z=+2.40
   13. CD63             z=+2.37
   14. CLEC12A          z=+2.31
   15. CD49d            z=+2.16

Pathway scores (LLM-defined gene programs scored against this cell; higher = more active program):
  Non-classical Monocyte   : +0.475
  CD1c+ Dendritic Cell     : +0.404
  Classical Monocyte       : +0.361
  Intermediate Monocyte    : +0.345
  CD141+ Dendritic Cell    : +0.319

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
Pathway scores rank non-classical monocyte highest, surface markers include high CD4 (typical of CD16+ monocytes), and CD14 is absent from top genes, supporting CD16 Mono over CD14 Mono.
```

