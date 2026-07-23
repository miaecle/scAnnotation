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

The transcriptome shows high IGKC (immunoglobulin kappa constant) and MHC class II genes (HLA-DRA, CD74, HLA-DPB1), indicating B cells. Surface proteins strongly express B cell markers CD19, CD22, CD21, and also CD35 and CD27, consistent with memory B cells. Monocyte markers are absent.
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
The gene expression profile (LYZ, CST3, AIF1, S100 family, CTSS) and surface markers (CD16, CD11b, CD172a) are characteristic of monocytes. The presence of CD16 and absence of CD14 in top surface proteins favor CD16+ non-classical monocytes. Platelet markers (CD41, CD62P, CLEC2) likely reflect contamination common in PBMC samples.
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
The gene expression profile (LYZ, HLA-DRA, CD74, CST3, S100A4, FOS) and surface markers (CD11b, CD18, CD35, CD93, CD49d, CD172a) are characteristic of monocytes, with classical CD14+ monocytes being most abundant in PBMC. The presence of platelet markers (CD62P, CD41, CD61) likely reflects platelet contamination or binding, a common observation in PBMC preparations.
```

## Record 4

- stage: stage2_program_query
- row_idx: 1
- cell_idx: 48
- cell_barcode: L1_AAAGAACCACCTCTAC
- true_label: B memory
- stage1_label: B memory

### stage1_reasoning

```text
The transcriptome shows high IGKC (immunoglobulin kappa constant) and MHC class II genes (HLA-DRA, CD74, HLA-DPB1), indicating B cells. Surface proteins strongly express B cell markers CD19, CD22, CD21, and also CD35 and CD27, consistent with memory B cells. Monocyte markers are absent.
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
The transcriptome shows high IGKC (immunoglobulin kappa constant) and MHC class II genes (HLA-DRA, CD74, HLA-DPB1), indicating B cells. Surface proteins strongly express B cell markers CD19, CD22, CD21, and also CD35 and CD27, consistent with memory B cells. Monocyte markers are absent.

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
The transcriptome shows high IGKC (immunoglobulin kappa constant) and MHC class II genes (HLA-DRA, CD74, HLA-DPB1), indicating B cells. Surface proteins strongly express B cell markers CD19, CD22, CD21, and also CD35 and CD27, consistent with memory B cells. Monocyte markers are absent.

