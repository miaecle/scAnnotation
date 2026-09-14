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
   21. PSAP (0.00090)
   22. TIMP1 (0.00089)
   23. LYZ (0.00089)
   24. SERPINA1 (0.00084)
   25. IFI30 (0.00082)
   26. LGALS1 (0.00080)
   27. CYBB (0.00075)
   28. FOS (0.00071)
   29. HLA-DRB5 (0.00070)
   30. MARCKS (0.00068)
   31. C1QA (0.00068)
   32. CD74 (0.00067)
   33. FGL2 (0.00062)
   34. CSF1R (0.00060)
   35. HLA-DPB1 (0.00059)
   36. SPI1 (0.00055)
   37. TNFRSF1B (0.00055)
   38. CEBPB (0.00054)
   39. PILRA (0.00052)
   40. RRAS (0.00052)
   41. HES4 (0.00051)
   42. SMIM25 (0.00051)
   43. S100A9 (0.00051)
   44. CSTA (0.00051)
   45. LRRC25 (0.00050)
   46. LILRB2 (0.00049)
   47. CD68 (0.00049)
   48. RHOB (0.00049)
   49. CX3CR1 (0.00048)
   50. HLA-DQB1 (0.00048)

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
FCGR3A, MS4A7, CX3CR1, CDKN1C, LST1, and C1QA support a CD16-positive monocyte identity, with relatively limited CD14/S100A9 inflammatory markers. Platelet-associated ADT signals likely reflect platelet contamination or adherence.
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
FCGR3A, MS4A7, CX3CR1, CDKN1C, LST1, and C1QA support a CD16-positive monocyte identity, with relatively limited CD14/S100A9 inflammatory markers. Platelet-associated ADT signals likely reflect platelet contamination or adherence.
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
  "Non-classical FCGR3A+ monocytes": {
    "genes": [
      "FCGR3A",
      "MS4A7",
      "LST1",
      "IFITM3",
      "IFITM1",
      "IFITM2",
      "LILRB1",
      "LILRA1",
      "SIGLEC10",
      "IFITM",
      "FCER1G",
      "TYMP",
      "AIF1",
      "SERPINA1",
      "CFD",
      "SAT1",
      "LGALS3",
      "CTSS",
      "CTSD",
      "CTSB",
      "LILRB2",
      "IFITM3",
      "MS4A7",
      "RHOC",
      "IFITM1"
    ],
    "description": "Patrolling CD16-high monocytes express FCGR3A, LST1, MS4A7, LILRB1, and relatively low levels of inflammatory S100A8 and S100A9."
  },
  "Intermediate CD14+CD16+ monocytes": {
    "genes": [
      "FCGR3A",
      "CD14",
      "LST1",
      "MS4A7",
      "IFITM3",
      "FCER1G",
      "LILRB1",
      "CTSS",
      "CTSD",
      "TYMP",
      "AIF1",
      "SERPINA1",
      "LGALS3",
      "CTSB",
      "LILRA1",
      "SAT1",
      "IFI30",
      "CFD",
      "IFITM1",
      "IFITM2",
      "S100A10",
      "VCAN",
      "FCN1",
      "CTSC",
      "LILRB2"
    ],
    "description": "Intermediate monocytes co-express CD14 and FCGR3A and show a hybrid inflammatory and antigen-presentation program."
  },
  "Classical CD14+ monocytes": {
    "genes": [
      "CD14",
      "S100A8",
      "S100A9",
      "LYZ",
      "FCN1",
      "VCAN",
      "CTSD",
      "CTSS",
      "LGALS3",
      "CTSB",
      "CTSC",
      "S100A10",
      "LGALS1",
      "SERPINA1",
      "CTSL",
      "FCER1G",
      "LST1",
      "TYMP",
      "AIF1",
      "MNDA",
      "CTSD",
      "FCN1",
      "FPR1",
      "SLC11A1",
      "LGALS3"
    ],
    "description": "Classical monocytes are CD14-high inflammatory cells marked by S100A8, S100A9, LYZ, FCN1, and VCAN."
  },
  "CD1C-positive conventional dendritic cells": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "CD1E",
      "HLA-DRA",
      "HLA-DPA1",
      "HLA-DPB1",
      "HLA-DQA1",
      "HLA-DQB1",
      "HLA-DMA",
      "HLA-DMB",
      "GPR183",
      "CST3",
      "CLEC12A",
      "IRF4",
      "CD74",
      "COTL1",
      "LILRA4",
      "CSTA",
      "HLA-DQA2",
      "FCER1G",
      "LST1",
      "CTSS",
      "LYZ",
      "CCDC50"
    ],
    "description": "CD1C-positive conventional dendritic cells are antigen-presenting myeloid cells with high CD1C, FCER1A, CLEC10A, and MHC class II expression."
  },
  "Natural killer cells": {
    "genes": [
      "NKG7",
      "GNLY",
      "PRF1",
      "GZMB",
      "GZMH",
      "CTSW",
      "KLRD1",
      "KLRF1",
      "KLRC1",
      "HCST",
      "TYROBP",
      "FCER1G",
      "CD247",
      "TRAC",
      "CCL5",
      "XCL1",
      "XCL2",
      "FGFBP2",
      "HOPX",
      "SH2D1B",
      "KLRB1",
      "S1PR5",
      "TRBC2",
      "GZMA",
      "KLRD1"
    ],
    "description": "Natural killer cells are cytotoxic lymphocytes distinguished from CD16 monocytes by strong NKG7, GNLY, PRF1, granzymes, and killer-receptor expression."
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
FCGR3A, MS4A7, CX3CR1, CDKN1C, LST1, and C1QA support a CD16-positive monocyte identity, with relatively limited CD14/S100A9 inflammatory markers. Platelet-associated ADT signals likely reflect platelet contamination or adherence.

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
  Non-classical FCGR3A+ monocytes: +1.45518
  Intermediate CD14+CD16+ monocytes: +1.22251
  Classical CD14+ monocytes: +0.72248
  CD1C-positive conventional dendritic cells: +0.47910
  Natural killer cells     : -0.62104

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
FCGR3A, MS4A7, CX3CR1-associated CDKN1C, LST1, and strong non-classical monocyte pathway activity support CD16 Mono. Limited inflammatory CD14/S100A9 expression argues against CD14 Mono; platelet-associated proteins likely reflect contamination/adherence.
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
   21. LINC00926 (0.00061)
   22. SPIB (0.00058)
   23. HLA-DMA (0.00055)
   24. TNFRSF13B (0.00055)
   25. TCF4 (0.00055)
   26. HLA-DRB5 (0.00054)
   27. RALGPS2 (0.00054)
   28. CD79B (0.00054)
   29. MEF2C (0.00054)
   30. CPNE5 (0.00049)
   31. TNFRSF13C (0.00046)
   32. TLR10 (0.00045)
   33. HLA-DMB (0.00045)
   34. JCHAIN (0.00045)
   35. FAM30A (0.00044)
   36. SWAP70 (0.00044)
   37. SHISA8 (0.00043)
   38. COCH (0.00041)
   39. HLA-DOB (0.00038)
   40. EBF1 (0.00038)
   41. ARID5B (0.00037)
   42. PDLIM1 (0.00036)
   43. COBLL1 (0.00035)
   44. CYB5D2 (0.00035)
   45. OSBPL10 (0.00035)
   46. ADAM28 (0.00034)
   47. MARCKS (0.00034)
   48. IGHG1 (0.00034)
   49. SEL1L3 (0.00033)
   50. LYPLAL1 (0.00032)

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
MS4A1, CD79A, CD19, CD22, CD21, BANK1, and abundant immunoglobulin genes clearly indicate a mature B-cell population, consistent with memory B cells rather than monocytes.
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
MS4A1, CD79A, CD19, CD22, CD21, BANK1, and abundant immunoglobulin genes clearly indicate a mature B-cell population, consistent with memory B cells rather than monocytes.
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
  "Class-switched memory B cell": {
    "genes": [
      "CD27",
      "IGHG1",
      "IGHG3",
      "IGHA1",
      "IGHA2",
      "TNFRSF13B",
      "FCRL2",
      "FCRL3",
      "AIM2",
      "BANK1",
      "CD79A",
      "CD79B",
      "MS4A1",
      "CD37",
      "CD22",
      "HLA-DRA",
      "HLA-DPA1",
      "HLA-DPB1",
      "CD74",
      "GPR183",
      "LTB",
      "CD40",
      "PAX5",
      "SPIB"
    ],
    "description": "Antigen-experienced B cells that have undergone class-switch recombination and commonly express CD27 together with IgG or IgA transcripts."
  },
  "IgM memory B cell": {
    "genes": [
      "IGHM",
      "IGHD",
      "CD27",
      "FCRL2",
      "FCRL3",
      "AIM2",
      "TNFRSF13B",
      "BANK1",
      "CD79A",
      "CD79B",
      "MS4A1",
      "CD37",
      "CD22",
      "HLA-DRA",
      "HLA-DPA1",
      "HLA-DPB1",
      "CD74",
      "GPR183",
      "LTB",
      "CD40",
      "PAX5",
      "SPIB",
      "BLK",
      "HVCN1"
    ],
    "description": "Unswitched memory B cells retain IgM and often IgD expression while showing CD27 and a mature antigen-experienced B-cell program."
  },
  "Atypical memory B cell": {
    "genes": [
      "FCRL5",
      "ITGAX",
      "TBX21",
      "SIGLEC6",
      "TCL1A",
      "CD11C",
      "FCRL3",
      "FCRL2",
      "ITGAM",
      "TLR7",
      "TLR9",
      "AIM2",
      "CD27",
      "TNFRSF13B",
      "MS4A1",
      "CD79A",
      "CD37",
      "CD22",
      "HLA-DRA",
      "CD74",
      "GPR183",
      "BANK1",
      "SPIB",
      "PAX5"
    ],
    "description": "A chronically stimulated, often CD11c-positive memory B-cell state enriched for TBX21, FCRL5, and innate-like activation programs."
  },
  "Naive B cell": {
    "genes": [
      "TCL1A",
      "IGHD",
      "IGHM",
      "FCER2",
      "IL4R",
      "CCR7",
      "MS4A1",
      "CD79A",
      "CD79B",
      "CD37",
      "CD22",
      "HLA-DRA",
      "HLA-DPA1",
      "HLA-DPB1",
      "CD74",
      "GPR183",
      "BANK1",
      "BLK",
      "HVCN1",
      "PAX5",
      "SPIB",
      "LTB",
      "MAL",
      "TCL1B"
    ],
    "description": "Antigen-inexperienced mature B cells characterized by TCL1A, IgD, IgM, and FCER2 expression with little or no memory-associated CD27."
  },
  "Plasmablast": {
    "genes": [
      "MZB1",
      "JCHAIN",
      "XBP1",
      "PRDM1",
      "SDC1",
      "CD38",
      "DERL3",
      "SEC11C",
      "TNFRSF17",
      "IGKC",
      "IGLC2",
      "IGHG1",
      "IGHG3",
      "IGHA1",
      "MALAT1",
      "SSR4",
      "FKBP11",
      "HSPA5",
      "DNAJB9",
      "MANF",
      "CD74",
      "HLA-DRA",
      "CD79A",
      "IRF4"
    ],
    "description": "Antibody-secreting B-cell precursors with high immunoglobulin production and a strong unfolded-protein-response and plasma-cell differentiation program."
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
MS4A1, CD79A, CD19, CD22, CD21, BANK1, and abundant immunoglobulin genes clearly indicate a mature B-cell population, consistent with memory B cells rather than monocytes.

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
  Class-switched memory B cell: +2.26867
  IgM memory B cell        : +1.81015
  Naive B cell             : +1.28763
  Atypical memory B cell   : +1.19710
  Plasmablast              : +1.12546

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
B memory
MS4A1, CD79A, CD19, CD22, CD21, BANK1, and abundant immunoglobulin transcripts establish a mature B-cell identity. CD27, CD73, CD35, CD21, and strong class-switched/IgM memory pathway scores support memory B cells, with immunoglobulin class switching evident (IGHA1/2, IGHG3).
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
   21. SAT1 (0.00071)
   22. CTSS (0.00071)
   23. HLA-DMA (0.00068)
   24. PSAP (0.00066)
   25. CYBB (0.00064)
   26. CPVL (0.00064)
   27. MARCKS (0.00060)
   28. COTL1 (0.00058)
   29. IFITM3 (0.00057)
   30. CEBPD (0.00055)
   31. IGSF6 (0.00052)
   32. MS4A7 (0.00052)
   33. CFD (0.00050)
   34. LGALS2 (0.00049)
   35. NPC2 (0.00047)
   36. CSTA (0.00044)
   37. S100A9 (0.00044)
   38. S100A11 (0.00044)
   39. FOSB (0.00044)
   40. RHOB (0.00044)
   41. HLA-DMB (0.00042)
   42. SERPINA1 (0.00042)
   43. DUSP1 (0.00041)
   44. NR4A2 (0.00041)
   45. LGALS1 (0.00041)
   46. CTSZ (0.00040)
   47. AP1S2 (0.00039)
   48. CALHM6 (0.00039)
   49. CLEC7A (0.00038)
   50. TNFAIP2 (0.00038)

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
LYZ, FCN1, S100A9, CST3, LILR/TYROBP, and strong HLA-DP/DQ/DR expression support a CD14⁺ classical monocyte identity. The platelet-associated ADT signals likely reflect ambient or platelet doublet contamination.
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
LYZ, FCN1, S100A9, CST3, LILR/TYROBP, and strong HLA-DP/DQ/DR expression support a CD14⁺ classical monocyte identity. The platelet-associated ADT signals likely reflect ambient or platelet doublet contamination.
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
  "Classical CD14 Monocytes": {
    "genes": [
      "S100A8",
      "S100A9",
      "CTSD",
      "CTSS",
      "CTSC",
      "FCN1",
      "LGALS3",
      "TYMP",
      "VCAN",
      "MNDA",
      "CTSL",
      "FCER1G",
      "LGALS9",
      "FPR1",
      "AIF1",
      "LILRB1",
      "SAT1",
      "IFITM3",
      "MS4A6A",
      "SLC11A1",
      "SERPINA1",
      "NAMPT",
      "CFD",
      "PSAP",
      "CYBA"
    ],
    "description": "Circulating inflammatory monocytes characterized by strong CD14, S100A8/S100A9, FCN1, VCAN, and lysosomal phagocyte programs."
  },
  "S100A8/S100A9-High Inflammatory Monocytes": {
    "genes": [
      "S100A8",
      "S100A9",
      "VCAN",
      "FCN1",
      "CTSD",
      "CTSS",
      "CTSC",
      "LGALS3",
      "TYMP",
      "FPR1",
      "MNDA",
      "VCAM1",
      "IL1B",
      "TNF",
      "CXCL8",
      "NLRP3",
      "NAMPT",
      "EREG",
      "SLC11A1",
      "OSM",
      "NFKBIA",
      "DUSP1",
      "IER3",
      "PTGS2",
      "PLAUR"
    ],
    "description": "Highly activated classical monocytes enriched for acute inflammatory, inflammasome, NF-kB, and S100A8/S100A9 programs."
  },
  "Intermediate CD14 Monocytes": {
    "genes": [
      "FCGR3A",
      "MS4A7",
      "LST1",
      "LILRB1",
      "IFITM3",
      "IFITM1",
      "IFITM2",
      "CTD-2006K23.1",
      "IFITM5",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPA1",
      "HLA-DPB1",
      "CD74",
      "CTSS",
      "FCER1G",
      "AIF1",
      "SERPINA1",
      "SAT1",
      "TYMP",
      "LGALS3",
      "CFD",
      "LILRA1",
      "LILRA2",
      "MS4A6A"
    ],
    "description": "CD14-positive monocytes with elevated FCGR3A and antigen-presentation programs, intermediate between classical and non-classical states."
  },
  "Non-Classical FCGR3A Monocytes": {
    "genes": [
      "FCGR3A",
      "LST1",
      "MS4A7",
      "IFITM3",
      "IFITM1",
      "IFITM2",
      "LILRB1",
      "LILRA1",
      "IFITM5",
      "SERPINA1",
      "AIF1",
      "FCER1G",
      "CTD-2006K23.1",
      "IFITM?"
    ],
    "description": "Patrolling monocytes marked by high FCGR3A, LST1, MS4A7, and LILRB-family expression with relatively reduced S100A8/S100A9 and FCN1."
  },
  "CD1C Conventional Dendritic Cells": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "CD1E",
      "CST3",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPA1",
      "HLA-DPB1",
      "HLA-DQA1",
      "HLA-DQB1",
      "CD74",
      "GPR183",
      "CLEC12A",
      "IRF4",
      "COTL1",
      "LILRA4",
      "CCDC50",
      "CD40",
      "CSTA",
      "CTSS",
      "LY86",
      "FCER1G",
      "LILRB1"
    ],
    "description": "Antigen-presenting conventional dendritic cells that can resemble CD14 monocytes but show CD1C, FCER1A, CLEC10A, and MHC-II enrichment."
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
LYZ, FCN1, S100A9, CST3, LILR/TYROBP, and strong HLA-DP/DQ/DR expression support a CD14⁺ classical monocyte identity. The platelet-associated ADT signals likely reflect ambient or platelet doublet contamination.

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
  Intermediate CD14 Monocytes: +0.93206
  CD1C Conventional Dendritic Cells: +0.76817
  Non-Classical FCGR3A Monocytes: +0.62068
  Classical CD14 Monocytes : +0.62050
  S100A8/S100A9-High Inflammatory Monocytes: +0.16520

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD14 Mono
LYZ, FCN1, CST3, TYROBP, LST1, and HLA-DP/DQ/DR expression support a classical/intermediate CD14⁺ monocyte. Platelet-associated proteins likely reflect ambient contamination or a minor doublet component; evidence does not support CD16 Mono or B memory.
```

