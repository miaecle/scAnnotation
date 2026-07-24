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

Top genes (ranked by TF-IDF specificity):
    1. CST3 (0.00330)
    2. LST1 (0.00258)
    3. AIF1 (0.00258)
    4. FCGR3A (0.00226)
    5. CDKN1C (0.00225)
    6. IFITM3 (0.00203)
    7. FCN1 (0.00184)
    8. TYROBP (0.00153)
    9. FCER1G (0.00145)
   10. CFD (0.00142)
   11. HLA-DRA (0.00135)
   12. MS4A7 (0.00116)
   13. HLA-DRB1 (0.00110)
   14. HLA-DPA1 (0.00108)
   15. COTL1 (0.00103)
   16. CTSS (0.00099)
   17. S100A11 (0.00096)
   18. TYMP (0.00095)
   19. SAT1 (0.00092)
   20. MNDA (0.00090)

Top expressed surface proteins / ADT markers (ranked by count):
    1. CD41 (3.94219)
    2. CD62P (3.93463)
    3. CD31 (3.82188)
    4. CD4-1 (3.70605)
    5. CD48 (3.09374)
    6. CD18 (3.08222)
    7. CD45-2 (3.01442)
    8. CLEC2 (2.94103)
    9. CD35 (2.82852)
   10. CD93 (2.77003)
   11. CD102 (2.71976)
   12. CD63 (2.49132)
   13. CD49d (2.47745)
   14. CD43 (2.46181)
   15. CD9 (2.43680)
   16. CD61 (2.42269)
   17. CD172a (2.41501)
   18. CD16 (2.37570)
   19. CD11b-1 (2.22251)
   20. CD47 (2.18024)

Choose the cell type from the following list (output exactly one of these names in the first line):
CD16 Mono, B memory, CD14 Mono

Based on the expression profile above, which cell type is this? Respond with the chosen cell type name (from the list above) in the first line, then in the second line provide very brief explanation (<100 words).
```

### output

```text
CD16 Mono

