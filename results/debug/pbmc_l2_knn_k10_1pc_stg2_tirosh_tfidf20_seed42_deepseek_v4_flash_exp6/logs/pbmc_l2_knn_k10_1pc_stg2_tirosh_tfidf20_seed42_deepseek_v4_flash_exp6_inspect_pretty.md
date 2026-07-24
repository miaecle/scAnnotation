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
The expression of FCGR3A (CD16), along with monocyte markers CST3, FCN1, and lack of CD14 in top genes, indicates non-classical (CD16+) monocytes. Surface proteins show CD16, CD11b, and platelet markers (CD41, CD62P) which can adhere to monocytes.
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
The expression of FCGR3A (CD16), along with monocyte markers CST3, FCN1, and lack of CD14 in top genes, indicates non-classical (CD16+) monocytes. Surface proteins show CD16, CD11b, and platelet markers (CD41, CD62P) which can adhere to monocytes.
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
  "Non-classical monocytes": {
    "genes": [
      "FCGR3A",
      "CDKN1C",
      "CX3CR1",
      "LST1",
      "AIF1",
      "RHOC",
      "FOS",
      "CFD",
      "LILRB1",
      "LILRA2",
      "TAGAP",
      "COTL1",
      "GPR65",
      "VNN2",
      "SIPA1L2",
      "RASSF2",
      "ARHGAP25",
      "SLC11A1",
      "IFITM3",
      "LST1",
      "LILRB2",
      "TREM1",
      "TIMD4",
      "CLEC7A",
      "FCGR1A"
    ],
    "description": "Non-classical CD16+ monocytes with high expression of FCGR3A and CX3CR1, acting as patrolling monocytes with anti-inflammatory functions."
  },
  "Classical monocytes": {
    "genes": [
      "CD14",
      "S100A8",
      "S100A9",
      "LYZ",
      "FCN1",
      "S100A12",
      "VCAN",
      "CTSS",
      "CCL3",
      "CCL4",
      "CLEC4E",
      "CLEC5A",
      "IL1B",
      "TNF",
      "LTF",
      "MPEG1",
      "MNDA",
      "PLBD1",
      "SERPINA1",
      "FCGR2A"
    ],
    "description": "Classical CD14+ monocytes with high expression of CD14 and S100A8/9, involved in phagocytosis and inflammatory responses."
  },
  "Intermediate monocytes": {
    "genes": [
      "CD14",
      "FCGR3A",
      "HLA-DRA",
      "CD74",
      "CLEC10A",
      "CST3",
      "FCGR1A",
      "CD163",
      "MERTK",
      "MAFB",
      "PLAUR",
      "VNN2",
      "S100A8",
      "S100A9",
      "CTSD",
      "CTSB",
      "LGALS3",
      "CCL2",
      "CXCL16",
      "TNFSF13B"
    ],
    "description": "Intermediate monocytes co-expressing CD14 and CD16, with high antigen-presentation capacity and inflammatory potential."
  },
  "NK cells": {
    "genes": [
      "NKG7",
      "GNLY",
      "PRF1",
      "GZMB",
      "GZMA",
      "KLRD1",
      "KLRK1",
      "KLRC1",
      "KLRB1",
      "NCR1",
      "FCGR3A",
      "CD247",
      "SH2D1B",
      "TYROBP",
      "XCL1",
      "XCL2",
      "CCL5",
      "CD160",
      "LAMP1",
      "HOPX"
    ],
    "description": "Natural killer cells with cytotoxic granules and expression of NKG7 and GNLY, mediating innate immune responses."
  },
  "cDC2 dendritic cells": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "HLA-DRA",
      "HLA-DPB1",
      "HLA-DQB1",
      "CD74",
      "CST3",
      "FCGR2B",
      "CLEC4A",
      "CLEC9A",
      "TLR10",
      "IDO1",
      "CCR7",
      "IRF4",
      "TIMP1",
      "ALS912",
      "PPM1N",
      "ATP6V1G3",
      "FZD2"
    ],
    "description": "Conventional type 2 dendritic cells expressing CD1c and FCER1A, specialized in antigen presentation and T-cell activation."
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
The expression of FCGR3A (CD16), along with monocyte markers CST3, FCN1, and lack of CD14 in top genes, indicates non-classical (CD16+) monocytes. Surface proteins show CD16, CD11b, and platelet markers (CD41, CD62P) which can adhere to monocytes.

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
  Non-classical monocytes  : +0.977
  Intermediate monocytes   : +0.500
  cDC2 dendritic cells     : +0.312
  Classical monocytes      : -0.088
  NK cells                 : -0.401

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
Strong expression of FCGR3A (CD16) and monocyte markers CST3, FCN1, with absent CD14, supports non-classical monocytes. Surface proteins include platelet markers (CD41, CD62P) consistent with CD16+ monocyte-platelet aggregates. Pathway scores highest for non-classical monocytes (+0.977).
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

