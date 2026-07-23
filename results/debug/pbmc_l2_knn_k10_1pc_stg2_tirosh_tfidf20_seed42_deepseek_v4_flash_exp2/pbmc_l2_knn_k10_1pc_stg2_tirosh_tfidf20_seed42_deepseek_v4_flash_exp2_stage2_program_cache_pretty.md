# Stage-2 Precomputed Programs

- tissue: PBMC
- n_program_genes: 50
- n_cached_cell_types: 3

## b memory

### B memory (activated)

Description: Activated memory B cells undergoing proliferation and differentiation, marked by CD38, CD69, and cell cycle genes.

Genes:
- MS4A1, CD79A, CD79B, CD19, CD27, CD38, CD69, CD86, CD80, MKI67, PCNA, TOP2A
- BIRC5, AURKB, CCNB1, CDK1, MYC, IRF4, XBP1, PRDM1, SLAMF7, CD138, JCHAIN, IGHA1
- IGHG1, IGHM, IGHD, IGKC, IGLC1, HLA-DRA, HLA-DRB1, CD74, B2M, CD40, CD83, IL4R
- TNFRSF13C, FAS, ICOSL, POU2AF1

### B memory (resting)

Description: Resting memory B cells expressing CD27 and BCL6, maintaining quiescence with low proliferation markers.

Genes:
- MS4A1, CD79A, CD79B, CD19, CXCR5, CD27, CD40, BACH2, PAX5, EBF1, BCL6, AICDA
- ICOSL, CD83, HLA-DRA, HLA-DRB1, CD74, B2M, CD37, CD22, FCGR2B, IL4R, TNFRSF13C, TNFRSF13B
- CR2, FCMR, BTLA, TCL1A, POU2F2, IRF8, SPIB, POU2AF1, MAF, MYB, BCL11A, MEF2C
- ETS1, CREBBP, EP300, HDAC7

### Naive B cell

Description: Naive B cells expressing IgD and CD27-negative, with CD5 typically low in PBMC but included as a marker.

Genes:
- MS4A1, CD79A, CD79B, CD19, CD27, CD38, IGHD, IGHM, IGHD, CD5, CD21, CD22
- CD23, CD24, CD40, CD72, CR2, FCER2, IL4R, BACH2, PAX5, EBF1, BCL6, TCL1A
- POU2F2, IRF8, SPIB, POU2AF1, MAF, MYB, BCL11A, MEF2C, ETS1, CREBBP, EP300, HDAC7
- HLA-DRA, HLA-DRB1, CD74, B2M

### Plasma cell

Description: Antibody-secreting plasma cells with high expression of immunoglobulin chains and endoplasmic reticulum stress response genes.

Genes:
- SDC1, XBP1, PRDM1, IRF4, JCHAIN, MZB1, SLAMF7, CD38, CD138, TNFRSF17, IGHA1, IGHG1
- IGHM, IGHD, IGKC, IGLC1, IGHV, IGKV, IGLV, HSP90B1, HSPA5, PDIA4, PDIA6, PDIA3
- ERP29, ERP44, CALR, CANX, FKBP11, SEC61A1, SEC61B, SRPRB, SSR1, SSR2, SSR3, SSR4
- TRAM1, TRAM2, STT3A, STT3B

## cd14 mono

### Classical Monocytes

Description: Classical CD14++CD16- monocytes are the most abundant monocyte subset in PBMC, expressing high levels of CD14 and low CD16, and are involved in phagocytosis, antigen presentation, and inflammatory responses.

Genes:
- CD14, LYZ, S100A8, S100A9, FCN1, CST3, CTSS, PSAP, CTSD, NPC2, LGALS3, GRN
- RNASE1, SERPINA1, FCGR2A, CSF1R, CD33, CD68, ITGAM, CLEC7A, CLEC4E, TLR2, TLR4, MYD88
- IRAK1, TNF, IL1B, IL6, CCL2, CCL3, CCL4, CXCL8, CXCL2, CXCL3, SOD2, HSPA1A
- HSPA1B, HSP90AA1, HSP90AB1, NFKB1, NFKB2, RELA, JUN, FOS, MAPK1, MAPK3, STAT3, STAT1

### Intermediate Monocytes

Description: Intermediate CD14++CD16+ monocytes express both CD14 and CD16, and are pro-inflammatory with higher antigen-presenting capacity than classical monocytes.

Genes:
- CD14, FCGR3A, CD163, CD86, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, CD74, CIITA
- CCR2, CX3CR1, TLR7, TLR8, TNF, IL1B, IL6, CCL3, CCL4, CCL5, CXCL9, CXCL10
- CXCL11, STAT1, STAT2, IRF1, IRF8, IFI6, IFIT1, IFIT3, MX1, OAS1, OAS2, OAS3
- ISG15, USP18, LY6E, SIGLEC1, CD169, CD163, FCGR2A, FCGR2B, FCGR3A