The gene and protein profile shows high expression of FCGR3A (CD16), CST3, FCN1, and other monocyte markers, along with surface CD16 and CD11b, consistent with CD16+ (non-classical) monocytes. The absence of high CD14 and presence of platelet markers like CD41 and CD62P may indicate platelet-monocyte aggregates, but the core identity is CD16+ monocytes.
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
The gene and protein profile shows high expression of FCGR3A (CD16), CST3, FCN1, and other monocyte markers, along with surface CD16 and CD11b, consistent with CD16+ (non-classical) monocytes. The absence of high CD14 and presence of platelet markers like CD41 and CD62P may indicate platelet-monocyte aggregates, but the core identity is CD16+ monocytes.
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
      "LILRB2",
      "LST1",
      "RHOC",
      "LILRA5",
      "MS4A7",
      "ALOX5AP",
      "SLC11A1",
      "CST3",
      "LYN",
      "FCER1G",
      "TLR8",
      "CD36",
      "CX3CR1",
      "CSF1R",
      "MAFB",
      "IRF8",
      "SRGN",
      "PSAP",
      "FGL2",
      "TIMP1",
      "SERPINA1",
      "SERPINB1",
      "LITAF",
      "CTSB",
      "CTSD",
      "LGMN",
      "CD14",
      "CD16",
      "CCR2",
      "FCGR1A",
      "CD4",
      "HLA-DRA",
      "HLA-DRB1",
      "CD74",
      "ITGAM",
      "ITGAX",
      "S100A8",
      "S100A9",
      "VCAN"
    ],
    "description": "Non-classical monocytes with high CD16 expression and low CD14, involved in patrolling vasculature and immune surveillance."
  },
  "CD14+ Monocyte (classical)": {
    "genes": [
      "CD14",
      "CCR2",
      "S100A8",
      "S100A9",
      "SELL",
      "LYZ",
      "CD33",
      "FCGR2A",
      "FCGR2B",
      "FCGR3A",
      "CX3CR1",
      "CD36",
      "CSF1R",
      "MAFB",
      "IRF8",
      "SRGN",
      "PSAP",
      "FGL2",
      "TIMP1",
      "SERPINA1",
      "SERPINB1",
      "LITAF",
      "CTSB",
      "CTSD",
      "LGMN",
      "HLA-DRA",
      "HLA-DRB1",
      "CD74",
      "ITGAM",
      "ITGAX",
      "VCAN",
      "ALOX5AP",
      "SLC11A1",
      "CST3",
      "LYN",
      "FCER1G",
      "TLR8",
      "LILRB2",
      "LST1",
      "RHOC"
    ],
    "description": "Classical monocytes with high CD14 expression, major phagocytic subset in blood."
  },
  "NK cell": {
    "genes": [
      "NKG7",
      "GNLY",
      "PRF1",
      "GZMB",
      "GZMH",
      "GZMK",
      "KLRD1",
      "KLRB1",
      "KLRF1",
      "KLRG1",
      "CD247",
      "CD3E",
      "CD8A",
      "CD8B",
      "NCAM1",
      "NCR1",
      "NCR3",
      "FCGR3A",
      "CD16",
      "XCL1",
      "XCL2",
      "CCL4",
      "CCL3",
      "IFNG",
      "GZMA",
      "GZMM",
      "GZMH",
      "CST7",
      "PRF1",
      "CTSW",
      "FCER1G",
      "TGFBI",
      "PLAC8",
      "FGFBP2",
      "SPON2",
      "KLRC1",
      "KLRC2",
      "KLRC3",
      "KIR2DL1",
      "KIR2DL3",
      "KIR3DL1"
    ],
    "description": "Natural killer cells that provide rapid cytotoxicity and cytokine production, often expressing CD16 (FcγRIII)."
  },
  "Conventional dendritic cell 2 (cDC2)": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "HLA-DQA1",
      "HLA-DQB1",
      "HLA-DRA",
      "HLA-DRB1",
      "CD74",
      "ITGAX",
      "ITGAM",
      "CSF1R",
      "FLT3",
      "IRF4",
      "IRF8",
      "ZEB2",
      "BATF3",
      "ID2",
      "CD4",
      "CD11C",
      "CD14",
      "CD16",
      "CD32",
      "CD64",
      "TLR1",
      "TLR2",
      "TLR4",
      "TLR6",
      "TLR8",
      "CLEC12A",
      "CLEC7A",
      "CD209",
      "ICAM3",
      "LSP1",
      "ARPC1B",
      "WIPF1",
      "AP1S2",
      "DNASE1L3",
      "HLA-DPA1",
      "HLA-DPB1",
      "HLA-DMA",
      "HLA-DMB"
    ],
    "description": "Conventional type 2 dendritic cells that present antigen to T cells and express CD1c, FceRI, and CLEC10A."
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
The gene and protein profile shows high expression of FCGR3A (CD16), CST3, FCN1, and other monocyte markers, along with surface CD16 and CD11b, consistent with CD16+ (non-classical) monocytes. The absence of high CD14 and presence of platelet markers like CD41 and CD62P may indicate platelet-monocyte aggregates, but the core identity is CD16+ monocytes.

Top 30 cell-specific genes by TF-IDF (weights by rarity across cells — highlights rare but highly expressed genes):
    1. CST3        (0.00330)
    2. LST1        (0.00258)
    3. AIF1        (0.00258)
    4. FCGR3A      (0.00226)
    5. CDKN1C      (0.00225)
    6. IFITM3      (0.00203)
    7. FCN1        (0.00184)
    8. TYROBP      (0.00153)
    9. FCER1G      (0.00145)
   10. CFD         (0.00142)
   11. HLA-DRA     (0.00135)
   12. MS4A7       (0.00116)
   13. HLA-DRB1    (0.00110)
   14. HLA-DPA1    (0.00108)
   15. COTL1       (0.00103)
   16. CTSS        (0.00099)
   17. S100A11     (0.00096)
   18. TYMP        (0.00095)
   19. SAT1        (0.00092)
   20. MNDA        (0.00090)
   21. PSAP        (0.00090)
   22. TIMP1       (0.00089)
   23. LYZ         (0.00089)
   24. SERPINA1    (0.00084)
   25. IFI30       (0.00082)
   26. LGALS1      (0.00080)
   27. CYBB        (0.00075)
   28. FOS         (0.00071)
   29. HLA-DRB5    (0.00070)
   30. MARCKS      (0.00068)

Surface proteins (z-score vs. population):
    1. CD41             z=+3.94219
    2. CD62P            z=+3.93463
    3. CD31             z=+3.82188
    4. CD4-1            z=+3.70605
    5. CD48             z=+3.09374
    6. CD18             z=+3.08222
    7. CD45-2           z=+3.01442
    8. CLEC2            z=+2.94103
    9. CD35             z=+2.82852
   10. CD93             z=+2.77003
   11. CD102            z=+2.71976
   12. CD63             z=+2.49132
   13. CD49d            z=+2.47745
   14. CD43             z=+2.46181
   15. CD9              z=+2.43680