```

### output

```text
{
  "B memory (switched)": {
    "genes": [
      "CD27",
      "CD22",
      "CR2",
      "CR1",
      "TNFRSF13B",
      "MS4A1",
      "IGKC",
      "IGHG1",
      "IGHA1",
      "HLA-DRA",
      "CD74",
      "HLA-DPB1",
      "CD19",
      "CD81",
      "CXCR5",
      "BCL6",
      "TCL1A",
      "AICDA",
      "PAX5",
      "EBF1",
      "IRF8",
      "PTPRC",
      "ITGB2",
      "CD40",
      "CD80",
      "IL4R",
      "CD72",
      "CD83",
      "TNFRSF13C",
      "LY9",
      "SLAMF6",
      "IL21R",
      "TOX",
      "TOX2",
      "ZBTB32",
      "MIR155HG",
      "LRMP",
      "SH3BP5",
      "FCMR",
      "RFTN1",
      "SPIB",
      "PXK",
      "PDLIM1",
      "LINC01781",
      "FAM30A",
      "RP11-156J8.5",
      "RP11-379F12.4",
      "RP11-13K12.1",
      "CTD-2619J13.13"
    ],
    "description": "Memory B cells that have undergone class switch recombination, expressing CD27 and lacking IgD, with high MHC class II and immunoglobulin genes."
  },
  "B naive": {
    "genes": [
      "IGHD",
      "IGHM",
      "FCER2",
      "CD24",
      "CD38",
      "CD19",
      "CD22",
      "CR2",
      "MS4A1",
      "CD74",
      "HLA-DRA",
      "HLA-DPB1",
      "PXK",
      "TCL1A",
      "BCL7A",
      "RGS13",
      "SOCS3",
      "EBF1",
      "PAX5",
      "IRF8",
      "PTPRC",
      "CD72",
      "CD40",
      "CD80",
      "IL4R",
      "CR1",
      "ITGB2",
      "CD81",
      "CXCR5",
      "TNFRSF13C",
      "LY9",
      "SLAMF6",
      "IL21R",
      "TOX",
      "TOX2",
      "ZBTB32",
      "MIR155HG",
      "LRMP",
      "FCMR",
      "RFTN1",
      "SPIB",
      "PDLIM1",
      "FAM30A",
      "LINC01781",
      "RP11-156J8.5",
      "RP11-379F12.4"
    ],
    "description": "Mature naive B cells expressing surface IgD and IgM, with high levels of CD23 and CD24, and lacking CD27."
  },
  "Plasma cells": {
    "genes": [
      "SDC1",
      "MZB1",
      "XBP1",
      "IRF4",
      "PRDM1",
      "JCHAIN",
      "IGHG1",
      "IGHG2",
      "IGHG3",
      "IGHG4",
      "IGHA1",
      "IGHA2",
      "IGHE",
      "IGK",
      "IGL",
      "CD38",
      "CD27",
      "CD19",
      "MS4A1",
      "HLA-DRA",
      "CD74",
      "PTPRC",
      "TNFRSF13B",
      "TNFRSF13C",
      "BCL2",
      "BCL2L11",
      "SH2D1A",
      "TNFRSF17",
      "CD22",
      "CR2",
      "CXCR4",
      "ITGB7",
      "ITGA4",
      "MME",
      "CD28",
      "CTLA4",
      "LAG3",
      "PDCD1",
      "ICOS",
      "TIGIT",
      "HAVCR2",
      "FOXP3",
      "IL10",
      "IL21",
      "IL6",
      "TNF",
      "TGFB1"
    ],
    "description": "Terminally differentiated B cells that produce antibodies, characterized by high expression of CD138, PRDM1, and XBP1, and low MHC class II."
  },
  "Plasmablasts": {
    "genes": [
      "CD27",
      "CD38",
      "IRF4",
      "PRDM1",
      "MKI67",
      "JCHAIN",
      "IGHG1",
      "IGHA1",
      "IGHE",
      "IGK",
      "IGL",
      "SDC1",
      "MZB1",
      "XBP1",
      "MS4A1",
      "HLA-DRA",
      "CD74",
      "PTPRC",
      "TNFRSF13B",
      "TNFRSF13C",
      "BCL2",
      "BCL2L11",
      "SH2D1A",
      "TNFRSF17",
      "CD22",
      "CR2",
      "CXCR4",
      "ITGB7",
      "ITGA4",
      "MME",
      "CD19",
      "CD20",
      "CD24",
      "FCER2",
      "IL6",
      "TNF",
      "TGFB1",
      "IL10",
      "IL21",
      "AICDA",
      "PAX5",
      "EBF1",
      "IRF8"
    ],
    "description": "Activated B cells that are antibody-secreting and proliferating, expressing high CD27, CD38, and PC markers, with decreased CD20."
  }
}
```

## Record 5

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
The transcriptome shows high IGKC (immunoglobulin kappa constant) and MHC class II genes (HLA-DRA, CD74, HLA-DPB1), indicating B cells. Surface proteins strongly express B cell markers CD19, CD22, CD21, and also CD35 and CD27, consistent with memory B cells. Monocyte markers are absent.

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
  B memory (switched)      : +0.793
  B naive                  : +0.757
  Plasmablasts             : +0.608
  Plasma cells             : +0.549

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
B memory
High IGKC, MS4A1, and MHC class II genes; surface proteins CD19, CD22, CD21, CD27, and CD35 confirm B cell identity. Pathway scores favor B memory over B naive, consistent with memory B cell.
```

