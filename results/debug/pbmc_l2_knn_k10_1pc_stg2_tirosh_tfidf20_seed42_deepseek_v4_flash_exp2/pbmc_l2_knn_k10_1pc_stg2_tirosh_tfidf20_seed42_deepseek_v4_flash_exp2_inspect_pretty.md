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

Top expressed genes (ranked by expression level):
    1. CST3 (0.003)
    2. LST1 (0.003)
    3. AIF1 (0.003)
    4. FCGR3A (0.002)
    5. CDKN1C (0.002)
    6. IFITM3 (0.002)
    7. FCN1 (0.002)
    8. TYROBP (0.002)
    9. FCER1G (0.001)
   10. CFD (0.001)
   11. HLA-DRA (0.001)
   12. MS4A7 (0.001)
   13. HLA-DRB1 (0.001)
   14. HLA-DPA1 (0.001)
   15. COTL1 (0.001)
   16. CTSS (0.001)
   17. S100A11 (0.001)
   18. TYMP (0.001)
   19. SAT1 (0.001)
   20. MNDA (0.001)

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

The gene expression profile (e.g., FCGR3A, FCN1, CST3, AIF1, HLA-DRA) and surface proteins (CD16, CD11b, CD4) indicate a monocyte, with high FCGR3A and absence of CD14 suggesting CD16+ non-classical monocytes. Platelet markers (CD41, CD62P) likely reflect platelet aggregates common in PBMC. B cell markers are absent, excluding B memory.
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
The gene expression profile (e.g., FCGR3A, FCN1, CST3, AIF1, HLA-DRA) and surface proteins (CD16, CD11b, CD4) indicate a monocyte, with high FCGR3A and absence of CD14 suggesting CD16+ non-classical monocytes. Platelet markers (CD41, CD62P) likely reflect platelet aggregates common in PBMC. B cell markers are absent, excluding B memory.
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
The gene expression profile (e.g., FCGR3A, FCN1, CST3, AIF1, HLA-DRA) and surface proteins (CD16, CD11b, CD4) indicate a monocyte, with high FCGR3A and absence of CD14 suggesting CD16+ non-classical monocytes. Platelet markers (CD41, CD62P) likely reflect platelet aggregates common in PBMC. B cell markers are absent, excluding B memory.

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
The gene expression profile (e.g., FCGR3A, FCN1, CST3, AIF1, HLA-DRA) and surface proteins (CD16, CD11b, CD4) indicate a monocyte, with high FCGR3A and absence of CD14 suggesting CD16+ non-classical monocytes. Platelet markers (CD41, CD62P) likely reflect platelet aggregates common in PBMC. B cell markers are absent, excluding B memory.

