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
High expression of FCGR3A (CD16), CST3, FCN1, and AIF1 indicates non-classical monocytes. Surface proteins include CD16, CD61, and platelet markers possibly from activation. Low CD14 and absence of B cell markers rule out CD14 Mono and B memory.
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
High expression of FCGR3A (CD16), CST3, FCN1, and AIF1 indicates non-classical monocytes. Surface proteins include CD16, CD61, and platelet markers possibly from activation. Low CD14 and absence of B cell markers rule out CD14 Mono and B memory.
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
High expression of FCGR3A (CD16), CST3, FCN1, and AIF1 indicates non-classical monocytes. Surface proteins include CD16, CD61, and platelet markers possibly from activation. Low CD14 and absence of B cell markers rule out CD14 Mono and B memory.

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
High expression of FCGR3A (CD16), CST3, FCN1, and AIF1 indicates non-classical monocytes. Surface proteins include CD16, CD61, and platelet markers possibly from activation. Low CD14 and absence of B cell markers rule out CD14 Mono and B memory.

```

### output

```text
{
  "CD16+ (Non-classical) Monocytes": {
    "genes": [
      "FCGR3A",
      "LILRB1",
      "LST1",
      "RHOC",
      "LILRB2",
      "CSF1R",
      "CTSL1",
      "GPR65",
      "NAPSB",
      "SLC15A3",
      "TNFAIP6",
      "C3AR1",
      "FCGR3B",
      "SIGLEC10",
      "FAM26F",
      "FCRLA",
      "FOLR3",
      "LILRA2",
      "LILRB3",
      "LILRB4",
      "LILRB5",
      "LST1",
      "MXD1",
      "PLAUR",
      "SERPINA1",
      "SIK1B",
      "SLC2A5",
      "SLC2A6",
      "SLC7A8",
      "SPP1",
      "TLR8",
      "TNIP3",
      "TREM2",
      "TYMP",
      "ZNF704",
      "ADAP2",
      "AIF1",
      "ALOX5AP",
      "ANPEP",
      "APOBEC3A"
    ],
    "description": "Non-classical monocytes expressing high levels of FCGR3A (CD16) and low CD14, involved in patrolling endothelium and antiviral responses."
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
High expression of FCGR3A (CD16), CST3, FCN1, and AIF1 indicates non-classical monocytes. Surface proteins include CD16, CD61, and platelet markers possibly from activation. Low CD14 and absence of B cell markers rule out CD14 Mono and B memory.

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
  CD16+ (Non-classical) Monocytes: +0.687

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
High FCGR3A, CST3, FCN1, AIF1, and positive CD16 monocyte pathway score confirm non-classical monocytes. Platelet markers (CD41, CD62P) suggest activation or aggregates, common in CD16+ monocytes. Low CD14 and absence of B cell markers rule out CD14 Mono and B memory.
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

This profile shows high expression of B cell markers (MS4A1/CD20, CD79A, BANK1, BLK) and immunoglobulins (IGKC, IGHA1, etc.), along with surface proteins CD19, CD22, CD21, and CD27. CD35 (complement receptor) is the top ADT marker, characteristic of memory B cells. This combination is distinct from monocytes.
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
This profile shows high expression of B cell markers (MS4A1/CD20, CD79A, BANK1, BLK) and immunoglobulins (IGKC, IGHA1, etc.), along with surface proteins CD19, CD22, CD21, and CD27. CD35 (complement receptor) is the top ADT marker, characteristic of memory B cells. This combination is distinct from monocytes.
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
This profile shows high expression of B cell markers (MS4A1/CD20, CD79A, BANK1, BLK) and immunoglobulins (IGKC, IGHA1, etc.), along with surface proteins CD19, CD22, CD21, and CD27. CD35 (complement receptor) is the top ADT marker, characteristic of memory B cells. This combination is distinct from monocytes.

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
This profile shows high expression of B cell markers (MS4A1/CD20, CD79A, BANK1, BLK) and immunoglobulins (IGKC, IGHA1, etc.), along with surface proteins CD19, CD22, CD21, and CD27. CD35 (complement receptor) is the top ADT marker, characteristic of memory B cells. This combination is distinct from monocytes.

```

### output

```text
{
  "B_memory": {
    "genes": [
      "CD27",
      "MS4A1",
      "CD79A",
      "CD79B",
      "CD19",
      "TNFRSF13C",
      "CD37",
      "IGHM",
      "IGHD",
      "CD83",
      "BANK1",
      "RALGPS2",
      "YWHAH",
      "ITPKB",
      "SEL1L3",
      "BIRC3",
      "CR2",
      "FCER2",
      "TCL1A",
      "KLF2",
      "SOX5",
      "PIM2",
      "MYC",
      "RGS1",
      "NFKB1",
      "NFKBIE",
      "CD52",
      "CD3E",
      "CD2",
      "CD8B"
    ],
    "description": "Memory B cells in PBMC are characterized by CD27 expression and class-switched immunoglobulin, providing rapid recall responses upon re-exposure to antigen."
  },
  "B_naive": {
    "genes": [
      "IGHD",
      "IGHM",
      "MS4A1",
      "CD79A",
      "CD79B",
      "CD19",
      "CD37",
      "BANK1",
      "RALGPS2",
      "YWHAH",
      "ITPKB",
      "SEL1L3",
      "BIRC3",
      "CR2",
      "FCER2",
      "TCL1A",
      "KLF2",
      "SOX5",
      "PIM2",
      "MYC",
      "RGS1",
      "NFKB1",
      "CD52",
      "CD3E",
      "CD2",
      "CD8B",
      "CD27",
      "CD38",
      "CD40",
      "CD72"
    ],
    "description": "Naive B cells in PBMC express high levels of IgM and IgD, lack CD27, and are precursors to germinal center reactions."
  },
  "Plasma_cell": {
    "genes": [
      "SDC1",
      "MZB1",
      "JCHAIN",
      "XBP1",
      "PRDM1",
      "CD38",
      "SSR4",
      "SEC61A2",
      "FKBP11",
      "HSP90B1",
      "ENO1",
      "TFRC",
      "CCT2",
      "CCT3",
      "CCT4",
      "CCT5",
      "CCT6A",
      "CCT7",
      "CCT8",
      "HSPA5",
      "CALR",
      "PDIA6",
      "PPIB",
      "ERP29",
      "HYOU1",
      "TXN",
      "SERPINE1",
      "CD79A",
      "CD19",
      "MS4A1"
    ],
    "description": "Plasma cells in PBMC are antibody-secreting cells marked by high CD38, SDC1, and MZB1, with low or absent B cell receptor components."
  },
  "CD4_T_memory": {
    "genes": [
      "CD4",
      "IL7R",
      "CCR7",
      "SELL",
      "LEF1",
      "TCF7",
      "CD69",
      "CD28",
      "CTLA4",
      "FOXP3",
      "IL2RA",
      "ICOS",
      "PDCD1",
      "GATA3",
      "TBX21",
      "RORC",
      "BCL6",
      "CXCR5",
      "CCR5",
      "CXCR3",
      "CCR4",
      "CCR6",
      "CD38",
      "HLA-DRA",
      "HLA-DRB1",
      "CD74",
      "MKI67",
      "PCNA",
      "TIPIN",
      "CSTB"
    ],
    "description": "Memory CD4+ T cells in PBMC express IL7R and are primed for rapid responses, with subsets including central memory (CCR7+) and effector memory (CCR7-)."
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
This profile shows high expression of B cell markers (MS4A1/CD20, CD79A, BANK1, BLK) and immunoglobulins (IGKC, IGHA1, etc.), along with surface proteins CD19, CD22, CD21, and CD27. CD35 (complement receptor) is the top ADT marker, characteristic of memory B cells. This combination is distinct from monocytes.

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
  B_memory                 : +0.739
  B_naive                  : +0.735
  Plasma_cell              : +0.197
  CD4_T_memory             : -0.048

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
B memory
High expression of B cell markers (MS4A1, CD79A, BANK1) and immunoglobulins, along with surface proteins CD19, CD22, CD21, and CD27. CD35 (complement receptor) is the top ADT marker, characteristic of memory B cells. Pathway scores show high B_memory activity. No monocyte markers.
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

The gene expression profile (high levels of CST3, LYZ, HLA-DR genes, CD74, FCN1, TYROBP) and surface protein markers (CD11b, CD18, CD31, CD45, CLEC12A, CD172a) are characteristic of classical CD14+ monocytes. The absence of B cell markers (e.g., CD19, CD20) and CD16 expression supports this identification.
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
The gene expression profile (high levels of CST3, LYZ, HLA-DR genes, CD74, FCN1, TYROBP) and surface protein markers (CD11b, CD18, CD31, CD45, CLEC12A, CD172a) are characteristic of classical CD14+ monocytes. The absence of B cell markers (e.g., CD19, CD20) and CD16 expression supports this identification.
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
The gene expression profile (high levels of CST3, LYZ, HLA-DR genes, CD74, FCN1, TYROBP) and surface protein markers (CD11b, CD18, CD31, CD45, CLEC12A, CD172a) are characteristic of classical CD14+ monocytes. The absence of B cell markers (e.g., CD19, CD20) and CD16 expression supports this identification.

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
The gene expression profile (high levels of CST3, LYZ, HLA-DR genes, CD74, FCN1, TYROBP) and surface protein markers (CD11b, CD18, CD31, CD45, CLEC12A, CD172a) are characteristic of classical CD14+ monocytes. The absence of B cell markers (e.g., CD19, CD20) and CD16 expression supports this identification.

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
      "LGALS2",
      "CFLAR",
      "TREM1",
      "CD33",
      "IL1B",
      "TNF",
      "CCL2",
      "CCL7",
      "CCL3",
      "CCL4",
      "CXCL8",
      "CXCL2",
      "SERPINA1",
      "PLA2G7",
      "LILRB2",
      "LILRB3",
      "CD300E",
      "CD300C",
      "CD300A",
      "CLEC7A",
      "CLEC4E",
      "CLEC12A",
      "CLEC5A",
      "TLR2",
      "TLR4",
      "TLR8",
      "NLRP3",
      "PYCARD",
      "IL1R2",
      "IL1RN",
      "SIGLEC7",
      "SIGLEC14",
      "FCGR2A",
      "FCGR2B",
      "FCGR3A",
      "CX3CR1",
      "CCR2",
      "ACKR1",
      "ACKR2",
      "ACKR3",
      "ACKR4",
      "ACKR5"
    ],
    "description": "Classical CD14++ monocytes are the most abundant monocytes in PBMC, expressing high levels of CD14 and low levels of CD16, and are involved in phagocytosis and pro-inflammatory responses."
  },
  "Non-classical Monocytes": {
    "genes": [
      "FCGR3A",
      "CD16",
      "CX3CR1",
      "CDKN1C",
      "AQP9",
      "RHOC",
      "CTSL",
      "GPR56",
      "PRDM1",
      "IRF4",
      "HMOX1",
      "FCGR2C",
      "MS4A7",
      "TLR7",
      "TLR9",
      "IFNGR1",
      "IFNGR2",
      "IL10",
      "IL13RA1",
      "CCR5",
      "CXCL9",
      "CXCL10",
      "CXCL11",
      "CXCL12",
      "CXCL13",
      "CXCL14",
      "CXCL16",
      "CXCL17",
      "CX3CR1",
      "ITGAL",
      "ITGAM",
      "ITGAX",
      "ITGB2",
      "ITGB7",
      "PECAM1",
      "SELPLG",
      "SELL",
      "SELP",
      "SELENBP1",
      "SELENOI",
      "SELENOP",
      "SELENOS",
      "SELENOT",
      "SELENOW",
      "SELENOF",
      "SELENOH",
      "SELENOI",
      "SELENOK",
      "SELENOM",
      "SELENON",
      "SELENOO",
      "SELENOP",
      "SELENOS",
      "SELENOT",
      "SELENOV",
      "SELENOW",
      "SELENOX"
    ],
    "description": "Non-classical CD16++ monocytes patrol the vasculature, scavenge debris, and produce anti-inflammatory cytokines; they express high levels of FCGR3A (CD16) and low levels of CD14."
  },
  "Intermediate Monocytes": {
    "genes": [
      "CD14",
      "FCGR3A",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DQB1",
      "HLA-DPB1",
      "HLA-DPA1",
      "CD86",
      "CD40",
      "TLR2",
      "TLR4",
      "TLR8",
      "IL6",
      "IL1B",
      "TNF",
      "CCL3",
      "CCL4",
      "CCL5",
      "CXCL8",
      "CXCL10",
      "CXCL9",
      "CXCL11",
      "CCR2",
      "CCR5",
      "CX3CR1",
      "FCGR1A",
      "FCGR1B",
      "FCGR2A",
      "FCGR2B",
      "FCGR2C",
      "FCGR3A",
      "FCGR3B",
      "CSF1R",
      "CSF2RA",
      "CSF2RB",
      "CSF3R",
      "IL3RA",
      "IL5RA",
      "IL6R",
      "IL6ST",
      "IL7R",
      "IL7",
      "IL15",
      "IL15RA",
      "IL18",
      "IL18R1",
      "IL18RAP",
      "IL1R1",
      "IL1R2",
      "IL1RL1",
      "IL1RL2"
    ],
    "description": "Intermediate monocytes (CD14+CD16+) exhibit both classical and non-classical features, with high antigen-presenting capacity and production of inflammatory cytokines."
  },
  "Myeloid Dendritic Cells": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "CD1A",
      "CD1B",
      "CD1D",
      "CD1E",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DQB1",
      "HLA-DPB1",
      "HLA-DPA1",
      "HLA-DMA",
      "HLA-DMB",
      "HLA-DOA",
      "HLA-DOB",
      "CD74",
      "LAMP3",
      "CCR7",
      "CD83",
      "CD86",
      "CD40",
      "CD80",
      "TLR4",
      "TLR8",
      "TLR9",
      "TLR3",
      "TLR7",
      "IRF4",
      "IRF8",
      "IRF1",
      "IRF2",
      "IRF3",
      "IRF5",
      "IRF6",
      "IRF7",
      "IRF9",
      "IRF10",
      "IRF11",
      "IRF12",
      "IRF13",
      "IRF14",
      "IRF15",
      "IRF16",
      "IRF17",
      "IRF18",
      "IRF19",
      "IRF20",
      "IRF21",
      "IRF22"
    ],
    "description": "Myeloid dendritic cells (mDCs) are antigen-presenting cells expressing CD1c and FCER1A, and are efficient at capturing and presenting antigens to T cells."
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
The gene expression profile (high levels of CST3, LYZ, HLA-DR genes, CD74, FCN1, TYROBP) and surface protein markers (CD11b, CD18, CD31, CD45, CLEC12A, CD172a) are characteristic of classical CD14+ monocytes. The absence of B cell markers (e.g., CD19, CD20) and CD16 expression supports this identification.

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
  Myeloid Dendritic Cells  : +0.586
  Intermediate Monocytes   : +0.274
  Classical Monocytes      : +0.216
  Non-classical Monocytes  : +0.161

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD14 Mono
The gene expression (CST3, LYZ, HLA-DR, FCN1) and surface markers (CD11b, CD18, CD31, CLEC12A) strongly support classical CD14+ monocytes. The high pathway score for myeloid dendritic cells may reflect shared activation markers, but the overall profile, including absence of CD16 and B cell markers, confirms CD14 Mono.
```

