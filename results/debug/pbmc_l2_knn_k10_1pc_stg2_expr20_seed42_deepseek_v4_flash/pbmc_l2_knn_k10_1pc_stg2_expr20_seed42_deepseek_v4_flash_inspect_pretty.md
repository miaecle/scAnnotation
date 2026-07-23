# Inspect Traces

Total records: 9

## Record 1

- stage: stage1_annotation
- row_idx: 1
- cell_idx: 48
- cell_barcode: L1_AAAGAACCACCTCTAC
- true_label: B memory

### prompt

```text
Tissue context: PBMC

Top expressed genes (ranked by expression level):
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

The gene expression includes IGKC (immunoglobulin kappa constant) and high HLA class II (HLA-DRA, CD74, HLA-DPB1), characteristic of B cells. Surface markers show strong expression of CD19, CD22, and CD35, specific to B cells, along with CD27 and CD45RA, indicating a memory B cell phenotype.
```

## Record 2

- stage: stage1_annotation
- row_idx: 0
- cell_idx: 13748
- cell_barcode: L1_TTTGTTGCAGCGAGTA
- true_label: CD16 Mono

### prompt

```text
Tissue context: PBMC

Top expressed genes (ranked by expression level):
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
Gene expression (CST3, LYZ, S100 family) and surface markers (CD16, CD11b, CD18) indicate monocyte lineage; absence of CD14 and presence of CD16 suggest non-classical CD16+ monocytes.
```

## Record 3

- stage: stage1_annotation
- row_idx: 2
- cell_idx: 6148
- cell_barcode: L1_CTGAATGAGGGCGAAG
- true_label: CD14 Mono

### prompt

```text
Tissue context: PBMC

Top expressed genes (ranked by expression level):
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

## Record 4

- stage: stage2_program_query
- row_idx: 0
- cell_idx: 13748
- cell_barcode: L1_TTTGTTGCAGCGAGTA
- true_label: CD16 Mono
- stage1_label: CD16 Mono

### stage1_reasoning

```text
Gene expression (CST3, LYZ, S100 family) and surface markers (CD16, CD11b, CD18) indicate monocyte lineage; absence of CD14 and presence of CD16 suggest non-classical CD16+ monocytes.
```

### prompt_prefix

```text
This annotation may have minor inaccuracies, or may have been confused with a neighboring type.

Return a JSON object with gene programs for:
  1. The fine-grained subtypes of this cell type commonly found in PBMC.
  2. The most commonly confused neighboring cell types in PBMC — especially any
     types hinted at by the stage-1 reasoning above.

Each key is a subtype/cell-type name; each value contains:
  "genes": list anywhere from 20 to 50 genes most specifically UPREGULATED in that subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)
  "description": one-sentence biological description

Include 3-5 subtypes total. Focus on subtypes commonly found in PBMC.
Return only the JSON.
```

### prompt

```text
A single cell in PBMC was annotated in a first pass as: "CD16 Mono"

Stage-1 reasoning that led to this annotation:
Gene expression (CST3, LYZ, S100 family) and surface markers (CD16, CD11b, CD18) indicate monocyte lineage; absence of CD14 and presence of CD16 suggest non-classical CD16+ monocytes.

```

### full_prompt

```text
This annotation may have minor inaccuracies, or may have been confused with a neighboring type.

Return a JSON object with gene programs for:
  1. The fine-grained subtypes of this cell type commonly found in PBMC.
  2. The most commonly confused neighboring cell types in PBMC — especially any
     types hinted at by the stage-1 reasoning above.

Each key is a subtype/cell-type name; each value contains:
  "genes": list anywhere from 20 to 50 genes most specifically UPREGULATED in that subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)
  "description": one-sentence biological description

Include 3-5 subtypes total. Focus on subtypes commonly found in PBMC.
Return only the JSON.

A single cell in PBMC was annotated in a first pass as: "CD16 Mono"

Stage-1 reasoning that led to this annotation:
Gene expression (CST3, LYZ, S100 family) and surface markers (CD16, CD11b, CD18) indicate monocyte lineage; absence of CD14 and presence of CD16 suggest non-classical CD16+ monocytes.