Pathway scores (LLM-defined gene programs scored against this cell; higher = more active program):
  CD16+ Monocyte (non-classical): +0.71352
  CD14+ Monocyte (classical): +0.59222
  Conventional dendritic cell 2 (cDC2): +0.44343
  NK cell                  : -0.45978

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
High expression of FCGR3A (CD16), CST3, FCN1, and other monocyte markers, plus pathway scores strongly favoring CD16+ non-classical monocytes over CD14+ classical ones, confirms the stage-1 annotation. Platelet markers (CD41, CD62P) suggest aggregates but do not alter core cell identity.
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

Top genes (ranked by TF-IDF specificity):
    1. IGKC (0.01036)
    2. HLA-DRA (0.00267)
    3. MS4A1 (0.00266)
    4. CD74 (0.00143)
    5. BANK1 (0.00140)
    6. IGHA1 (0.00136)
    7. HLA-DQA1 (0.00128)
    8. HLA-DRB1 (0.00118)
    9. HLA-DPB1 (0.00112)
   10. CD79A (0.00108)
   11. HLA-DPA1 (0.00104)
   12. IGHE (0.00098)
   13. LINC01781 (0.00082)
   14. HLA-DQB1 (0.00081)
   15. BLK (0.00075)
   16. IGHA2 (0.00070)
   17. LTB (0.00070)
   18. IGHG3 (0.00066)
   19. AIM2 (0.00063)
   20. SSPN (0.00062)

Top expressed surface proteins / ADT markers (ranked by count):
    1. CD35 (4.64813)
    2. CD73 (3.90991)
    3. CD19 (3.65352)
    4. CD22 (3.61087)
    5. CD4-1 (3.10164)
    6. CD48 (3.02112)
    7. CD71 (2.49240)
    8. CD45-2 (2.39245)
    9. CD62P (2.38433)
   10. CD21 (2.33703)
   11. Integrin-7 (2.31008)
   12. CD8a (2.21497)
   13. CD18 (2.15414)
   14. CD49d (2.06599)
   15. CD27 (2.05849)
   16. CD93 (2.01489)
   17. CD102 (1.89678)
   18. CD45RA (1.86227)
   19. CD47 (1.83126)
   20. CD268 (1.80250)

Choose the cell type from the following list (output exactly one of these names in the first line):
CD16 Mono, B memory, CD14 Mono

