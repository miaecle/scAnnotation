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

The top surface proteins include B cell markers CD19, CD22, CD21, and CD27, along with IGHE expression (immunoglobulin heavy epsilon), indicating a memory B cell profile. Monocyte markers CD14 or CD16 are absent.
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

## Record 4

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
  "Non-classical Monocytes": {
    "genes": [
      "FCGR3A",
      "LST1",
      "CX3CR1",
      "LILRB1",
      "LILRB2",
      "CDKN1C",
      "RHOC",
      "S100A10",
      "S100A11",
      "SERPINA1",
      "TXN",
      "TKT",
      "PGD",
      "GCLC",
      "GCLM",
      "FTL",
      "FTH1",
      "SOD2",
      "CAT",
      "GPX1",
      "PRDX1",
      "HMOX1",
      "NAMPT",
      "CD36",
      "FCN1",
      "CLEC12A",
      "CD300E",
      "CD300LF",
      "IFITM3",
      "IFITM1"
    ],
    "description": "Non-classical monocytes (CD14lowCD16+) are patrolling monocytes that survey the vasculature and are involved in inflammation resolution, expressing high levels of FCGR3A and CX3CR1."
  },
  "Classical Monocytes": {
    "genes": [
      "CD14",
      "LYZ",
      "S100A8",
      "S100A9",
      "VCAN",
      "FCN1",
      "CLEC12A",
      "CD36",
      "CST3",
      "TSPO",
      "FOS",
      "EGR1",
      "NFKBIA",
      "TNF",
      "CCL3",
      "CCL4",
      "IL1B",
      "TNFAIP6",
      "CD83",
      "CD86",
      "HLA-DRA",
      "HLA-DRB1",
      "CD74",
      "CTSS",
      "CTSB",
      "CSTB",
      "PSAP",
      "NPC2",
      "GNS",
      "CD68"
    ],
    "description": "Classical monocytes (CD14+CD16-) are the most abundant monocyte subset, highly phagocytic and expressing high levels of CD14 and S100 family proteins."
  },
  "NK cells": {
    "genes": [
      "NKG7",
      "GNLY",
      "PRF1",
      "GZMB",
      "KLRD1",
      "KLRK1",
      "NCR1",
      "NCR3",
      "CD247",
      "FCGR3A",
      "SH2D1B",
      "CXCR1",
      "CXCR2",
      "CCL3",
      "CCL4",
      "XCL1",
      "XCL2",
      "IL2RB",
      "IL12RB2",
      "IFNG",
      "TBX21",
      "EOMES",
      "ZEB2",
      "PRDM1",
      "MYBL1",
      "CLIC3",
      "ITGAL",
      "ITGB2",
      "CD2",
      "CD226"
    ],
    "description": "Natural killer cells are innate lymphocytes that provide rapid responses against infected or stressed cells, characterized by expression of NKG7, GNLY, and perforin."
  },
  "Intermediate Monocytes": {
    "genes": [
      "CD14",
      "FCGR3A",
      "HLA-DRA",
      "HLA-DRB1",
      "CD86",
      "CD74",
      "CTSS",
      "CTSB",
      "CST3",
      "CD40",
      "ICAM1",
      "IL1B",
      "TNF",
      "CCL3",
      "CCL4",
      "CCR2",
      "CCR5",
      "CX3CR1",
      "CXCR4",
      "IRF4",
      "IRF8",
      "MAFB",
      "CEBPB",
      "FOS",
      "JUN",
      "EGR1",
      "NFKBIA",
      "TNFAIP3",
      "BIRC3",
      "NFKBIE"
    ],
    "description": "Intermediate monocytes (CD14+CD16+) exhibit both classical and non-classical features, with high antigen-presenting capacity and pro-inflammatory cytokine production."
  }
}
```

## Record 5

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
  "Classical CD14+ Monocyte": {
    "genes": [
      "CD14",
      "FCGR1A",
      "S100A8",
      "S100A9",
      "LYZ",
      "FCN1",
      "CTSS",
      "CSF1R",
      "CEBPA",
      "CD33",
      "CD68",
      "MNDA",
      "PLAC8",
      "STX11",
      "TNFAIP6",
      "IL1B",
      "CCL2",
      "CCL7",
      "CCL8",
      "CCL13",
      "CCR2",
      "SELL",
      "LST1",
      "FCER1G",
      "TREM1",
      "NLRP3",
      "CASP1",
      "IL18",
      "MYD88",
      "TLR2",
      "TLR4",
      "CD36",
      "CD163",
      "CD206"
    ],
    "description": "Classical monocytes characterized by high CD14 expression and lack of CD16, functioning primarily in phagocytosis and pro-inflammatory cytokine production."
  },
  "Intermediate CD14+CD16+ Monocyte": {
    "genes": [
      "CD14",
      "FCGR3A",
      "CDKN1C",
      "HLA-DRA",
      "CD86",
      "CCR2",
      "CX3CR1",
      "CCR5",
      "IL10",
      "TNF",
      "IL6",
      "CD40",
      "TLR7",
      "TLR8",
      "IRF4",
      "IRF5",
      "MAFB",
      "BCL6",
      "FOS",
      "JUN",
      "EGR1",
      "NR4A1",
      "SEMA4A",
      "GPR34",
      "LPAR5",
      "P2RY14",
      "S100A12",
      "RGS1"
    ],
    "description": "Intermediate monocytes expressing both CD14 and CD16 (FCGR3A) with enhanced antigen presentation capacity and inflammatory profile."
  },
  "Non-classical CD16+ Monocyte": {
    "genes": [
      "FCGR3A",
      "CX3CR1",
      "FCN1",
      "LST1",
      "AIF1",
      "C1QA",
      "C1QB",
      "C1QC",
      "MAFB",
      "SELENOP",
      "CLEC4E",
      "CD36",
      "CD163",
      "MRC1",
      "MSR1",
      "STAB1",
      "FOLR2",
      "MERTK",
      "TGM2",
      "EGR2",
      "MAF",
      "JDP2",
      "CCL3",
      "CCL4",
      "CCL5"
    ],
    "description": "Non-classical monocytes with low CD14 and high CD16 (FCGR3A), involved in patrolling vasculature and anti-inflammatory responses."
  },
  "Myeloid Dendritic Cell (CD1c+ DC)": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "ITGAX",
      "CD33",
      "CD86",
      "CD83",
      "CCR7",
      "CCL19",
      "CCL22",
      "LAMP3",
      "FSCN1",
      "BATF3",
      "IRF8",
      "ZBTB46",
      "TLR3",
      "TLR8",
      "MYCL1",
      "CEBPD",
      "SPI1",
      "IRF4",
      "FLT3",
      "CSF1R",
      "MARCH1",
      "CD74",
      "HLA-DRA",
      "HLA-DPB1",
      "HLA-DQB1"
    ],
    "description": "Conventional type 2 dendritic cells (cDC2) expressing CD1c, specialized in presenting antigens to CD4+ T cells and modulating immune responses."
  }
}
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
The top surface proteins include B cell markers CD19, CD22, CD21, and CD27, along with IGHE expression (immunoglobulin heavy epsilon), indicating a memory B cell profile. Monocyte markers CD14 or CD16 are absent.
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
The top surface proteins include B cell markers CD19, CD22, CD21, and CD27, along with IGHE expression (immunoglobulin heavy epsilon), indicating a memory B cell profile. Monocyte markers CD14 or CD16 are absent.

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
The top surface proteins include B cell markers CD19, CD22, CD21, and CD27, along with IGHE expression (immunoglobulin heavy epsilon), indicating a memory B cell profile. Monocyte markers CD14 or CD16 are absent.

```