```

### output

```text
{
  "Non-classical monocytes (CD16+)": {
    "genes": [
      "FCGR3A",
      "CMKLRI",
      "LST1",
      "AIF1",
      "MS4A7",
      "RHOC",
      "IFITM3",
      "CFH",
      "CKB",
      "CSF1R",
      "CX3CR1",
      "FCGR3B",
      "FGR",
      "FOLR3",
      "FTL",
      "HK3",
      "ITGAM",
      "LRRC25",
      "MNDA",
      "NCF1",
      "NCF2",
      "NLRP3",
      "PLBD1",
      "PSAP",
      "PTGS1",
      "RAB31",
      "RNASE2",
      "S100A8",
      "S100A9",
      "SERPINA1",
      "SLC11A1",
      "SLC31A2",
      "SPI1",
      "TALDO1",
      "TCIRG1",
      "TREM1",
      "TYROBP",
      "VNN2",
      "WARS"
    ],
    "description": "Non-classical CD16+ monocytes are patrolling monocytes that survey the endothelium and produce pro-inflammatory cytokines upon activation."
  },
  "Classical monocytes (CD14+)": {
    "genes": [
      "CD14",
      "VCAN",
      "S100A8",
      "S100A9",
      "LYZ",
      "CTSS",
      "FCN1",
      "LILRB2",
      "LILRB4",
      "CFD",
      "CST3",
      "FOLR1",
      "FOLR2",
      "HLA-DRB1",
      "HLA-DRB5",
      "ITGAX",
      "MNDA",
      "MPEG1",
      "NLRP3",
      "PLBD1",
      "PSAP",
      "RNASE2",
      "SERPINA1",
      "SLC11A1",
      "SLC31A2",
      "SPI1",
      "TALDO1",
      "TCIRG1",
      "TYROBP",
      "VNN2",
      "CTSD",
      "GPNMB",
      "IFITM2",
      "LGALS1",
      "LIPA",
      "MACROH2A1",
      "MCL1",
      "NDRG2",
      "NPC2",
      "RAB7A"
    ],
    "description": "Classical CD14+ monocytes are phagocytic cells that respond to pathogens and differentiate into macrophages or dendritic cells."
  },
  "Intermediate monocytes (CD14+CD16+)": {
    "genes": [
      "CD14",
      "FCGR3A",
      "HLA-DRB1",
      "HLA-DRB5",
      "CLEC5A",
      "CLEC7A",
      "CSF1R",
      "CX3CR1",
      "FCGR3B",
      "FGR",
      "FOLR3",
      "IFITM3",
      "ITGAM",
      "LILRB2",
      "LILRB4",
      "LRRC25",
      "LYZ",
      "MNDA",
      "MS4A7",
      "NCF1",
      "NCF2",
      "NLRP3",
      "PLBD1",
      "PSAP",
      "RAB31",
      "RHOC",
      "RNASE2",
      "S100A8",
      "S100A9",
      "SERPINA1",
      "SLC11A1",
      "SLC31A2",
      "SPI1",
      "TALDO1",
      "TCIRG1",
      "TREM1",
      "TYROBP",
      "VNN2",
      "WARS"
    ],
    "description": "Intermediate CD14+CD16+ monocytes are a transitional subset with high antigen-presenting capacity and pro-inflammatory cytokine production."
  },
  "NK cells": {
    "genes": [
      "NKG7",
      "GNLY",
      "GZMB",
      "PRF1",
      "KLRD1",
      "KLRF1",
      "KLRG1",
      "FCGR3A",
      "KIR2DL1",
      "KIR2DL2",
      "KIR2DL3",
      "KIR3DL1",
      "KIR3DL2",
      "NCR1",
      "NCR3",
      "CD247",
      "CD3E",
      "CD3D",
      "CD3G",
      "CD8A",
      "CD8B",
      "CD2",
      "CD7",
      "IL2RB",
      "IL2RG",
      "ITGAL",
      "ITGB2",
      "CCL4",
      "CCL5",
      "XCL1",
      "XCL2",
      "GZMA",
      "GZMH",
      "GZMK",
      "GZMM",
      "FASLG",
      "TNFSF10",
      "IFNG",
      "PRKCA",
      "SH2D1B",
      "ZAP70",
      "TYROBP",
      "KLRB1",
      "KLRK1"
    ],
    "description": "Natural killer cells are cytotoxic lymphocytes that provide innate immune responses to infected or transformed cells."
  },
  "Myeloid dendritic cells (mDCs)": {
    "genes": [
      "CLEC9A",
      "CLEC10A",
      "FCER1A",
      "CD1C",
      "CADM1",
      "FLT3",
      "ITGAX",
      "ITGAM",
      "CD11B",
      "CD33",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DQB1",
      "HLA-DPB1",
      "CD86",
      "CD80",
      "CCR7",
      "CXCL16",
      "LAMP3",
      "CD83",
      "LILRA4",
      "IL3RA",
      "BCL11A",
      "ZBTB46",
      "IRF8",
      "IRF4",
      "CSF1R",
      "CSF2RA",
      "CSF2RB",
      "TLR1",
      "TLR2",
      "TLR4",
      "TLR8",
      "MYD88",
      "TRAF1",
      "TRAF3",
      "NFKB1",
      "RELB",
      "STAT3",
      "STAT4",
      "JAK2",
      "TYK2",
      "MAPK14",
      "MAPK1",
      "PIK3CA"
    ],
    "description": "Myeloid dendritic cells are antigen-presenting cells that capture, process, and present antigens to T cells, initiating adaptive immune responses."
  }
}
```

## Record 5

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
Gene expression (CST3, LYZ, S100 family) and surface markers (CD16, CD11b, CD18) indicate monocyte lineage; absence of CD14 and presence of CD16 suggest non-classical CD16+ monocytes.

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
  Non-classical monocytes (CD16+): +0.858
  Intermediate monocytes (CD14+CD16+): +0.728
  Classical monocytes (CD14+): +0.562
  Myeloid dendritic cells (mDCs): +0.139
  NK cells                 : -0.476

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
High expression of monocyte/myeloid genes (CST3, LYZ, S100A4, AIF1, TYROBP) and surface markers (CD18, CD35, CD93) confirm monocyte lineage. Pathway scores highest for non-classical CD16+ monocytes (+0.858) over intermediate (+0.728) and classical (+0.562). Absence of CD14 in top markers and presence of CD41/62P (possible platelet aggregation) do not outweigh the strong non-classical monocyte gene program.
```

