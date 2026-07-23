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

The gene expression profile shows high levels of FCGR3A (CD16), AIF1, FCN1, and TYROBP, which are characteristic of non-classical monocytes. The top surface proteins include CD16, CD11b, and platelet-associated markers (CD41, CD62P) often seen in this subset, while CD14 is notably absent, confirming CD16+ monocytes.
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
The gene expression profile shows high levels of FCGR3A (CD16), AIF1, FCN1, and TYROBP, which are characteristic of non-classical monocytes. The top surface proteins include CD16, CD11b, and platelet-associated markers (CD41, CD62P) often seen in this subset, while CD14 is notably absent, confirming CD16+ monocytes.
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
The gene expression profile shows high levels of FCGR3A (CD16), AIF1, FCN1, and TYROBP, which are characteristic of non-classical monocytes. The top surface proteins include CD16, CD11b, and platelet-associated markers (CD41, CD62P) often seen in this subset, while CD14 is notably absent, confirming CD16+ monocytes.

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
The gene expression profile shows high levels of FCGR3A (CD16), AIF1, FCN1, and TYROBP, which are characteristic of non-classical monocytes. The top surface proteins include CD16, CD11b, and platelet-associated markers (CD41, CD62P) often seen in this subset, while CD14 is notably absent, confirming CD16+ monocytes.

