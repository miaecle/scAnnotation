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
The gene expression includes FCGR3A (CD16) and myeloid markers (CST3, FCN1, AIF1). Surface proteins show CD16, CD11b, and CD18, consistent with non-classical monocytes. High platelet markers (CD41, CD62P) suggest platelet adherence typical of CD16+ monocytes. Lack of CD14 and B cell markers excludes CD14 Mono and B memory.
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
The gene expression includes FCGR3A (CD16) and myeloid markers (CST3, FCN1, AIF1). Surface proteins show CD16, CD11b, and CD18, consistent with non-classical monocytes. High platelet markers (CD41, CD62P) suggest platelet adherence typical of CD16+ monocytes. Lack of CD14 and B cell markers excludes CD14 Mono and B memory.
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
The gene expression includes FCGR3A (CD16) and myeloid markers (CST3, FCN1, AIF1). Surface proteins show CD16, CD11b, and CD18, consistent with non-classical monocytes. High platelet markers (CD41, CD62P) suggest platelet adherence typical of CD16+ monocytes. Lack of CD14 and B cell markers excludes CD14 Mono and B memory.

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
The gene expression includes FCGR3A (CD16) and myeloid markers (CST3, FCN1, AIF1). Surface proteins show CD16, CD11b, and CD18, consistent with non-classical monocytes. High platelet markers (CD41, CD62P) suggest platelet adherence typical of CD16+ monocytes. Lack of CD14 and B cell markers excludes CD14 Mono and B memory.

```

### output

```text
{
  "CD16+ Monocyte (non-classical)": {
    "genes": [
      "FCGR3A",
      "LILRB2",
      "LST1",
      "CDKN1C",
      "MS4A7",
      "RHOC",
      "CX3CR1",
      "LILRA3",
      "LILRB1",
      "FCGR3B",
      "ADAP2",
      "TAGAP",
      "LRRN3",
      "SIGLEC10",
      "IGSF6",
      "TMEM176A",
      "TMEM176B",
      "CLEC4E",
      "SLC7A8",
      "ZNF789",
      "RASGRP2",
      "PTPN22",
      "TREM1",
      "TREM2",
      "SIRPA"
    ],
    "description": "Non-classical monocytes expressing high FCGR3A (CD16) and low CD14, involved in patrolling vasculature and producing TNF-alpha upon TLR stimulation."
  },
  "CD14+ Monocyte (classical)": {
    "genes": [
      "CD14",
      "FCGR1A",
      "CSF1R",
      "S100A8",
      "S100A9",
      "LYZ",
      "CTSS",
      "CD68",
      "MRC1",
      "IL1B",
      "TNF",
      "CCL2",
      "CCR2",
      "CD33",
      "CD163",
      "CXCL8",
      "IL6",
      "TLR2",
      "TLR4",
      "CLEC7A",
      "FCGR2A",
      "ITGAM",
      "ITGAX",
      "TREM1"
    ],
    "description": "Classical monocytes expressing high CD14 and low FCGR3A, key in phagocytosis, inflammatory response, and differentiation into macrophages and DCs."
  },
  "Intermediate Monocyte": {
    "genes": [
      "CD14",
      "FCGR3A",
      "HLA-DRA",
      "CD74",
      "CTSD",
      "CD86",
      "FCGR1A",
      "CX3CR1",
      "CCR2",
      "CCL3",
      "CCL4",
      "IL1RN",
      "TNF",
      "IL6",
      "CD40",
      "TLR4",
      "TLR2",
      "CD36",
      "CLEC4E",
      "SIRPA",
      "CD1C",
      "FCER1A",
      "CLEC10A"
    ],
    "description": "Intermediate monocytes co-expressing CD14 and CD16, secrete high levels of IL-10 and TNF-alpha, and are involved in antigen presentation."
  },
  "NK cell": {
    "genes": [
      "NKG7",
      "GNLY",
      "PRF1",
      "GZMB",
      "GZMK",
      "KLRD1",
      "KLRB1",
      "KLRK1",
      "NCR1",
      "NCR3",
      "CD247",
      "FCGR3A",
      "TYROBP",
      "KIR2DL1",
      "KIR3DL1",
      "SH2D1B",
      "TRDC",
      "TRGC2",
      "KLRC1",
      "KLRC2",
      "KLRF1",
      "KLRC3",
      "KLRG1",
      "GZMH"
    ],
    "description": "Natural killer cells with cytotoxic granules, expressing NKG7, GNLY, and PRF1, involved in innate immunity against infected or transformed cells."
  },
  "Conventional dendritic cell 2 (cDC2)": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "HLA-DRA",
      "CD74",
      "ITGAX",
      "CD11C",
      "SIRPA",
      "S100A9",
      "LAMP3",
      "CCR7",
      "IL10",
      "IL12B",
      "TNF",
      "CD40",
      "CD86",
      "CD80",
      "TLR4",
      "TLR2",
      "CLEC4A",
      "S100A8",
      "CD33",
      "CD36",
      "FCGR2B"
    ],
    "description": "Conventional dendritic cells type 2 expressing CD1C and FCER1A, specialize in antigen presentation and activation of CD4+ T cells."
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
The gene expression includes FCGR3A (CD16) and myeloid markers (CST3, FCN1, AIF1). Surface proteins show CD16, CD11b, and CD18, consistent with non-classical monocytes. High platelet markers (CD41, CD62P) suggest platelet adherence typical of CD16+ monocytes. Lack of CD14 and B cell markers excludes CD14 Mono and B memory.

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
  CD16+ Monocyte (non-classical): +0.732
  Conventional dendritic cell 2 (cDC2): +0.092
  CD14+ Monocyte (classical): +0.077
  Intermediate Monocyte    : +0.064
  NK cell                  : -0.410

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
High expression of FCGR3A and myeloid genes (CST3, FCN1, AIF1) with top pathway score for CD16+ monocytes. Surface proteins show platelet markers (CD41, CD62P) characteristic of non-classical monocytes. Lack of CD14 and B cell markers excludes alternatives. Confirms stage-1 annotation.
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