This profile indicates a B cell, with high expression of immunoglobulins (IGKC, IGHA, IGHE, IGHG) and B cell markers (MS4A1, CD79A, BANK1, BLK). Surface proteins include CD19, CD22, CD21, CD35, and CD27, consistent with memory B cells.
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
This profile indicates a B cell, with high expression of immunoglobulins (IGKC, IGHA, IGHE, IGHG) and B cell markers (MS4A1, CD79A, BANK1, BLK). Surface proteins include CD19, CD22, CD21, CD35, and CD27, consistent with memory B cells.
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
  "Switched_memory_B": {
    "genes": [
      "CD27",
      "MS4A1",
      "CD79A",
      "CD79B",
      "CXCR5",
      "BCL6",
      "IL4R",
      "CD40",
      "TNFRSF13B",
      "TNFRSF13C",
      "CR2",
      "FCRL5",
      "FCRL3",
      "FCRL2",
      "FCRL1",
      "FCER2",
      "CD83",
      "CD86",
      "CD80",
      "IRF4",
      "PRDM1",
      "XBP1",
      "MKI67",
      "AICDA",
      "PAX5",
      "EBF1",
      "TCF3",
      "ID3",
      "CD22",
      "PTPRC",
      "CD37",
      "CD52",
      "CD74",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPB1",
      "HLA-DQA1",
      "HLA-DQB1",
      "CD1C",
      "FCGR2B",
      "ITGAX",
      "ITGAM",
      "ITGB7",
      "SELL",
      "LMO2",
      "CXCR4",
      "S1PR1",
      "GPR183"
    ],
    "description": "IgG-positive memory B cells, expressing class-switched immunoglobulin and high CD27, involved in recall responses."
  },
  "Unswitched_memory_B": {
    "genes": [
      "CD27",
      "MS4A1",
      "CD79A",
      "CD79B",
      "CXCR5",
      "BCL6",
      "IL4R",
      "CD40",
      "TNFRSF13B",
      "TNFRSF13C",
      "CR2",
      "FCRL5",
      "FCER2",
      "CD83",
      "CD86",
      "CD80",
      "IRF4",
      "PRDM1",
      "XBP1",
      "MKI67",
      "AICDA",
      "PAX5",
      "EBF1",
      "TCF3",
      "ID3",
      "CD22",
      "PTPRC",
      "CD37",
      "CD52",
      "CD74",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPB1",
      "HLA-DQA1",
      "HLA-DQB1",
      "CD1C",
      "FCGR2B",
      "ITGAX",
      "ITGAM",
      "ITGB7",
      "SELL",
      "LMO2",
      "CXCR4",
      "S1PR1",
      "GPR183",
      "IGHM",
      "IGHD",
      "CD38",
      "CD24"
    ],
    "description": "IgM/IgD-positive memory B cells, unswitched, expressing CD27 and surface IgM, important for T-independent responses."
  },
  "Naive_B": {
    "genes": [
      "MS4A1",
      "CD79A",
      "CD79B",
      "PAX5",
      "EBF1",
      "TCF3",
      "ID3",
      "CD22",
      "PTPRC",
      "CD37",
      "CD52",
      "CD74",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPB1",
      "HLA-DQA1",
      "HLA-DQB1",
      "CD1C",
      "FCGR2B",
      "ITGAX",
      "ITGAM",
      "ITGB7",
      "SELL",
      "LMO2",
      "CXCR4",
      "S1PR1",
      "GPR183",
      "IGHM",
      "IGHD",
      "CD38",
      "CD24",
      "CD21",
      "CD23",
      "CD40",
      "TNFRSF13B",
      "TNFRSF13C",
      "CR2",
      "FCRL5",
      "FCER2",
      "CD83",
      "CD86",
      "CD80",
      "IRF4",
      "MKI67",
      "AICDA",
      "PRDM1",
      "XBP1",
      "IL4R",
      "CXCR5",
      "BCL6"
    ],
    "description": "Mature naïve B cells, expressing surface IgM and IgD, lacking CD27 and activation markers."
  },
  "Plasma_cell": {
    "genes": [
      "SDC1",
      "MZB1",
      "CD38",
      "XBP1",
      "PRDM1",
      "IRF4",
      "CD27",
      "CD138",
      "CD79A",
      "CD79B",
      "MS4A1",
      "PAX5",
      "EBF1",
      "TCF3",
      "ID3",
      "CD22",
      "PTPRC",
      "CD37",
      "CD52",
      "CD74",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPB1",
      "HLA-DQA1",
      "HLA-DQB1",
      "CD1C",
      "FCGR2B",
      "ITGAX",
      "ITGAM",
      "ITGB7",
      "SELL",
      "LMO2",
      "CXCR4",
      "S1PR1",
      "GPR183",
      "IGHM",
      "IGHD",
      "CD24",
      "CD21",
      "CD23",
      "CD40",
      "TNFRSF13B",
      "TNFRSF13C",
      "CR2",
      "FCRL5",
      "FCER2",
      "CD83",
      "CD86",
      "CD80",
      "MKI67",
      "AICDA"
    ],
    "description": "Antibody-secreting plasma cells, high CD38 and SDC1, low CD20, expressing high levels of immunoglobulin."
  },
  "CD4_T_cell": {
    "genes": [
      "CD3D",
      "CD3E",
      "CD3G",
      "CD4",
      "CD8A",
      "CD8B",
      "TRAC",
      "TRBC1",
      "TRBC2",
      "CD28",
      "CD40LG",
      "ICOS",
      "IL2RA",
      "FOXP3",
      "IL7R",
      "CCR7",
      "SELL",
      "CD27",
      "CD62L",
      "CD45RA",
      "CD45RO",
      "CD95",
      "TNFRSF9",
      "TNFRSF4",
      "TNFRSF18",
      "CTLA4",
      "PDCD1",
      "LAG3",
      "TIGIT",
      "HAVCR2",
      "GZMB",
      "PRF1",
      "IFNG",
      "IL4",
      "IL5",
      "IL13",
      "CCL4",
      "CCL5",
      "GZMK",
      "GZMH",
      "KLRG1",
      "KLRB1",
      "NCR3",
      "NKG7",
      "GNLY",
      "FASLG",
      "SPN",
      "PTPRC",
      "CD52",
      "CD37"
    ],
    "description": "CD4-positive T helper cells, expressing CD3 and CD4, regulating immune responses."
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
This profile indicates a B cell, with high expression of immunoglobulins (IGKC, IGHA, IGHE, IGHG) and B cell markers (MS4A1, CD79A, BANK1, BLK). Surface proteins include CD19, CD22, CD21, CD35, and CD27, consistent with memory B cells.

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
  Switched_memory_B        : +0.859
  Naive_B                  : +0.856
  Unswitched_memory_B      : +0.837
  Plasma_cell              : +0.828
  CD4_T_cell               : -0.282

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
B memory
Strong B cell identity from top genes (MS4A1, CD79A, BANK1, IGKC, IGHA, IGHE, IGHG) and surface proteins (CD19, CD22, CD21, CD35, CD27). CD27 positivity and isotype-switched immunoglobulins indicate memory B cells. Pathway score confirms Switched_memory_B as most active. No monocyte markers (CD14, CD16) are present.
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
High expression of monocyte markers (CST3, LYZ, FCN1, HLA class II) and surface proteins (CD11b, CD18, CD93, CD35) indicate classical CD14+ monocytes. FCN1 is specific to CD14+ monocytes, not CD16+ or B cells.
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
High expression of monocyte markers (CST3, LYZ, FCN1, HLA class II) and surface proteins (CD11b, CD18, CD93, CD35) indicate classical CD14+ monocytes. FCN1 is specific to CD14+ monocytes, not CD16+ or B cells.
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
  "Classic CD14+ monocyte": {
    "genes": [
      "S100A8",
      "S100A9",
      "LYZ",
      "CD14",
      "CCR2",
      "CST3",
      "FCN1",
      "VCAN",
      "THBS1",
      "MNDA",
      "CTSS",
      "S100A12",
      "TYMP",
      "FOS",
      "IL1B",
      "VNN2",
      "FTL",
      "CSTA",
      "CD163",
      "CD68",
      "CD36",
      "MSR1",
      "LIPA",
      "APOE",
      "CTSB",
      "CTSD",
      "LAMP1",
      "NPC2",
      "SLC11A1",
      "FCGR2A"
    ],
    "description": "Classical CD14+ monocytes are the most abundant monocyte subset, characterized by high CD14 expression and lack of CD16, and play key roles in phagocytosis and inflammation."
  },
  "Intermediate CD14+CD16+ monocyte": {
    "genes": [
      "FCGR3A",
      "CD14",
      "CD163",
      "HLA-DRA",
      "CD86",
      "LTA4H",
      "SIGLEC1",
      "MRC1",
      "CCL3",
      "CCL4",
      "CCL5",
      "GPR56",
      "IL1R2",
      "TNF",
      "IL6",
      "CXCL8",
      "CXCL10",
      "CXCL9",
      "CCR5",
      "CD274",
      "PDL2",
      "CD80",
      "TLR4",
      "TLR2",
      "CD40",
      "CD83",
      "ICAM1",
      "VCAM1",
      "SELL",
      "ITGAL"
    ],
    "description": "Intermediate monocytes co-express CD14 and CD16, exhibit both classical and non-classical features, and are involved in antigen presentation and cytokine production."
  },
  "Non-classic CD16+ monocyte": {
    "genes": [
      "FCGR3A",
      "CDKN1C",
      "LILRB2",
      "LST1",
      "MS4A7",
      "CX3CR1",
      "CEBPD",
      "RAB7L1",
      "IFITM1",
      "IFITM2",
      "IFITM3",
      "PLAC8",
      "PLEK",
      "KLF4",
      "NR4A1",
      "ATF3",
      "FOSB",
      "EGR1",
      "JUNB",
      "NFKBIA",
      "TNFAIP3",
      "TSC22D3",
      "ZFP36",
      "DUSP1",
      "SOCS3",
      "IRF2BP2",
      "KLF2",
      "MCL1",
      "BCL2A1",
      "IL1RN"
    ],
    "description": "Non-classical monocytes are CD14lowCD16++ and patrol the vasculature, characterized by a unique transcriptional program involving CX3CR1 and anti-inflammatory functions."
  },
  "Myeloid dendritic cell type 2": {
    "genes": [
      "FCER1A",
      "CD1C",
      "CLEC10A",
      "HLA-DRB1",
      "CD1E",
      "CD207",
      "ZBTB46",
      "IRF4",
      "ITGAX",
      "CD11C",
      "FCGR2B",
      "CD33",
      "CD86",
      "HLA-DQA1",
      "HLA-DQB1",
      "HLA-DPA1",
      "HLA-DPB1",
      "CD74",
      "CIITA",
      "RFX5",
      "NFKB1",
      "REL",
      "RELA",
      "MAPK1",
      "MAPK3",
      "AKT1",
      "PIK3R1",
      "PTEN",
      "TLR8",
      "TLR7"
    ],
    "description": "Myeloid dendritic cells type 2 (cDC2) are professional antigen-presenting cells that express CD1c and CLEC10A, and are specialized in presenting antigens to CD4+ T cells."
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
High expression of monocyte markers (CST3, LYZ, FCN1, HLA class II) and surface proteins (CD11b, CD18, CD93, CD35) indicate classical CD14+ monocytes. FCN1 is specific to CD14+ monocytes, not CD16+ or B cells.

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
  Myeloid dendritic cell type 2: +0.569
  Classic CD14+ monocyte   : +0.521
  Non-classic CD16+ monocyte: +0.371
  Intermediate CD14+CD16+ monocyte: +0.110

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD14 Mono
High expression of CST3, LYZ, FCN1, and HLA class II genes, along with surface proteins CD11b, CD18, CD93, CD35—all specific to classical CD14+ monocytes. Pathway scores also highly support this subtype despite minor myeloid DC2 overlap.
```

