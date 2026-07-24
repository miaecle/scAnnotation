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

Top genes (ranked by population-relative z-score):
    1. AC084782.2 (15.324)
    2. AC007556.1 (14.617)
    3. TH2LCRR (13.583)
    4. RTP1 (10.444)
    5. AC106900.1 (8.387)
    6. SLIT2 (7.891)
    7. AC068946.2 (7.226)
    8. NHLH2 (6.899)
    9. AC090952.2 (6.458)
   10. GOLGA8K (6.457)
   11. A2ML1 (6.399)
   12. AC096772.1 (6.227)
   13. SLC2A12 (5.924)
   14. LINC01526 (5.881)
   15. KANK4 (5.805)
   16. AF127936.1 (5.598)
   17. LINC00337 (5.500)
   18. AC145098.1 (5.140)
   19. MESP2 (5.039)
   20. FAM3D (4.832)

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

The presence of CD16, CD11b, and CD18 suggests a monocyte lineage, with CD16 specifically indicating non-classical monocytes. Strong platelet markers (CD41, CD62P, CD61) likely reflect platelet-monocyte aggregates common in PBMC preparations. Absence of CD14 and B cell markers further supports CD16+ monocytes over CD14+ monocytes or B memory cells.
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
The presence of CD16, CD11b, and CD18 suggests a monocyte lineage, with CD16 specifically indicating non-classical monocytes. Strong platelet markers (CD41, CD62P, CD61) likely reflect platelet-monocyte aggregates common in PBMC preparations. Absence of CD14 and B cell markers further supports CD16+ monocytes over CD14+ monocytes or B memory cells.
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
      "LST1",
      "AIF1",
      "MS4A7",
      "RHOC",
      "FCGRT",
      "SIGLEC10",
      "LILRB5",
      "CX3CR1",
      "ITGAL",
      "CD86",
      "CSF1R",
      "CD53",
      "FGR",
      "LYN",
      "SYK",
      "TYROBP",
      "HCST",
      "NCF1",
      "CYBA",
      "RAC2",
      "VAV1",
      "WAS",
      "PTPRC"
    ],
    "description": "Non-classical monocytes are CD16+CD14- cells that patrol the vasculature and are involved in antiviral immunity and tissue repair."
  },
  "Classical monocytes": {
    "genes": [
      "CD14",
      "S100A8",
      "S100A9",
      "S100A12",
      "LYZ",
      "FCN1",
      "CST3",
      "FOS",
      "JUN",
      "IL1B",
      "CCL3",
      "CCL4",
      "CD68",
      "CD163",
      "MRC1",
      "MERTK",
      "CTSB",
      "CTSS",
      "LILRB2",
      "LILRA3",
      "TLR2",
      "TLR4",
      "CD33",
      "FCGR2A",
      "FCGR2B",
      "ITGAM"
    ],
    "description": "Classical monocytes are CD14+CD16- cells that are pro-inflammatory and phagocytic, responding to infections."
  },
  "Intermediate monocytes": {
    "genes": [
      "CD14",
      "FCGR3A",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DQA1",
      "HLA-DQB1",
      "CD74",
      "CX3CR1",
      "CD86",
      "ITGAL",
      "ICAM1",
      "VEGFA",
      "IL1RN",
      "TNF",
      "CCL2",
      "CCL7",
      "CCL8",
      "CXCL2",
      "CXCL3",
      "IL6",
      "IL10",
      "CDKN1C",
      "LST1",
      "AIF1",
      "RHOC"
    ],
    "description": "Intermediate monocytes are CD14+CD16+ cells with mixed features, involved in antigen presentation and inflammation."
  },
  "Myeloid dendritic cells": {
    "genes": [
      "FCER1A",
      "CD1C",
      "CD1E",
      "CD1A",
      "CLEC10A",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DQA1",
      "HLA-DQB1",
      "CD74",
      "CST3",
      "BIRC3",
      "IRF4",
      "IRF8",
      "ZBTB46",
      "FLT3",
      "ITGAX",
      "CD86",
      "CD40",
      "PTPRC",
      "CD83",
      "IL13RA1",
      "IL4R",
      "SNX17",
      "LAMP3"
    ],
    "description": "Myeloid dendritic cells are antigen-presenting cells that prime T-cell responses and express CD1c and FCER1A."
  },
  "Plasmacytoid dendritic cells": {
    "genes": [
      "LILRA4",
      "CLEC4C",
      "IL3RA",
      "TCF4",
      "IRF4",
      "IRF8",
      "JCHAIN",
      "PTPRS",
      "SCT",
      "NRP1",
      "GPR174",
      "TLR7",
      "TLR9",
      "MYD88",
      "IRAK1",
      "IRAK4",
      "TRAF6",
      "IRF7",
      "IRF5",
      "IFI27",
      "IFI44L",
      "IFI6",
      "MX1",
      "OAS1"
    ],
    "description": "Plasmacytoid dendritic cells are specialized in type I interferon production in response to viruses, expressing CD123 and CLEC4C."
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
The presence of CD16, CD11b, and CD18 suggests a monocyte lineage, with CD16 specifically indicating non-classical monocytes. Strong platelet markers (CD41, CD62P, CD61) likely reflect platelet-monocyte aggregates common in PBMC preparations. Absence of CD14 and B cell markers further supports CD16+ monocytes over CD14+ monocytes or B memory cells.

Top 30 cell-specific genes by z-score vs. population (higher = more specific to this cell):
    1. AC084782.2  z=+15.32
    2. AC007556.1  z=+14.62
    3. TH2LCRR     z=+13.58
    4. RTP1        z=+10.44
    5. AC106900.1  z=+8.39
    6. SLIT2       z=+7.89
    7. AC068946.2  z=+7.23
    8. NHLH2       z=+6.90
    9. AC090952.2  z=+6.46
   10. GOLGA8K     z=+6.46
   11. A2ML1       z=+6.40
   12. AC096772.1  z=+6.23
   13. SLC2A12     z=+5.92
   14. LINC01526   z=+5.88
   15. KANK4       z=+5.80
   16. AF127936.1  z=+5.60
   17. LINC00337   z=+5.50
   18. AC145098.1  z=+5.14
   19. MESP2       z=+5.04
   20. FAM3D       z=+4.83
   21. AOC2        z=+4.54
   22. CDKN1C      z=+4.53
   23. LINC00599   z=+4.35
   24. L1TD1       z=+4.08
   25. TENT5B      z=+4.07
   26. C1QA        z=+3.94
   27. DNMBP-AS1   z=+3.90
   28. AC092384.1  z=+3.76
   29. MMEL1       z=+3.67
   30. AC093525.3  z=+3.66

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
  Non-classical monocytes  : +1.133
  Intermediate monocytes   : +0.629
  Myeloid dendritic cells  : +0.241
  Plasmacytoid dendritic cells: +0.134
  Classical monocytes      : +0.124

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
Pathway scores strongly favor non-classical (CD16+) monocytes, surface proteins lack CD14 and include platelet markers consistent with aggregates, and top genes like C1QA align with monocyte lineage. No B cell markers appear.
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

Top genes (ranked by population-relative z-score):
    1. AC005618.2 (51.362)
    2. PCDHB14 (25.935)
    3. AC110760.2 (14.733)
    4. IGHE (14.090)
    5. AC104123.1 (14.039)
    6. SMCO2 (13.412)
    7. KCNMA1-AS1 (12.930)
    8. KCNJ1 (9.842)
    9. AL390066.1 (8.632)
   10. FNDC5 (7.450)
   11. SHISA8 (7.045)
   12. EYA2 (6.904)
   13. ESRRG (6.890)
   14. GNG3 (6.839)
   15. SSPN (6.806)
   16. TLX2 (6.349)
   17. MARC2 (6.319)
   18. AC034102.5 (6.168)
   19. C12orf74 (6.005)
   20. BTNL9 (5.695)

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
  "Memory B cell (switched)": {
    "genes": [
      "MS4A1",
      "CD79A",
      "CD79B",
      "CD19",
      "CD22",
      "PAX5",
      "BANK1",
      "BLK",
      "CD72",
      "FCER2",
      "CR2",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DQB1",
      "IGHG1",
      "IGHG2",
      "IGHG3",
      "IGHG4",
      "IGHA1",
      "IGHA2",
      "CD27",
      "TNFRSF13C",
      "TNFRSF17",
      "TCL1A",
      "VPREB3",
      "SPIB",
      "EBF1",
      "IRF8",
      "POU2F2",
      "BCL11A",
      "MYB"
    ],
    "description": "A memory B cell subtype that has undergone class switching, expressing surface IgG or IgA and CD27."
  },
  "Memory B cell (unswitched)": {
    "genes": [
      "MS4A1",
      "CD79A",
      "CD79B",
      "CD19",
      "CD22",
      "PAX5",
      "BANK1",
      "BLK",
      "CD72",
      "FCER2",
      "CR2",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DQB1",
      "IGHM",
      "IGHD",
      "CD27",
      "TNFRSF13C",
      "TNFRSF17",
      "TCL1A",
      "VPREB3",
      "SPIB",
      "EBF1",
      "IRF8",
      "POU2F2",
      "BCL11A",
      "MYB",
      "CD24",
      "CD38",
      "CD1C",
      "CD9"
    ],
    "description": "A memory B cell subtype that expresses IgM and IgD with low CD38 and retains the ability to undergo class switching."
  },
  "Plasmablast": {
    "genes": [
      "SDC1",
      "XBP1",
      "MZB1",
      "JCHAIN",
      "CD38",
      "DERL3",
      "FCRL5",
      "SLAMF7",
      "PTPRC",
      "PRDM1",
      "IRF4",
      "TCP1",
      "HSPA5",
      "PDIA4",
      "FKBP11",
      "TRBC1",
      "TRBC2",
      "IGLL1",
      "IGLL5",
      "CD27",
      "CD79A",
      "CD79B",
      "CD19",
      "MS4A1",
      "PAX5",
      "BANK1",
      "TNFRSF13C",
      "TNFRSF17",
      "CD22",
      "FCER2"
    ],
    "description": "A terminally differentiated antibody-secreting B cell with high CD38 and SDC1 expression, often found in peripheral blood."
  },
  "CD4+ Tfh": {
    "genes": [
      "CXCR5",
      "PDCD1",
      "ICOS",
      "BCL6",
      "TIGIT",
      "IL21",
      "CXCL13",
      "BTLA",
      "TCF7",
      "CD28",
      "CD4",
      "FOXP1",
      "MAF",
      "TOX",
      "BCL2",
      "STAT3",
      "IL6ST",
      "IL4R",
      "IFNGR1",
      "LAG3",
      "CTLA4",
      "CD40LG",
      "CD40",
      "TNFRSF4",
      "TNFRSF8",
      "ICAM1",
      "CCR5",
      "CCR7",
      "SELL",
      "CD27"
    ],
    "description": "A CD4+ T helper subtype specialized in providing help to B cells within germinal centers, marked by CXCR5 and PD-1."
  },
  "NK cell": {
    "genes": [
      "NKG7",
      "GNLY",
      "PRF1",
      "GZMB",
      "GZMA",
      "KLRD1",
      "KLRK1",
      "KIR2DL3",
      "KIR3DL1",
      "NCR1",
      "FCGR3A",
      "CD16",
      "CD56",
      "NCAM1",
      "KLRC1",
      "KLRC2",
      "KLRC3",
      "KLRB1",
      "CD226",
      "CD244",
      "CD2",
      "CD7",
      "CD8A",
      "CD8B",
      "XCL1",
      "XCL2",
      "GZMH",
      "GZMM",
      "GZMK",
      "CST7"
    ],
    "description": "An innate lymphoid cell that kills infected or malignant cells without prior sensitization, characterized by cytotoxic granules and NK receptors."
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

Top 30 cell-specific genes by z-score vs. population (higher = more specific to this cell):
    1. AC005618.2  z=+51.36
    2. PCDHB14     z=+25.94
    3. AC110760.2  z=+14.73
    4. IGHE        z=+14.09
    5. AC104123.1  z=+14.04
    6. SMCO2       z=+13.41
    7. KCNMA1-AS1  z=+12.93
    8. KCNJ1       z=+9.84
    9. AL390066.1  z=+8.63
   10. FNDC5       z=+7.45
   11. SHISA8      z=+7.04
   12. EYA2        z=+6.90
   13. ESRRG       z=+6.89
   14. GNG3        z=+6.84
   15. SSPN        z=+6.81
   16. TLX2        z=+6.35
   17. MARC2       z=+6.32
   18. AC034102.5  z=+6.17
   19. C12orf74    z=+6.01
   20. BTNL9       z=+5.69
   21. RASSF6      z=+5.68
   22. AP002990.1  z=+5.59
   23. PLA2G2D     z=+5.53
   24. AC092040.1  z=+5.52
   25. KCNJ13      z=+5.45
   26. COCH        z=+5.37
   27. AK8         z=+5.29
   28. AC107067.1  z=+5.25
   29. LINC00574   z=+5.24
   30. EBI3        z=+5.24

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
  Memory B cell (switched) : +1.876
  Memory B cell (unswitched): +1.310
  Plasmablast              : +0.674
  CD4+ Tfh                 : -0.062
  NK cell                  : -0.491

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
B memory
Surface proteins CD19, CD22, CD21, CD27 and pathway scores (Memory B cell switched: +1.876) confirm B memory. IGHE and other B-lineage genes support this, with no monocyte markers evident.
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

Top genes (ranked by population-relative z-score):
    1. GGTLC3 (16.729)
    2. AL445623.2 (14.871)
    3. AC093849.1 (10.226)
    4. OR8H1 (9.192)
    5. TMEM233 (8.276)
    6. AGBL1 (7.474)
    7. MSX1 (6.156)
    8. AC007349.4 (6.086)
    9. AC079171.1 (5.721)
   10. AL512506.3 (5.617)
   11. AC004554.2 (5.248)
   12. IL19 (5.162)
   13. TGM2 (4.564)
   14. MYBPH (4.441)
   15. AL157884.2 (4.275)
   16. AC092159.2 (4.188)
   17. OLFM1 (4.141)
   18. AC008440.1 (3.877)
   19. MAP3K20-AS1 (3.653)
   20. RHBDL2 (3.573)

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
      "LYZ",
      "S100A8",
      "S100A9",
      "CCL2",
      "CCR2",
      "FCN1",
      "VCAN",
      "CSF1R",
      "CD33",
      "CST3",
      "FOS",
      "JUN",
      "TYMP",
      "THBS1",
      "FTL",
      "FTH1",
      "CTSB",
      "CTSD",
      "LAPTM5",
      "IFITM3",
      "NAMPT",
      "MARCKS",
      "MGLL",
      "PLBD1",
      "PSAP",
      "RASGRP3",
      "S100A11",
      "S100A12",
      "SEPTIN10",
      "SERPINA1",
      "SLC11A1",
      "TIMP1",
      "TREM1",
      "TSPO",
      "VNN2",
      "ZFP36L2"
    ],
    "description": "Classical monocytes (CD14++CD16-) are phagocytic cells that patrol the vasculature and initiate inflammatory responses."
  },
  "Intermediate Monocyte": {
    "genes": [
      "CD14",
      "FCGR3A",
      "CD163",
      "LILRB2",
      "HLA-DRA",
      "CTSS",
      "S100A6",
      "S100A10",
      "ANXA1",
      "ANXA2",
      "FABP4",
      "FABP5",
      "LST1",
      "MPEG1",
      "MNDA",
      "MYO1F",
      "NCF2",
      "NFE2L2",
      "PLTP",
      "PTPN6",
      "SDCBP",
      "SIGLEC1",
      "SLC40A1",
      "STAB1",
      "TLR7",
      "TLR8",
      "TNFAIP2",
      "TUBB2A"
    ],
    "description": "Intermediate monocytes (CD14+CD16+) are pro-inflammatory cells with high antigen-presenting capacity and elevated HLA-DR expression."
  },
  "Non-classical Monocyte": {
    "genes": [
      "FCGR3A",
      "CDKN1C",
      "CX3CR1",
      "AXL",
      "ITGAL",
      "LST1",
      "RHOC",
      "TCF7L2",
      "RHOB",
      "ZFP36",
      "FHL1",
      "HES1",
      "IGFBP4",
      "KLF2",
      "KLF4",
      "MARCH1",
      "MARCKSL1",
      "MAFB",
      "MT1E",
      "MT2A",
      "NR4A1",
      "NR4A2",
      "PANX1",
      "PDK4",
      "PIM1",
      "PPP1R15A",
      "RGS1",
      "RGS2",
      "S100A4",
      "S100A6",
      "S100A10",
      "SOCS3",
      "TXNIP",
      "VDR",
      "ZFP36L1"
    ],
    "description": "Non-classical monocytes (CD14dimCD16++) are patrolling cells that survey endothelium and promote tissue repair with a unique transcriptome enriched for cytoskeletal and anti-apoptotic genes."
  },
  "Myeloid Dendritic Cell": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "ITGAX",
      "HLA-DRA",
      "HLA-DQB1",
      "HLA-DQA1",
      "HLA-DRB1",
      "CD74",
      "FCGR2B",
      "LILRB1",
      "LILRB2",
      "CLEC4A",
      "CLEC7A",
      "CLEC12A",
      "CD86",
      "TLR7",
      "TLR8",
      "IRF4",
      "IRF8",
      "BATF3",
      "IDO1",
      "ADAMDEC1",
      "RAB11FIP1",
      "RAB32",
      "CSF2RA",
      "IL3RA"
    ],
    "description": "Myeloid dendritic cells (CD1c+) are professional antigen-presenting cells that prime T-cell responses and are commonly confused with monocytes due to shared myeloid lineage."
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