Based on the expression profile above, which cell type is this? Respond with the chosen cell type name (from the list above) in the first line, then in the second line provide very brief explanation (<100 words).
```

### output

```text
B memory
High expression of B cell marker genes (MS4A1, CD79A, BANK1, BLK) and immunoglobulins, along with surface proteins CD19, CD22, CD21, and CD27, indicate memory B cells.
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
High expression of B cell marker genes (MS4A1, CD79A, BANK1, BLK) and immunoglobulins, along with surface proteins CD19, CD22, CD21, and CD27, indicate memory B cells.
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
      "IGHG1",
      "IGHA1",
      "CR2",
      "CD40",
      "ICOSL",
      "BCL6",
      "AICDA",
      "BACH2",
      "CXCR5",
      "IL4R",
      "CD86",
      "TNFRSF13C",
      "TNFRSF13B",
      "FCRL2",
      "FCRL3",
      "FCRL5",
      "CD79A",
      "CD79B",
      "MS4A1",
      "PAX5",
      "EBF1",
      "IRF8",
      "POU2AF1",
      "SPIB",
      "TCF4",
      "BCL11A",
      "CD19",
      "CD22",
      "CD38",
      "CD72",
      "CD81",
      "CD84",
      "CD180",
      "SWAP70",
      "RC3H1",
      "MEF2C",
      "MEF2B",
      "ETS1",
      "RUNX2",
      "CREM",
      "NFATC1",
      "NFKBIZ",
      "BCL2",
      "BCL2L1",
      "BCL2L11",
      "MCL1",
      "BAX",
      "BID",
      "BIM"
    ],
    "description": "Class-switched memory B cells that have undergone immunoglobulin class switch recombination, expressing IgG or IgA and CD27."
  },
  "Non-switched memory B": {
    "genes": [
      "CD27",
      "IGHD",
      "IGHM",
      "CD1C",
      "CR2",
      "CD40",
      "ICOSL",
      "BCL6",
      "CXCR5",
      "IL4R",
      "CD86",
      "TNFRSF13C",
      "TNFRSF13B",
      "FCRL1",
      "FCRL2",
      "FCRL5",
      "CD79A",
      "CD79B",
      "MS4A1",
      "PAX5",
      "EBF1",
      "IRF8",
      "POU2AF1",
      "SPIB",
      "TCF4",
      "BCL11A",
      "CD19",
      "CD22",
      "CD38",
      "CD72",
      "CD81",
      "CD84",
      "CD180",
      "FCER2",
      "CD24",
      "CD44",
      "CD62L",
      "CD73",
      "CD200",
      "CD307",
      "CD357",
      "CD358",
      "CD360",
      "CD361",
      "CD362",
      "CD363",
      "CD364",
      "CD365"
    ],
    "description": "Non-switched memory B cells that retain expression of IgD and IgM along with CD27, typical of marginal zone or unswitched memory."
  },
  "Atypical memory B": {
    "genes": [
      "ITGAX",
      "TBX21",
      "FCRL5",
      "FCRL4",
      "FCRL3",
      "CD11C",
      "T-bet",
      "CXCR3",
      "CXCR6",
      "CCR5",
      "CCR6",
      "CD27",
      "CD21",
      "CD19",
      "CD20",
      "CD79A",
      "CD79B",
      "MS4A1",
      "PAX5",
      "EBF1",
      "IRF8",
      "POU2AF1",
      "SPIB",
      "TCF4",
      "BCL11A",
      "CD22",
      "CD38",
      "CD72",
      "CD81",
      "CD84",
      "CD180",
      "FCER2",
      "CD24",
      "CD44",
      "CD62L",
      "CD73",
      "CD200",
      "CD307",
      "CD357",
      "CD358",
      "CD360",
      "CD361",
      "CD362",
      "CD363",
      "CD364",
      "CD365"
    ],
    "description": "Atypical memory B cells, also known as double-negative or T-bet+ memory B cells, which are expanded in certain infections and autoimmune conditions."
  },
  "Plasma cells": {
    "genes": [
      "SDC1",
      "MZB1",
      "XBP1",
      "PRDM1",
      "JCHAIN",
      "IGLL5",
      "DERL3",
      "FNDC3B",
      "FKBP11",
      "SEC61A2",
      "SEC61B",
      "SEC61G",
      "SSR4",
      "P4HB",
      "PDIA4",
      "PDIA6",
      "ERO1A",
      "HYOU1",
      "HSPA5",
      "HSP90B1",
      "CANX",
      "CALR",
      "PDIA3",
      "PDIA5",
      "PDIA2",
      "CALU",
      "ERP29",
      "ERP44",
      "TXNDC5",
      "VIMP",
      "SEL1L",
      "EDEM1",
      "EDEM2",
      "EDEM3",
      "OS9",
      "MAN1A1",
      "MAN1B1",
      "MAN1C1",
      "MAN2A1",
      "MAN2B1",
      "MAN2C1",
      "GANA",
      "GANAB",
      "GANC",
      "GBA",
      "GLA",
      "GLB1",
      "GLB1L",
      "GLT25D1",
      "GLT25D2"
    ],
    "description": "Plasma cells, the antibody-secreting effector cells that highly express CD138 and are specialized in immunoglobulin production."
  },
  "Naive B": {
    "genes": [
      "IGHD",
      "IGHM",
      "CD24",
      "CD38",
      "FCER2",
      "CR2",
      "CD40",
      "ICOSL",
      "BCL6",
      "CXCR5",
      "IL4R",
      "CD86",
      "TNFRSF13C",
      "TNFRSF13B",
      "FCRL1",
      "FCRL2",
      "FCRL5",
      "CD79A",
      "CD79B",
      "MS4A1",
      "PAX5",
      "EBF1",
      "IRF8",
      "POU2AF1",
      "SPIB",
      "TCF4",
      "BCL11A",
      "CD19",
      "CD22",
      "CD72",
      "CD81",
      "CD84",
      "CD180",
      "CD27",
      "CD44",
      "CD62L",
      "CD73",
      "CD200",
      "CD307",
      "CD357",
      "CD358",
      "CD360",
      "CD361",
      "CD362",
      "CD363",
      "CD364",
      "CD365"
    ],
    "description": "Naive B cells that have not yet encountered antigen, expressing IgD and IgM but lacking CD27 and memory markers."
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
High expression of B cell marker genes (MS4A1, CD79A, BANK1, BLK) and immunoglobulins, along with surface proteins CD19, CD22, CD21, and CD27, indicate memory B cells.

Top 30 cell-specific genes by TF-IDF (weights by rarity across cells — highlights rare but highly expressed genes):
    1. IGKC        (0.01036)
    2. HLA-DRA     (0.00267)
    3. MS4A1       (0.00266)
    4. CD74        (0.00143)
    5. BANK1       (0.00140)
    6. IGHA1       (0.00136)
    7. HLA-DQA1    (0.00128)
    8. HLA-DRB1    (0.00118)
    9. HLA-DPB1    (0.00112)
   10. CD79A       (0.00108)
   11. HLA-DPA1    (0.00104)
   12. IGHE        (0.00098)
   13. LINC01781   (0.00082)
   14. HLA-DQB1    (0.00081)
   15. BLK         (0.00075)
   16. IGHA2       (0.00070)
   17. LTB         (0.00070)
   18. IGHG3       (0.00066)
   19. AIM2        (0.00063)
   20. SSPN        (0.00062)
   21. LINC00926   (0.00061)
   22. SPIB        (0.00058)
   23. HLA-DMA     (0.00055)
   24. TNFRSF13B   (0.00055)
   25. TCF4        (0.00055)
   26. HLA-DRB5    (0.00054)
   27. RALGPS2     (0.00054)
   28. CD79B       (0.00054)
   29. MEF2C       (0.00054)
   30. CPNE5       (0.00049)

Surface proteins (z-score vs. population):
    1. CD35             z=+4.64813
    2. CD73             z=+3.90991
    3. CD19             z=+3.65352
    4. CD22             z=+3.61087
    5. CD4-1            z=+3.10164
    6. CD48             z=+3.02112
    7. CD71             z=+2.49240
    8. CD45-2           z=+2.39245
    9. CD62P            z=+2.38433
   10. CD21             z=+2.33703
   11. Integrin-7       z=+2.31008
   12. CD8a             z=+2.21497
   13. CD18             z=+2.15414
   14. CD49d            z=+2.06599
   15. CD27             z=+2.05849

Pathway scores (LLM-defined gene programs scored against this cell; higher = more active program):
  Naive B                  : +1.14533
  Non-switched memory B    : +1.11889
  Switched memory B        : +1.00501
  Atypical memory B        : +0.91644
  Plasma cells             : -0.03874

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
B memory
High expression of B cell markers (MS4A1, CD79A, BANK1, BLK) and immunoglobulins, plus surface CD19, CD22, CD21, CD27 confirm B cell identity. Pathway scores for memory B subtypes are elevated, supporting memory B cell annotation. No monocyte markers (e.g., CD14, FCGR3A) are present.
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

Top genes (ranked by TF-IDF specificity):
    1. CST3 (0.00312)
    2. LYZ (0.00308)
    3. HLA-DRA (0.00301)
    4. FOS (0.00189)
    5. HLA-DRB5 (0.00181)
    6. HLA-DPA1 (0.00157)
    7. HLA-DRB1 (0.00151)
    8. CD74 (0.00147)
    9. AIF1 (0.00147)
   10. FCN1 (0.00134)
   11. HLA-DPB1 (0.00132)
   12. HLA-DQB1 (0.00125)
   13. TYROBP (0.00106)
   14. HLA-DQA1 (0.00105)
   15. LST1 (0.00087)
   16. MNDA (0.00087)
   17. TYMP (0.00087)
   18. FCER1G (0.00086)
   19. MS4A6A (0.00080)
   20. FGL2 (0.00078)

Top expressed surface proteins / ADT markers (ranked by count):
    1. CD62P (4.07846)
    2. CD4-1 (4.01436)
    3. CD41 (3.62269)
    4. CD31 (3.44134)
    5. CD93 (3.35531)
    6. CD48 (3.06236)
    7. CD35 (3.01361)
    8. CD18 (2.91109)
    9. CD45-2 (2.70463)
   10. CLEC2 (2.58048)
   11. CD11b-1 (2.48212)
   12. CD102 (2.39901)
   13. CD63 (2.37185)
   14. CLEC12A (2.31397)
   15. CD49d (2.15557)
   16. CD9 (2.06981)
   17. CD47 (2.03514)
   18. CD305 (2.01191)
   19. CD61 (1.99583)
   20. CD172a (1.98984)

Choose the cell type from the following list (output exactly one of these names in the first line):
CD16 Mono, B memory, CD14 Mono

Based on the expression profile above, which cell type is this? Respond with the chosen cell type name (from the list above) in the first line, then in the second line provide very brief explanation (<100 words).
```

### output

```text
CD14 Mono
The top genes (CST3, LYZ, HLA-DRA, FCN1, CD74) are classic CD14+ monocyte markers, and surface proteins (CD11b, CD18, CD4) further support monocyte identity. Platelet markers (CD41, CD62P) likely reflect monocyte-platelet aggregates common in PBMC.
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
The top genes (CST3, LYZ, HLA-DRA, FCN1, CD74) are classic CD14+ monocyte markers, and surface proteins (CD11b, CD18, CD4) further support monocyte identity. Platelet markers (CD41, CD62P) likely reflect monocyte-platelet aggregates common in PBMC.
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
  "Classical CD14++ Monocyte": {
    "genes": [
      "CD14",
      "LYZ",
      "S100A8",
      "S100A9",
      "FCN1",
      "CST3",
      "S100A12",
      "VCAN",
      "CTSS",
      "CD68",
      "CD33",
      "CSF1R",
      "CCL2",
      "CLEC7A",
      "TLR2",
      "TLR4",
      "IRF8",
      "MAFB",
      "CEBPB",
      "GATA2",
      "SPI1",
      "MNDA",
      "LILRB2",
      "LILRA5",
      "FPR1",
      "FPR2",
      "NLRP3",
      "IL1B",
      "TNF",
      "SERPINA1",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPB1",
      "HLA-DPA1",
      "CD74",
      "IFITM3",
      "IFITM2",
      "MX1",
      "ISG15",
      "OAS1",
      "OAS2",
      "OAS3",
      "IRF7",
      "STAT1",
      "STAT2",
      "IFI6",
      "IFIT1",
      "IFIT3",
      "RSAD2"
    ],
    "description": "Classical monocytes are CD14++CD16- cells that play a key role in phagocytosis, inflammatory responses, and tissue remodeling."
  },
  "Intermediate CD14+CD16+ Monocyte": {
    "genes": [
      "CD14",
      "FCGR3A",
      "FCGR3B",
      "CD16",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPB1",
      "HLA-DPA1",
      "CD74",
      "CD86",
      "CD80",
      "TLR4",
      "TLR2",
      "IL1B",
      "TNF",
      "IL6",
      "CCL3",
      "CCL4",
      "CCR2",
      "CX3CR1",
      "CXCL8",
      "CXCL10",
      "CXCL9",
      "CCL5",
      "SOD2",
      "NFKBIA",
      "NFKBIZ",
      "IER3",
      "JUN",
      "FOS",
      "PTGS2",
      "PLAUR",
      "SERPINE1",
      "TIMP1",
      "MMP9",
      "MMP14",
      "ADAM17",
      "LILRB2",
      "LILRA5",
      "LILRB1",
      "LILRA3",
      "LILRA6",
      "NLRP3",
      "CASP1",
      "PYCARD",
      "IL18",
      "IL10",
      "CCL22"
    ],
    "description": "Intermediate monocytes are CD14+CD16+ cells with high antigen-presenting capacity and a strong pro-inflammatory cytokine profile."
  },
  "Non-classical CD14lowCD16+ Monocyte": {
    "genes": [
      "FCGR3A",
      "CDKN1C",
      "LILRB2",
      "LILRB1",
      "LILRA5",
      "LILRA3",
      "LILRA6",
      "LILRB4",
      "LILRB5",
      "LILRA2",
      "LILRA4",
      "LILRA1",
      "LILRA8",
      "LILRB3",
      "LILRB1",
      "LILRB2",
      "CD16",
      "CD86",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPB1",
      "HLA-DPA1",
      "CD74",
      "CST3",
      "CSF1R",
      "CX3CR1",
      "CXCL16",
      "CCL3",
      "CCL4",
      "CCR5",
      "CCR2",
      "TLR7",
      "TLR8",
      "IRF4",
      "IRF8",
      "MAFB",
      "CEBPB",
      "SPI1",
      "ETS1",
      "FLI1",
      "MEF2C",
      "RUNX1",
      "GATA2",
      "MPO",
      "PRTN3",
      "AZU1",
      "ELANE",
      "CTSG",
      "RNASE2"
    ],
    "description": "Non-classical monocytes are CD14lowCD16+ cells that patrol the vasculature and are involved in wound healing and immune surveillance."
  },
  "CD1c+ Dendritic Cell": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "CD1E",
      "CD1D",
      "CD1B",
      "CD1A",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPB1",
      "HLA-DPA1",
      "HLA-DQA1",
      "HLA-DQB1",
      "HLA-DMA",
      "HLA-DMB",
      "HLA-DOA",
      "HLA-DOB",
      "CD74",
      "CD80",
      "CD86",
      "CD40",
      "CCR7",
      "CCL17",
      "CCL22",
      "CXCL16",
      "IL12B",
      "IL23A",
      "IL6",
      "TNF",
      "IRF4",
      "IRF8",
      "ZBTB46",
      "FLT3",
      "AXL",
      "SIGLEC6",
      "SIGLEC10",
      "CLEC4C",
      "CLEC4A",
      "CLEC7A",
      "CLEC12A",
      "LILRA4",
      "LILRB4",
      "LILRB2",
      "LILRA5",
      "TLR3",
      "TLR7",
      "TLR8",
      "TLR9"
    ],
    "description": "CD1c+ dendritic cells are a subset of conventional dendritic cells that are potent antigen-presenting cells and key regulators of adaptive immunity."
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

