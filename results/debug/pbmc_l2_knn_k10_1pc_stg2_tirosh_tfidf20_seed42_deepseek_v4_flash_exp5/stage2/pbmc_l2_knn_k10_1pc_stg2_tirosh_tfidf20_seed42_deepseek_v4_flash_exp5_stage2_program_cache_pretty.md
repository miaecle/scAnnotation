# Stage-2 Precomputed Programs

- tissue: PBMC
- n_program_genes: 50
- n_cached_cell_types: 3

## b memory

### B memory

Description: Memory B cells are antigen-experienced B cells that express CD27 and CD19, capable of rapid response upon re-exposure to antigen.

Genes:
- CD27, MS4A1, CD19, CD79A, CD79B, BANK1, PAX5, TCL1A, LTB, TNFRSF13C, CD40, BCL2
- IL4R, POU2F2, IRF4, MEF2B, EBF1, VPREB3, JCHAIN, PIM2, MYC, CCND2, MKI67, AICDA
- BCL6

### B naive

Description: Naive B cells are mature B cells that have not encountered antigen, expressing surface IgM and IgD along with CD19 and CD20.

Genes:
- IGHD, IGHM, MS4A1, CD19, CD79A, CD79B, PAX5, BANK1, TCL1A, FCER2, CR2, IL4R
- POU2F2, EBF1, VPREB3, LTB, TNFRSF13C, BCL2, CD40, MEF2B, IRF4, PIM2, MYC, CCND2
- CD22

### CD4+ memory T cells

Description: CD4+ memory T cells are antigen-experienced helper T cells that express CD4 and IL7R, providing rapid responses upon recall antigen exposure.

Genes:
- CD4, IL7R, CCR7, SELL, LEF1, TCF7, FOXP1, MYC, BCL2, LTB, IL6ST, CD27
- CD28, ICOS, CD40LG, TNFRSF4, TNFRSF25, BATF, IRF4, STAT3, GATA3, CCL5

### Plasma cells

Description: Plasma cells are antibody-secreting cells derived from B cells, characterized by high expression of CD38 and SDC1 (CD138) and low or absent CD20.

Genes:
- SDC1, CD38, MZB1, XBP1, IRF4, PRDM1, JCHAIN, IGHG1, IGHA1, IGLL5, DERL3, FKBP11
- SSR4, PDIA4, TNFRSF17, SLAMF7, CD27, POU2AF1, IL6R, CD19

## cd14 mono

### CD1c+ Dendritic Cells

Description: CD1c+ conventional dendritic cells (cDC2) are specialized in antigen presentation to CD4+ T cells and express high levels of MHC class II and CD1c.

Genes:
- CD1C, FCER1A, CLEC10A, CD1E, HLA-DRA, HLA-DRB1, CD86, CD40, CCR7, IRF4, IRF8, ZBTB46
- FLT3, FCGR2B, CD11c, ITGAX, AXL, SIGLEC6, BCL6, ID2, BATF3, TLR1, TLR2, TLR3
- TLR4, TLR6, TLR8, IL12A, IL12B, IL23A

### Classical Monocytes

Description: Classical CD14++CD16- monocytes are phagocytic and pro-inflammatory, expressing high levels of CD14 and myeloid-related proteins.

Genes:
- CD14, LYZ, S100A8, S100A9, FCGR1A, CSF1R, CCR2, CD33, ITGAM, CD68, CTSS, CTSD
- FOS, JUN, S100A12, VCAN, FPR1, FPR2, TREM1, TLR2, TLR4, CD86, HLA-DRA, HLA-DRB1
- CD163, MNDA, NCF1, NCF2, CYBB, CLEC7A, CLEC4E

### Intermediate Monocytes

Description: Intermediate CD14+CD16+ monocytes exhibit a mixed phenotype with high antigen presentation capacity and inflammatory cytokine production.

Genes:
- CD14, FCGR3A, CD16, HLA-DRA, HLA-DRB1, CD86, CCR5, CX3CR1, TLR4, TLR2, IL1B, TNF
- CCL3, CCL4, CCL5, CXCL8, IL6, CD40, CD80, ICAM1, VCAM1, LTA, LTB, FOS
- JUN, NFKB1, RELA, IRF1, IRF8, STAT1

### Non-classical Monocytes

Description: Non-classical CD14lowCD16++ monocytes patrol the vasculature and exhibit a more anti-inflammatory or housekeeping function.

Genes:
- FCGR3A, CD16, CX3CR1, LILRA3, LILRB1, LILRB2, LILRB4, NR4A1, Nur77, MAFB, KLF4, ITGAL
- CD11c, ITGAX, CD49d, FCER1G, FCGR2C, FCGR2B, CSF1R, CD86, HLA-DRA, HLA-DRB1, CD14low, CD163low
- CCR2low, TLR7, TLR8, IRF4, IRF2, LYVE1