Top 30 cell-specific genes by z-score vs. population (higher = more specific to this cell):
    1. GGTLC3      z=+16.73
    2. AL445623.2  z=+14.87
    3. AC093849.1  z=+10.23
    4. OR8H1       z=+9.19
    5. TMEM233     z=+8.28
    6. AGBL1       z=+7.47
    7. MSX1        z=+6.16
    8. AC007349.4  z=+6.09
    9. AC079171.1  z=+5.72
   10. AL512506.3  z=+5.62
   11. AC004554.2  z=+5.25
   12. IL19        z=+5.16
   13. TGM2        z=+4.56
   14. MYBPH       z=+4.44
   15. AL157884.2  z=+4.27
   16. AC092159.2  z=+4.19
   17. OLFM1       z=+4.14
   18. AC008440.1  z=+3.88
   19. MAP3K20-AS1  z=+3.65
   20. RHBDL2      z=+3.57
   21. DNER        z=+3.39
   22. PPP1R26-AS1  z=+3.38
   23. NYNRIN      z=+3.30
   24. AC100803.1  z=+3.29
   25. TMEM249     z=+3.22
   26. NID1        z=+3.13
   27. AC004069.1  z=+3.12
   28. TMED7-TICAM2  z=+3.06
   29. GAS6        z=+3.05
   30. SIGLEC12    z=+3.03

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
  Myeloid Dendritic Cell   : +0.763
  Intermediate Monocyte    : +0.425
  Classical Monocyte       : +0.410
  Non-classical Monocyte   : +0.399

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD14 Mono
High expression of platelet markers (CD41, CLEC2, CD62P) likely reflects monocyte-platelet aggregates, a common PBMC artifact, while myeloid markers (CD11b, CD35, CD93) and monocyte-associated genes (IL19, TGM2, GAS6) confirm monocyte identity. Pathway scores favor classical/intermediate monocytes over non-classical (CD16+), and no B cell markers are present.
```

