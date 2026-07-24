# Stage-2 Precomputed Programs

- tissue: PBMC
- n_program_genes: 50
- n_cached_cell_types: 3

## b memory

### Atypical memory B

Description: Atypical memory B cells are CD27- IgD- and often express CD11c; they are expanded in autoimmune and infectious diseases and exhibit a transcriptional profile distinct from classical memory B cells.

Genes:
- CD19, MS4A1, CD27, CD11c, ITGAX, TNFRSF13C, CD81, CR2, FCRL2, FCRL5, IGHD, IGHM
- CD24, CD38, CD72, IL4R, TNFRSF9, TNFRSF4, ICOSL, CD40, CD48, IRF8, PAX5, BCL6
- AICDA, CD80, CD86, CCR6, CXCR5, TCL1A

### Naive B

Description: Naive B cells are CD27- IgD+ IgM+ and have not encountered antigen; they express high levels of TCL1A and low CD38, and circulate in blood awaiting activation.

Genes:
- CD19, MS4A1, CD27, TNFRSF13C, CD81, CR2, FCRL2, FCRL5, IGHD, IGHM, TCL1A, CD24
- CD38, CD72, CCR7, CXCR4, IL4R, CD40, CD48, IRF8, PAX5, BCL6, CD83, CD86
- HLA-DRA, HLA-DQB1, HLA-DRB1, CD74, CD79A, CD79B

### Plasma cell

Description: Plasma cells are terminally differentiated antibody-secreting cells with high CD38 and SDC1 expression; they are found in bone marrow and peripheral blood at low frequencies.

Genes:
- SDC1, MZB1, XBP1, PRDM1, TNFRSF17, CD38, CD27, CD19, MS4A1, IGHA1, IGHG1, IGHG3
- IGHM, IGLL5, JCHAIN, FKBP11, PDIA4, PDIA6, HSP90B1, PPIB, TXNDC5, SEC61G, SSR3, DERL3
- ATP1B1, MYBL1, IRF4, MCL1, BCL2, CD44

### Switched memory B

Description: Switched memory B cells are CD27+ IgD- IgM- and have undergone class switch recombination, expressing IgG or IgA; they circulate in blood and can rapidly differentiate into plasmablasts upon re-encounter with antigen.

Genes:
- CD19, MS4A1, CD27, TNFRSF13C, CD81, CR2, FCRL2, FCRL5, IGHG1, IGHG3, IGHA1, CD80
- CD86, AICDA, BCL6, PAX5, CCR6, CXCR5, IL4R, TNFRSF9, TNFRSF4, ICOSL, CD40, CD48
- IRF8, MYC, MKI67, CD38, CD24, CD72

### Unswitched memory B

Description: Unswitched memory B cells are CD27+ IgD+ IgM+ and retain the ability to undergo class switching; they represent a transitional memory population with both naive and memory features.

Genes:
- CD19, MS4A1, CD27, TNFRSF13C, CD81, CR2, FCRL2, FCRL5, IGHD, IGHM, CD24, CD38
- CD72, IL4R, TNFRSF9, TNFRSF4, ICOSL, CD40, CD48, IRF8, MYC, MKI67, CCR6, CXCR5
- BCL6, PAX5, AICDA, CD80, CD86, TCL1A

## cd14 mono

### Classical Monocytes

Description: Classical monocytes are CD14++CD16- cells that express high levels of CD14, S100A8/A9, and are involved in phagocytosis and inflammation.

Genes:
- CD14, S100A8, S100A9, LYZ, FCGR1A, CST3, FCN1, S100A12, CCR2, CLEC7A, CD163, CD68
- TLR4, IL6, TNF, CXCL8, IL1B, CD33, CD11b, MNDA, FPR1, FPR2, C5AR1, NLRP3
- IRF1, STAT1, NFKB1, RELA, HOXA1, MAFB

### Intermediate Monocytes

Description: Intermediate monocytes are CD14+CD16+ cells with high MHC class II expression and are pro-inflammatory.