## Record 6

- stage: stage2_program_query
- row_idx: 1
- cell_idx: 48
- cell_barcode: L1_AAAGAACCACCTCTAC
- true_label: B memory
- stage1_label: B memory

### stage1_reasoning

```text
The gene expression includes IGKC (immunoglobulin kappa constant) and high HLA class II (HLA-DRA, CD74, HLA-DPB1), characteristic of B cells. Surface markers show strong expression of CD19, CD22, and CD35, specific to B cells, along with CD27 and CD45RA, indicating a memory B cell phenotype.
```

### prompt_prefix

```text
This annotation may have minor inaccuracies, or may have been confused with a neighboring type.

Return a JSON object with gene programs for:
  1. The fine-grained subtypes of this cell type commonly found in PBMC.
  2. The most commonly confused neighboring cell types in PBMC — especially any
     types hinted at by the stage-1 reasoning above.

Each key is a subtype/cell-type name; each value contains:
  "genes": list anywhere from 20 to 50 genes most specifically UPREGULATED in that subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)
  "description": one-sentence biological description

Include 3-5 subtypes total. Focus on subtypes commonly found in PBMC.
Return only the JSON.
```

### prompt

```text
A single cell in PBMC was annotated in a first pass as: "B memory"

Stage-1 reasoning that led to this annotation:
The gene expression includes IGKC (immunoglobulin kappa constant) and high HLA class II (HLA-DRA, CD74, HLA-DPB1), characteristic of B cells. Surface markers show strong expression of CD19, CD22, and CD35, specific to B cells, along with CD27 and CD45RA, indicating a memory B cell phenotype.

```

### full_prompt

```text
This annotation may have minor inaccuracies, or may have been confused with a neighboring type.

Return a JSON object with gene programs for:
  1. The fine-grained subtypes of this cell type commonly found in PBMC.
  2. The most commonly confused neighboring cell types in PBMC — especially any
     types hinted at by the stage-1 reasoning above.

Each key is a subtype/cell-type name; each value contains:
  "genes": list anywhere from 20 to 50 genes most specifically UPREGULATED in that subtype (HGNC symbols as they appear in RNA-seq count matrices, e.g. NKG7 not Nkg7)
  "description": one-sentence biological description

Include 3-5 subtypes total. Focus on subtypes commonly found in PBMC.
Return only the JSON.

A single cell in PBMC was annotated in a first pass as: "B memory"

Stage-1 reasoning that led to this annotation:
The gene expression includes IGKC (immunoglobulin kappa constant) and high HLA class II (HLA-DRA, CD74, HLA-DPB1), characteristic of B cells. Surface markers show strong expression of CD19, CD22, and CD35, specific to B cells, along with CD27 and CD45RA, indicating a memory B cell phenotype.

```

### output