Stage-1 reasoning:
The top genes (CST3, LYZ, HLA-DRA, FCN1, CD74) are classic CD14+ monocyte markers, and surface proteins (CD11b, CD18, CD4) further support monocyte identity. Platelet markers (CD41, CD62P) likely reflect monocyte-platelet aggregates common in PBMC.

Top 30 cell-specific genes by TF-IDF (weights by rarity across cells — highlights rare but highly expressed genes):
    1. CST3        (0.00312)
    2. LYZ         (0.00308)
    3. HLA-DRA     (0.00301)
    4. FOS         (0.00189)
    5. HLA-DRB5    (0.00181)
    6. HLA-DPA1    (0.00157)
    7. HLA-DRB1    (0.00151)
    8. CD74        (0.00147)
    9. AIF1        (0.00147)
   10. FCN1        (0.00134)
   11. HLA-DPB1    (0.00132)
   12. HLA-DQB1    (0.00125)
   13. TYROBP      (0.00106)
   14. HLA-DQA1    (0.00105)
   15. LST1        (0.00087)
   16. MNDA        (0.00087)
   17. TYMP        (0.00087)
   18. FCER1G      (0.00086)
   19. MS4A6A      (0.00080)
   20. FGL2        (0.00078)
   21. SAT1        (0.00071)
   22. CTSS        (0.00071)
   23. HLA-DMA     (0.00068)
   24. PSAP        (0.00066)
   25. CYBB        (0.00064)
   26. CPVL        (0.00064)
   27. MARCKS      (0.00060)
   28. COTL1       (0.00058)
   29. IFITM3      (0.00057)
   30. CEBPD       (0.00055)