## Record 6

- stage: stage2_program_query
- row_idx: 2
- cell_idx: 6148
- cell_barcode: L1_CTGAATGAGGGCGAAG
- true_label: CD14 Mono
- stage1_label: CD14 Mono

### stage1_reasoning

```text
The gene expression profile (LYZ, HLA-DRA, CD74, CST3, S100A4, FOS) and surface markers (CD11b, CD18, CD35, CD93, CD49d, CD172a) are characteristic of monocytes, with classical CD14+ monocytes being most abundant in PBMC. The presence of platelet markers (CD62P, CD41, CD61) likely reflects platelet contamination or binding, a common observation in PBMC preparations.
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
The gene expression profile (LYZ, HLA-DRA, CD74, CST3, S100A4, FOS) and surface markers (CD11b, CD18, CD35, CD93, CD49d, CD172a) are characteristic of monocytes, with classical CD14+ monocytes being most abundant in PBMC. The presence of platelet markers (CD62P, CD41, CD61) likely reflects platelet contamination or binding, a common observation in PBMC preparations.

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
The gene expression profile (LYZ, HLA-DRA, CD74, CST3, S100A4, FOS) and surface markers (CD11b, CD18, CD35, CD93, CD49d, CD172a) are characteristic of monocytes, with classical CD14+ monocytes being most abundant in PBMC. The presence of platelet markers (CD62P, CD41, CD61) likely reflects platelet contamination or binding, a common observation in PBMC preparations.

```

### output