```text
{
  "Switched memory B cell": {
    "genes": [
      "CD27",
      "MS4A1",
      "HLA-DRA",
      "HLA-DPB1",
      "CD74",
      "IGKC",
      "IGHA1",
      "IGHG1",
      "JCHAIN",
      "CD79A",
      "CD79B",
      "PAX5",
      "EBF1",
      "BCL6",
      "CD22",
      "CD19",
      "CR2",
      "TNFRSF13B",
      "TNFRSF13C",
      "FCGR2B",
      "IRF4",
      "CD81",
      "CD72",
      "CD37",
      "BANK1",
      "BLNK",
      "SYK",
      "LYN",
      "DAPP1",
      "SOX5"
    ],
    "description": "Memory B cell that has undergone class switch recombination, expressing surface IgG, IgA, or IgE, and CD27."
  },
  "Unswitched memory B cell": {
    "genes": [
      "CD27",
      "IGHD",
      "IGHM",
      "MS4A1",
      "HLA-DRA",
      "CD74",
      "TCL1A",
      "FCER2",
      "CR2",
      "CD22",
      "CD19",
      "PAX5",
      "EBF1",
      "BANK1",
      "BLNK",
      "SYK",
      "LYN",
      "DAPP1",
      "SOX5",
      "CD72",
      "CD37",
      "IRF4",
      "TNFRSF13B",
      "TNFRSF13C",
      "FCGR2B",
      "CD81",
      "CD79A",
      "CD79B",
      "JCHAIN",
      "IGKC"
    ],
    "description": "Memory B cell retaining IgD and IgM, often associated with marginal zone, expressing CD27."
  },
  "Double-negative memory B cell": {
    "genes": [
      "ITGAX",
      "TBX21",
      "CXCR3",
      "CD38",
      "CD86",
      "HLA-DRA",
      "CD74",
      "MS4A1",
      "CD19",
      "CD22",
      "PAX5",
      "IRF4",
      "PRDM1",
      "TNFRSF13B",
      "FCGR2B",
      "BANK1",
      "BLNK",
      "SYK",
      "LYN",
      "DAPP1",
      "SOX5",
      "CD79A",
      "CD79B",
      "JCHAIN",
      "IGKC",
      "IGHG1",
      "IGHA1",
      "TNFRSF17",
      "MZB1",
      "XBP1"
    ],
    "description": "Memory B cell lacking CD27 and surface IgD, often expanded in autoimmunity and aging, expressing CD11c and T-bet."
  },
  "Plasmablast/plasma cell": {
    "genes": [
      "MZB1",
      "XBP1",
      "SDC1",
      "PRDM1",
      "IRF4",
      "TNFRSF17",
      "JCHAIN",
      "IGHA1",
      "IGHG1",
      "IGKC",
      "IGLV",
      "CD38",
      "CD27",
      "SLAMF7",
      "FKBP11",
      "TXNDC5",
      "SSR4",
      "PPIB",
      "SEC61B",
      "PDIA6",
      "HSPA5",
      "CALR",
      "PDIA4",
      "PDIA3",
      "P4HB",
      "ERP29",
      "HYOU1",
      "SHCBP1",
      "EMP3",
      "FAM46C"
    ],
    "description": "Antibody-secreting cell, characterized by high expression of MZB1, XBP1, SDC1, and low CD20."
  },
  "CD8+ TEMRA cell": {
    "genes": [
      "CD3E",
      "CD8A",
      "CD8B",
      "NKG7",
      "GZMB",
      "GZMK",
      "GNLY",
      "PRF1",
      "KLRD1",
      "KLRG1",
      "PTPRC",
      "EOMES",
      "TBX21",
      "ZEB2",
      "CCL5",
      "CST7",
      "FGFBP2",
      "FCGR3A",
      "LILRB1",
      "CD244",
      "GZMH",
      "KIR2DL3",
      "KIR3DL1",
      "KIR2DL1",
      "KIR2DL4",
      "KIR3DL2",
      "CD247",
      "CD3G",
      "CD3D",
      "TRAT1"
    ],
    "description": "Terminal effector memory T cell re-expressing CD45RA, with low CD27 and strong cytotoxic effector molecules."
  }
}
```