Genes:
- CD14, FCGR3A, FCGR1A, HLA-DRA, HLA-DRB1, CD163, CD86, CXCL10, CCL3, CCL4, IL6, TNF
- IL1B, TLR2, TLR4, TRAF1, NFKB1, IRF5, STAT1, S100A8, S100A9, LYZ, CST3, FCN1

### Myeloid Dendritic Cells (cDC2)

Description: Myeloid dendritic cells (cDC2) are CD1c+ dendritic cells that are potent antigen-presenting cells and often confused with monocytes.

Genes:
- CD1C, FCER1A, CLEC10A, CD33, HLA-DRA, HLA-DRB1, CD11c, ITGAX, CD86, CD40, FLT3, IRF4
- ZBTB46, CD207, CLEC4A, CLEC4C, CCR7, CCL17, CCL22, IL12, IL23, TNF, IL6, IL1B

### Non-classical Monocytes

Description: Non-classical monocytes are CD14dimCD16++ cells that patrol the vasculature and have a unique transcription factor profile.

Genes:
- FCGR3A, CD14, CX3CR1, CDKN1C, PRAM1, LILRA2, FCER1G, ITGAL, NR4A1, NR4A2, KLF2, AHR
- PTPRC, SIGLEC10, TNFAIP3, IL13RA1, IL10, TGFB1, C1QA, C1QB, VSIG4, MERTK

## cd16 mono

### CD14+ Monocyte (classical)

Description: Classical monocytes expressing high CD14 and low FCGR3A, key in phagocytosis, inflammatory response, and differentiation into macrophages and DCs.

Genes:
- CD14, FCGR1A, CSF1R, S100A8, S100A9, LYZ, CTSS, CD68, MRC1, IL1B, TNF, CCL2
- CCR2, CD33, CD163, CXCL8, IL6, TLR2, TLR4, CLEC7A, FCGR2A, ITGAM, ITGAX, TREM1

### CD16+ Monocyte (non-classical)

Description: Non-classical monocytes expressing high FCGR3A (CD16) and low CD14, involved in patrolling vasculature and producing TNF-alpha upon TLR stimulation.

Genes:
- FCGR3A, LILRB2, LST1, CDKN1C, MS4A7, RHOC, CX3CR1, LILRA3, LILRB1, FCGR3B, ADAP2, TAGAP
- LRRN3, SIGLEC10, IGSF6, TMEM176A, TMEM176B, CLEC4E, SLC7A8, ZNF789, RASGRP2, PTPN22, TREM1, TREM2
- SIRPA

### Conventional dendritic cell 2 (cDC2)

Description: Conventional dendritic cells type 2 expressing CD1C and FCER1A, specialize in antigen presentation and activation of CD4+ T cells.

Genes:
- CD1C, FCER1A, CLEC10A, HLA-DRA, CD74, ITGAX, CD11C, SIRPA, S100A9, LAMP3, CCR7, IL10
- IL12B, TNF, CD40, CD86, CD80, TLR4, TLR2, CLEC4A, S100A8, CD33, CD36, FCGR2B

### Intermediate Monocyte

Description: Intermediate monocytes co-expressing CD14 and CD16, secrete high levels of IL-10 and TNF-alpha, and are involved in antigen presentation.

Genes:
- CD14, FCGR3A, HLA-DRA, CD74, CTSD, CD86, FCGR1A, CX3CR1, CCR2, CCL3, CCL4, IL1RN
- TNF, IL6, CD40, TLR4, TLR2, CD36, CLEC4E, SIRPA, CD1C, FCER1A, CLEC10A

### NK cell

Description: Natural killer cells with cytotoxic granules, expressing NKG7, GNLY, and PRF1, involved in innate immunity against infected or transformed cells.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMK, KLRD1, KLRB1, KLRK1, NCR1, NCR3, CD247, FCGR3A
- TYROBP, KIR2DL1, KIR3DL1, SH2D1B, TRDC, TRGC2, KLRC1, KLRC2, KLRF1, KLRC3, KLRG1, GZMH