### output

```text
{
  "Switched memory B cell": {
    "genes": [
      "CD27",
      "CD19",
      "MS4A1",
      "CD22",
      "CR2",
      "CD40",
      "IGHA1",
      "IGHG1",
      "IGHG3",
      "IGHG4",
      "IGHE",
      "AICDA",
      "BCL6",
      "CD79A",
      "CD79B",
      "PAX5",
      "BANK1",
      "FCRL2",
      "FCRL5",
      "MEF2C",
      "BCL11A",
      "SPIB",
      "TCF4",
      "CD72",
      "NFATC1",
      "IRF4",
      "CD86",
      "CD83",
      "ICOSL"
    ],
    "description": "Memory B cell that has undergone class switching, expressing IgG, IgA, or IgE and CD27, involved in recall responses."
  },
  "Unswitched memory B cell": {
    "genes": [
      "CD27",
      "IGHD",
      "IGHM",
      "CD19",
      "MS4A1",
      "CD22",
      "CR2",
      "CD40",
      "CD79A",
      "CD79B",
      "PAX5",
      "BANK1",
      "BCL11A",
      "SPIB",
      "CD72",
      "CD83",
      "CD86",
      "ICOSL",
      "AICDA",
      "BCL6",
      "MEF2C",
      "TCF4",
      "NFATC1",
      "IRF4",
      "PTPN6",
      "SYK",
      "BLNK",
      "FYB2",
      "PIK3CD"
    ],
    "description": "Memory B cell retaining IgM and IgD expression with CD27, representing early memory responses."
  },
  "Naive B cell": {
    "genes": [
      "FCER2",
      "TCL1A",
      "IGHD",
      "IGHM",
      "CD19",
      "MS4A1",
      "CD22",
      "CR2",
      "CD72",
      "CD79A",
      "CD79B",
      "PAX5",
      "BANK1",
      "BCL11A",
      "EBF1",
      "SPIB",
      "PTPN6",
      "SYK",
      "BLNK",
      "FYB2",
      "PIK3CD",
      "PIK3R1",
      "CD40",
      "CD80",
      "IL4R",
      "IGLL1",
      "VPREB3"
    ],
    "description": "Mature B cell that has not yet encountered antigen, characterized by high IgD and IgM, CD27 negativity, and CD23 expression."
  },
  "Plasma cell": {
    "genes": [
      "SDC1",
      "MZB1",
      "XBP1",
      "PRDM1",
      "TNFRSF17",
      "CD38",
      "JCHAIN",
      "IRF4",
      "DERL3",
      "HSP90B1",
      "FKBP11",
      "PPIB",
      "SSR3",
      "SEC61B",
      "CALR",
      "CANX",
      "PDIA4",
      "PDIA6",
      "ERP44",
      "TMX1",
      "COPB2",
      "ARCN1",
      "IGHG1",
      "IGHA1",
      "IGHE"
    ],
    "description": "Terminally differentiated B cell responsible for antibody secretion, characterized by high expression of CD38, CD138, and transcription factors such as PRDM1 and XBP1."
  }
}
```