```

### output

```text
{
  "CD16+ Monocyte (Non-classical)": {
    "genes": [
      "FCGR3A",
      "MS4A7",
      "LST1",
      "CX3CR1",
      "LILRA2",
      "CSF1R",
      "LRRC25",
      "HES4",
      "RHOC",
      "TBCC",
      "NCF1",
      "CLEC4E",
      "SIGLEC10",
      "FGR",
      "MYO1F",
      "FCGR2A",
      "IFITM3",
      "IFITM2",
      "S100A12",
      "S100A8",
      "S100A9",
      "LYZ",
      "VCAN",
      "FOS",
      "JUNB",
      "EGR1",
      "NR4A1",
      "NR4A2",
      "TXN",
      "TXNIP",
      "PFN1",
      "ACTB",
      "GAPDH",
      "RPLP0",
      "RPL13A",
      "RPS18",
      "RPS27A",
      "RPL32",
      "RPL27",
      "RPS3",
      "RPS8",
      "RPL41",
      "RPS15A",
      "RPL17"
    ],
    "description": "Non-classical monocytes expressing CD16 (FCGR3A) and patrolling chemokine receptor CX3CR1, involved in vascular surveillance and inflammation."
  },
  "Classical Monocyte (CD14+)": {
    "genes": [
      "CD14",
      "LYZ",
      "S100A8",
      "S100A9",
      "FCN1",
      "CTSS",
      "CST3",
      "PSAP",
      "LGALS1",
      "LGALS3",
      "S100A11",
      "S100A6",
      "S100A4",
      "NPC2",
      "FTL",
      "FTH1",
      "TIMP1",
      "MARCKS",
      "FOS",
      "JUNB",
      "EGR1",
      "NR4A1",
      "NR4A2",
      "TXN",
      "TXNIP",
      "PFN1",
      "ACTB",
      "GAPDH",
      "RPLP0",
      "RPL13A",
      "RPS18",
      "RPS27A",
      "RPL32",
      "RPL27",
      "RPS3",
      "RPS8",
      "RPL41",
      "RPS15A",
      "RPL17"
    ],
    "description": "Classical monocytes with high CD14 expression, strong phagocytic activity, and production of pro-inflammatory cytokines like IL-6 and TNF-α."
  },
  "NK Cell": {
    "genes": [
      "NKG7",
      "GNLY",
      "PRF1",
      "GZMB",
      "GZMK",
      "GZMH",
      "KLRD1",
      "KLRB1",
      "KLRK1",
      "KLRC1",
      "KLRC2",
      "KLRF1",
      "CD247",
      "CD3E",
      "CD3D",
      "CD3G",
      "CD2",
      "CD7",
      "IL2RB",
      "IL2RG",
      "FCGR3A",
      "FGFBP2",
      "SPON2",
      "CCL3",
      "CCL4",
      "XCL1",
      "XCL2",
      "IFNG",
      "PRDM1",
      "ZEB2",
      "TBX21",
      "EOMES",
      "ID2",
      "STAT4",
      "IL12RB2",
      "IL18RAP",
      "IL18R1",
      "KIR2DL1",
      "KIR2DL3",
      "KIR3DL1",
      "LILRB1",
      "LILRB2",
      "HLA-C",
      "HLA-E",
      "HLA-G"
    ],
    "description": "Natural killer cells expressing NKG7, GNLY, PRF1, and GZMB, with cytotoxic function and production of interferon-gamma."
  },
  "Myeloid Dendritic Cell (cDC)": {
    "genes": [
      "FCER1A",
      "CLEC10A",
      "CD1C",
      "CD1E",
      "CD1A",
      "CD1B",
      "FCGR2B",
      "FSCN1",
      "CCL22",
      "CCL17",
      "CCR7",
      "LAMP3",
      "CD40",
      "CD80",
      "CD86",
      "ICOSLG",
      "PDCD1LG2",
      "CD274",
      "CD83",
      "HLA-DRA",
      "HLA-DPB1",
      "HLA-DPA1",
      "HLA-DQA1",
      "HLA-DQB1",
      "HLA-DRB1",
      "HLA-DRB5",
      "CIITA",
      "CD74",
      "IRF4",
      "IRF8",
      "ZBTB46",
      "FLT3",
      "CSF1R",
      "AXL",
      "SIGLEC6",
      "SIGLEC10",
      "CD33",
      "CD14",
      "LYZ",
      "CTSS",
      "CST3",
      "PSAP",
      "NPC2",
      "LGALS3",
      "LGALS1",
      "FTL",
      "FTH1"
    ],
    "description": "Conventional myeloid dendritic cells expressing FCER1A, CLEC10A, and CD1C, specialized in antigen presentation and T-cell activation."
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
The gene expression profile (e.g., FCGR3A, FCN1, CST3, AIF1, HLA-DRA) and surface proteins (CD16, CD11b, CD4) indicate a monocyte, with high FCGR3A and absence of CD14 suggesting CD16+ non-classical monocytes. Platelet markers (CD41, CD62P) likely reflect platelet aggregates common in PBMC. B cell markers are absent, excluding B memory.

Top 30 cell-specific genes by TF-IDF (weights by rarity across cells — highlights rare but highly expressed genes):
    1. CST3
    2. LST1
    3. AIF1
    4. FCGR3A
    5. CDKN1C
    6. IFITM3
    7. FCN1
    8. TYROBP
    9. FCER1G
   10. CFD
   11. HLA-DRA
   12. MS4A7
   13. HLA-DRB1
   14. HLA-DPA1
   15. COTL1
   16. CTSS
   17. S100A11
   18. TYMP
   19. SAT1
   20. MNDA
   21. PSAP
   22. TIMP1
   23. LYZ
   24. SERPINA1
   25. IFI30
   26. LGALS1
   27. CYBB
   28. FOS
   29. HLA-DRB5
   30. MARCKS

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
  CD16+ Monocyte (Non-classical): +0.843
  Classical Monocyte (CD14+): +0.714
  Myeloid Dendritic Cell (cDC): +0.419
  NK Cell                  : -0.409

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
Gene expression (FCGR3A, FCN1, CST3, HLA-DRA) and pathway scores favor CD16+ non-classical monocytes. High platelet markers (CD41, CD62P) reflect common aggregates in PBMC, not a different lineage. Absence of CD14 and B cell markers excludes CD14 Mono and B memory.
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

Top expressed genes (ranked by expression level):
    1. IGKC (0.010)
    2. HLA-DRA (0.003)
    3. MS4A1 (0.003)
    4. CD74 (0.001)
    5. BANK1 (0.001)
    6. IGHA1 (0.001)
    7. HLA-DQA1 (0.001)
    8. HLA-DRB1 (0.001)
    9. HLA-DPB1 (0.001)
   10. CD79A (0.001)
   11. HLA-DPA1 (0.001)
   12. IGHE (0.001)
   13. LINC01781 (0.001)
   14. HLA-DQB1 (0.001)
   15. BLK (0.001)
   16. IGHA2 (0.001)
   17. LTB (0.001)
   18. IGHG3 (0.001)
   19. AIM2 (0.001)
   20. SSPN (0.001)

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

The expression of B-cell specific markers (MS4A1, CD79A, BANK1) and immunoglobulin genes (IGKC, IGHA1, IGHE, IGHG3) along with surface proteins CD19, CD22, CD21, and CD27 indicate a memory B cell, not a monocyte.
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
The expression of B-cell specific markers (MS4A1, CD79A, BANK1) and immunoglobulin genes (IGKC, IGHA1, IGHE, IGHG3) along with surface proteins CD19, CD22, CD21, and CD27 indicate a memory B cell, not a monocyte.
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
The expression of B-cell specific markers (MS4A1, CD79A, BANK1) and immunoglobulin genes (IGKC, IGHA1, IGHE, IGHG3) along with surface proteins CD19, CD22, CD21, and CD27 indicate a memory B cell, not a monocyte.

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
The expression of B-cell specific markers (MS4A1, CD79A, BANK1) and immunoglobulin genes (IGKC, IGHA1, IGHE, IGHG3) along with surface proteins CD19, CD22, CD21, and CD27 indicate a memory B cell, not a monocyte.

```

### output

```text
{
  "B memory (resting)": {
    "genes": [
      "MS4A1",
      "CD79A",
      "CD79B",
      "CD19",
      "CXCR5",
      "CD27",
      "CD40",
      "BACH2",
      "PAX5",
      "EBF1",
      "BCL6",
      "AICDA",
      "ICOSL",
      "CD83",
      "HLA-DRA",
      "HLA-DRB1",
      "CD74",
      "B2M",
      "CD37",
      "CD22",
      "FCGR2B",
      "IL4R",
      "TNFRSF13C",
      "TNFRSF13B",
      "CR2",
      "FCMR",
      "BTLA",
      "TCL1A",
      "POU2F2",
      "IRF8",
      "SPIB",
      "POU2AF1",
      "MAF",
      "MYB",
      "BCL11A",
      "MEF2C",
      "ETS1",
      "CREBBP",
      "EP300",
      "HDAC7"
    ],
    "description": "Resting memory B cells expressing CD27 and BCL6, maintaining quiescence with low proliferation markers."
  },
  "B memory (activated)": {
    "genes": [
      "MS4A1",
      "CD79A",
      "CD79B",
      "CD19",
      "CD27",
      "CD38",
      "CD69",
      "CD86",
      "CD80",
      "MKI67",
      "PCNA",
      "TOP2A",
      "BIRC5",
      "AURKB",
      "CCNB1",
      "CDK1",
      "MYC",
      "IRF4",
      "XBP1",
      "PRDM1",
      "SLAMF7",
      "CD138",
      "JCHAIN",
      "IGHA1",
      "IGHG1",
      "IGHM",
      "IGHD",
      "IGKC",
      "IGLC1",
      "HLA-DRA",
      "HLA-DRB1",
      "CD74",
      "B2M",
      "CD40",
      "CD83",
      "IL4R",
      "TNFRSF13C",
      "FAS",
      "ICOSL",
      "POU2AF1"
    ],
    "description": "Activated memory B cells undergoing proliferation and differentiation, marked by CD38, CD69, and cell cycle genes."
  },
  "Plasma cell": {
    "genes": [
      "SDC1",
      "XBP1",
      "PRDM1",
      "IRF4",
      "JCHAIN",
      "MZB1",
      "SLAMF7",
      "CD38",
      "CD138",
      "TNFRSF17",
      "IGHA1",
      "IGHG1",
      "IGHM",
      "IGHD",
      "IGKC",
      "IGLC1",
      "IGHV",
      "IGKV",
      "IGLV",
      "HSP90B1",
      "HSPA5",
      "PDIA4",
      "PDIA6",
      "PDIA3",
      "ERP29",
      "ERP44",
      "CALR",
      "CANX",
      "FKBP11",
      "SEC61A1",
      "SEC61B",
      "SRPRB",
      "SSR1",
      "SSR2",
      "SSR3",
      "SSR4",
      "TRAM1",
      "TRAM2",
      "STT3A",
      "STT3B"
    ],
    "description": "Antibody-secreting plasma cells with high expression of immunoglobulin chains and endoplasmic reticulum stress response genes."
  },
  "Naive B cell": {
    "genes": [
      "MS4A1",
      "CD79A",
      "CD79B",
      "CD19",
      "CD27",
      "CD38",
      "IGHD",
      "IGHM",
      "IGHD",
      "CD5",
      "CD21",
      "CD22",
      "CD23",
      "CD24",
      "CD40",
      "CD72",
      "CR2",
      "FCER2",
      "IL4R",
      "BACH2",
      "PAX5",
      "EBF1",
      "BCL6",
      "TCL1A",
      "POU2F2",
      "IRF8",
      "SPIB",
      "POU2AF1",
      "MAF",
      "MYB",
      "BCL11A",
      "MEF2C",
      "ETS1",
      "CREBBP",
      "EP300",
      "HDAC7",
      "HLA-DRA",
      "HLA-DRB1",
      "CD74",
      "B2M"
    ],
    "description": "Naive B cells expressing IgD and CD27-negative, with CD5 typically low in PBMC but included as a marker."
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
The expression of B-cell specific markers (MS4A1, CD79A, BANK1) and immunoglobulin genes (IGKC, IGHA1, IGHE, IGHG3) along with surface proteins CD19, CD22, CD21, and CD27 indicate a memory B cell, not a monocyte.

Top 30 cell-specific genes by TF-IDF (weights by rarity across cells — highlights rare but highly expressed genes):
    1. IGKC
    2. HLA-DRA
    3. MS4A1
    4. CD74
    5. BANK1
    6. IGHA1
    7. HLA-DQA1
    8. HLA-DRB1
    9. HLA-DPB1
   10. CD79A
   11. HLA-DPA1
   12. IGHE
   13. LINC01781
   14. HLA-DQB1
   15. BLK
   16. IGHA2
   17. LTB
   18. IGHG3
   19. AIM2
   20. SSPN
   21. LINC00926
   22. SPIB
   23. HLA-DMA
   24. TNFRSF13B
   25. TCF4
   26. HLA-DRB5
   27. RALGPS2
   28. CD79B
   29. MEF2C
   30. CPNE5

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
  B memory (resting)       : +1.185
  Naive B cell             : +0.888
  B memory (activated)     : +0.822
  Plasma cell              : +0.201

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
B memory
Strong B cell markers (MS4A1, CD79A, BANK1, immunoglobulins) and surface proteins CD19, CD21, CD22, CD27, along with top pathway score for B memory (resting), confirm memory B cell, not monocytes.
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

Top expressed genes (ranked by expression level):
    1. CST3 (0.003)
    2. LYZ (0.003)
    3. HLA-DRA (0.003)
    4. FOS (0.002)
    5. HLA-DRB5 (0.002)
    6. HLA-DPA1 (0.002)
    7. HLA-DRB1 (0.002)
    8. CD74 (0.001)
    9. AIF1 (0.001)
   10. FCN1 (0.001)
   11. HLA-DPB1 (0.001)
   12. HLA-DQB1 (0.001)
   13. TYROBP (0.001)
   14. HLA-DQA1 (0.001)
   15. LST1 (0.001)
   16. MNDA (0.001)
   17. TYMP (0.001)
   18. FCER1G (0.001)
   19. MS4A6A (0.001)
   20. FGL2 (0.001)

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

The top expressed genes (LYZ, CST3, FCN1, CD74, AIF1) and surface proteins (CD11b, CD18, CD31, CD93, CD48) are highly characteristic of classical CD14+ monocytes. While ADT markers include platelet-associated proteins (CD41, CD61, CD62P) suggesting possible platelet binding, the overall profile lacks B cell markers (e.g., CD19) and CD16 (FCGR3A), thus aligning with CD14 Mono.
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
The top expressed genes (LYZ, CST3, FCN1, CD74, AIF1) and surface proteins (CD11b, CD18, CD31, CD93, CD48) are highly characteristic of classical CD14+ monocytes. While ADT markers include platelet-associated proteins (CD41, CD61, CD62P) suggesting possible platelet binding, the overall profile lacks B cell markers (e.g., CD19) and CD16 (FCGR3A), thus aligning with CD14 Mono.
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

Stage-1 reasoning that led to this annotation:
The top expressed genes (LYZ, CST3, FCN1, CD74, AIF1) and surface proteins (CD11b, CD18, CD31, CD93, CD48) are highly characteristic of classical CD14+ monocytes. While ADT markers include platelet-associated proteins (CD41, CD61, CD62P) suggesting possible platelet binding, the overall profile lacks B cell markers (e.g., CD19) and CD16 (FCGR3A), thus aligning with CD14 Mono.

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

Stage-1 reasoning that led to this annotation:
The top expressed genes (LYZ, CST3, FCN1, CD74, AIF1) and surface proteins (CD11b, CD18, CD31, CD93, CD48) are highly characteristic of classical CD14+ monocytes. While ADT markers include platelet-associated proteins (CD41, CD61, CD62P) suggesting possible platelet binding, the overall profile lacks B cell markers (e.g., CD19) and CD16 (FCGR3A), thus aligning with CD14 Mono.

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
      "CST3",
      "CTSS",
      "PSAP",
      "CTSD",
      "NPC2",
      "LGALS3",
      "GRN",
      "RNASE1",
      "SERPINA1",
      "FCGR2A",
      "CSF1R",
      "CD33",
      "CD68",
      "ITGAM",
      "CLEC7A",
      "CLEC4E",
      "TLR2",
      "TLR4",
      "MYD88",
      "IRAK1",
      "TNF",
      "IL1B",
      "IL6",
      "CCL2",
      "CCL3",
      "CCL4",
      "CXCL8",
      "CXCL2",
      "CXCL3",
      "SOD2",
      "HSPA1A",
      "HSPA1B",
      "HSP90AA1",
      "HSP90AB1",
      "NFKB1",
      "NFKB2",
      "RELA",
      "JUN",
      "FOS",
      "MAPK1",
      "MAPK3",
      "STAT3",
      "STAT1"
    ],
    "description": "Classical CD14++CD16- monocytes are the most abundant monocyte subset in PBMC, expressing high levels of CD14 and low CD16, and are involved in phagocytosis, antigen presentation, and inflammatory responses."
  },
  "Intermediate Monocytes": {
    "genes": [
      "CD14",
      "FCGR3A",
      "CD163",
      "CD86",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DQA1",
      "HLA-DQB1",
      "HLA-DPA1",
      "HLA-DPB1",
      "CD74",
      "CIITA",
      "CCR2",
      "CX3CR1",
      "TLR7",
      "TLR8",
      "TNF",
      "IL1B",
      "IL6",
      "CCL3",
      "CCL4",
      "CCL5",
      "CXCL9",
      "CXCL10",
      "CXCL11",
      "STAT1",
      "STAT2",
      "IRF1",
      "IRF8",
      "IFI6",
      "IFIT1",
      "IFIT3",
      "MX1",
      "OAS1",
      "OAS2",
      "OAS3",
      "ISG15",
      "USP18",
      "LY6E",
      "SIGLEC1",
      "CD169",
      "CD163",
      "FCGR2A",
      "FCGR2B",
      "FCGR3A"
    ],
    "description": "Intermediate CD14++CD16+ monocytes express both CD14 and CD16, and are pro-inflammatory with higher antigen-presenting capacity than classical monocytes."
  },
  "Non-classical Monocytes": {
    "genes": [
      "FCGR3A",
      "MS4A7",
      "CDKN1C",
      "NR4A1",
      "NR4A2",
      "NR4A3",
      "KLF2",
      "KLF4",
      "KLF7",
      "CCL3L1",
      "CCL4L1",
      "CXCL16",
      "SLCO2B1",
      "SIGLEC10",
      "LILRB2",
      "LILRB4",
      "FCGR2A",
      "FCGR2C",
      "FCGR3B",
      "TLR1",
      "TLR6",
      "TLR10",
      "IL10",
      "TGFB1",
      "CCL2",
      "CCL7",
      "CCL8",
      "CCL13",
      "CXCL5",
      "CXCL6",
      "CXCL12",
      "CXCR4",
      "ITGAL",
      "ITGB2",
      "ITGAM",
      "ITGAX",
      "FCER1G",
      "LST1",
      "AIF1",
      "SAT1",
      "TFRC",
      "SCARB2",
      "CD83",
      "CD86",
      "HLA-DRA",
      "HLA-DRB1"
    ],
    "description": "Non-classical CD14+CD16++ monocytes patrol the vasculature, scan for damage, and secrete anti-inflammatory cytokines."
  },
  "Myeloid Dendritic Cells": {
    "genes": [
      "FCER1A",
      "CLEC10A",
      "CD1C",
      "CD1A",
      "CD1B",
      "CD1D",
      "CD1E",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DQA1",
      "HLA-DQB1",
      "HLA-DPA1",
      "HLA-DPB1",
      "CD74",
      "CIITA",
      "IRF8",
      "IRF4",
      "ZBTB46",
      "CLEC4A",
      "CLEC6A",
      "CLEC7A",
      "CD209",
      "LAMP3",
      "CCL17",
      "CCL22",
      "IL12B",
      "IL23A",
      "TNF",
      "CD40",
      "CD80",
      "CD86",
      "ICOSLG",
      "PDL1",
      "CD83",
      "IDO1",
      "IDO2",
      "ARG2",
      "S100A9",
      "S100A8",
      "CD14",
      "CD16",
      "CD11C",
      "ITGAX",
      "CSF1R",
      "FLT3",
      "FLT3LG"
    ],
    "description": "Myeloid dendritic cells (cDC2) are professional antigen-presenting cells that can be confused with monocytes due to shared CD11c and CD14 expression, but they uniquely express CLEC10A and CD1c."
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
The top expressed genes (LYZ, CST3, FCN1, CD74, AIF1) and surface proteins (CD11b, CD18, CD31, CD93, CD48) are highly characteristic of classical CD14+ monocytes. While ADT markers include platelet-associated proteins (CD41, CD61, CD62P) suggesting possible platelet binding, the overall profile lacks B cell markers (e.g., CD19) and CD16 (FCGR3A), thus aligning with CD14 Mono.

Top 30 cell-specific genes by TF-IDF (weights by rarity across cells — highlights rare but highly expressed genes):
    1. CST3
    2. LYZ
    3. HLA-DRA
    4. FOS
    5. HLA-DRB5
    6. HLA-DPA1
    7. HLA-DRB1
    8. CD74
    9. AIF1
   10. FCN1
   11. HLA-DPB1
   12. HLA-DQB1
   13. TYROBP
   14. HLA-DQA1
   15. LST1
   16. MNDA
   17. TYMP
   18. FCER1G
   19. MS4A6A
   20. FGL2
   21. SAT1
   22. CTSS
   23. HLA-DMA
   24. PSAP
   25. CYBB
   26. CPVL
   27. MARCKS
   28. COTL1
   29. IFITM3
   30. CEBPD

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
  Non-classical Monocytes  : +0.450
  Intermediate Monocytes   : +0.449
  Myeloid Dendritic Cells  : +0.399
  Classical Monocytes      : +0.260

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD14 Mono

High expression of classical monocyte genes (LYZ, CST3, FCN1, CD74, HLA class II) and surface proteins (CD11b, CD18, CD31, CD93, CD48) without CD16 (FCGR3A) confirms CD14+ monocytes. Platelet markers (CD41, CD62P) reflect common platelet aggregates in PBMC. Pathway scores are overridden by direct marker evidence.
```