### Myeloid Dendritic Cells

Description: Myeloid dendritic cells (cDC2) are professional antigen-presenting cells that can be confused with monocytes due to shared CD11c and CD14 expression, but they uniquely express CLEC10A and CD1c.

Genes:
- FCER1A, CLEC10A, CD1C, CD1A, CD1B, CD1D, CD1E, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1
- HLA-DPB1, CD74, CIITA, IRF8, IRF4, ZBTB46, CLEC4A, CLEC6A, CLEC7A, CD209, LAMP3, CCL17
- CCL22, IL12B, IL23A, TNF, CD40, CD80, CD86, ICOSLG, PDL1, CD83, IDO1, IDO2
- ARG2, S100A9, S100A8, CD14, CD16, CD11C, ITGAX, CSF1R, FLT3, FLT3LG

### Non-classical Monocytes

Description: Non-classical CD14+CD16++ monocytes patrol the vasculature, scan for damage, and secrete anti-inflammatory cytokines.

Genes:
- FCGR3A, MS4A7, CDKN1C, NR4A1, NR4A2, NR4A3, KLF2, KLF4, KLF7, CCL3L1, CCL4L1, CXCL16
- SLCO2B1, SIGLEC10, LILRB2, LILRB4, FCGR2A, FCGR2C, FCGR3B, TLR1, TLR6, TLR10, IL10, TGFB1
- CCL2, CCL7, CCL8, CCL13, CXCL5, CXCL6, CXCL12, CXCR4, ITGAL, ITGB2, ITGAM, ITGAX
- FCER1G, LST1, AIF1, SAT1, TFRC, SCARB2, CD83, CD86, HLA-DRA, HLA-DRB1

## cd16 mono

### CD16+ Monocyte (Non-classical)

Description: Non-classical monocytes expressing CD16 (FCGR3A) and patrolling chemokine receptor CX3CR1, involved in vascular surveillance and inflammation.

Genes:
- FCGR3A, MS4A7, LST1, CX3CR1, LILRA2, CSF1R, LRRC25, HES4, RHOC, TBCC, NCF1, CLEC4E
- SIGLEC10, FGR, MYO1F, FCGR2A, IFITM3, IFITM2, S100A12, S100A8, S100A9, LYZ, VCAN, FOS
- JUNB, EGR1, NR4A1, NR4A2, TXN, TXNIP, PFN1, ACTB, GAPDH, RPLP0, RPL13A, RPS18
- RPS27A, RPL32, RPL27, RPS3, RPS8, RPL41, RPS15A, RPL17

### Classical Monocyte (CD14+)

Description: Classical monocytes with high CD14 expression, strong phagocytic activity, and production of pro-inflammatory cytokines like IL-6 and TNF-α.

Genes:
- CD14, LYZ, S100A8, S100A9, FCN1, CTSS, CST3, PSAP, LGALS1, LGALS3, S100A11, S100A6
- S100A4, NPC2, FTL, FTH1, TIMP1, MARCKS, FOS, JUNB, EGR1, NR4A1, NR4A2, TXN
- TXNIP, PFN1, ACTB, GAPDH, RPLP0, RPL13A, RPS18, RPS27A, RPL32, RPL27, RPS3, RPS8
- RPL41, RPS15A, RPL17

### Myeloid Dendritic Cell (cDC)

Description: Conventional myeloid dendritic cells expressing FCER1A, CLEC10A, and CD1C, specialized in antigen presentation and T-cell activation.

Genes:
- FCER1A, CLEC10A, CD1C, CD1E, CD1A, CD1B, FCGR2B, FSCN1, CCL22, CCL17, CCR7, LAMP3
- CD40, CD80, CD86, ICOSLG, PDCD1LG2, CD274, CD83, HLA-DRA, HLA-DPB1, HLA-DPA1, HLA-DQA1, HLA-DQB1
- HLA-DRB1, HLA-DRB5, CIITA, CD74, IRF4, IRF8, ZBTB46, FLT3, CSF1R, AXL, SIGLEC6, SIGLEC10
- CD33, CD14, LYZ, CTSS, CST3, PSAP, NPC2, LGALS3, LGALS1, FTL, FTH1

### NK Cell

Description: Natural killer cells expressing NKG7, GNLY, PRF1, and GZMB, with cytotoxic function and production of interferon-gamma.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMK, GZMH, KLRD1, KLRB1, KLRK1, KLRC1, KLRC2, KLRF1
- CD247, CD3E, CD3D, CD3G, CD2, CD7, IL2RB, IL2RG, FCGR3A, FGFBP2, SPON2, CCL3
- CCL4, XCL1, XCL2, IFNG, PRDM1, ZEB2, TBX21, EOMES, ID2, STAT4, IL12RB2, IL18RAP
- IL18R1, KIR2DL1, KIR2DL3, KIR3DL1, LILRB1, LILRB2, HLA-C, HLA-E, HLA-G