```

### output

```text
{
  "Non-classical Monocyte": {
    "genes": [
      "FCGR3A",
      "AIF1",
      "FCN1",
      "TYROBP",
      "CDKN1C",
      "MS4A7",
      "LST1",
      "IFI30",
      "CFD",
      "S100A12",
      "RHOC",
      "GOSR2",
      "FGR",
      "HCST",
      "NCSTN",
      "PSAP",
      "CTSS",
      "CTSL",
      "CYBB",
      "NCF1",
      "NCF2",
      "NCF4",
      "RAC2",
      "RAC1",
      "RAP1B",
      "VAMP8",
      "STXBP2",
      "UNC13D",
      "AP3B1",
      "LAMP1",
      "LAMP2",
      "CD63",
      "CD68",
      "CD163",
      "CD14"
    ],
    "description": "Non-classical monocytes are CD16+CD14- patrolling monocytes that survey the endothelium and respond to viral infections, characterized by high expression of FCGR3A and low CD14."
  },
  "Classical Monocyte": {
    "genes": [
      "CD14",
      "CSF1R",
      "S100A8",
      "S100A9",
      "S100A12",
      "VCAN",
      "LYZ",
      "CST3",
      "CD33",
      "FCGR1A",
      "FCGR1B",
      "FCGR2A",
      "FCGR2B",
      "FCGR3A",
      "ITGAM",
      "ITGB2",
      "CCR2",
      "CXCR4",
      "CD163",
      "MARCO",
      "MSR1",
      "TREM2",
      "TLR2",
      "TLR4",
      "TLR8",
      "MYD88",
      "IRAK1",
      "IRAK4",
      "NFKB1",
      "RELA"
    ],
    "description": "Classical monocytes are CD14+CD16- phagocytic cells that produce inflammatory cytokines and express high CD14, S100A8/S100A9, and CSF1R."
  },
  "Intermediate Monocyte": {
    "genes": [
      "CD14",
      "FCGR3A",
      "FCGR1A",
      "HLA-DRA",
      "HLA-DRB1",
      "CD86",
      "CD40",
      "TNF",
      "IL1B",
      "IL6",
      "CCL2",
      "CCL3",
      "CCL4",
      "CCL5",
      "CXCL8",
      "CXCL10",
      "CCR2",
      "CCR5",
      "CX3CR1",
      "TLR2",
      "TLR4",
      "TLR8",
      "MYD88",
      "NFKB1",
      "RELA",
      "STAT1",
      "STAT3",
      "IRF1",
      "IRF5",
      "IRF8"
    ],
    "description": "Intermediate monocytes are CD14+CD16+ cells that exhibit both classical and non-classical features, with high levels of CD14 and FCGR3A, and produce pro-inflammatory cytokines."
  },
  "NK Cell": {
    "genes": [
      "NKG7",
      "GZMB",
      "PRF1",
      "GZMA",
      "GZMK",
      "KLRD1",
      "KLRK1",
      "NCR1",
      "NCR3",
      "CD247",
      "FCGR3A",
      "CD16",
      "CD56",
      "NCAM1",
      "KLRC1",
      "KLRC2",
      "KLRC3",
      "KIR2DL1",
      "KIR2DL2",
      "KIR2DL3",
      "KIR3DL1",
      "KIR3DL2",
      "SH2D1B",
      "SLAMF7",
      "CD244",
      "CD226",
      "CD96",
      "TIGIT",
      "LAG3",
      "PDCD1"
    ],
    "description": "Natural killer cells are innate lymphoid cells that kill virally infected and tumor cells, expressing NKG7, GZMB, PRF1, and FCGR3A (CD16)."
  },
  "Myeloid Dendritic Cell": {
    "genes": [
      "CLEC10A",
      "FCER1A",
      "CD1C",
      "CD1E",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPB1",
      "HLA-DPA1",
      "CCR7",
      "CST3",
      "FLT3",
      "ZBTB46",
      "IRF4",
      "IRF8",
      "BATF3",
      "ID2",
      "NOTCH2",
      "CD83",
      "CD80",
      "CD86",
      "CD40",
      "TLR3",
      "TLR7",
      "TLR8",
      "TLR9",
      "MYD88",
      "IRAK4",
      "TRAF6",
      "NFKB1",
      "RELA"
    ],
    "description": "Myeloid dendritic cells are professional antigen-presenting cells that express CLEC10A, FCER1A, CD1C, and high levels of MHC class II molecules."
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
The gene expression profile shows high levels of FCGR3A (CD16), AIF1, FCN1, and TYROBP, which are characteristic of non-classical monocytes. The top surface proteins include CD16, CD11b, and platelet-associated markers (CD41, CD62P) often seen in this subset, while CD14 is notably absent, confirming CD16+ monocytes.

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
  Non-classical Monocyte   : +0.936
  Myeloid Dendritic Cell   : +0.246
  Classical Monocyte       : +0.175
  Intermediate Monocyte    : +0.045
  NK Cell                  : -0.325

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
High expression of FCGR3A, AIF1, FCN1, and TYROBP with absent CD14; surface proteins include CD16, CD11b, and platelet markers (CD41, CD62P); pathway score strongly favors non-classical monocytes.
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

High expression of B cell markers (MS4A1, CD79A, BANK1, BLK), immunoglobulins (IGKC, IGHA1, etc.), and surface proteins CD19, CD22, CD21, CD27 indicates a memory B cell. CD27 and CD21 are typical for memory B cells, and the absence of monocyte markers (CD14) or CD16 Mono signature supports this identification.
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
High expression of B cell markers (MS4A1, CD79A, BANK1, BLK), immunoglobulins (IGKC, IGHA1, etc.), and surface proteins CD19, CD22, CD21, CD27 indicates a memory B cell. CD27 and CD21 are typical for memory B cells, and the absence of monocyte markers (CD14) or CD16 Mono signature supports this identification.
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
High expression of B cell markers (MS4A1, CD79A, BANK1, BLK), immunoglobulins (IGKC, IGHA1, etc.), and surface proteins CD19, CD22, CD21, CD27 indicates a memory B cell. CD27 and CD21 are typical for memory B cells, and the absence of monocyte markers (CD14) or CD16 Mono signature supports this identification.

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
High expression of B cell markers (MS4A1, CD79A, BANK1, BLK), immunoglobulins (IGKC, IGHA1, etc.), and surface proteins CD19, CD22, CD21, CD27 indicates a memory B cell. CD27 and CD21 are typical for memory B cells, and the absence of monocyte markers (CD14) or CD16 Mono signature supports this identification.

```

### output

```text
{
  "Switched memory B cell": {
    "genes": [
      "MS4A1",
      "CD79A",
      "BANK1",
      "BLK",
      "IGHA1",
      "IGHA2",
      "IGHG1",
      "IGHG2",
      "IGHG3",
      "IGHG4",
      "IGHE",
      "CD27",
      "CD22",
      "CR2",
      "TNFRSF13B",
      "TNFRSF13C",
      "POU2AF1",
      "PAX5",
      "EBF1",
      "IRF8",
      "BCL6",
      "SUGCT",
      "ADAM28",
      "SLC7A8",
      "PPIB",
      "CD69",
      "HLA-DRA",
      "HLA-DQB1",
      "HLA-DPA1",
      "HLA-DRB1",
      "CD83",
      "CXCR5",
      "CCR7",
      "S1PR1",
      "GPR18",
      "SELPLG",
      "ITGA4",
      "ITGB7",
      "ICOSL",
      "IL4R",
      "IL6R",
      "IL21R",
      "STAT3",
      "JAK3",
      "MYC",
      "MCL1"
    ],
    "description": "Class-switched memory B cells that have undergone immunoglobulin class switching and express CD27 and lack IgD."
  },
  "Unswitched memory B cell": {
    "genes": [
      "MS4A1",
      "CD79A",
      "BANK1",
      "BLK",
      "IGHD",
      "IGHM",
      "CD27",
      "CD21",
      "TNFRSF13C",
      "CD22",
      "CR2",
      "POU2AF1",
      "PAX5",
      "EBF1",
      "IRF8",
      "BCL6",
      "SUGCT",
      "ADAM28",
      "SLC7A8",
      "PPIB",
      "CD69",
      "HLA-DRA",
      "HLA-DQB1",
      "HLA-DPA1",
      "HLA-DRB1",
      "CD83",
      "CXCR5",
      "CCR7",
      "S1PR1",
      "GPR18",
      "SELPLG",
      "ITGA4",
      "ITGB7",
      "ICOSL",
      "IL4R",
      "IL6R",
      "IL21R",
      "STAT3",
      "JAK3",
      "MYC",
      "MCL1"
    ],
    "description": "Unswitched memory B cells expressing surface IgD and IgM along with CD27, typical of splenic marginal zone-like B cells."
  },
  "Plasma cell": {
    "genes": [
      "SDC1",
      "CD38",
      "MZB1",
      "JCHAIN",
      "PTPRCAP",
      "XBP1",
      "IRF4",
      "PRDM1",
      "FCRL5",
      "CD27",
      "TNFRSF17",
      "SLAMF7",
      "ITGA6",
      "TYROBP",
      "FKBP11",
      "SEC11C",
      "SSR4",
      "DNAJB9",
      "CRELD2",
      "PDIA4",
      "PDIA6",
      "HSP90B1",
      "HYOU1",
      "ERP29",
      "CANX",
      "CALR",
      "UGGT1",
      "EDEM1",
      "MANF",
      "SEL1L",
      "SYVN1",
      "DERL1",
      "VCP",
      "NPLOC4",
      "UFD1L",
      "UBE2G2",
      "AMFR",
      "OS9",
      "ERO1A",
      "PDILT",
      "CLGN",
      "PDIA5",
      "TXNDC5",
      "PDIA3",
      "HSPA5",
      "HSP90B1",
      "HSPA1A",
      "HSPA1B",
      "HSPA8"
    ],
    "description": "Antibody-secreting plasma cells with high expression of endoplasmic reticulum and secretory pathway genes, lacking CD19 and CD20."
  },
  "Naive B cell": {
    "genes": [
      "MS4A1",
      "CD79A",
      "BANK1",
      "BLK",
      "IGHD",
      "IGHM",
      "CD19",
      "CD22",
      "CR2",
      "TNFRSF13C",
      "CD72",
      "CD79B",
      "POU2AF1",
      "PAX5",
      "EBF1",
      "IRF8",
      "BCL6",
      "SUGCT",
      "ADAM28",
      "SLC7A8",
      "PPIB",
      "CD69",
      "HLA-DRA",
      "HLA-DQB1",
      "HLA-DPA1",
      "HLA-DRB1",
      "CD83",
      "CXCR5",
      "CCR7",
      "S1PR1",
      "GPR18",
      "SELPLG",
      "ITGA4",
      "ITGB7",
      "ICOSL",
      "IL4R",
      "IL6R",
      "IL21R",
      "STAT3",
      "JAK3",
      "MYC",
      "MCL1",
      "BCL2",
      "CD44",
      "SELL"
    ],
    "description": "Mature naive B cells expressing surface IgM and IgD with no memory or activation markers."
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
High expression of B cell markers (MS4A1, CD79A, BANK1, BLK), immunoglobulins (IGKC, IGHA1, etc.), and surface proteins CD19, CD22, CD21, CD27 indicates a memory B cell. CD27 and CD21 are typical for memory B cells, and the absence of monocyte markers (CD14) or CD16 Mono signature supports this identification.

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
  Switched memory B cell   : +1.563
  Unswitched memory B cell : +0.890
  Naive B cell             : +0.872
  Plasma cell              : +0.047

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
B memory
High B cell markers (MS4A1, CD79A, BANK1, BLK) and immunoglobulins, plus surface CD19, CD22, CD21, CD27 strongly indicate B memory. Pathway scores confirm switched memory B cell as the most active program. No monocyte markers (CD14, CD16) are present.
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
High expression of monocyte-specific genes (CST3, LYZ, HLA-DRA, FCN1, CD74, TYROBP) and surface proteins (CD11b, CD18, CD4, CD31, CD48) confirms CD14+ monocytes. Lack of B cell or CD16 monocyte markers excludes other options.
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
High expression of monocyte-specific genes (CST3, LYZ, HLA-DRA, FCN1, CD74, TYROBP) and surface proteins (CD11b, CD18, CD4, CD31, CD48) confirms CD14+ monocytes. Lack of B cell or CD16 monocyte markers excludes other options.
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
High expression of monocyte-specific genes (CST3, LYZ, HLA-DRA, FCN1, CD74, TYROBP) and surface proteins (CD11b, CD18, CD4, CD31, CD48) confirms CD14+ monocytes. Lack of B cell or CD16 monocyte markers excludes other options.

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
High expression of monocyte-specific genes (CST3, LYZ, HLA-DRA, FCN1, CD74, TYROBP) and surface proteins (CD11b, CD18, CD4, CD31, CD48) confirms CD14+ monocytes. Lack of B cell or CD16 monocyte markers excludes other options.

```

### output

```text
{
  "Classical Monocytes": {
    "genes": [
      "FCN1",
      "S100A8",
      "S100A9",
      "CD14",
      "LYZ",
      "CST3",
      "CCR2",
      "VCAN",
      "THBS1",
      "FPR1",
      "LGALS3",
      "MNDA",
      "CTSS",
      "PLAC8",
      "COTL1",
      "GPX1",
      "AKR1C3",
      "FCGR2A",
      "CD68",
      "CD93",
      "CD163",
      "TLR4",
      "TLR2",
      "ITGAM",
      "CSF1R",
      "IRF8"
    ],
    "description": "Classical monocytes (CD14++CD16-) are the most abundant monocyte subset in PBMC, characterized by high expression of CD14 and chemokine receptor CCR2, and they play key roles in phagocytosis and inflammation."
  },
  "Intermediate Monocytes": {
    "genes": [
      "CD14",
      "FCGR3A",
      "HLA-DRA",
      "HLA-DRB1",
      "CD74",
      "CCR2",
      "CD163",
      "TLR4",
      "TLR8",
      "IL1B",
      "TNF",
      "CCL3",
      "CCL4",
      "CXCL8",
      "CCR5",
      "CX3CR1",
      "ITGAM",
      "ITGAX",
      "CD36",
      "S100A12",
      "LYZ",
      "CST3",
      "FCGR1A",
      "FCGR2A",
      "FCGR3B"
    ],
    "description": "Intermediate monocytes (CD14++CD16+) co-express high levels of CD14 and CD16, along with MHC class II molecules, and are associated with antigen presentation and proinflammatory cytokine production."
  },
  "Non-classical Monocytes": {
    "genes": [
      "FCGR3A",
      "MS4A7",
      "LILRB2",
      "CX3CR1",
      "IFITM3",
      "CTSD",
      "C3AR1",
      "RHOC",
      "CLEC12A",
      "RNASE6",
      "TLR7",
      "NRROS",
      "LST1",
      "AIF1",
      "TLR5",
      "TREM1",
      "PLA2G7",
      "GPR84",
      "TCF7L2",
      "CD16",
      "FCGR3B",
      "SIGLEC10",
      "LILRB5",
      "GPNMB",
      "CSF1R"
    ],
    "description": "Non-classical monocytes (CD14+CD16++) express low CD14 and high CD16 (FcγRIII), patrol the vasculature, and are involved in immune surveillance and tissue repair."
  },
  "Myeloid Dendritic Cells": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "HLA-DRA",
      "HLA-DRB1",
      "CD74",
      "IRF4",
      "FLT3",
      "CCR7",
      "CCL22",
      "IL3RA",
      "CD83",
      "CD86",
      "LAMP3",
      "BATF3",
      "CLEC9A",
      "XCR1",
      "CADM1",
      "CD141",
      "THBD",
      "CLEC4A",
      "CLEC12A",
      "FAM65B",
      "SCN9A",
      "S100B"
    ],
    "description": "Myeloid dendritic cells (mDCs) are professional antigen-presenting cells in PBMC, expressing high levels of MHC class II and specific markers like CD1c and FCER1A, and are crucial for initiating T-cell responses."
  },
  "Plasmacytoid Dendritic Cells": {
    "genes": [
      "IL3RA",
      "CLEC4C",
      "LILRA4",
      "SLC15A4",
      "TLR7",
      "TLR9",
      "IRF7",
      "IRF8",
      "BCL11A",
      "TCF4",
      "NR4A1",
      "FCER1A",
      "IL3RA",
      "CD123",
      "HLA-DRA",
      "HLA-DRB1",
      "CD74",
      "CXCR3",
      "CXCL10",
      "ICOSLG",
      "PTPRS",
      "SIGLEC5",
      "SIGLECH",
      "PTGDR2",
      "CCR11"
    ],
    "description": "Plasmacytoid dendritic cells (pDCs) are specialized in type I interferon production upon viral recognition, expressing high levels of CD123 (IL3RA), CLEC4C, and TLR7/9."
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
High expression of monocyte-specific genes (CST3, LYZ, HLA-DRA, FCN1, CD74, TYROBP) and surface proteins (CD11b, CD18, CD4, CD31, CD48) confirms CD14+ monocytes. Lack of B cell or CD16 monocyte markers excludes other options.

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
  Non-classical Monocytes  : +0.589
  Plasmacytoid Dendritic Cells: +0.492
  Classical Monocytes      : +0.480
  Intermediate Monocytes   : +0.367
  Myeloid Dendritic Cells  : +0.328

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD14 Mono
High expression of classical monocyte markers (FCN1, CST3, LYZ, HLA-DR genes) and surface proteins (CD11b, CD18, CD4, CD31) confirms CD14+ monocytes. No CD16 expression is detected, excluding non-classical monocytes. Pathway scores are secondary to direct evidence.
```