```text
{
  "Classical Monocyte (CD14+)": {
    "genes": [
      "LYZ",
      "S100A8",
      "S100A9",
      "CD14",
      "CST3",
      "FCGR3A",
      "S100A4",
      "FOS",
      "HLA-DRA",
      "CD74",
      "CTSS",
      "TYROBP",
      "FCGR2A",
      "CSF1R",
      "CD33",
      "ITGAM",
      "ITGAX",
      "CD163",
      "MNDA",
      "TLR2",
      "TLR4",
      "MYD88",
      "IRAK1",
      "TRAF6",
      "NFKB1",
      "IL1B",
      "TNF",
      "CCL2",
      "CCL3",
      "CCL4",
      "CXCL8",
      "CXCL2",
      "CD9",
      "CD93",
      "CD49d",
      "CD172a"
    ],
    "description": "Classical CD14+ monocytes are the most abundant monocyte subset in PBMC, characterized by high expression of CD14, LYZ, and S100A8/A9, and are involved in phagocytosis and inflammatory responses."
  },
  "Non-classical Monocyte (CD16+)": {
    "genes": [
      "FCGR3A",
      "CDKN1C",
      "LST1",
      "MS4A7",
      "RHOC",
      "CX3CR1",
      "NR4A2",
      "IER3",
      "MAFB",
      "S100A12",
      "AIF1",
      "C5AR1",
      "FPR3",
      "TLR7",
      "TLR8",
      "IRF7",
      "IFITM3",
      "ICAM1",
      "ITGB2",
      "CSF1R",
      "CD36",
      "FCN1",
      "C1QA",
      "C1QB",
      "C1QC",
      "SERPINA1",
      "CTSD",
      "CTSZ",
      "LIPA",
      "NLRP3",
      "PYCARD",
      "CASP1",
      "IL18",
      "CCL5",
      "CXCL16"
    ],
    "description": "Non-classical CD16+ monocytes show high expression of FCGR3A and CX3CR1, patrol the vasculature, and are involved in immune surveillance and inflammation resolution."
  },
  "Intermediate Monocyte (CD14+CD16+)": {
    "genes": [
      "CD14",
      "FCGR3A",
      "HLA-DRA",
      "CD74",
      "CTSS",
      "CST3",
      "LYZ",
      "S100A8",
      "S100A9",
      "FCGR1A",
      "FCGR2A",
      "TLR2",
      "TLR4",
      "IL1B",
      "TNF",
      "CCL3",
      "CCL4",
      "CXCL8",
      "CCR2",
      "CX3CR1",
      "CD163",
      "CD33",
      "ITGAM",
      "ITGAX",
      "CSF1R",
      "MAFB",
      "AIF1",
      "LST1",
      "MS4A7",
      "RHOC",
      "CDKN1C",
      "NR4A2",
      "IER3",
      "S100A12",
      "TLR7",
      "TLR8",
      "IRF7",
      "IFITM3",
      "ICAM1",
      "ITGB2"
    ],
    "description": "Intermediate CD14+CD16+ monocytes represent a transitional subset combining features of classical and non-classical monocytes, with roles in antigen presentation and inflammation."
  },
  "Myeloid Dendritic Cell (mDC)": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "CD207",
      "CCR7",
      "CCL19",
      "CCL21",
      "LAMP3",
      "CD80",
      "CD86",
      "CD83",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPB1",
      "HLA-DQB1",
      "CD74",
      "BATF3",
      "IRF8",
      "ZBTB46",
      "FLT3",
      "CSF1R",
      "CST3",
      "CTSS",
      "LGMN",
      "CCL17",
      "CCL22",
      "IL12B",
      "IL23A",
      "IL6",
      "TNF",
      "IFNB1",
      "CXCL10",
      "CXCL9",
      "CCL5",
      "S100A4",
      "S100A6",
      "S100A11",
      "ACTB",
      "GAPDH"
    ],
    "description": "Myeloid dendritic cells (mDCs) are potent antigen-presenting cells characterized by expression of CD1C and FCER1A, and are crucial for initiating T-cell responses."
  },
  "Plasmacytoid Dendritic Cell (pDC)": {
    "genes": [
      "CLEC4C",
      "IL3RA",
      "LILRA4",
      "TCF4",
      "IRF7",
      "IRF8",
      "SPIB",
      "RUNX2",
      "BCL11A",
      "EBF1",
      "AFF2",
      "PLAC8",
      "SCL25A37",
      "MPEG1",
      "SERPINF1",
      "DERL3",
      "B4GALT1",
      "IGJ",
      "KLF4",
      "MYC",
      "CCL4",
      "CXCL10",
      "IFNA1",
      "IFNA2",
      "IFNA4",
      "IFNA5",
      "IFNA6",
      "IFNA7",
      "IFNA8",
      "IFNA10",
      "IFNA13",
      "IFNA14",
      "IFNA16",
      "IFNA17",
      "IFNB1",
      "IL28A",
      "IL29",
      "IL28B",
      "TNF",
      "CD40",
      "CD80",
      "CD86",
      "HLA-DRA",
      "HLA-DRB1",
      "HLA-DPB1"
    ],
    "description": "Plasmacytoid dendritic cells (pDCs) are specialized type I interferon-producing cells, identified by expression of CLEC4C and IL3RA, and play a key role in antiviral immunity."
  }
}
```

## Record 7

- stage: stage2_program_query
- row_idx: 0
- cell_idx: 13748
- cell_barcode: L1_TTTGTTGCAGCGAGTA
- true_label: CD16 Mono
- stage1_label: CD16 Mono

### stage1_reasoning

```text
The gene expression profile (LYZ, CST3, AIF1, S100 family, CTSS) and surface markers (CD16, CD11b, CD172a) are characteristic of monocytes. The presence of CD16 and absence of CD14 in top surface proteins favor CD16+ non-classical monocytes. Platelet markers (CD41, CD62P, CLEC2) likely reflect contamination common in PBMC samples.
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
The gene expression profile (LYZ, CST3, AIF1, S100 family, CTSS) and surface markers (CD16, CD11b, CD172a) are characteristic of monocytes. The presence of CD16 and absence of CD14 in top surface proteins favor CD16+ non-classical monocytes. Platelet markers (CD41, CD62P, CLEC2) likely reflect contamination common in PBMC samples.

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
The gene expression profile (LYZ, CST3, AIF1, S100 family, CTSS) and surface markers (CD16, CD11b, CD172a) are characteristic of monocytes. The presence of CD16 and absence of CD14 in top surface proteins favor CD16+ non-classical monocytes. Platelet markers (CD41, CD62P, CLEC2) likely reflect contamination common in PBMC samples.

```