Surface proteins (z-score vs. population):
    1. CD62P            z=+4.07846
    2. CD4-1            z=+4.01436
    3. CD41             z=+3.62269
    4. CD31             z=+3.44134
    5. CD93             z=+3.35531
    6. CD48             z=+3.06236
    7. CD35             z=+3.01361
    8. CD18             z=+2.91109
    9. CD45-2           z=+2.70463
   10. CLEC2            z=+2.58048
   11. CD11b-1          z=+2.48212
   12. CD102            z=+2.39901
   13. CD63             z=+2.37185
   14. CLEC12A          z=+2.31397
   15. CD49d            z=+2.15557

Pathway scores (LLM-defined gene programs scored against this cell; higher = more active program):
  CD1c+ Dendritic Cell     : +0.57679
  Classical CD14++ Monocyte: +0.52396
  Non-classical CD14lowCD16+ Monocyte: +0.50225
  Intermediate CD14+CD16+ Monocyte: +0.25055

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD14 Mono
Top genes (CST3, LYZ, FCN1) and surface proteins (CD11b, CD18, CD4) are classic markers of CD14+ monocytes. Pathway scores favor Classical CD14++ Monocyte over other subtypes or B cells, confirming the stage-1 annotation. Platelet markers likely reflect monocyte-platelet aggregates.
```