## Record 7

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
The gene expression includes IGKC (immunoglobulin kappa constant) and high HLA class II (HLA-DRA, CD74, HLA-DPB1), characteristic of B cells. Surface markers show strong expression of CD19, CD22, and CD35, specific to B cells, along with CD27 and CD45RA, indicating a memory B cell phenotype.

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
  Switched memory B cell   : +1.609
  Unswitched memory B cell : +1.358
  Double-negative memory B cell: +1.259
  Plasmablast/plasma cell  : +0.381
  CD8+ TEMRA cell          : -0.539

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
B memory
High expression of IGKC, HLA class II, MS4A1, and surface markers CD19, CD22, CD35, CD27 confirm B cell identity. Pathway scores highest for switched and unswitched memory B cell programs, consistent with memory B cell phenotype. No monocyte-specific markers (e.g., CD14) are elevated.
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
  2. The most commonly confused neighboring cell types in PBMC — especially any
     types hinted at by the stage-1 reasoning above.

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
  2. The most commonly confused neighboring cell types in PBMC — especially any
     types hinted at by the stage-1 reasoning above.

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
  "Classical Monocytes": {
    "genes": [
      "CD14",
      "LYZ",
      "S100A8",
      "S100A9",
      "FCN1",
      "CSTA",
      "CD163",
      "VCAN",
      "MNDA",
      "LST1",
      "AIF1",
      "PSAP",
      "CTSS",
      "CTSD",
      "FTL",
      "FTH1",
      "S100A11",
      "S100A12",
      "S100A6",
      "S100A4",
      "S100A10",
      "S100A16",
      "CD68",
      "CD33",
      "ITGAM",
      "LILRB2",
      "CLEC7A",
      "CSF1R",
      "CCR2",
      "CX3CR1"
    ],
    "description": "CD14++CD16- classical monocytes with high phagocytic activity and expression of antimicrobial genes."
  },
  "Intermediate Monocytes": {
    "genes": [
      "FCGR3A",
      "CD14",
      "CD86",
      "CD40",
      "HLA-DRA",
      "HLA-DRB1",
      "CD74",
      "CLEC4D",
      "CLEC4E",
      "IL1B",
      "IL6",
      "TNF",
      "CCL3",
      "CCL4",
      "CXCL8",
      "FCGR1A",
      "MSR1",
      "CCR5",
      "CCR2",
      "TREM2",
      "CD80",
      "CD83",
      "CDKN1C",
      "APOBEC3A",
      "PTPN6"
    ],
    "description": "CD14++CD16+ intermediate monocytes with pro-inflammatory properties and antigen presentation capacity."
  },
  "Non-classical Monocytes": {
    "genes": [
      "FCGR3A",
      "CX3CR1",
      "MS4A7",
      "LILRA5",
      "LILRB1",
      "LILRB2",
      "LILRB3",
      "LILRB4",
      "LILRA1",
      "LILRA2",
      "LILRA3",
      "LILRA6",
      "LILRB5",
      "KIR2DL4",
      "KIR3DL2",
      "KIR3DL1",
      "KIR2DS2",
      "CDKN1C",
      "APOBEC3A",
      "PTPN6",
      "LSP1",
      "SYNGR2",
      "SIGLEC10",
      "SIGLEC7",
      "SIGLEC5"
    ],
    "description": "CD14+CD16++ non-classical monocytes patrolling endothelium and involved in viral sensing."
  },
  "Myeloid Dendritic Cells": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "CD1E",
      "CD1A",
      "CD1D",
      "CD1B",
      "FCGR2B",
      "ITGAX",
      "CD80",
      "CD86",
      "CD83",
      "HLA-DRA",
      "HLA-DPB1",
      "HLA-DQB1",
      "IRF4",
      "IRF8",
      "BATF3",
      "CLEC4A",
      "CD302",
      "LILRA1",
      "LILRB2",
      "FCGR2A",
      "CCR7",
      "LAMP3"
    ],
    "description": "Professional antigen-presenting cells expressing CD1c and involved in T cell activation."
  },
  "Plasmacytoid Dendritic Cells": {
    "genes": [
      "IL3RA",
      "CLEC4C",
      "LILRA4",
      "TCF4",
      "IRF7",
      "IRF8",
      "PACSIN2",
      "PLD4",
      "SERPINF1",
      "LAMP5",
      "TLR7",
      "TLR9",
      "MYD88",
      "CD4",
      "CD44",
      "CD123",
      "JCHAIN",
      "MZB1",
      "DERL3",
      "BCL2A1",
      "BCL2",
      "BCL2L1",
      "LTB",
      "LTA",
      "TNFRSF17"
    ],
    "description": "Interferon-producing dendritic cells expressing CD303 and CD304."
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
  Non-classical Monocytes  : +0.569
  Classical Monocytes      : +0.558
  Myeloid Dendritic Cells  : +0.484
  Intermediate Monocytes   : +0.167
  Plasmacytoid Dendritic Cells: +0.082

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
Top genes (LYZ, CD74, CST3, AIF1) confirm a monocyte identity. Surface protein profile shows platelet markers (CD41, CD62P, CLEC2) often associated with monocyte-platelet aggregates, which are more common in CD16+ (non-classical) monocytes. Pathway scores also favor non-classical over classical monocytes (+0.569 vs +0.558). Thus, the stage-1 CD14 Mono label should be corrected to CD16 Mono.
```