### output

```text
{
  "Non-classical monocyte": {
    "genes": [
      "FCGR3A",
      "CX3CR1",
      "MS4A7",
      "LILRA5",
      "LILRA2",
      "CDKN1C",
      "LST1",
      "LRRC25",
      "CSF1R",
      "IRF8",
      "S100A8",
      "S100A9",
      "LYZ",
      "CST3",
      "AIF1",
      "CTSS",
      "TYROBP",
      "FCER1G",
      "SPI1",
      "CEBPB",
      "FOS",
      "JUN",
      "MAFB",
      "CD86",
      "HLA-DRA",
      "HLA-DPB1",
      "HLA-DQB1",
      "CD74",
      "ITGAM",
      "ITGAX",
      "CD33",
      "CD16",
      "CD11b",
      "CD172a",
      "CD41",
      "CD62P",
      "CLEC2",
      "GNA15",
      "TNFAIP6",
      "PTGS2"
    ],
    "description": "Non-classical monocytes (CD14lowCD16+) patrol the endothelium, scavenge particles, and produce anti-inflammatory cytokines."
  },
  "Intermediate monocyte": {
    "genes": [
      "CD14",
      "FCGR3A",
      "CX3CR1",
      "CCR2",
      "CD163",
      "MS4A7",
      "LILRA5",
      "LILRA2",
      "LST1",
      "CDKN1C",
      "S100A8",
      "S100A9",
      "LYZ",
      "CST3",
      "AIF1",
      "CTSS",
      "TYROBP",
      "FCER1G",
      "SPI1",
      "CEBPB",
      "FOS",
      "JUN",
      "MAFB",
      "CD86",
      "HLA-DRA",
      "HLA-DPB1",
      "HLA-DQB1",
      "CD74",
      "ITGAM",
      "ITGAX",
      "CD33",
      "CD16",
      "CD14",
      "CD11b",
      "CD172a",
      "GNA15",
      "TNFAIP6",
      "PTGS2",
      "IL1B",
      "TNF"
    ],
    "description": "Intermediate monocytes (CD14+CD16+) are pro-inflammatory and produce high levels of TNF and IL-1β."
  },
  "Classical monocyte": {
    "genes": [
      "CD14",
      "CCR2",
      "S100A8",
      "S100A9",
      "LYZ",
      "CST3",
      "AIF1",
      "CTSS",
      "TYROBP",
      "FCER1G",
      "SPI1",
      "CEBPB",
      "FOS",
      "JUN",
      "MAFB",
      "CD86",
      "HLA-DRA",
      "HLA-DPB1",
      "HLA-DQB1",
      "CD74",
      "ITGAM",
      "ITGAX",
      "CD33",
      "CD11b",
      "CD172a",
      "CD41",
      "CD62P",
      "CLEC2",
      "GNA15",
      "TNFAIP6",
      "PTGS2",
      "IL1B",
      "TNF",
      "CCL2",
      "CSF1R",
      "IRF8"
    ],
    "description": "Classical monocytes (CD14+CD16-) are highly phagocytic and migrate to sites of inflammation via CCR2."
  },
  "Natural killer cell": {
    "genes": [
      "NKG7",
      "GNLY",
      "PRF1",
      "GZMB",
      "GZMA",
      "GZMH",
      "KLRD1",
      "KLRB1",
      "KLRK1",
      "NCR1",
      "CD247",
      "FCGR3A",
      "CD16",
      "CD56",
      "NCAM1",
      "CD3E",
      "CD8B",
      "CD2",
      "IL2RB",
      "IL18RAP",
      "KIR2DL1",
      "KIR2DL4",
      "KIR3DL1",
      "KLRC1",
      "KLRC2",
      "KLRC3",
      "KLRF1",
      "SH2D1B",
      "TRAV1-2",
      "TRDV1",
      "TRGV9",
      "TRGJP1",
      "TRGJP2"
    ],
    "description": "Natural killer cells are innate lymphocytes that kill infected or cancerous cells via cytotoxic granules and express Fc receptors."
  },
  "Myeloid dendritic cell": {
    "genes": [
      "CD1C",
      "FCER1A",
      "CLEC10A",
      "CCR7",
      "CLEC4A",
      "CD80",
      "CD86",
      "HLA-DRA",
      "HLA-DPB1",
      "HLA-DQB1",
      "CD74",
      "IRF4",
      "IRF8",
      "FLT3",
      "CSF2RA",
      "CSF1R",
      "ITGAX",
      "ITGAM",
      "CD33",
      "CD16",
      "CD11b",
      "CD11c",
      "CD40",
      "CD83",
      "CCL17",
      "CCL22",
      "IL12B",
      "IL23A",
      "TNF",
      "LAMP3",
      "MARCKS",
      "MARCKSL1"
    ],
    "description": "Myeloid dendritic cells are professional antigen-presenting cells that capture antigens and prime T cells in lymphoid tissues."
  }
}
```