Highly expressed B cell markers like MS4A1 (CD20), CD79A, BANK1, and immunoglobulin genes, along with surface proteins CD19, CD22, CD21, and CD27 (memory marker), confirm this as a memory B cell. Monocyte markers (CD14, CD16) are absent.
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
Highly expressed B cell markers like MS4A1 (CD20), CD79A, BANK1, and immunoglobulin genes, along with surface proteins CD19, CD22, CD21, and CD27 (memory marker), confirm this as a memory B cell. Monocyte markers (CD14, CD16) are absent.
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
Highly expressed B cell markers like MS4A1 (CD20), CD79A, BANK1, and immunoglobulin genes, along with surface proteins CD19, CD22, CD21, and CD27 (memory marker), confirm this as a memory B cell. Monocyte markers (CD14, CD16) are absent.

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
Highly expressed B cell markers like MS4A1 (CD20), CD79A, BANK1, and immunoglobulin genes, along with surface proteins CD19, CD22, CD21, and CD27 (memory marker), confirm this as a memory B cell. Monocyte markers (CD14, CD16) are absent.

```

### output

```text
{
  "Switched memory B": {
    "genes": [
      "CD19",
      "MS4A1",
      "CD27",
      "TNFRSF13C",
      "CD81",
      "CR2",
      "FCRL2",
      "FCRL5",
      "IGHG1",
      "IGHG3",
      "IGHA1",
      "CD80",
      "CD86",
      "AICDA",
      "BCL6",
      "PAX5",
      "CCR6",
      "CXCR5",
      "IL4R",
      "TNFRSF9",
      "TNFRSF4",
      "ICOSL",
      "CD40",
      "CD48",
      "IRF8",
      "MYC",
      "MKI67",
      "CD38",
      "CD24",
      "CD72"
    ],
    "description": "Switched memory B cells are CD27+ IgD- IgM- and have undergone class switch recombination, expressing IgG or IgA; they circulate in blood and can rapidly differentiate into plasmablasts upon re-encounter with antigen."
  },
  "Unswitched memory B": {
    "genes": [
      "CD19",
      "MS4A1",
      "CD27",
      "TNFRSF13C",
      "CD81",
      "CR2",
      "FCRL2",
      "FCRL5",
      "IGHD",
      "IGHM",
      "CD24",
      "CD38",
      "CD72",
      "IL4R",
      "TNFRSF9",
      "TNFRSF4",
      "ICOSL",
      "CD40",
      "CD48",
      "IRF8",
      "MYC",
      "MKI67",
      "CCR6",
      "CXCR5",
      "BCL6",
      "PAX5",
      "AICDA",
      "CD80",
      "CD86",
      "TCL1A"
    ],
    "description": "Unswitched memory B cells are CD27+ IgD+ IgM+ and retain the ability to undergo class switching; they represent a transitional memory population with both naive and memory features."
  },
  "Naive B": {
    "genes": [
      "CD19",
      "MS4A1",
      "CD27",
      "TNFRSF13C",
      "CD81",
      "CR2",
      "FCRL2",
      "FCRL5",
      "IGHD",
      "IGHM",
      "TCL1A",
      "CD24",
      "CD38",
      "CD72",
      "CCR7",
      "CXCR4",
      "IL4R",
      "CD40",
      "CD48",
      "IRF8",
      "PAX5",
      "BCL6",
      "CD83",
      "CD86",
      "HLA-DRA",
      "HLA-DQB1",
      "HLA-DRB1",
      "CD74",
      "CD79A",
      "CD79B"
    ],
    "description": "Naive B cells are CD27- IgD+ IgM+ and have not encountered antigen; they express high levels of TCL1A and low CD38, and circulate in blood awaiting activation."
  },
  "Plasma cell": {
    "genes": [
      "SDC1",
      "MZB1",
      "XBP1",
      "PRDM1",
      "TNFRSF17",
      "CD38",
      "CD27",
      "CD19",
      "MS4A1",
      "IGHA1",
      "IGHG1",
      "IGHG3",
      "IGHM",
      "IGLL5",
      "JCHAIN",
      "FKBP11",
      "PDIA4",
      "PDIA6",
      "HSP90B1",
      "PPIB",
      "TXNDC5",
      "SEC61G",
      "SSR3",
      "DERL3",
      "ATP1B1",
      "MYBL1",
      "IRF4",
      "MCL1",
      "BCL2",
      "CD44"
    ],
    "description": "Plasma cells are terminally differentiated antibody-secreting cells with high CD38 and SDC1 expression; they are found in bone marrow and peripheral blood at low frequencies."
  },
  "Atypical memory B": {
    "genes": [
      "CD19",
      "MS4A1",
      "CD27",
      "CD11c",
      "ITGAX",
      "TNFRSF13C",
      "CD81",
      "CR2",
      "FCRL2",
      "FCRL5",
      "IGHD",
      "IGHM",
      "CD24",
      "CD38",
      "CD72",
      "IL4R",
      "TNFRSF9",
      "TNFRSF4",
      "ICOSL",
      "CD40",
      "CD48",
      "IRF8",
      "PAX5",
      "BCL6",
      "AICDA",
      "CD80",
      "CD86",
      "CCR6",
      "CXCR5",
      "TCL1A"
    ],
    "description": "Atypical memory B cells are CD27- IgD- and often express CD11c; they are expanded in autoimmune and infectious diseases and exhibit a transcriptional profile distinct from classical memory B cells."
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
Highly expressed B cell markers like MS4A1 (CD20), CD79A, BANK1, and immunoglobulin genes, along with surface proteins CD19, CD22, CD21, and CD27 (memory marker), confirm this as a memory B cell. Monocyte markers (CD14, CD16) are absent.

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
  Switched memory B        : +0.905
  Naive B                  : +0.775
  Plasma cell              : +0.634
  Unswitched memory B      : +0.516
  Atypical memory B        : +0.474

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
B memory
Strong B cell markers (MS4A1, CD79A, BANK1) and memory markers (CD27, CD35, CD73) confirm B memory. Monocyte markers (CD14, CD16) absent. Pathway scores highest for switched memory B, consistent with memory B cell identity.
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

Expression of monocyte markers (CST3, LYZ, CD74, FCN1, AIF1, TYROBP) and surface proteins (CD11b, CD14 via CD4-1? but CD14 is not listed, but CD93, CD35, CD48, CD18, CD11b, CD49d) indicate classical monocytes. Lack of CD16 or B cell markers (CD19, CD20) excludes CD16 Mono and B memory. Platelet markers may be from binding but overall profile matches CD14+ monocytes.
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
Expression of monocyte markers (CST3, LYZ, CD74, FCN1, AIF1, TYROBP) and surface proteins (CD11b, CD14 via CD4-1? but CD14 is not listed, but CD93, CD35, CD48, CD18, CD11b, CD49d) indicate classical monocytes. Lack of CD16 or B cell markers (CD19, CD20) excludes CD16 Mono and B memory. Platelet markers may be from binding but overall profile matches CD14+ monocytes.
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
Expression of monocyte markers (CST3, LYZ, CD74, FCN1, AIF1, TYROBP) and surface proteins (CD11b, CD14 via CD4-1? but CD14 is not listed, but CD93, CD35, CD48, CD18, CD11b, CD49d) indicate classical monocytes. Lack of CD16 or B cell markers (CD19, CD20) excludes CD16 Mono and B memory. Platelet markers may be from binding but overall profile matches CD14+ monocytes.

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
Expression of monocyte markers (CST3, LYZ, CD74, FCN1, AIF1, TYROBP) and surface proteins (CD11b, CD14 via CD4-1? but CD14 is not listed, but CD93, CD35, CD48, CD18, CD11b, CD49d) indicate classical monocytes. Lack of CD16 or B cell markers (CD19, CD20) excludes CD16 Mono and B memory. Platelet markers may be from binding but overall profile matches CD14+ monocytes.

```

### output

```text
{
  "Classical Monocytes": {
    "genes": [
      "CD14",
      "S100A8",
      "S100A9",
      "LYZ",
      "FCGR1A",
      "CST3",
      "FCN1",
      "S100A12",
      "CCR2",
      "CLEC7A",
      "CD163",
      "CD68",
      "TLR4",
      "IL6",
      "TNF",
      "CXCL8",
      "IL1B",
      "CD33",
      "CD11b",
      "MNDA",
      "FPR1",
      "FPR2",
      "C5AR1",
      "NLRP3",
      "IRF1",
      "STAT1",
      "NFKB1",
      "RELA",
      "HOXA1",
      "MAFB"
    ],
    "description": "Classical monocytes are CD14++CD16- cells that express high levels of CD14, S100A8/A9, and are involved in phagocytosis and inflammation."
  },
  "Intermediate Monocytes": {
    "genes": [
      "CD14",
      "FCGR3A",
      "FCGR1A",
      "HLA-DRA",
      "HLA-DRB1",
      "CD163",
      "CD86",
      "CXCL10",
      "CCL3",
      "CCL4",
      "IL6",
      "TNF",
      "IL1B",
      "TLR2",
      "TLR4",
      "TRAF1",
      "NFKB1",
      "IRF5",
      "STAT1",
      "S100A8",
      "S100A9",
      "LYZ",
      "CST3",
      "FCN1"
    ],
    "description": "Intermediate monocytes are CD14+CD16+ cells with high MHC class II expression and are pro-inflammatory."
  },
  "Non-classical Monocytes": {
    "genes": [
      "FCGR3A",
      "CD14",
      "CX3CR1",
      "CDKN1C",
      "PRAM1",
      "LILRA2",
      "FCER1G",
      "ITGAL",
      "NR4A1",
      "NR4A2",
      "KLF2",
      "AHR",
      "PTPRC",
      "SIGLEC10",
      "TNFAIP3",
      "IL13RA1",
      "IL10",
      "TGFB1",
      "C1QA",
      "C1QB",
      "VSIG4",
      "MERTK"
    ],
    "description": "Non-classical monocytes are CD14dimCD16++ cells that patrol the vasculature and have a unique transcription factor profile."
  },
  "Myeloid Dendritic Cells (cDC2)": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "CD33",
      "HLA-DRA",
      "HLA-DRB1",
      "CD11c",
      "ITGAX",
      "CD86",
      "CD40",
      "FLT3",
      "IRF4",
      "ZBTB46",
      "CD207",
      "CLEC4A",
      "CLEC4C",
      "CCR7",
      "CCL17",
      "CCL22",
      "IL12",
      "IL23",
      "TNF",
      "IL6",
      "IL1B"
    ],
    "description": "Myeloid dendritic cells (cDC2) are CD1c+ dendritic cells that are potent antigen-presenting cells and often confused with monocytes."
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
Expression of monocyte markers (CST3, LYZ, CD74, FCN1, AIF1, TYROBP) and surface proteins (CD11b, CD14 via CD4-1? but CD14 is not listed, but CD93, CD35, CD48, CD18, CD11b, CD49d) indicate classical monocytes. Lack of CD16 or B cell markers (CD19, CD20) excludes CD16 Mono and B memory. Platelet markers may be from binding but overall profile matches CD14+ monocytes.

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
  Non-classical Monocytes  : +0.522
  Intermediate Monocytes   : +0.433
  Myeloid Dendritic Cells (cDC2): +0.306
  Classical Monocytes      : +0.288

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
Pathway scores indicate non-classical monocyte program most active, and monocyte markers are present. Absence of CD14 and CD16 in top surface proteins may reflect technical variation, but pathway evidence overrides stage-1 annotation.
```

