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
A single cell in PBMC was annotated in a first pass as: "CD16 Mono"

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

```

### output

```text
{
  "CD16 Monocyte": {
    "genes": [
      "FCGR3A",
      "MS4A7",
      "LST1",
      "CSF1R",
      "CX3CR1",
      "LILRA3",
      "RHOC",
      "MNDA",
      "CTSS",
      "IFITM3",
      "CFP",
      "FTL",
      "LGALS2",
      "PSAP",
      "TYROBP",
      "FCGRT",
      "ATP1B3",
      "LRRC25",
      "SIGLEC10",
      "PLAC8",
      "PECAM1",
      "CDKN1C",
      "NR4A2",
      "TREM2",
      "SLC2A3",
      "MARCKS",
      "CYBB",
      "MAFB",
      "C5AR1",
      "TNFRSF1B",
      "IL1B",
      "CCL3",
      "CCL4",
      "CCL4L2",
      "CXCL8",
      "TIMP1",
      "LGALS3",
      "S100A4",
      "S100A11",
      "S100A6",
      "S100A10",
      "CALM2",
      "CD99",
      "COTL1",
      "ARPC3",
      "ARPC4",
      "SRGN",
      "GABARAPL1"
    ],
    "description": "Non-classical CD16+ monocytes with high expression of FCGR3A and CX3CR1, patrolling endothelium and involved in inflammation."
  },
  "CD14 Monocyte": {
    "genes": [
      "CD14",
      "S100A8",
      "S100A9",
      "LYZ",
      "FCN1",
      "VCAN",
      "CCL2",
      "CCL7",
      "CXCL1",
      "CXCL2",
      "CXCL3",
      "IL1RN",
      "IL1R1",
      "NFKB1",
      "NFKB2",
      "REL",
      "RELA",
      "SERPINA1",
      "SERPINB2",
      "PLAUR",
      "SLPI",
      "TIMP2",
      "TIMP3",
      "MMP9",
      "MMP12",
      "CTSD",
      "CTSB",
      "CTSK",
      "CST3",
      "CPVL",
      "RNASE1",
      "RNASE2",
      "RNASE3",
      "ARHGDIB",
      "RAB7A",
      "RAB31",
      "RAB32",
      "CD68",
      "CD163",
      "MSR1",
      "SCARB1",
      "SCARB2",
      "MERTK",
      "AXL",
      "TYRO3",
      "GA87",
      "GAS6"
    ],
    "description": "Classical CD14+ monocytes with high expression of CD14 and S100A8/A9, primary responders to infection and tissue damage."
  },
  "NK Cell": {
    "genes": [
      "NKG7",
      "GNLY",
      "PRF1",
      "GZMB",
      "GZMA",
      "GZMH",
      "GZMK",
      "GZMM",
      "KLRD1",
      "KLRK1",
      "KLRC1",
      "KLRC2",
      "KLRC3",
      "KLRF1",
      "KLRG1",
      "NCR1",
      "NCR3",
      "NCR2",
      "CD160",
      "CD244",
      "CD247",
      "KIR2DL1",
      "KIR2DL2",
      "KIR2DL3",
      "KIR3DL1",
      "KIR3DL2",
      "FCGR3A",
      "FGFBP2",
      "SPON2",
      "HOPX",
      "XCL1",
      "XCL2",
      "CCL5",
      "PRSS23",
      "S100A4",
      "FOS",
      "JUN",
      "DUSP1",
      "DUSP2",
      "ZFP36",
      "ZFP36L1",
      "ZFP36L2",
      "EGR1",
      "EGR2",
      "NR4A1",
      "NR4A2",
      "NR4A3"
    ],
    "description": "NK cells expressing cytotoxic molecules such as NKG7, GNLY, and PRF1, and KIR receptors, mediating innate killing of infected or tumor cells."
  },
  "cDC2": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "CLEC4A",
      "CD1E",
      "CD1B",
      "CD1D",
      "CD207",
      "LAMP3",
      "CCR7",
      "CCL17",
      "CCL22",
      "IL12B",
      "IL23A",
      "IL1B",
      "IL6",
      "TNF",
      "IRF4",
      "IRF8",
      "BATF3",
      "ID2",
      "ZBTB46",
      "FLT3",
      "CSF2RA",
      "CSF2RB",
      "CD86",
      "CD80",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DQA1",
      "HLA-DQB1",
      "HLA-DPA1",
      "HLA-DPB1",
      "CD74",
      "CIITA",
      "CTSS",
      "CTSL",
      "IFNGR1",
      "IFNGR2",
      "TNFRSF9",
      "CD40",
      "CD83",
      "CD200",
      "CD274",
      "PDCD1LG2",
      "CDKN1A",
      "BIRC3",
      "NFKB1"
    ],
    "description": "Conventional dendritic cells type 2 (cDC2) with high CD1C and FCER1A, capable of priming CD4+ T cell responses to antigens."
  },
  "pDC": {
    "genes": [
      "IL3RA",
      "CLEC4C",
      "LILRA4",
      "TCF4",
      "IRF7",
      "IRF8",
      "IRF4",
      "BCL11A",
      "SPIB",
      "E2-2",
      "TLR7",
      "TLR9",
      "MYD88",
      "SLC15A4",
      "PACSIN1",
      "SIGLEC1",
      "SIGLEC5",
      "SIGLEC6",
      "SIGLEC10",
      "BST2",
      "PLAC8",
      "CCDC50",
      "GPR174",
      "ITM2C",
      "SCARB1",
      "LAMP5",
      "MPEG1",
      "CTSH",
      "CTSL",
      "CTSB",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DQA1",
      "HLA-DQB1",
      "HLA-DPA1",
      "HLA-DPB1",
      "CD74",
      "IFITM1",
      "IFITM2",
      "IFITM3",
      "MX1",
      "MX2",
      "OAS1",
      "OAS2",
      "OAS3",
      "ISG15",
      "IFIT1",
      "IFIT2",
      "IFIT3",
      "IFI44",
      "IFI44L"
    ],
    "description": "Plasmacytoid dendritic cells (pDC) with high IL3RA and CLEC4C, specialized in type I interferon production in response to viral infection."
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
  CD16 Monocyte            : +0.935
  pDC                      : +0.434
  CD14 Monocyte            : +0.236
  cDC2                     : +0.223
  NK Cell                  : -0.304

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
Top genes (FCGR3A, FCN1, CST3) and highest pathway score (+0.935) strongly support CD16 monocyte. Surface protein platelet markers (CD41, CD62P) likely reflect platelet-monocyte aggregates typical of PBMC, not a different cell type.
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

The gene expression shows B cell markers (MS4A1, CD79A, BANK1, BLK, IGKC) and surface proteins include CD19, CD22, CD21, and CD27, which are characteristic of memory B cells. CD27 is a definitive memory B cell marker.
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
The gene expression shows B cell markers (MS4A1, CD79A, BANK1, BLK, IGKC) and surface proteins include CD19, CD22, CD21, and CD27, which are characteristic of memory B cells. CD27 is a definitive memory B cell marker.
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
The gene expression shows B cell markers (MS4A1, CD79A, BANK1, BLK, IGKC) and surface proteins include CD19, CD22, CD21, and CD27, which are characteristic of memory B cells. CD27 is a definitive memory B cell marker.

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
The gene expression shows B cell markers (MS4A1, CD79A, BANK1, BLK, IGKC) and surface proteins include CD19, CD22, CD21, and CD27, which are characteristic of memory B cells. CD27 is a definitive memory B cell marker.

```

### output

```text
{
  "B memory": {
    "genes": [
      "CD27",
      "MS4A1",
      "CD19",
      "CD79A",
      "CD79B",
      "BANK1",
      "PAX5",
      "TCL1A",
      "LTB",
      "TNFRSF13C",
      "CD40",
      "BCL2",
      "IL4R",
      "POU2F2",
      "IRF4",
      "MEF2B",
      "EBF1",
      "VPREB3",
      "JCHAIN",
      "PIM2",
      "MYC",
      "CCND2",
      "MKI67",
      "AICDA",
      "BCL6"
    ],
    "description": "Memory B cells are antigen-experienced B cells that express CD27 and CD19, capable of rapid response upon re-exposure to antigen."
  },
  "B naive": {
    "genes": [
      "IGHD",
      "IGHM",
      "MS4A1",
      "CD19",
      "CD79A",
      "CD79B",
      "PAX5",
      "BANK1",
      "TCL1A",
      "FCER2",
      "CR2",
      "IL4R",
      "POU2F2",
      "EBF1",
      "VPREB3",
      "LTB",
      "TNFRSF13C",
      "BCL2",
      "CD40",
      "MEF2B",
      "IRF4",
      "PIM2",
      "MYC",
      "CCND2",
      "CD22"
    ],
    "description": "Naive B cells are mature B cells that have not encountered antigen, expressing surface IgM and IgD along with CD19 and CD20."
  },
  "Plasma cells": {
    "genes": [
      "SDC1",
      "CD38",
      "MZB1",
      "XBP1",
      "IRF4",
      "PRDM1",
      "JCHAIN",
      "IGHG1",
      "IGHA1",
      "IGLL5",
      "DERL3",
      "FKBP11",
      "SSR4",
      "PDIA4",
      "TNFRSF17",
      "SLAMF7",
      "CD27",
      "POU2AF1",
      "IL6R",
      "CD19"
    ],
    "description": "Plasma cells are antibody-secreting cells derived from B cells, characterized by high expression of CD38 and SDC1 (CD138) and low or absent CD20."
  },
  "CD4+ memory T cells": {
    "genes": [
      "CD4",
      "IL7R",
      "CCR7",
      "SELL",
      "LEF1",
      "TCF7",
      "FOXP1",
      "MYC",
      "BCL2",
      "LTB",
      "IL6ST",
      "CD27",
      "CD28",
      "ICOS",
      "CD40LG",
      "TNFRSF4",
      "TNFRSF25",
      "BATF",
      "IRF4",
      "STAT3",
      "GATA3",
      "CCL5"
    ],
    "description": "CD4+ memory T cells are antigen-experienced helper T cells that express CD4 and IL7R, providing rapid responses upon recall antigen exposure."
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
The gene expression shows B cell markers (MS4A1, CD79A, BANK1, BLK, IGKC) and surface proteins include CD19, CD22, CD21, and CD27, which are characteristic of memory B cells. CD27 is a definitive memory B cell marker.

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
  B naive                  : +1.176
  B memory                 : +1.071
  Plasma cells             : +0.780
  CD4+ memory T cells      : -0.235

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
B memory
The top genes (MS4A1, CD79A, BANK1, BLK, IGKC) and surface proteins (CD19, CD22, CD21, CD27) are characteristic of memory B cells. Pathway scores strongly favor B naive and B memory programs, with no monocyte markers (CD14, CD16) present. Thus, the annotation remains B memory.
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

The expression profile shows high levels of monocyte markers such as CST3, LYZ, FCN1, and multiple HLA class II genes, along with surface proteins like CD11b, CD18, CD31, and CD172a. This pattern is characteristic of classical CD14+ monocytes, rather than CD16+ monocytes or B memory cells.
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
The expression profile shows high levels of monocyte markers such as CST3, LYZ, FCN1, and multiple HLA class II genes, along with surface proteins like CD11b, CD18, CD31, and CD172a. This pattern is characteristic of classical CD14+ monocytes, rather than CD16+ monocytes or B memory cells.
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
The expression profile shows high levels of monocyte markers such as CST3, LYZ, FCN1, and multiple HLA class II genes, along with surface proteins like CD11b, CD18, CD31, and CD172a. This pattern is characteristic of classical CD14+ monocytes, rather than CD16+ monocytes or B memory cells.

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
The expression profile shows high levels of monocyte markers such as CST3, LYZ, FCN1, and multiple HLA class II genes, along with surface proteins like CD11b, CD18, CD31, and CD172a. This pattern is characteristic of classical CD14+ monocytes, rather than CD16+ monocytes or B memory cells.

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
      "FCGR1A",
      "CSF1R",
      "CCR2",
      "CD33",
      "ITGAM",
      "CD68",
      "CTSS",
      "CTSD",
      "FOS",
      "JUN",
      "S100A12",
      "VCAN",
      "FPR1",
      "FPR2",
      "TREM1",
      "TLR2",
      "TLR4",
      "CD86",
      "HLA-DRA",
      "HLA-DRB1",
      "CD163",
      "MNDA",
      "NCF1",
      "NCF2",
      "CYBB",
      "CLEC7A",
      "CLEC4E"
    ],
    "description": "Classical CD14++CD16- monocytes are phagocytic and pro-inflammatory, expressing high levels of CD14 and myeloid-related proteins."
  },
  "Intermediate Monocytes": {
    "genes": [
      "CD14",
      "FCGR3A",
      "CD16",
      "HLA-DRA",
      "HLA-DRB1",
      "CD86",
      "CCR5",
      "CX3CR1",
      "TLR4",
      "TLR2",
      "IL1B",
      "TNF",
      "CCL3",
      "CCL4",
      "CCL5",
      "CXCL8",
      "IL6",
      "CD40",
      "CD80",
      "ICAM1",
      "VCAM1",
      "LTA",
      "LTB",
      "FOS",
      "JUN",
      "NFKB1",
      "RELA",
      "IRF1",
      "IRF8",
      "STAT1"
    ],
    "description": "Intermediate CD14+CD16+ monocytes exhibit a mixed phenotype with high antigen presentation capacity and inflammatory cytokine production."
  },
  "Non-classical Monocytes": {
    "genes": [
      "FCGR3A",
      "CD16",
      "CX3CR1",
      "LILRA3",
      "LILRB1",
      "LILRB2",
      "LILRB4",
      "NR4A1",
      "Nur77",
      "MAFB",
      "KLF4",
      "ITGAL",
      "CD11c",
      "ITGAX",
      "CD49d",
      "FCER1G",
      "FCGR2C",
      "FCGR2B",
      "CSF1R",
      "CD86",
      "HLA-DRA",
      "HLA-DRB1",
      "CD14low",
      "CD163low",
      "CCR2low",
      "TLR7",
      "TLR8",
      "IRF4",
      "IRF2",
      "LYVE1"
    ],
    "description": "Non-classical CD14lowCD16++ monocytes patrol the vasculature and exhibit a more anti-inflammatory or housekeeping function."
  },
  "CD1c+ Dendritic Cells": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "CD1E",
      "HLA-DRA",
      "HLA-DRB1",
      "CD86",
      "CD40",
      "CCR7",
      "IRF4",
      "IRF8",
      "ZBTB46",
      "FLT3",
      "FCGR2B",
      "CD11c",
      "ITGAX",
      "AXL",
      "SIGLEC6",
      "BCL6",
      "ID2",
      "BATF3",
      "TLR1",
      "TLR2",
      "TLR3",
      "TLR4",
      "TLR6",
      "TLR8",
      "IL12A",
      "IL12B",
      "IL23A"
    ],
    "description": "CD1c+ conventional dendritic cells (cDC2) are specialized in antigen presentation to CD4+ T cells and express high levels of MHC class II and CD1c."
  },
  "Plasmacytoid Dendritic Cells": {
    "genes": [
      "IL3RA",
      "CD123",
      "CLEC4C",
      "CD303",
      "BDCA2",
      "LILRA2",
      "IRF7",
      "IRF8",
      "TLR7",
      "TLR9",
      "MYD88",
      "IFIH1",
      "DDX58",
      "LY6E",
      "BST2",
      "CD4",
      "CD68",
      "HLA-DRA",
      "HLA-DRB1",
      "CD86",
      "CD40",
      "CCR5",
      "CXCR3",
      "CXCR4",
      "IL15",
      "IL18",
      "IFNA1",
      "IFNA2",
      "IFNB1",
      "TNF"
    ],
    "description": "Plasmacytoid dendritic cells are specialized in type I interferon production in response to viral nucleic acids and express CD123 and BDCA-2."
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
The expression profile shows high levels of monocyte markers such as CST3, LYZ, FCN1, and multiple HLA class II genes, along with surface proteins like CD11b, CD18, CD31, and CD172a. This pattern is characteristic of classical CD14+ monocytes, rather than CD16+ monocytes or B memory cells.

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
  Non-classical Monocytes  : +0.755
  Plasmacytoid Dendritic Cells: +0.522
  Classical Monocytes      : +0.412
  CD1c+ Dendritic Cells    : +0.323
  Intermediate Monocytes   : +0.138

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD14 Mono
The top genes (CST3, LYZ, FCN1, HLA class II) and surface proteins (CD11b, CD18, CD35, CD4) strongly support classical CD14+ monocytes. No CD16 (FCGR3A) expression is detected in the top genes, ruling out CD16+ monocytes. The high non-classical pathway score may reflect activation or technical artifact, but direct markers confirm CD14 Mono.
```