## Record 8

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
The gene expression profile (LYZ, CST3, AIF1, S100 family, CTSS) and surface markers (CD16, CD11b, CD172a) are characteristic of monocytes. The presence of CD16 and absence of CD14 in top surface proteins favor CD16+ non-classical monocytes. Platelet markers (CD41, CD62P, CLEC2) likely reflect contamination common in PBMC samples.

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
  Non-classical monocyte   : +0.847
  Intermediate monocyte    : +0.707
  Classical monocyte       : +0.683
  Myeloid dendritic cell   : +0.598
  Natural killer cell      : +0.108

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono
Top genes (LYZ, CST3, AIF1, CTSS) and surface profile (no CD14, monocyte markers) confirm monocyte lineage. Pathway scores strongly favor non-classical monocyte (+0.847) over classical (+0.683) and intermediate (+0.707), consistent with CD16+ non-classical identity. Platelet markers reflect common contamination.
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
The gene expression profile (LYZ, HLA-DRA, CD74, CST3, S100A4, FOS) and surface markers (CD11b, CD18, CD35, CD93, CD49d, CD172a) are characteristic of monocytes, with classical CD14+ monocytes being most abundant in PBMC. The presence of platelet markers (CD62P, CD41, CD61) likely reflects platelet contamination or binding, a common observation in PBMC preparations.

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
  Non-classical Monocyte (CD16+): +0.869
  Intermediate Monocyte (CD14+CD16+): +0.782
  Classical Monocyte (CD14+): +0.723
  Myeloid Dendritic Cell (mDC): +0.638
  Plasmacytoid Dendritic Cell (pDC): +0.603

Choose the cell type from the following list (output exactly one of these names in Line 1):
CD16 Mono, B memory, CD14 Mono

Considering all of the above — genes (across all scoring methods), surface proteins, pathway scores, and the stage-1 reasoning — confirm or correct the stage-1 annotation by choosing the most appropriate subtype from the list above. Trust direct gene/protein evidence over the stage-1 label when they conflict.
Line 1: final cell type (from the list above).  Line 2: brief rationale (<100 words).
```

### output

```text
CD16 Mono

Pathway scores show non-classical monocyte program is most active (+0.869 vs +0.723 for classical). Surface markers include CD93, CD35, CD11b, CD4, and platelet markers (CD62P, CD41, CLEC2), which are associated with CD16+ monocytes that exhibit higher platelet binding. Genes like FOS, JUNB, S100A4 are elevated in CD16+ monocytes. Direct evidence supports correcting to CD16 Mono.
```