### Plasmacytoid Dendritic Cells

Description: Plasmacytoid dendritic cells are specialized in type I interferon production in response to viral nucleic acids and express CD123 and BDCA-2.

Genes:
- IL3RA, CD123, CLEC4C, CD303, BDCA2, LILRA2, IRF7, IRF8, TLR7, TLR9, MYD88, IFIH1
- DDX58, LY6E, BST2, CD4, CD68, HLA-DRA, HLA-DRB1, CD86, CD40, CCR5, CXCR3, CXCR4
- IL15, IL18, IFNA1, IFNA2, IFNB1, TNF

## cd16 mono

### CD14 Monocyte

Description: Classical CD14+ monocytes with high expression of CD14 and S100A8/A9, primary responders to infection and tissue damage.

Genes:
- CD14, S100A8, S100A9, LYZ, FCN1, VCAN, CCL2, CCL7, CXCL1, CXCL2, CXCL3, IL1RN
- IL1R1, NFKB1, NFKB2, REL, RELA, SERPINA1, SERPINB2, PLAUR, SLPI, TIMP2, TIMP3, MMP9
- MMP12, CTSD, CTSB, CTSK, CST3, CPVL, RNASE1, RNASE2, RNASE3, ARHGDIB, RAB7A, RAB31
- RAB32, CD68, CD163, MSR1, SCARB1, SCARB2, MERTK, AXL, TYRO3, GA87, GAS6

### CD16 Monocyte

Description: Non-classical CD16+ monocytes with high expression of FCGR3A and CX3CR1, patrolling endothelium and involved in inflammation.

Genes:
- FCGR3A, MS4A7, LST1, CSF1R, CX3CR1, LILRA3, RHOC, MNDA, CTSS, IFITM3, CFP, FTL
- LGALS2, PSAP, TYROBP, FCGRT, ATP1B3, LRRC25, SIGLEC10, PLAC8, PECAM1, CDKN1C, NR4A2, TREM2
- SLC2A3, MARCKS, CYBB, MAFB, C5AR1, TNFRSF1B, IL1B, CCL3, CCL4, CCL4L2, CXCL8, TIMP1
- LGALS3, S100A4, S100A11, S100A6, S100A10, CALM2, CD99, COTL1, ARPC3, ARPC4, SRGN, GABARAPL1

### NK Cell

Description: NK cells expressing cytotoxic molecules such as NKG7, GNLY, and PRF1, and KIR receptors, mediating innate killing of infected or tumor cells.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMA, GZMH, GZMK, GZMM, KLRD1, KLRK1, KLRC1, KLRC2
- KLRC3, KLRF1, KLRG1, NCR1, NCR3, NCR2, CD160, CD244, CD247, KIR2DL1, KIR2DL2, KIR2DL3
- KIR3DL1, KIR3DL2, FCGR3A, FGFBP2, SPON2, HOPX, XCL1, XCL2, CCL5, PRSS23, S100A4, FOS
- JUN, DUSP1, DUSP2, ZFP36, ZFP36L1, ZFP36L2, EGR1, EGR2, NR4A1, NR4A2, NR4A3

### cDC2

Description: Conventional dendritic cells type 2 (cDC2) with high CD1C and FCER1A, capable of priming CD4+ T cell responses to antigens.

Genes:
- CD1C, FCER1A, CLEC10A, CLEC4A, CD1E, CD1B, CD1D, CD207, LAMP3, CCR7, CCL17, CCL22
- IL12B, IL23A, IL1B, IL6, TNF, IRF4, IRF8, BATF3, ID2, ZBTB46, FLT3, CSF2RA
- CSF2RB, CD86, CD80, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, CD74, CIITA, CTSS
- CTSL, IFNGR1, IFNGR2, TNFRSF9, CD40, CD83, CD200, CD274, PDCD1LG2, CDKN1A, BIRC3, NFKB1

### pDC

Description: Plasmacytoid dendritic cells (pDC) with high IL3RA and CLEC4C, specialized in type I interferon production in response to viral infection.

Genes:
- IL3RA, CLEC4C, LILRA4, TCF4, IRF7, IRF8, IRF4, BCL11A, SPIB, E2-2, TLR7, TLR9
- MYD88, SLC15A4, PACSIN1, SIGLEC1, SIGLEC5, SIGLEC6, SIGLEC10, BST2, PLAC8, CCDC50, GPR174, ITM2C
- SCARB1, LAMP5, MPEG1, CTSH, CTSL, CTSB, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1
- CD74, IFITM1, IFITM2, IFITM3, MX1, MX2, OAS1, OAS2, OAS3, ISG15, IFIT1, IFIT2
- IFIT3, IFI44, IFI44L