## Record 7

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
  Non-classical Monocytes  : +1.474
  Classical Monocytes      : +0.705
  Intermediate Monocytes   : +0.425
  NK cells                 : -0.110

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
Highest pathway score for non-classical monocytes supports CD16 Mono. Despite platelet markers (CD41, CD62P) possibly from contaminants, the gene and pathway evidence aligns with CD16+ monocytes (e.g., C1QA). No B cell markers, so CD16 Mono is the best fit.
```

## Record 8

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
The top surface proteins include B cell markers CD19, CD22, CD21, and CD27, along with IGHE expression (immunoglobulin heavy epsilon), indicating a memory B cell profile. Monocyte markers CD14 or CD16 are absent.

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
  Switched memory B cell   : +1.951
  Naive B cell             : +1.262
  Unswitched memory B cell : +1.158
  Plasma cell              : +1.046

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
B memory
Strong B cell markers (CD19, CD22, CD21, CD27) and IGHE expression, along with the highest pathway score for switched memory B cell, confirm B memory identity. No monocyte markers (CD14, CD16) are present.
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
  Non-classical CD16+ Monocyte: +0.754
  Myeloid Dendritic Cell (CD1c+ DC): +0.745
  Classical CD14+ Monocyte : +0.656
  Intermediate CD14+CD16+ Monocyte: +0.573

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
The highest pathway score is for non-classical CD16+ monocytes, and surface proteins include CD4, CD18, CD11b, and CD45, consistent with monocytes. Platelet markers (CD41, CD62P) may reflect aggregates, but gene expression (IL19, TGM2, GAS6) and absence of CD14 in top proteins support CD16+ monocyte identity over classical CD14+ monocytes.
```

