# Stage-2 Precomputed Programs

- tissue: PBMC
- n_program_genes: 50
- n_cached_cell_types: 31

## asdc

### ASDC

Description: Sialic acid-binding immunoglobulin-type lectin (Siglec) expressing dendritic cell (ASDC), a CD1c+ conventional dendritic cell subset in PBMC characterized by high expression of CD1C, FCER1A, and CLEC10A, involved in antigen presentation and immune regulation.

Genes:
- CD1C, FCER1A, CLEC10A, CD1A, TREM1, CD1B, ITGAX, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, HLA-DQA1
- HLA-DQB1, CD74, FCGR2A, FCGR2B, CD36, MRC1, CD1D, CD1E, CLEC4C, LILRA4, IRF4, IRF8
- BATF3, TCF4, CTSC, LYZ, S100A4, S100A6, S100A10, S100A11, ANXA1, ANXA2, ANXA5, LGALS1
- LGALS3, LGALS9, CST3, TYROBP

### B_cell

Description: B cell, a lymphoid cell subset in PBMC responsible for antibody production and antigen presentation, characterized by expression of B cell markers such as CD19, MS4A1 (CD20), and CD79A/B.

Genes:
- CD19, MS4A1, CD79A, CD79B, BLK, BANK1, CD22, FCRL2, FCRL4, FCRL5, TCL1A, TCL1B
- IGHM, IGHD, IGKC, IGLC2, IGLL1, VPREB3, CD24, CD38, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1
- HLA-DQA1, HLA-DQB1, CD74, FCER2, CR2, CD21, CD81, CD82, CD53, CD37, CD52, LYN
- SYK, BTK, BLNK, PAX5

### cDC2

Description: Conventional dendritic cell type 2 (cDC2), a major dendritic cell subset in PBMC specialized in CD4+ T cell priming, characterized by expression of CD1C, FCER1A, and MHC class II molecules.

Genes:
- CD1C, FCER1A, CLEC10A, CD1A, ITGAX, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, CD74
- FCGR2A, CD36, MRC1, CD1D, CD1E, CLEC4C, LILRA4, IRF4, IRF8, BATF3, TCF4, CTSC
- LYZ, S100A4, S100A6, S100A10, S100A11, ANXA1, ANXA2, ANXA5, LGALS1, LGALS3, LGALS9, CST3
- TYROBP, FCGR1A, FCGR3A, CD68

### monocyte

Description: Monocyte, a myeloid cell subset in PBMC that can differentiate into macrophages or dendritic cells, characterized by high expression of CD14, LYZ, and S100A8/S100A9.

Genes:
- CD14, LYZ, S100A4, S100A6, S100A8, S100A9, S100A10, S100A11, ANXA1, ANXA2, ANXA5, LGALS1
- LGALS2, LGALS3, CST3, FCGR3A, FCGR2A, FCGR1A, CD68, CD36, MRC1, ITGAM, ITGAX, CCR2
- CCR5, CX3CR1, TYROBP, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, CD74, FCER1A, CD1C
- CD1A, CLEC10A, CTSC

### pDC

Description: Plasmacytoid dendritic cell (pDC), a specialized dendritic cell subset in PBMC that produces large amounts of type I interferons in response to viral infections, characterized by expression of CLEC4C, LILRA4, and TCF4.

Genes:
- CLEC4C, LILRA4, ITM2C, TCF4, IRF7, IRF8, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1
- CD74, FCER1A, CD1C, CD1A, ITGAX, CD303, CD304, NRP1, CD2AP, SERPINF1, GZMB, GZMA
- NKG7, GNLY, CST3, LYZ, S100A4, S100A6, S100A10, S100A11, ANXA1, ANXA2, ANXA5, LGALS1
- LGALS3, LGALS9, TYROBP, FCGR2A

## b intermediate

### Memory B cells

Description: Antigen-experienced B cells that provide rapid response upon re-exposure, marked by CD27 expression.

Genes:
- MS4A1, CD19, CD27, CD79A, CD79B, CD22, CD21, CD20, CD24, CD38, CD40, CD72
- CD81, CD82, CD180, CD200, CD300A, CD300C, CD300E, CD300H, CD300LB, CD300LD, CD300LE, BANK1
- BLK, FCER2, TCL1A, TCL1B, CD83, CD9

### Naive B cells

Description: Mature B cells that have not yet encountered antigen, expressing high levels of MS4A1 (CD20) and CD19.

Genes:
- MS4A1, CD19, CD79A, CD79B, CD22, CD21, CD20, CD24, CD38, CD40, CD72, CD81
- CD82, CD180, CD200, CD300A, CD300C, CD300E, CD300H, CD300LB, CD300LD, CD300LE, BANK1, BLK
- FCER2, TCL1A, TCL1B, CD27, CD83, CD9

### Plasma cells

Description: Terminally differentiated B cells that secrete large amounts of antibodies, characterized by high CD38 and loss of CD20.

Genes:
- CD38, CD27, CD19, CD79A, CD79B, MS4A1, CD22, CD21, CD20, CD24, CD40, CD72
- CD81, CD82, CD180, CD200, CD300A, CD300C, CD300E, CD300H, CD300LB, CD300LD, CD300LE, BANK1
- BLK, FCER2, TCL1A, TCL1B, CD83, CD9

### Plasmablasts

Description: Activated B cells that have begun differentiating into plasma cells, secreting antibodies and expressing high CD38.

Genes:
- CD27, CD38, CD19, CD79A, CD79B, MS4A1, CD22, CD21, CD20, CD24, CD40, CD72
- CD81, CD82, CD180, CD200, CD300A, CD300C, CD300E, CD300H, CD300LB, CD300LD, CD300LE, BANK1
- BLK, FCER2, TCL1A, TCL1B, CD83, CD9

### Transitional B cells

Description: Immature B cells transitioning from bone marrow to periphery, characterized by high CD24 and CD38 expression.

Genes:
- CD24, CD38, MS4A1, CD19, TCL1A, TCL1B, CD27, CD79A, CD79B, BLK, BANK1, FCER2
- CD72, CD81, CD82, CD83, CD9, CD180, CD19, CD20, CD21, CD22, CD23, CD24
- CD38, CD40, CD79A, CD79B, CD80, CD86, CD180, CD200, CD248, CD300A, CD300C, CD300E
- CD300H, CD300LB, CD300LD, CD300LE

## b memory

### B memory

Description: Circulating antigen-experienced B cells expressing memory markers such as CD27 and class-switched or IgM-only BCRs, poised for rapid recall responses.

Genes:
- CD19, MS4A1, CD79A, CD79B, BANK1, BLK, FCRL4, FCRL5, TCL1A, TCL1B, CD27, ITGA4
- SELL, CD83, TNFRSF13C, IGHM, IGHD, IGHA1, IGHG1, PAX5, SPIB, IKZF3, CD37, CD53
- LINC00926, FCER2, CR2, CD24, CD81, CD82

### B naive

Description: Mature naive B cells expressing IgM/IgD BCRs and homing receptors such as CD62L, not yet exposed to antigen.

Genes:
- CD19, MS4A1, CD79A, CD79B, BANK1, BLK, TCL1A, TCL1B, SELL, IGHM, IGHD, FCER2
- CR2, CD24, PAX5, IKZF3, CD37, CD53, CD81, CD82, IGHA2, IGKC, IGLC2, VPREB3
- CD72, FCRL1, FCRL2, FCRL3, CD74, HLA-DRA

### B transitional

Description: Recent bone marrow emigrants with high CD24 and CD38 expression undergoing peripheral tolerance selection.

Genes:
- CD19, MS4A1, CD79A, CD79B, CD24, CD38, TCL1A, TCL1B, BANK1, BLK, CD27, SELL
- PAX5, IKZF3, CD37, CD53, CD81, CD82, CD74, HLA-DRA, HLA-DRB1, FCRL1, FCRL2, FCRL3
- FCRL4, FCRL5, CR2, FCER2, IGLL5, VPREB3

### Monocyte classical

Description: Classical CD14++ CD16- monocytes with strong phagocytic and inflammatory cytokine production capacity, commonly confused with B cells in low-resolution clustering.

Genes:
- CD14, FCGR3A, LYZ, S100A8, S100A9, S100A4, S100A6, S100A10, S100A11, FCN1, VCAN, CST3
- TYMP, MNDA, IFITM2, IFITM3, CFP, LST1, AIF1, CTSS, HLA-DRA, HLA-DRB1, CD74, IL1B
- TNF, CCL3, CCL4, CXCL8, NLRP3, NAMPT

### Plasmablast

Description: Antibody-secreting blasts recently activated in germinal centers, characterized by high immunoglobulin and ER chaperone expression.

Genes:
- CD19, CD27, CD38, MZB1, JCHAIN, IGHG1, IGHA1, IGKC, IGLC2, XBP1, PRDM1, IRF4
- TNFRSF17, SDC1, PAX5, SPIB, CD79A, CD79B, MS4A1, FCRL5, TCL1A, HSPA9, HSP90B1, DERL3
- SYND1, ELL3, SSR4, SEC61A1, DNAJC3, FKBP11

## b naive

### B activated

Description: Antigen-activated B cells upregulating HLA class II, co-stimulatory molecules (CD80/CD86), early activation markers (CD69, CD83), and plasma cell–directed factors.

Genes:
- MS4A1, CD19, CD79A, CD79B, CD69, CD83, CD86, CD80, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1
- HLA-DPA1, HLA-DPB1, CD74, TNFRSF17, TNFRSF13B, TNFRSF13C, PRDM1, IRF4, XBP1, MZB1, JCHAIN, IGHA1
- IGHG1, IGKC, IGLC2, CD27, CD38, TCL1A, BANK1, FCRL2, FCRL4, FCRL5, PAX5, SPIB
- BCL6, CD37, CD53, CD81

### B memory

Description: Class-switched and unswitched memory B cells marked by CD27, expressing Fc receptors and antigen-experienced transcriptional programs.

Genes:
- MS4A1, CD19, CD79A, CD79B, CD27, TCL1A, BANK1, BLK, FCRL2, FCRL4, FCRL5, CD80
- CD86, ITGAM, CD44, SELL, CXCR5, CD37, CD53, CD72, CD81, CD82, PAX5, SPIB
- BCL6, IRF8, IGHA1, IGHG1, IGKC, IGLC2, TNFRSF13B, TNFRSF13C, PRDM1, PAX1, FCRL1, FCRL6
- CD24, CD38, IGHM, IGHD

### B naive

Description: Mature naive B cells expressing surface IgM/IgD, homing receptors like CXCR5 and SELL, and lacking activation or memory markers.

Genes:
- MS4A1, CD19, CD79A, CD79B, BANK1, BLK, FCRL2, FCRL4, TCL1A, TCL1B, CD24, IGHM
- IGHD, IGLL5, VPREB3, CD22, PAX5, SPIB, BCL6, SELL, CXCR5, ITGB1, CD80, CD86
- FCER2, TNFRSF13C, IGHA1, IGHG1, IGKC, IGLC2, CD37, CD53, CD72, CD81, CD82, FCRL1
- FCRL5, FCRL6, LINC01781, TSPAN13

### B transitional

Description: Recent bone marrow emigrants in blood co-expressing CD24 and CD38 with high TCL1A, representing an immature transitional B cell stage.

Genes:
- CD24, CD38, MS4A1, CD19, CD79A, CD79B, TCL1A, TCL1B, BANK1, BLK, CD93, CD10
- MME, IGLL5, VPREB3, FCRL2, SELL, CXCR5, CD81, CD82, CD37, CD53, CD72, PAX5
- SPIB, IGHM, IGHD, IGKC, IGLC2, FCRL1, FCRL4, FCRL5, FCRL6, TNFRSF13C, BCL6, ITGB1
- CD22, CD80, CD86, FCER2

### Plasmablast

Description: Antibody-secreting plasmablasts with high CD38, MZB1, JCHAIN, and PRDM1, representing late differentiation from activated B cells.

Genes:
- CD38, CD27, MZB1, JCHAIN, PRDM1, IRF4, XBP1, TNFRSF17, SDC1, PAX5, SPIB, IGHA1
- IGHG1, IGKC, IGLC2, IGHA2, IGHG2, IGHG3, IGHG4, IGLL5, VPREB3, CD79A, CD79B, MS4A1
- CD19, HLA-DRA, HLA-DRB1, CD74, TCL1A, BANK1, FCRL4, FCRL5, CD83, CD69, CD44, ITGAM
- CXCR4, CCR10, ITGB1, SELL

## cd14 mono

### CD14 Mono

Description: Classical monocytes characterized by high CD14 expression, involved in innate immune responses, phagocytosis, and pro-inflammatory cytokine production.

Genes:
- CD14, LYZ, S100A8, S100A9, S100A12, FCN1, VCAN, TYMP, CSF3R, CD36, CST3, CTSS
- LST1, CFP, FPR1, FPR2, ITGAM, TLR2, TLR4, IL1B, TNF, CCL3, CCL4, CXCL8
- NAMPT, MNDA, IFITM2, IFITM3, S100A6, S100A4, LGALS2, LGALS3, FCGR3B, MMP9, SERPINA1, SERPIND1
- LTF, APOC1, HMOX1, NCF1, NCF2, NCF4, CYBB, RAC2

### CD16 Mono

Description: Non-classical monocytes with lower CD14 and higher CD16 (FCGR3A) expression, involved in patrolling, antiviral responses, and tissue repair.

Genes:
- FCGR3A, MS4A7, CDKN1C, LILRB1, LILRB2, LILRA3, SIGLEC1, CD9, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1
- HLA-DQA1, HLA-DQB1, CD74, FCER1G, SYK, LYN, ITGAL, ITGAM, CX3CR1, CCR5, CCR2, CD86
- CD80, IL10, TGFB1, VEGFA, MMP14, ADAM8, FOLR2, MRC1, CD163, MSR1, TREM2, GPNMB
- FABP5, LIPA, CTSB, CTSD, CTSL, CTSZ, GZMB, PRF1

### Intermediate Mono

Description: Intermediate monocytes co-expressing CD14 and CD16, representing a transitional state between classical and non-classical monocytes with roles in antigen presentation and inflammation.

Genes:
- CCR2, CX3CR1, FCGR3A, CD14, LYZ, S100A8, S100A9, VCAN, FCN1, TYMP, CSF3R, CD36
- CST3, CTSS, LST1, CFP, FPR1, FPR2, ITGAM, TLR2, TLR4, IL1B, TNF, CCL3
- CCL4, CXCL8, NAMPT, MNDA, IFITM2, IFITM3, S100A6, S100A4, LGALS2, LGALS3, MMP9, SERPINA1
- SERPIND1, LTF, APOC1, HMOX1, NCF1, NCF2, NCF4, CYBB, RAC2, HLA-DRA, HLA-DRB1

### cDC2

Description: Conventional type 2 dendritic cells specialized in antigen presentation to CD4+ T cells, characterized by CD1C and FCER1A expression.

Genes:
- FCER1A, CLEC10A, CD1C, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, CD74, ITGAX, CD14
- FCGR1A, FCGR2A, FCGR3A, CD36, CD86, CD80, CD40, CCR7, CCL22, CXCL10, IL12A, IL12B
- IL23A, TNF, IL1B, IL6, CCL3, CCL4, CCL5, CXCL8, CXCL9, IRF4, BATF3, ZBTB46
- CIITA, NLRP3, NOD2, TLR2, TLR4, TLR7, TLR8, MYD88, IRF5

### pDC

Description: Plasmacytoid dendritic cells specialized in type I interferon production in response to viral infections, characterized by NRP1, IL3RA, and TLR7/TLR8 expression.

Genes:
- NRP1, IL3RA, CD303, CD304, TCF4, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, CD74
- ITGAX, CD14, FCGR1A, FCGR2A, FCGR3A, CD36, CD86, CD80, CD40, CCR7, CCL22, CXCL10
- IL12A, IL12B, IL23A, TNF, IL1B, IL6, CCL3, CCL4, CCL5, CXCL8, CXCL9, IRF4
- BATF3, ZBTB46, CIITA, NLRP3, NOD2, TLR2, TLR4, TLR7, TLR8, MYD88, IRF5, IRF7

## cd16 mono

### Classical Monocytes

Description: CD14++CD16- classical monocytes that patrol the vasculature and are the most abundant monocyte subset in peripheral blood.

Genes:
- FCN1, S100A8, S100A9, S100A12, LYZ, VCAN, CD14, FCGR3A, CST3, TYMP, MNDA, S100A6
- S100A4, FTH1, FTL, CFP, LST1, IFITM2, IFITM3, GPR183, CTSS, HLA-DRA, HLA-DRB1, IL1B
- TNF, CCL3, CCL4, CXCL8, NAMPT, NCF1, NCF2, NCF4, CYBA, CYBB, RAC2, RAB37
- MMP9, MMP8, SERPINA1, SERPINA3, ALDH2, ANXA2, ANXA3, LGALS2, LGALS3

### Intermediate Monocytes

Description: CD14++CD16+ intermediate monocytes with high MHC-II expression that serve as transitional cells between classical and non-classical monocytes and are potent antigen-presenting cells.

Genes:
- FCGR3A, CD14, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, CCR2, CCR5, CX3CR1, FCN1
- LYZ, VCAN, S100A8, S100A9, S100A12, CST3, TYMP, MNDA, IFITM2, IFITM3, CFP, LST1
- NAMPT, IL1B, TNF, CCL3, CCL4, CXCL10, CXCL11, CXCL9, IDO1, IDO2, IDO3, IDO4
- IDO5, IDO6, IDO7, IDO8, IDO9, IDO10, IDO11, IDO12, IDO13, IDO14, IDO15

### Non-classical Monocytes

Description: CD14dimCD16+ non-classical monocytes that patrol the endothelium, respond to nucleic acids via TLR7/8, and are involved in vascular repair and antiviral responses.

Genes:
- FCGR3A, CX3CR1, CDKN1C, MS4A7, LYN, TREM1, SIGLEC10, SIGLEC1, CD163, MRC1, C1QA, C1QB
- C1QC, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, FCN1, LYZ, VCAN, S100A8, S100A9, S100A12, CST3
- TYMP, MNDA, IFITM2, IFITM3, CFP, LST1, NAMPT, IL1B, TNF, CCL3, CCL4, CXCL10
- CXCL11, CXCL9, IDO1, IDO2, IDO3, IDO4, IDO5, IDO6, IDO7, IDO8, IDO9, IDO10
- IDO11, IDO12, IDO13, IDO14, IDO15

### cDC2

Description: Conventional type 2 dendritic cells that present antigen to CD4+ T cells and can be confused with monocytes due to shared myeloid markers and morphology.

Genes:
- FCER1A, CLEC10A, CD1C, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, FCN1, LYZ, VCAN
- S100A8, S100A9, S100A12, CST3, TYMP, MNDA, IFITM2, IFITM3, CFP, LST1, NAMPT, IL1B
- TNF, CCL3, CCL4, CXCL10, CXCL11, CXCL9, IDO1, IDO2, IDO3, IDO4, IDO5, IDO6
- IDO7, IDO8, IDO9, IDO10, IDO11, IDO12, IDO13, IDO14, IDO15, CD14, FCGR3A, S100A4
- S100A6

### pDC

Description: Plasmacytoid dendritic cells specialized for type I interferon production in response to viral infections and can be confused with monocytes due to shared HLA and myeloid markers.

Genes:
- IL3RA, CLEC4C, TCF4, NRP1, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, FCN1, LYZ
- VCAN, S100A8, S100A9, S100A12, CST3, TYMP, MNDA, IFITM2, IFITM3, CFP, LST1, NAMPT
- IL1B, TNF, CCL3, CCL4, CXCL10, CXCL11, CXCL9, IDO1, IDO2, IDO3, IDO4, IDO5
- IDO6, IDO7, IDO8, IDO9, IDO10, IDO11, IDO12, IDO13, IDO14, IDO15, CD14, FCGR3A
- S100A4, S100A6

## cd4 ctl

### CD4 CTL

Description: Cytotoxic CD4+ T cells with effector cytotoxic granule programs, often expanded in chronic infection, cancer, and aging.

Genes:
- GZMB, PRF1, NKG7, GNLY, GZMH, GZMA, CST7, IFNG, FASLG, EOMES, TBX21, CX3CR1
- FGFBP2, KLRD1, KLRB1, CD8A, CD8B, KLRK1, KLRG1, TYMP, GZMK, IL32, CCL4, CCL3
- XCL1, XCL2, HOPX, RUNX3, ZEB2, CD27

### CD4 TCM

Description: Central memory CD4+ T cells with lymph-node homing and self-renewal capacity, lacking cytotoxic granule markers.

Genes:
- CCR7, SELL, LEF1, TCF7, IL7R, MAL, S1PR1, CD27, CD28, ITGB1, CXCR4, CD40LG
- ICOS, CD69, CD44, CD2, CD3D, CD3E, CD3G, LCK, ZAP70, LAT, THEMIS, TRAT1
- GADS, PLCG1, PIK3CD, VAV1, ITK, RHOH

### CD4 TEM

Description: Effector memory CD4+ T cells with tissue-homing and co-stimulatory markers, distinct from the cytotoxic program.

Genes:
- CCR7, SELL, IL7R, CD40LG, ICOS, CTLA4, TNFRSF9, TNFRSF4, PDCD1, LAG3, HAVCR2, TIGIT
- TOX, TCF7, LEF1, MAL, ITGB1, CD69, CD44, CXCR4, IL2RA, FOXP3, IKZF2, BATF
- IRF4, MAF, CD28, CD2, CD3D, CD3E

### CD8 TEM

Description: Cytotoxic CD8+ effector memory T cells that share cytotoxic programs with CD4 CTL but are distinguished by CD8A/CD8B expression.

Genes:
- CD8A, CD8B, GZMB, PRF1, NKG7, GNLY, GZMH, GZMA, CST7, FGFBP2, CX3CR1, KLRD1
- KLRG1, EOMES, TBX21, IFNG, FASLG, TYMP, GZMK, IL32, CCL4, CCL3, XCL1, XCL2
- HOPX, RUNX3, ZEB2, CD27, CD57, FCGR3A

### NK cells

Description: Natural killer cells with abundant cytotoxic granules and NK receptors, lacking CD3/TCR expression and often confused with CD4 CTL in low-resolution clustering.

Genes:
- NCAM1, NKG7, GNLY, KLRD1, KLRB1, KLRK1, KLRG1, FCGR3A, FCER1G, TYROBP, EOMES, TBX21
- PRF1, GZMB, GZMH, GZMA, CST7, FGFBP2, CX3CR1, TYMP, IL2RB, IL15RA, CD7, CD2
- CD3D, CD3E, CD244, SLAMF7, TNFRSF10A, TNFRSF10B

## cd4 naive

### B cell Naive

Description: Mature, antigen-inexperienced B cells expressing surface IgM/IgD and B cell receptor components, circulating in blood and secondary lymphoid organs.

Genes:
- CD19, MS4A1, CD79A, CD79B, BLK, BANK1, CD22, PAX5, TCL1A, TCL1B, FCER2, CD24
- CD38, IGHM, IGHD, IGLL5, VPREB3, CD79A, CD79B, BLK, BANK1, CD19, MS4A1, CD22
- FCER2, TCL1A, TCL1B, CD24, CD38, IGHM

### CD4 Central Memory T cell

Description: Antigen-experienced CD4+ T cells retaining lymphoid homing capacity via CCR7 expression, capable of rapid recall responses and helper functions.

Genes:
- CCR7, IL7R, CD27, CD28, CD3D, CD3E, CD2, GIMAP5, GIMAP2, GIMAP4, GIMAP7, GIMAP8
- TRAT1, MAL, LEF1, TCF7, BACH2, FOXO1, KLF2, KLF4, MYC, S100A4, ITGB1, LTB
- SELL, CD40LG, ICOS, TNFRSF9, TNFRSF4, CD69

### CD4 Effector Memory T cell

Description: Antigen-experienced CD4+ T cells lacking CCR7, circulating through peripheral tissues with effector functions including cytokine production and cytotoxic potential.

Genes:
- GZMA, GZMB, GZMH, GZMK, PRF1, NKG7, GNLY, CCL4, CCL3, CCL5, IFNG, TNF
- IL2, CD3D, CD3E, CD2, CD28, CD7, ITGB1, ITGAE, CXCR3, CXCR6, CCR6, CCR4
- ICOS, CD69, CD40LG, FGFBP2, HOPX, EOMES

### CD4 Naive T cell

Description: Resting, antigen-inexperienced CD4+ T cells expressing lymphoid homing receptors CCR7 and L-selectin, poised for primary immune responses.

Genes:
- CCR7, LEF1, SELL, TCF7, MAL, IL7R, CD27, CD28, LTB, ITGB1, CD3D, CD3E
- CD2, GIMAP5, GIMAP2, GIMAP4, GIMAP7, GIMAP8, TRAT1, S100A4, MYC, BACH2, FOXO1, KLF2
- KLF4, LEF1, TCF7, CCR7, SELL, IL7R

### CD8 Naive T cell

Description: Resting, antigen-inexperienced CD8+ T cells expressing lymphoid homing markers, requiring activation to differentiate into cytotoxic effectors.

Genes:
- CCR7, LEF1, SELL, TCF7, MAL, IL7R, CD27, CD28, LTB, ITGB1, CD3D, CD3E
- CD8A, CD8B, CD2, GIMAP5, GIMAP2, GIMAP4, GIMAP7, GIMAP8, TRAT1, S100A4, MYC, BACH2
- FOXO1, KLF2, KLF4, LEF1, TCF7, CCR7

## cd4 proliferating

### CD4 Memory

Description: Antigen-experienced memory CD4+ T cells with enhanced effector and survival capabilities, expressing activation and memory markers.

Genes:
- IL7R, CD40LG, CD28, ICOS, CD69, ITGB1, ITGA4, CXCR4, CD44, GZMK, GZMA, NKG7
- PRF1, CST7, GNLY, EOMES, TBX21, CXCR3, CCR6, CTLA4, TNFRSF9, TNFRSF4, PDCD1, TOX
- IRF4, BATF, MAF, CD2, LCK, LAT, THEMIS, CORO1A, RHOH, FAS, BCL2, IL6R
- IL6ST, STAT3, SOCS3, CISH, SOCS1

### CD4 Naive

Description: Resting naive CD4+ T cells that have not yet encountered antigen, marked by lymphoid homing receptors and naive-associated transcription factors.

Genes:
- CCR7, LEF1, TCF7, SELL, IL7R, CD27, CD28, MAL, ITGB1, ITGA4, CD40LG, GIMAP2
- GIMAP4, GIMAP5, GIMAP6, GIMAP7, GIMAP8, FAS, BACH2, KLF2, KLF4, FOXO1, S1PR1, LTB
- AC005154.6, TRAT1, CD3D, CD3E, CD2, LCK, LAT, THEMIS, CORO1A, RHOH, MYO1G, TSC22D3
- LEF1-AS1, SATB1, TCF7-AS1, MYC, BCL11B

### CD4 Proliferating

Description: Activated CD4+ T cells undergoing cell cycle progression, characterized by high expression of proliferation and mitosis-associated genes.

Genes:
- MKI67, TOP2A, BIRC5, PCNA, MCM2, MCM3, MCM4, MCM5, MCM6, MCM7, CDC20, CDK1
- CCNB2, CCNA2, AURKA, AURKB, BUB1, BUB1B, CENPF, CENPE, KIF11, KIF20A, KIF23, PLK1
- HMMR, HMGB2, HMGB1, CDK4, CDK6, E2F1, TYMS, DHFR, TK1, RRM2, RRM1, PRC1
- NUF2, KIF4A, KIF18A, CDCA8, CDCA3, CDCA2, CDCA7, CDCA7L, ANLN, ASPM, CENPA, CENPB
- CENPC, CENPD

### CD4 Treg

Description: Immunosuppressive regulatory CD4+ T cells defined by FOXP3 expression and high levels of inhibitory receptors such as CTLA4 and IL2RA.

Genes:
- FOXP3, IL2RA, CTLA4, TNFRSF18, TNFRSF4, IKZF2, TIGIT, LAG3, ENTPD1, ITGAE, CCR8, IKZF4
- SATB1, SATB2, TNFRSF9, TNFRSF18, GZMB, PRF1, GZMA, GZMK, NKG7, CST7, CD27, CD38
- HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, CD74, FCRL3, CD5L, CD5, CD6, ICOS
- PDCD1, TOX, IRF4, BATF, MAF, STAT5A, STAT5B, SOCS1, CISH, IL1R2, IL1R1, TGFBR1

### CD8 Proliferating

Description: Proliferating CD8+ T cells in active cell cycle, often confused with CD4 proliferating cells due to shared cell cycle gene signatures but distinguished by CD8A/CD8B expression.

Genes:
- MKI67, TOP2A, BIRC5, PCNA, MCM2, MCM3, MCM4, MCM5, MCM6, MCM7, CDC20, CDK1
- CCNB2, CCNA2, AURKA, AURKB, BUB1, BUB1B, CENPF, CENPE, KIF11, KIF20A, KIF23, PLK1
- HMMR, HMGB2, HMGB1, CDK4, CDK6, E2F1, TYMS, DHFR, TK1, RRM2, RRM1, PRC1
- NUF2, KIF4A, KIF18A, CDCA8, CDCA3, CDCA2, CDCA7, CDCA7L, ANLN, ASPM, CENPA, CENPB
- CENPC, CENPD, CD8A, CD8B, GZMB, NKG7, PRF1, GNLY

## cd4 tcm

### CD4 TCM

Description: Central memory CD4+ T cells characterized by lymph-node homing capacity (CCR7+, SELL+), high LEF1/TCF7 expression, and poised proliferative recall responses.

Genes:
- LEF1, SELL, IL7R, CCR7, TCF7, MAL, ITGB1, CD40LG, ICOS, CD28, LIMD2, TRAT1
- ITGAE, CD3D, CD3E, CD4, LCK, THEMIS, GIMAP2, GIMAP5, GIMAP8, GIMAP1, GIMAP4, GIMAP6
- GIMAP7

### CD4 TEM

Description: Effector memory CD4+ T cells lacking lymph-node homing receptors, enriched for cytotoxic/granzyme modules and tissue-homing integrins.

Genes:
- GZMA, GZMK, GZMH, GZMB, PRF1, NKG7, CST7, GNLY, FGFBP2, CX3CR1, ITGAE, ITGB1
- CD4, CD3D, CD3E, CD2, KLRB1, KLRD1, KLRG1, FCGR3A, TYROBP, SYK, ZAP70, LCK
- THEMIS

### CD4 TEMRA

Description: Terminally differentiated effector CD4+ T cells re-expressing CD45RA, with strong cytotoxic signatures and loss of CCR7/SELL.

Genes:
- GZMB, PRF1, NKG7, CST7, GNLY, FGFBP2, CX3CR1, FCGR3A, KLRG1, KLRD1, CD4, CD3D
- CD3E, CD2, TYROBP, SYK, ZAP70, LCK, ITGAL, ITGB2, S100A4, S100A6, S100A10, ANXA1
- ANXA2

### CD8 TCM

Description: Central memory CD8+ T cells with lymph-node homing (CCR7+, SELL+), high TCF7/LEF1, and stem-like self-renewal capacity.

Genes:
- LEF1, SELL, IL7R, CCR7, TCF7, CD8A, CD8B, CD3D, CD3E, MAL, ITGB1, CD28
- LCK, THEMIS, GIMAP2, GIMAP5, GIMAP8, GIMAP1, GIMAP4, GIMAP6, GIMAP7, TRAT1, ITGAE, CD40LG
- ICOS

### Treg

Description: Regulatory CD4+ T cells defined by FOXP3/IL2RA/CTLA4 expression that mediate immune suppression and tolerance.

Genes:
- FOXP3, IL2RA, CTLA4, TNFRSF18, TNFRSF4, IKZF2, TIGIT, CCR8, IKZF4, ENTPD1, CD3D, CD3E
- CD4, LCK, THEMIS, ITGAE, ITGB1, CD28, ICOS, CD40LG, LEF1, SELL, CCR7, IL7R
- TCF7

## cd4 tem

### CD4 CM (CCR7+ CD45RA-)

Description: Central memory CD4+ T cells expressing lymph-node homing receptors CCR7 and L-selectin, with high proliferative potential and self-renewal capacity.

Genes:
- CCR7, SELL, IL7R, TCF7, LEF1, MAL, CD44, CD27, CD28, ICOS, CXCR4, CXCR5
- ITGAL, LTA, LTB, BCL2, STAT3, IL6ST, CD3D, CD3E, CD4, TRAT1, CD40LG, TNFRSF9
- TNFRSF4, CTLA4, PDCD1, LAG3, TIGIT, TOX

### CD4 TEM (CCR7-)

Description: Effector memory CD4+ T cells lacking CCR7, enriched for cytotoxic molecules and tissue-homing receptors, poised for rapid effector function in peripheral tissues.

Genes:
- IL7R, GZMB, GZMH, PRF1, NKG7, GNLY, CST7, FGFBP2, KLRD1, KLRB1, CX3CR1, ITGAE
- ITGAL, CD44, CD69, FASLG, IFNG, TNF, IL2RA, CTSW, GZMA, GZMK, EOMES, TBX21
- CXCR3, CCR5, CXCR6, ITGAX, SELL, CD27

### CD4 TEMRA (CCR7- CD45RA+)

Description: Terminally differentiated effector CD4+ T cells re-expressing CD45RA, highly cytotoxic with low proliferative capacity, often expanded in chronic infection and aging.

Genes:
- GZMB, GZMH, PRF1, NKG7, GNLY, CST7, FGFBP2, CX3CR1, KLRD1, KLRC1, KLRK1, CD44
- CD69, IFNG, TNF, EOMES, TBX21, GZMA, GZMK, CTSW, ITGAL, ITGAX, CXCR3, CCR5
- FASLG, IL2RA, CD27, CD57, B2M, HLA-A

### CD4 Tfh (CXCR5+)

Description: Follicular helper CD4+ T cells defined by CXCR5 expression, specialized in providing help to B cells for germinal center reactions and antibody production.

Genes:
- CXCR5, PDCD1, ICOS, IL21, IL6ST, MAF, BCL6, CD40LG, CXCR4, SELL, CCR7, CD44
- IL7R, TCF7, LEF1, ITGAL, CD28, CTLA4, TNFRSF4, TNFRSF9, CD3D, CD3E, CD4, SH2D1A
- SLAM, CD84, CD83, TOX, BATF, IRF4

### CD8 TEM (confused neighbor)

Description: Effector memory CD8+ cytotoxic T cells that share many cytotoxic and tissue-homing markers with CD4 TEM, commonly confused due to overlapping transcriptional programs.

Genes:
- CD8A, CD8B, GZMB, GZMH, PRF1, NKG7, GNLY, CST7, FGFBP2, CX3CR1, KLRD1, KLRC1
- KLRB1, CD44, CD69, IFNG, TNF, EOMES, TBX21, GZMA, GZMK, CTSW, ITGAL, ITGAX
- CXCR3, CCR5, FASLG, IL2RA, CD27, CD57

## cd8 naive

### CD4 Naive

Description: Antigen-inexperienced helper T cells expressing lymphoid homing markers, commonly confused with CD8 naive due to shared CCR7/SELL/LEF1 signature but distinguished by CD4 expression.

Genes:
- CCR7, LEF1, SELL, TCF7, IL7R, MAL, ITGB1, CD27, CD28, CD40LG, CD4, CD3D
- CD3E, LCK, ZAP70, LAT, TRAT1, ITK, THEMIS, CD7, CD5, BACH2, KLF2, FOXO1
- FAS, CD69, CD44, ICOS, CTLA4, PDCD1

### CD8 Central Memory

Description: Memory CD8 T cells retaining lymphoid tissue homing capacity via CCR7 and SELL expression, with enhanced proliferative potential upon re-encounter with antigen.

Genes:
- CCR7, SELL, LEF1, TCF7, IL7R, CD27, CD28, CD40LG, CD3D, CD3E, CD8A, CD8B
- LCK, ZAP70, LAT, ITK, THEMIS, CD7, CD5, BACH2, KLF2, FOXO1, MAL, ITGB1
- GZMK, FAS, TRAT1, CD69, GZMA, PRF1

### CD8 Effector Memory

Description: Terminally differentiated effector-memory CD8 T cells lacking CCR7, enriched for cytotoxic granule components and peripheral tissue homing receptors.

Genes:
- GZMB, PRF1, NKG7, GNLY, GZMH, GZMA, CST7, IFNG, TNF, CCL4, CCL3, XCL1
- XCL2, FGFBP2, CD8A, CD8B, CD3D, CD3E, CD27, CD28, ITGAE, ITGA1, CX3CR1, KLRD1
- KLRC1, KLRB1, CD160, TYROBP, FCGR3A, EOMES

### CD8 Effector Memory RA (TEMRA)

Description: Highly cytotoxic CD8 T cells re-expressing CCR7 but lacking SELL, characterized by elevated perforin/granzyme content and senescence markers.

Genes:
- GZMB, PRF1, NKG7, GNLY, GZMH, FGFBP2, CST7, CX3CR1, FCGR3A, KLRD1, KLRC1, KLRB1
- CD160, TYROBP, EOMES, TBX21, IFNG, TNF, CCL4, CCL3, XCL1, XCL2, CD8A, CD8B
- CD3D, CD3E, ITGAE, GZMA, CD57, FCGR3A

### CD8 Naive

Description: Antigen-inexperienced cytotoxic T lymphocytes expressing lymphoid homing receptors CCR7 and L-selectin, poised for primary immune responses.

Genes:
- CCR7, LEF1, SELL, TCF7, IL7R, MAL, ITGB1, CD27, CD28, CD40LG, GZMK, FAS
- CD69, CD3D, CD3E, CD8A, CD8B, LCK, ZAP70, LAT, TRAT1, ITK, THEMIS, CD7
- CD5, LEF1, TCF7, BACH2, KLF2, FOXO1

## cd8 proliferating

### CD4 Proliferating

Description: Cycling CD4+ T helper cells undergoing clonal expansion, sharing cell cycle gene signatures with proliferating CD8+ T cells but distinguished by CD4 expression.

Genes:
- MKI67, TOP2A, BIRC5, PCNA, MCM2, MCM3, MCM4, MCM5, MCM6, MCM7, CDC20, CCNB2
- CCNB1, CDK1, AURKA, AURKB, BUB1, BUB1B, KIF11, KIF20A, KIF23, HMGB2, HMGB1, CDCA8
- CENPF, CENPE, CENPA, CENPB, CENPC, CENPU, NUF2, NDC80, SPAG5, PRC1, ANLN, PLK1
- RRM2, TYMS, DHFR, TK1, CD4, CD3D, CD3E, CD2, CD5

### CD8 Central Memory

Description: Memory CD8+ T cells with lymphoid homing capacity and self-renewal potential, expressing CCR7 and SELL for secondary lymphoid organ recirculation.

Genes:
- CCR7, SELL, LEF1, TCF7, IL7R, CD27, CD28, CD40LG, MAL, GIMAP2, GIMAP4, GIMAP5
- GIMAP6, GIMAP7, GIMAP8, BACH2, FOXO1, KLF2, KLF4, S1PR1, CD3D, CD3E, CD8A, CD8B
- CD2, CD5, CD7, CD28, CD40LG, CCR7, LEF1, TCF7, SELL, IL7R, CD27, MAL
- GIMAP2, GIMAP4, GIMAP5, GZMA, GZMK, PRF1, NKG7, CST7

### CD8 Effector Memory

Description: Terminally differentiated, highly cytotoxic CD8+ T cells with immediate effector function, characterized by high granzyme and perforin expression and tissue-homing capacity.

Genes:
- GZMA, GZMB, GZMH, GZMK, PRF1, NKG7, GNLY, CST7, FGFBP2, CCL4, CCL3, CCL5
- XCL1, XCL2, IFNG, TNF, CX3CR1, ITGAE, ITGAM, CD16A, FCGR3A, KLRD1, KLRF1, KLRB1
- NCR1, NKG7, CD8A, CD8B, CD3D, CD3E, GZMB, PRF1, NKG7, GNLY, CST7, FGFBP2
- CCL4, CCL3, IFNG, CX3CR1, ITGAE

### CD8 Naive

Description: Resting, antigen-inexperienced CD8+ T cells with high lymphoid homing and survival gene expression, capable of differentiation into effector cells upon activation.

Genes:
- CCR7, LEF1, TCF7, SELL, IL7R, MAL, CD27, CD28, CD40LG, ITGB1, ITGA4, LTB
- GIMAP2, GIMAP4, GIMAP5, GIMAP6, GIMAP7, GIMAP8, FOS, JUN, LEF1, TCF7, BACH2, FOXO1
- KLF2, KLF4, S1PR1, CD3D, CD3E, CD8A, CD8B, CD2, CD5, CD7, CD28, CD40LG
- CCR7, LEF1, TCF7, SELL, IL7R

### CD8 Proliferating

Description: Cycling effector CD8+ T cells actively undergoing cell division, characterized by high expression of cell cycle and mitotic genes alongside cytotoxic markers.

Genes:
- MKI67, TOP2A, BIRC5, PCNA, MCM2, MCM3, MCM4, MCM5, MCM6, MCM7, CDC20, CCNB2
- CCNB1, CDK1, AURKA, AURKB, BUB1, BUB1B, KIF11, KIF20A, KIF23, HMGB2, HMGB1, CDCA8
- CENPF, CENPE, CENPA, CENPB, CENPC, CENPU, NUF2, NDC80, SPAG5, PRC1, ANLN, PLK1
- RRM2, TYMS, DHFR, TK1, CD8A, CD8B, GZMB, PRF1, NKG7

## cd8 tcm

### CD8 Central Memory T cells (TCM)

Description: Memory CD8 T cells with lymphoid homing capacity, expressing CCR7 and SELL, capable of self-renewal and recall responses.

Genes:
- CCR7, SELL, IL7R, CD27, CD28, LEF1, TCF7, CD40LG, GZMK, GZMA, PRF1, NKG7
- GNLY, IFNG, CXCR3, CXCR4, ITGAE, ITGAL, CD69, CD44, ICOS, TNFRSF9, TNFRSF4, BCL2
- STAT5A

### CD8 Effector Memory T cells (TEM)

Description: Differentiated memory CD8 T cells lacking CCR7, enriched for cytotoxic effector molecules and peripheral tissue homing receptors.

Genes:
- GZMB, GZMH, GZMA, PRF1, NKG7, GNLY, IFNG, CCL4, CCL3, CX3CR1, FGFBP2, KLRD1
- KLRC1, KLRB1, CD160, ITGAE, CXCR3, CXCR6, CD69, CD38, HLA-DRB1, EOMES, TBX21, FASLG
- TNF

### CD8 Effector T cells (TEFF)

Description: Terminally differentiated CD8 T cells with high cytotoxic potential, expressing abundant granzymes and perforin, often found during acute infection.

Genes:
- GZMB, GZMH, GZMA, GZMK, PRF1, NKG7, GNLY, IFNG, CCL4, CCL3, CX3CR1, FGFBP2
- KLRD1, KLRC1, CD160, FASLG, TNF, EOMES, TBX21, CD38, HLA-DRB1, CXCR3, CXCR6, CD69
- ITGAE

### CD8 Naive T cells

Description: Antigen-inexperienced CD8 T cells expressing lymphoid homing receptors CCR7 and L-selectin, poised for initial activation.

Genes:
- CCR7, LEF1, SELL, TCF7, IL7R, MAL, CD27, CD28, GIMAP2, GIMAP5, GIMAP8, ITGB1
- CD40LG, TRAF1, BACH2, FOXO1, KLF2, KLF4, LTB, COTL1, ACAP1, MYC, STAT3, CD7
- S100A4

### CD8 Tissue-Resident Memory T cells (TRM-like)

Description: CD8 T cells expressing tissue-residency markers such as CD69 and integrin alpha E (CD103), adapted for peripheral tissue surveillance.

Genes:
- ITGAE, ITGAL, CD69, CXCR6, CD103, GZMB, GZMH, PRF1, NKG7, GNLY, IFNG, CCL4
- CCL3, CX3CR1, FGFBP2, KLRD1, KLRC1, EOMES, TBX21, CD38, HLA-DRB1, FASLG, TNF, CXCR3
- CD161

## cd8 tem

### CD4 Naive T cells

Description: Antigen-inexperienced CD4+ T cells with lymph node homing markers, often confused with CD8 naive due to shared naive phenotype markers.

Genes:
- CCR7, LEF1, SELL, TCF7, MAL, IL7R, CD27, CD28, ITGB1, CD40LG, GZMK, FAS
- BACH2, KLF2, FOXO1, LTB, S1PR1, CD69, CD38, CD45RA, CD4, CD3D, CD3E, TRAC
- TRBC1, TRBC2, LCK, ZAP70, LAT, THEMIS

### CD8 Central Memory T cells (T_CM)

Description: Memory CD8+ T cells retaining lymph node homing receptors (CCR7, SELL) with high proliferative capacity and moderate effector function.

Genes:
- CCR7, SELL, LEF1, TCF7, IL7R, CD27, CD28, CD40LG, MAL, ITGB1, BACH2, KLF2
- FOXO1, LTB, S1PR1, CD38, CD69, GZMK, FAS, CD45RA, CD27, CD28, ITGB1, CD40LG
- GZMK, FAS, BACH2, KLF2, FOXO1, LTB

### CD8 Effector Memory T cells (T_EM)

Description: Differentiated effector-memory CD8+ T cells lacking CCR7, with high cytotoxic granule content and tissue-homing capacity.

Genes:
- GZMB, PRF1, NKG7, GNLY, GZMH, GZMA, CST7, IFNG, TNF, CX3CR1, FGFBP2, KLRD1
- KLRC1, KLRB1, EOMES, TBX21, ITGAE, CD69, CD38, HLA-DRB1, GZMB, PRF1, NKG7, GNLY
- GZMH, GZMA, CST7, IFNG, TNF, CX3CR1

### CD8 Naive T cells

Description: Resting, antigen-inexperienced CD8+ T cells with high lymph node homing capacity and low cytotoxic potential.

Genes:
- CCR7, LEF1, SELL, TCF7, MAL, IL7R, CD27, CD28, ITGB1, CD40LG, GZMK, FAS
- BACH2, KLF2, FOXO1, LTB, Ccr7, S1PR1, CD69, CD38, CD45RA, CD27, CD28, ITGB1
- CD40LG, GZMK, FAS, BACH2, KLF2, FOXO1

### CD8 Terminally Differentiated Effector T cells (T_EMRA)

Description: Highly differentiated CD8+ T cells with loss of CD28/CD27, high CD57 expression, and potent immediate effector function.

Genes:
- GZMB, PRF1, NKG7, GNLY, GZMH, FGFBP2, CX3CR1, KLRD1, KLRC1, KLRB1, EOMES, TBX21
- IFNG, TNF, CST7, CD57, FCGR3A, CD8A, CD8B, GZMK, GZMB, PRF1, NKG7, GNLY
- GZMH, FGFBP2, CX3CR1, KLRD1, KLRC1, KLRB1

## cdc1

### B cell

Description: B lymphocyte that can be confused with dendritic cells due to shared HLA class II and antigen presentation machinery expression.

Genes:
- CD19, MS4A1, CD79A, CD79B, PAX5, BLK, BANK1, CD22, FCRL2, FCRL1, TCL1A, TCL1B
- IGHM, IGHD, CD24, CD38, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, CD74, B2M, CD1C, FCER1A
- ITGAX, LAMP3, NKG7, GZMB, GZMA, PRF1

### cDC1

Description: Classical type 1 conventional dendritic cell specialized in cross-presentation of exogenous antigens to CD8+ T cells.

Genes:
- CLEC9A, CADM1, IRF8, BATF3, IDO1, XCR1, CD1C, FCER1A, LAMP3, CD141, THBD, CLEC14A
- CXCR3, ITGAX, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, CD74, TAP1, TAP2, B2M, IRF4, NKG7
- GZMB, GZMA, PRF1, CCL17, CCL22, CXCL9

### cDC2

Description: Classical type 2 conventional dendritic cell specialized in antigen presentation to CD4+ T cells and Th polarization.

Genes:
- CD1C, FCER1A, CLEC10A, CLEC4M, FSCN1, ITGAX, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, CD74, B2M
- IRF4, MAF, C1QA, C1QB, C1QC, FCGR1A, CD36, MRC1, CD209, LAMP3, CCR7, CXCR4
- NKG7, GZMB, GZMA, PRF1, CCL17, CCL22

### monocyte-derived DC

Description: Monocyte-derived dendritic cell that differentiates from circulating monocytes during inflammation and can mimic cDC2 phenotype.

Genes:
- CD14, FCGR3A, CD68, CD163, MRC1, C1QA, C1QB, C1QC, FCGR1A, CD36, ITGAX, HLA-DRA
- HLA-DRB1, HLA-DPA1, HLA-DPB1, CD74, B2M, IRF4, MAF, FSCN1, LAMP3, CCR7, CXCR4, NKG7
- GZMB, GZMA, PRF1, CCL17, CCL22, IDO1

### pDC

Description: Plasmacytoid dendritic cell specialized in rapid type I interferon production in response to viral nucleic acids.

Genes:
- IL3RA, TCF4, NRP1, CD2AP, GZMB, GZMA, GZMK, PRF1, NKG7, IRF7, IRF8, BATF2
- HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, CD74, B2M, FCER1A, LILRA4, CD303, CD304, CXCR3, CXCR4
- ITGAX, CCL17, CCL22, IDO1, TAP1, TAP2

## cdc2

### CD14+ monocyte

Description: Classical CD14+ monocyte often confused with cDC2 due to shared myeloid markers and moderate MHC-II expression.

Genes:
- CD14, LYZ, S100A8, S100A9, S100A4, S100A6, S100A10, ANXA2, ANXA1, FSCN1, CTSB, CTSC
- CTSD, CST3, FCGR2A, FCGR3A, ITGAM, ITGAX, HLA-DRA, HLA-DRB1, CD74, CD1C, CLEC10A, FCER1A
- IRF4, CD40, CD86, CCR7, LAMP3, CLEC4C

### cDC1

Description: Classical type 1 conventional dendritic cell specialized in cross-presentation of exogenous antigens to CD8+ T cells.

Genes:
- CLEC9A, BDCA3, IRF8, BATF3, CD141, THBD, XCR1, IDO1, CXCR3, FCER1A, HLA-DRA, HLA-DRB1
- CD74, ITGAX, LAMP3, CCR7, CD40, CD86, S100A4, S100A6, ANXA2, FSCN1, CTSB, CTSC
- CTSD, LYZ, CST3, FCGR2A, CD1C, CLEC10A

### cDC2

Description: Classical type 2 conventional dendritic cell specialized in CD4+ T cell priming and antigen presentation via MHC-II.

Genes:
- FCER1A, CLEC10A, CD1C, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, CD74, ITGAX, FCGR2A
- CD1A, CLEC4C, IRF4, CD40, CD86, CCR7, LAMP3, CST3, LYZ, S100A4, S100A6, S100A10
- ANXA2, ANXA1, FSCN1, CTSB, CTSC, CTSD

### monocyte-derived DC

Description: Monocyte-derived dendritic cell arising from circulating monocytes with intermediate marker expression between monocytes and cDC2.

Genes:
- CD14, FCGR3A, LYZ, S100A8, S100A9, S100A4, S100A6, S100A10, ANXA2, ANXA1, FSCN1, CTSB
- CTSC, CTSD, CST3, FCGR2A, HLA-DRA, HLA-DRB1, CD74, ITGAX, CD1C, CLEC10A, FCER1A, IRF4
- CD40, CD86, CCR7, LAMP3, CLEC4C, IL3RA

### pDC

Description: Plasmacytoid dendritic cell specialized in type I interferon production in response to viral nucleic acids via TLR7/9.

Genes:
- CLEC4C, IL3RA, TCF4, NRP1, CD2, CD300A, FCER1A, HLA-DRA, HLA-DRB1, CD74, ITGAX, S100A4
- S100A6, ANXA2, FSCN1, CTSB, CTSC, CTSD, LYZ, CST3, FCGR2A, CD1C, CLEC10A, IRF4
- CD40, CD86, CCR7, LAMP3, S100A10, ANXA1

## dnt

### CD4_T_cells

Description: CD4+ helper T lymphocytes including naive, memory, and regulatory subsets that orchestrate adaptive immune responses.

Genes:
- CD4, CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, IL7R, LEF1, TCF7, CCR7, SELL
- MAL, LAT, LCK, ITK, CD28, ICOS, CD40LG, CTLA4, FOXP3, NKG7, GZMK, CXCR5
- CXCR3, CXCR4, CD69, CD27, CD52, BACH2

### CD8_T_cells

Description: CD8+ cytotoxic T lymphocytes capable of direct killing of infected or malignant cells via perforin/granzyme release.

Genes:
- CD8A, CD8B, CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, NKG7, GZMB, GZMH, GZMA
- PRF1, GNLY, CCL4, CCL5, CXCR3, CX3CR1, CD27, CD69, PDCD1, LAG3, HAVCR2, TOX
- EOMES, TBX21, ITGAE, ITGAL, GZMK, IL7R

### NKT_cells

Description: Natural killer T cells recognizing lipid antigens via an invariant or semi-invariant TCR, co-expressing NK-associated markers.

Genes:
- TRAV10, CD3D, CD3E, CD3G, CD161, KIR2DL1, KIR2DL3, KIR3DL1, NKG7, GZMB, GZMH, PRF1
- GNLY, CXCR6, CD69, CD160, ITGAL, ITGAE, PLZF, TBX21, EOMES, IL7R, CCR7, CD4
- CD8A, CD8B, NCR3, KLRC1, KLRD1

### dnT_cells

Description: Double-negative T cells lacking CD4 and CD8 that exhibit memory/effector phenotypes and are enriched in autoimmune contexts.

Genes:
- TRAC, TRBC1, TRBC2, CD3D, CD3E, CD3G, NKG7, GZMB, GZMH, PRF1, GNLY, CCL4
- CCL5, CXCR3, CXCR6, ITGAE, ITGAL, CD27, CD69, PDCD1, LAG3, HAVCR2, TOX, TCF7
- EOMES, TBX21, IKZF2, FOXP3, CTLA4, ICOS

### gamma_delta_T_cells

Description: T cells expressing a gamma-delta TCR rather than alpha-beta, often lacking CD4/CD8 and enriched for innate-like cytotoxic functions.

Genes:
- TRDC, TRGC1, TRGC2, TRDV1, TRDV2, CD3D, CD3E, CD3G, NKG7, GZMB, GZMH, PRF1
- GNLY, CXCR6, CXCR3, CD27, CD69, CD160, BTN3A1, BTNL9, ITGAE, ITGAL, EOMES, TBX21
- KLRD1, KLRC1, KLRK1, NCR3, FCGR3A, CCL4

## doublet

### B-Naive-Cell

Description: Mature, antigen-inexperienced B lymphocytes expressing surface IgM and IgD that circulate in blood and home to secondary lymphoid organs for antigen surveillance.

Genes:
- MS4A1, CD19, CD79A, CD79B, CD22, CD24, TCL1A, BANK1, BLK, FCER2, PAX5, SPIB
- IGHM, IGHD, CD37, CD53, CD81, CD82, TSPAN13, LINC00926, VPREB3, IGLL5, CD180, FCRL2
- FCRL4, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, B2M, ACTB, GAPDH, MALAT1, NEAT1
- RPL13A, RPS27A, TMSB4X, TMSB10

### CD4-Naive-T-Cell

Description: Resting, antigen-inexperienced CD4+ T lymphocytes that circulate through secondary lymphoid organs and are characterized by high expression of homing receptors such as CCR7, L-selectin, and LEF1.

Genes:
- CD4, CD3D, CD3E, CCR7, LEF1, TCF7, SELL, IL7R, MAL, GIMAP5, GIMAP8, CD27
- CD28, LCK, ITK, TRAT1, THEMIS, LAT, CD5, CD2, CD6, CD7, CD40LG, ICOS
- LTB, Ccr7, S100A4, TMSB4X, TMSB10, B2M, HLA-A, HLA-B, HLA-C, RPL13A, RPS27A, ACTB
- GAPDH, MALAT1, NEAT1, LEF1-AS1

### CD8-Naive-T-Cell

Description: Antigen-inexperienced cytotoxic T lymphocytes expressing CD8A/CD8B that patrol secondary lymphoid tissues and are poised for activation upon antigen encounter.

Genes:
- CD8A, CD8B, CD3D, CD3E, CCR7, LEF1, TCF7, SELL, IL7R, GIMAP5, GIMAP8, CD27
- CD28, LCK, ITK, TRAT1, THEMIS, LAT, CD5, CD2, CD7, TMSB4X, TMSB10, B2M
- HLA-A, HLA-B, HLA-C, RPL13A, RPS27A, ACTB, GAPDH, MALAT1, NEAT1, LEF1-AS1, NKG7, GZMB
- PRF1, GNLY, CST7, EOMES

### Classical-Monocyte

Description: The most abundant monocyte subset in human blood, characterized by high CD14 and low/negative FCGR3A (CD16) expression, functioning primarily in phagocytosis and inflammatory cytokine production.

Genes:
- CD14, LYZ, S100A8, S100A9, S100A4, S100A6, FCN1, FCGR3A, CST3, VCAN, TYMP, IFITM2
- IFITM3, MNDA, CFP, LST1, NCF1, NCF2, NCF4, CTSS, FTH1, FTL, LGALS2, LGALS3
- IL1B, TNF, CXCL8, CCL3, CCL4, CCL5, ITGAM, CD68, CD163, FCGR1A, HLA-DRA, HLA-DRB1
- B2M, ACTB, GAPDH, MALAT1

### Doublet

Description: A computationally inferred artifact arising from the co-capture of two or more distinct cells in a single droplet, characterized by the simultaneous expression of lineage-specific markers from multiple unrelated cell types.

Genes:
- CD3D, CD3E, CD79A, MS4A1, NKG7, GNLY, LYZ, S100A4, FCGR3A, CD14, PPBP, PF4
- HBB, HBA1, HBA2, CST3, FCER1A, SERPINF1, IL3RA, CD1C, CD79B, CD19, CD8A, CD4
- CD163, CD68, ITGAM, FCGR1A, CDKN2C, TMSB4X, TMSB10, B2M, HLA-A, HLA-B, HLA-C, HLA-DRA
- HLA-DRB1, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, MALAT1, NEAT1, RPL13A, RPS27A, ACTB, GAPDH, MTRNR2L1
- MTRNR2L8, MTRNR2L12

## eryth

### Contaminating Neutrophil

Description: Polymorphonuclear neutrophils that may contaminate PBMC preparations, identified by high expression of neutrophil granule proteins and Fc gamma receptor IIIb.

Genes:
- FCGR3B, CSF3R, CXCR2, CXCR1, MMP9, MMP8, ELANE, PRTN3, CTSG, AZU1, FUT4, LTF
- CAMP, LCN2, S100A8, S100A9, S100A12, FCN1, CD177, ITGAM, CD24, NAMPT, G0S2, NCF1
- NCF2, NCF4, CYBB, RAB37, ACPP, MPO

### Contaminating Platelet

Description: Anucleate platelets frequently co-isolated with PBMC, characterized by high expression of platelet-specific glycoproteins and coagulation factors.

Genes:
- PF4, PPBP, GP1BA, GP1BB, GP5, GP9, ITGA2B, ITGB3, CD9, CD36, TUBB1, THBS1
- CXCL3, CCL5, PDGFAP, SPARC, GNG11, HIST1H2BC, HIST1H4C, HIST1H3A, RPL13A, RPL19, RPL32, RPS27A
- RPS28, RPS12, RPS3A, RPS4X, RPS19, RPL41

### Erythroid Progenitor (BFU-E/CFU-E)

Description: Nucleated erythroid progenitors and precursors in PBMC, characterized by high hemoglobin and erythroid differentiation gene expression.

Genes:
- HBB, HBA1, HBA2, ALAS2, SLC4A1, AHSP, EPB42, EPB41, KLF1, GATA1, TAL1, GYPA
- GYPC, SNCA, CA1, CA2, BLVRB, HBD, HBZ, HBM, TSPAN32, CLIC4, RHD, RHCE
- MARCHF8, SEC14L2, MAP2K3, BPGM, NCOA4, FECH

### Megakaryocyte-Erythroid Progenitor (MEP)

Description: Bipotent progenitors in the erythroid-megakaryocytic lineage, co-expressing erythroid and early megakaryocytic markers.

Genes:
- HBB, HBA1, HBA2, ALAS2, SLC4A1, AHSP, EPB42, KLF1, GATA1, TAL1, GYPA, CA1
- CA2, BLVRB, HBD, TSPAN32, CLIC4, BPGM, NCOA4, FECH, GP9, GP1BA, ITGA2B, CD9
- MPL, PF4, PPBP, HBM, HBZ, SNCA

### Reticulocyte

Description: Mature enucleated red blood cell precursors recently released from bone marrow, retaining residual ribosomal RNA and high hemoglobin content.

Genes:
- HBB, HBA1, HBA2, ALAS2, SLC4A1, AHSP, EPB42, GYPA, CA1, CA2, BLVRB, HBD
- TSPAN32, CLIC4, BPGM, NCOA4, FECH, SNCA, KLF1, GATA1, TAL1, HBZ, HBM, EPB41
- GYPC, SEC14L2, MAP2K3, RHD, RHCE, MARCHF8

## gdt

### CD4_T

Description: Conventional alpha-beta CD4+ helper T cells expressing CD4 co-receptor and diverse TCR alpha/beta chains.

Genes:
- CD4, CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, LEF1, TCF7, CCR7, LSEL, IL7R
- MAL, CD40LG, ICOS, CTLA4, FOXP3, CD28, GATA3, TBX21, BCL2, LTB, CD2, CD5
- CD7, ITK, LCK, ZAP70, LAT

### CD8_T

Description: Cytotoxic alpha-beta CD8+ T cells expressing CD8 co-receptor and cytotoxic effector molecules.

Genes:
- CD8A, CD8B, CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, GZMB, GZMH, GZMA, PRF1
- NKG7, GNLY, CST7, CXCR3, CX3CR1, CD27, CD28, EOMES, TBX21, IFNG, FASLG, CD5
- CD7, ITK, LCK, ZAP70, GZMK, IL7R

### MAIT

Description: Mucosal-associated invariant T cells with semi-invariant TRAV1-2/TRAJ33 TCR, CD161+ phenotype, and IL-17/IFN-gamma production.

Genes:
- TRAV1-2, NCR3, KLRB1, CD161, IL18R1, IL18RAP, IL7R, CD3D, CD3E, CD3G, CD8A, CD8B
- SLC4A10, RORC, IL17A, IL22, IFNG, GZMB, NKG7, PRF1, GNLY, CST7, CXCR6, CCR6
- CD2, CD5, CD7, ITK, LCK, ZAP70

### NK

Description: Natural killer cells lacking TCR rearrangements but expressing cytotoxic granules and activating/inhibitory NK receptors.

Genes:
- NKG7, GNLY, GZMB, GZMH, GZMA, PRF1, CST7, KLRD1, KLRC1, KLRK1, NCAM1, FCGR3A
- CD2, CD7, TYROBP, FCER1G, SYK, EOMES, TBX21, CXCR3, CX3CR1, ITGAE, IFNG, TNF
- CD160, KLRB1, NCR1, NCR3, TRDC, TRGC1

### gdT

Description: Gamma-delta T cells in PBMC characterized by TCR gamma/delta chains, innate-like cytotoxicity, and IL-17/IFN-gamma production.

Genes:
- TRDC, TRGC1, TRGC2, TRAV1-2, TRDV1, TRDV2, TRGV9, TRGV2, TRGV3, TRGV5, NKG7, GZMB
- GZMH, GZMA, PRF1, GNLY, CST7, KLRD1, KLRC1, KLRK1, CD27, CD69, ITGAE, ITGAL
- CXCR6, CCR6, IL17A, IL22, IFNG, TNF

## hspc

### CLP

Description: Common lymphoid progenitors committed to B, T, and NK cell lineages with limited myeloid potential.

Genes:
- CD34, CD38, CD10, CD7, CD127, IL7R, FLT3, CD135, IL3RA, CD123, CD45RA, CD19
- CD20, CD3, CD56, CD16, CD14, CD11b, CD161, CD25, CD69, CD62L, CD27, CD28
- CD45, CD90, CD133, PROM1, MME, ENG, ITGA6, ITGAX, CD184, CD29, CD49f, THY1
- CXCR4, HOXA9, MEIS1, GATA2, RUNX1, TAL1, LMO2, MYB, KIT, CD33, CD117, CD93
- CD44

### HSC

Description: Long-term hematopoietic stem cells with self-renewal capacity and multipotent differentiation potential.

Genes:
- CD34, THY1, PROM1, MME, ENG, ITGA6, CXCR4, HOXA9, MEIS1, GATA2, RUNX1, TAL1
- LMO2, SCL, MYB, KIT, FLT3, CD44, ITGAX, CD33, CD38, CD90, CD133, CD117
- CD135, CD123, CD93, CD184, CD29, CD49f, CD45RA, CD45, CD11b, CD14, CD16, CD19
- CD20, CD3, CD56, CD57, CD161, CD127, CD25, CD69, CD62L, CD27, CD28

### LMPP

Description: Lymphoid-primed multipotent progenitors with myeloid and lymphoid potential but restricted erythroid/megakaryocyte capacity.

Genes:
- CD34, CD38, CD45RA, CD10, CD7, FLT3, CD135, IL3RA, CD123, CD33, CD117, CD93
- CD44, CXCR4, HOXA9, MEIS1, GATA2, RUNX1, TAL1, LMO2, MYB, KIT, CD19, CD20
- CD3, CD56, CD16, CD14, CD11b, CD161, CD127, CD25, CD69, CD62L, CD27, CD28
- CD45, CD90, CD133, PROM1, MME, ENG, ITGA6, ITGAX, CD184, CD29, CD49f, THY1

### MEP

Description: Megakaryocyte-erythroid progenitors committed to platelet and red blood cell lineages.

Genes:
- CD34, CD38, CD45RA, CD123, IL3RA, CD33, CD117, KIT, CD44, CXCR4, HOXA9, MEIS1
- GATA2, RUNX1, TAL1, LMO2, MYB, FLT3, CD135, CD93, CD19, CD20, CD3, CD56
- CD16, CD14, CD11b, CD161, CD127, CD25, CD69, CD62L, CD27, CD28, CD45, CD90
- CD133, PROM1, MME, ENG, ITGA6, ITGAX, CD184, CD29, CD49f, THY1, CD7, CD10
- CD45RA

### MPP

Description: Multipotent progenitors with lymphoid and myeloid differentiation potential but limited self-renewal capacity.

Genes:
- CD34, THY1, CD38, CD45RA, CD90, CD133, CD117, CD135, CD123, CD33, CD44, CXCR4
- HOXA9, MEIS1, GATA2, RUNX1, TAL1, LMO2, MYB, KIT, FLT3, IL3RA, CD7, CD10
- CD19, CD20, CD3, CD56, CD16, CD14, CD11b, CD161, CD127, CD25, CD69, CD62L
- CD27, CD28, CD45, CD29, CD49f, CD93, CD184, ITGA6, PROM1, MME, ENG, ITGAX

## ilc

### CD4_T_cells

Description: CD4+ T helper lymphocytes expressing TCR and co-receptor CD4, providing help to B cells and other immune cells through cytokine production.

Genes:
- CD3D, CD3E, CD4, CD40LG, IL7R, CCR7, LEF1, TCF7, MAL, LCK, ITK, GATA3
- IL6ST, ICOS, CTLA4, TNFRSF4, TNFRSF18, CD28, CD2, CD5, CD7, CD69, CD6, CD44
- HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, CD74, PDCD1

### ILC1

Description: T-bet+ innate lymphoid cells producing IFN-gamma, enriched in mucosal tissues and PBMC, involved in antiviral and intracellular pathogen responses.

Genes:
- TBX21, CXCR3, IFNG, IL12RB1, IL12RB2, IL18R1, IL18RAP, STAT1, STAT4, NCR1, CD160, ITGAE
- CXCR6, CD69, EOMES, RUNX3, ID2, TOX, NKG7, GZMB, GZMK, PRF1, FASLG, TNF
- IL7R, CCR5, CXCR4, CD7, CD38, HLA-DRA

### ILC2

Description: GATA3+ innate lymphoid cells producing type 2 cytokines (IL-5, IL-13), critical for anti-helminth immunity and allergic inflammation.

Genes:
- GATA3, IL1RL1, IL17RB, CRTH2, CD161, IL9, IL5, IL13, IL4, AREG, CCL1, CCL3
- CCL4, KIT, ICOS, TSLPR, IL33, IL25, RORA, MYC, GFI1, BCL11B, CD7, CD38
- CD69, CD44, ITGAE, ITGB1, TNFRSF18, TNFRSF4

### ILC3

Description: RORγt+ innate lymphoid cells producing IL-17 and IL-22, important for mucosal barrier integrity and interactions with gut microbiota.

Genes:
- RORC, AHR, IL23R, IL1R1, IL7R, CCR6, CXCR5, CD161, NKp44, NCR2, LINC01800, IL22
- IL17A, IL17F, CCL20, TNF, CSF2, LYZ, FCGR3A, CD4, CD84, SLAMF7, CD8A, CD8B
- CD3D, CD3E, CD2, CD5, CD7, CD38

### NK_cells

Description: Cytotoxic innate lymphoid cells with NK receptors (NKG2A, KIRs) that kill target cells via perforin/granzyme and produce IFN-gamma.

Genes:
- NKG7, GNLY, KLRD1, KLRF1, KLRB1, NCAM1, FCGR3A, FCGR2A, EOMES, TBX21, CXCR3, CX3CR1
- CD160, TYROBP, FCER1G, GZMA, GZMB, GZMH, GZMK, PRF1, FASLG, IFNG, TNF, CCL3
- CCL4, XCL1, XCL2, ITGAE, CD7, CD38

## mait

### CD14_Mono

Description: Classical CD14+ monocytes with phagocytic and pro-inflammatory functions, often confused with MAIT due to shared myeloid-like transcriptomic features.

Genes:
- CD14, LYZ, S100A8, S100A9, S100A10, S100A11, FCN1, FCGR3A, VCAN, TYMP, CFP, PSAP
- MNDA, CST3, CTSB, CTSD, CTSL, CTSS, LST1, AIF1, TYROBP, FCER1G, CD68, CD163
- MRC1, MSR1, C1QA, C1QB, C1QC, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, CD74
- IL1B, TNF, IL6, CCL3, CCL4, CXCL8, NFKB1, RELA, IRF8, SPI1, CEBPA, CEBPB

### CD4_TCM

Description: Central memory CD4+ T helper cells with lymphoid homing and broad cytokine production capacity.

Genes:
- CD4, CD3D, CD3E, CD2, CD5, CD7, CCR7, SELL, LEF1, TCF7, IL7R, CD27
- CD28, CD45RO, CD45RA, BCL2, CXCR4, ITGAE, ITGB1, ITGB7, MADCAM1, CXCR3, CCR6, CD69
- CD127, ICOS, CD40LG, PDCD1, LAG3, HAVCR2, TOX, CXCR5, CTLA4, TNFRSF4, TNFRSF9, TNFRSF18
- GZMK, GZMA, PRF1, NKG7, GNLY, GZMB, IFNG, TNF, CCL4, CCL3, IL2RA

### CD8_TCM

Description: Central memory CD8+ T cells with lymphoid-homing capacity and self-renewal potential.

Genes:
- CD8A, CD8B, CCR7, SELL, LEF1, TCF7, IL7R, CD27, CD28, CD3D, CD3E, CD2
- CD7, CD5, CD45RO, CD45RA, BCL2, CXCR4, ITGAE, ITGB1, ITGB7, MADCAM1, CXCR3, CCR6
- CD69, CD127, EOMES, TBX21, GZMK, GZMA, PRF1, NKG7, GNLY, GZMB, IFNG, TNF
- CCL4, CCL3, CD40LG, ICOS, PDCD1, LAG3, HAVCR2, TOX, CXCR5

### CD8_TEM

Description: Effector memory CD8+ T cells with cytotoxic capacity and tissue-homing potential.

Genes:
- CD8A, CD8B, GZMB, PRF1, NKG7, GNLY, GZMH, GZMA, GZMK, IFNG, TNF, CCL4
- CCL3, CX3CR1, FGFBP2, KLRD1, KLRC1, KLRK1, NCR1, CD160, EOMES, TBX21, CD45RA, CD45RO
- CD3D, CD3E, ITGAE, ITGB1, CXCR3, CCR5, CX3CR1, FCGR3A, TYROBP, FCER1G, AIF1, LST1
- CD2, CD7, CD27, CD28, CD57, KLRG1, PDCD1, LAG3, HAVCR2, TOX

### MAIT

Description: Mucosal-associated invariant T cells recognizing MR1-presented microbial metabolites, enriched in blood and mucosal tissues.

Genes:
- TRAV1-2, KLRB1, RORC, IL7R, SLC4A10, ZBTB16, NCR3, CXCR6, ITGAM, CD161, GZMK, GZMA
- PRF1, GZMB, NKG7, GNLY, CCL4, CCL3, IFNG, TNF, IL17A, IL22, IL23R, CCR6
- CD69, CD45RA, CD45RO, CD3D, CD3E, CD8A, CD8B, EOMES, TBX21, BCL11B, TCF7, LEF1
- SELL, CCR7, CXCR3, CXCR4, ITGAE, ITGB1, ITGB7, MADCAM1, FCGR3A

## nk

### NK_adaptive

Description: Adaptive-like NK cells expanded during viral infections, characterized by NKG2C expression and enhanced antibody-dependent cellular cytotoxicity.

Genes:
- FCGR3A, NKG2C, KLRC1, KLRG1, CD57, FCER1G, SYK, BCL11B, EOMES, TBX21, CX3CR1, ITGAE
- CD103, GZMB, PRF1, NKG7, GNLY, CST7, TYROBP, KLRD1, KLRF1, NCAM1, CD247, GZMH
- FGFBP2

### NK_cycling

Description: Proliferating NK cells undergoing active cell division, identifiable by high expression of cell cycle and mitosis-related genes.

Genes:
- MKI67, TOP2A, BIRC5, CCNB2, CCNB1, CDK1, AURKA, AURKB, BUB1, BUB1B, MAD2L1, TTK
- KIF11, KIF20A, KIF23, CENPF, CENPE, SMC4, SMC2, HMMR, NUF2, NUSAP1, PBK, PLK1
- CDC20

### NK_cytotoxic

Description: Mature cytotoxic NK cells with high expression of perforin and granzymes, mediating direct target cell lysis.

Genes:
- NKG7, GNLY, GZMB, GZMH, GZMA, PRF1, FGFBP2, CST7, KLRD1, KLRF1, KLRK1, NCR1
- NCAM1, FCGR3A, TYROBP, EOMES, TBX21, CX3CR1, CD247, GZMK, SPON2, HOPX, MTSS1, PLXND1
- ITGAL

### NK_exhausted

Description: Exhausted NK cells with upregulated inhibitory receptors and transcription factors associated with functional impairment in chronic disease states.

Genes:
- PDCD1, LAG3, HAVCR2, TIGIT, CTLA4, TOX, TOX2, BATF, BATF2, IRF4, IRF8, EOMES
- TBX21, CXCR5, CXCR3, CCR7, SELL, CD69, CD38, HLA-DRB1, HLA-DRA, CD74, FCGR3A, NKG7
- GZMB

### NK_regulatory

Description: Immunoregulatory NK cells with antigen-presenting capabilities and cytokine production functions.

Genes:
- CD56, NCAM1, FCGR2A, CD69, CD27, SELL, CCR7, CXCR4, IL7R, TNFRSF4, TNFRSF18, ITGAX
- CD1C, FCER1G, TYROBP, KLRB1, CD40LG, ICOS, TNFRSF9, CD40, CD80, CD86, HLA-DRA, HLA-DRB1
- CD74

## nk proliferating

### NK CD56bright

Description: Immunoregulatory CD56bright NK cells with high cytokine responsiveness, MHC class II expression, and lower cytotoxic granule content compared to CD56dim NK cells.

Genes:
- NCAM1, IL2RA, IL7R, CCR7, SELL, LEF1, TCF7, CXCR4, CD38, CD1c, FCER1A, CD74
- HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, TNFRSF4, TNFRSF18, TNFRSF9, CD69, NCR1, NCR2, NCR3, KLRB1
- KLRG1, EOMES, TBX21, GZMK, GZMA, PRF1

### NK Immature

Description: Immature or transitional NK cells with lower cytotoxicity and higher expression of homing, lymphoid progenitor, and activation markers.

Genes:
- CD34, CD7, CD10, IL7R, CCR7, SELL, LEF1, TCF7, ITGAL, CD69, CXCR4, FLT3
- IL2RA, CD44, CD160, NCR3, NCR2, KLRG1, CD56, NCAM1, TNFRSF18, TNFRSF4, CD63, CD82
- CD9, CD81, ITGB1, ITGB2, LFA1, VLA4

### NK Mature

Description: Mature cytotoxic NK cells with high expression of cytotoxic granule genes, activating/inhibitory receptors, and transcription factors EOMES and TBX21.

Genes:
- NKG7, GNLY, GZMB, GZMH, GZMA, PRF1, KLRD1, KLRK1, NCAM1, FCGR3A, CD247, EOMES
- TBX21, FGFBP2, CX3CR1, ITGAE, TYROBP, FCER1G, SYK, PLCG2, PIK3CG, LCK, ZAP70, CD7
- CD38, HLA-DRB1, IL2RB, IL15RA, NCR1, KLRB1

### NK Proliferating

Description: Cycling natural killer cells in G2/M or S phase characterized by high expression of cell cycle and mitosis genes alongside canonical NK cytotoxic markers.

Genes:
- MKI67, TOP2A, PCNA, BIRC5, HMGB2, HMGB1, H2AFZ, TYMS, MCM2, MCM3, MCM4, MCM5
- MCM6, MCM7, CDK1, CCNB2, CCNB1, CDC20, CENPF, CENPA, KIF11, AURKB, BUB1, NUSAP1
- KIF20A, KIF23, PRC1, ANLN, ASPM, TPX3, NKG7, GNLY, GZMB, GZMA, KLRD1, NCAM1
- FCGR3A, CD247, EOMES, TBX21

### T Proliferating

Description: Cycling T cells in active cell cycle phases expressing proliferation markers alongside T cell receptor signaling genes, often confused with proliferating NK cells due to shared cell cycle signatures.

Genes:
- MKI67, TOP2A, PCNA, BIRC5, HMGB2, TYMS, MCM2, MCM3, MCM4, MCM5, MCM6, MCM7
- CDK1, CCNB2, CCNB1, CDC20, CENPF, KIF11, AURKB, NUSAP1, CD3D, CD3E, CD28, IL7R
- LEF1, TCF7, CCR7, SELL, MAL, LCK, ZAP70, CD7, CD2, TRAT1, THEMIS, GADS
- LAT, ITK, PRKCQ, CD40LG

## nk_cd56bright

### NK_CD56bright

Description: Immunoregulatory CD56-bright natural killer cells enriched in lymph nodes and secondary lymphoid tissues, characterized by high cytokine production and low baseline cytotoxicity.

Genes:
- NCAM1, CD56, NKG7, KLRD1, KLRC1, KLRK1, FCGR3A, CD2, CD7, CD38, CXCR4, CCR7
- SELL, ITGAE, ITGB2, GZMB, PRF1, GNLY, TYROBP, FCER1G, CD94, NCR1, NCR2, NCR3
- SLAMF7, CD69, CD160, TNFRSF18, TNFRSF4, IL2RB, IL7R, XCL1, XCL2, CCL4, CCL3, IFNG
- TNF, LTA, LTB, EOMES, TBX21, TOX, TCF7, LEF1

### NK_CD56dim

Description: Circulating CD56-dim cytotoxic natural killer cells that constitute the majority of peripheral blood NK cells and mediate antibody-dependent cellular cytotoxicity and direct target cell lysis.

Genes:
- FCGR3A, NCAM1, NKG7, GNLY, GZMB, GZMA, GZMH, GZMK, PRF1, KLRD1, KLRC1, KLRK1
- KLRB1, CD2, CD7, CD38, TYROBP, FCER1G, CD94, NCR1, NCR2, NCR3, SLAMF7, CD160
- FGFBP2, CX3CR1, ITGAE, ITGB2, IL2RB, IL7R, EOMES, TBX21, TNFRSF10B, FAS, FASLG, TNF
- IFNG, CCL4, CCL3, XCL1, XCL2, LTA, LTB, CD69

### NK_Proliferating

Description: Proliferating NK cells in G2/M or S phase characterized by high expression of cell cycle and mitotic genes, representing activated or recently divided NK cells.

Genes:
- MKI67, TOP2A, BIRC5, CCNB2, CCNB1, CDK1, PCNA, MCM2, MCM3, MCM4, MCM5, MCM6
- MCM7, TYMS, DHFR, RRM1, RRM2, TK1, HMGB2, HMGB1, H2AZ1, H2AFX, NUSAP1, KIF11
- KIF20A, AURKA, AURKB, BUB1, BUB1B, CDC20, CENPF, CENPE, CENPA, CENPB, CENPC, CENPU
- CENPW, CENPN, CENPL, CENPM, CENPO, CENPQ, CENPR, CENPS, CENPT, CENPU, CENPV, CENPW
- CENPX

### cDC2

Description: Conventional type 2 dendritic cells specialized for antigen presentation and T cell priming, characterized by expression of CD1c and FcεRIα.

Genes:
- CD1C, FCER1A, CLEC10A, CLEC4C, ITGAX, ITGAM, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1
- CD74, CD1B, CD1A, FCER1G, TYROBP, CTSL, CTSS, MRC1, CD303, CD304, IL3RA, NRP1
- CD123, CLEC9A, CD141, THBD, IRF4, IRF8, BATF3, ZBTB46, CD40, CD80, CD86, CCR7
- CXCR4, CX3CR1, CD2, CD7, CD38, CD33, CD36, CD44, ITGB2, FCGR1A, FCGR2A, FCGR3A

### pDC

Description: Plasmacytoid dendritic cells specialized for type I interferon production in response to viral infections, expressing high levels of IL3RA and Toll-like receptors.

Genes:
- IL3RA, CD303, CD304, TCF4, CD2AP, NRP1, FCER1A, CLEC4C, GZMB, IRF7, IRF8, SPIB
- PAX5, CD123, LILRA4, LILRA2, LILRA1, LILRB1, LILRB2, LILRA6, SERPINF1, MRC1, CD1C, CD1B
- CD1A, FCER1G, TYROBP, CTSL, CTSS, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, CD74
- ITGAX, ITGAM, CXCR3, CXCR4, CCR6, CCR7, SELL, CD45RA, PTCRA, BCL11A

## pdc

### B_cell

Description: B lymphocytes are antibody-producing adaptive immune cells that can be confused with pDCs due to shared B-cell-like transcriptional programs and HLA-DR expression.

Genes:
- CD19, MS4A1, CD79A, CD79B, BLK, BANK1, CD22, PAX5, SPIB, BCL11A, TCL1A, TCL1B
- FCRL2, FCRL4, CD24, CD38, IGHM, IGHD, IGKC, IGLC2, VPREB3, VPREB1, IGHA1, IGHG1
- CD27, TNFRSF13C, TNFRSF13B, AICDA, MZB1, DERL3

### Monocyte

Description: Monocytes are innate myeloid cells that can be misannotated as pDCs due to overlapping expression of HLA-DR, Fc receptors, and antigen-processing genes.

Genes:
- CD14, LYZ, S100A8, S100A9, S100A4, S100A6, S100A10, FCN1, FCGR3A, VCAN, CFD, TYMP
- MNDA, LST1, NCF1, NCF2, NCF4, CST3, CTSB, CTSD, CTSS, HLA-DRA, HLA-DRB1, CD74
- ITGAM, ITGAX, CCR2, CX3CR1, FCGR1A, CD68

### cDC1

Description: Conventional type 1 dendritic cells specialize in cross-presentation of exogenous antigens to CD8+ T cells and are marked by CLEC9A and CD141.

Genes:
- CLEC9A, CD141, THBD, IRF8, BATF3, ID2, XCR1, TLR3, CXCR3, FCER1A, HLA-DRA, HLA-DRB1
- CD74, ITGAX, CD36, NEURL1, CADM1, LAMP3, CCR7, CCL19, CCL22, FSCN1, VCAN, S100A4
- S100A6, ANXA2, CD1C, CD1D, CD1B, FCGR2B

### cDC2

Description: Conventional type 2 dendritic cells are potent CD4+ T cell priming antigen-presenting cells characterized by CD1c and FcεRIα expression.

Genes:
- CD1C, FCER1A, CLEC10A, ITGAX, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, CD74, FCGR2B, CD40, CD86
- CD80, CCR7, CCL22, IRF4, ZEB2, CD14, LYZ, S100A4, S100A6, S100A10, ANXA2, FSCN1
- VCAN, FCN1, CFD, TREM1, CD1D, CD1B

### pDC

Description: Plasmacytoid dendritic cells are specialized type I interferon-producing antigen-presenting cells that sense viral nucleic acids via TLR7/TLR9.

Genes:
- IL3RA, TCF4, CD303, CD304, NRP1, CD2AP, RUNX2, IRF8, SPIB, BCL11A, LILRA4, GZMB
- SERPINF1, FCER1A, CD123, ITGAX, HLA-DRA, HLA-DRB1, CD74, CXCR4, CD44, VCAN, FCRLA, BDC
- IRF7, MYD88, TLR9, TLR7, CD1c, FCGR2B

## plasmablast

### Dendritic cell

Description: Professional antigen-presenting cells with high MHC-II and co-stimulatory molecule expression, frequently confused with plasmablasts due to overlapping HLA and CD74 signatures.

Genes:
- CLEC9A, CD1C, FCER1A, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, CD74, ITGAX, ITGAM
- CD11B, CD14, LYZ, FCGR3A, S100A8, S100A9, S100A4, VCAN, TYMP, CFP, MNDA, LST1
- AIF1, CTSS, CST3, PSAP, IRF4, IRF8, BATF3, CD83, CD86, CD40, CCR7, CXCR4
- IL3RA, NRP1, CD303, CD304

### Memory B cell

Description: Class-switched or IgM+ antigen-experienced B cells expressing CD27, ready for rapid recall responses upon re-exposure.

Genes:
- CD27, MS4A1, CD19, CD79A, CD79B, TCL1A, TCL1B, BANK1, FCRL2, FCRL4, FCRL5, ITGAX
- CD80, CD86, TNFRSF13C, TNFRSF13B, IGHG1, IGHA1, IGHM, IGHD, CR2, CD21, CD40, PAX5
- SPIB, BLK, CD24, HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, CD74, FCER2, CD38
- PRDM1, IRF4, XBP1, MZB1

### Monocyte

Description: Myeloid phagocytes with high lysosomal and inflammatory gene expression, often misannotated as plasmablasts due to shared HLA and CD74 expression.

Genes:
- CD14, LYZ, S100A8, S100A9, S100A4, S100A6, FCN1, VCAN, TYMP, IFITM3, CFP, FGL2
- MNDA, LST1, AIF1, CTSS, CSTB, CST3, PSAP, PSMB4, FCGR3A, HLA-DRA, HLA-DRB1, HLA-DQA1
- HLA-DQB1, HLA-DPA1, HLA-DPB1, CD74, IL1B, TNF, IL6, CCL3, CCL4, CXCL8, NLRP3, TLR4
- TLR2, ITGAM, ITGAX, CD11B

### Naive B cell

Description: Mature recirculating B cells expressing surface IgD and IgM, poised for antigen encounter and germinal center entry.

Genes:
- MS4A1, CD19, CD79A, CD79B, BLK, BANK1, FCRL2, FCRL1, TCL1A, TCL1B, CD24, IGHD
- IGHM, LINC00926, FCER2, CD22, SPIB, PAX5, IGHG1, IGHA1, CD83, CD69, CD86, HLA-DRA
- HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, CD74, TNFRSF13C, TNFRSF13B, BAFFR, IGLL5, VPREB3, CD40
- CR2, CD21, FCRL4, FCRL5, FCRL6

### Plasmablast

Description: Antibody-secreting B-cell precursors transitioning from germinal center B cells, characterized by high immunoglobulin and ER chaperone expression.

Genes:
- MZB1, JCHAIN, IGHG1, IGHA1, IGHM, IGKC, IGLC2, SDC1, CD27, CD38, PRDM1, XBP1
- IRF4, TNFRSF17, PAX5, CD19, CD79A, CD79B, DERL3, FKBP11, HSPA5, HERPUD1, DNAJC3, SYND1
- TAP1, TAP2, SEC61A1, SEC61B, SSR1, RPN1, CALR, CANX, HSP90B1, PDIA3, PDIA6, ERP29
- EDEM1, MANF, CRELD1, IGLL5

## platelet

### Erythrocyte

Description: Anucleate red blood cells specialized for oxygen transport via hemoglobin, occasionally detected as circulating contaminants in PBMC preparations.

Genes:
- HBB, HBA1, HBA2, ALAS2, SLC4A1, AHSP, CA1, ANK1, SPTA1, SPTB, EPB42, EPB41
- GYPA, GYPC, RHAG, RHCE, RHD, KEL, DARC, TFRC, TFR2, EPOR, GYPB, GYPE
- GYPF, GYPG, GYPH, KLF1, BPGM, CAT, SOD2, GLRX5, FECH, HMOX1, HMOX2, BLVRB
- BLVRA, GCLC, GCLM, GSR, GSTM1, GSTP1, GSTT1, GSTZ1

### Megakaryocyte

Description: Large bone marrow-derived polyploid progenitor cells that produce platelets and express high levels of platelet surface glycoproteins.

Genes:
- ITGA2B, ITGB3, GP1BB, GP5, GP9, PF4, PPBP, THBS1, TUBB1, CD9, CD63, CXCR4
- CMTM5, SPARC, GNG11, VWF, MPL, GP1BA, GP6, SELP, PECAM1, CD44, CD36, CD38
- CD61, CD41, CD42A, CD42B, CD42C, CD42D, CD49D, CD49F, CD51, CD62P, CD107A, CD107B
- CD147, CD151, CD162, CD164, CD177, CD226, CD229, CD231, CD235A, CD235B

### Monocyte

Description: Circulating myeloid phagocytes that can be mis-annotated as platelets in droplet-based scRNA-seq due to shared granule-derived transcripts and ambient RNA.

Genes:
- CD14, LYZ, S100A8, S100A9, S100A4, S100A6, FCN1, VCAN, TYMP, CFP, FGL2, MNDA
- CST3, CTSB, CTSD, CTSL, CTSS, LST1, AIF1, FCGR3A, MS4A7, CD68, CD36, C1QA
- C1QB, C1QC, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, ITGAM, ITGAX, CCR2, CX3CR1
- FCGR1A, FCGR2A, FCGR2B, TLR2, TLR4, TLR8, NCF1, NCF2, NCF4, CYBA, CYBB

### Neutrophil

Description: Polymorphonuclear granulocytes with multilobed nuclei and abundant cytoplasmic granules, frequently co-captured with platelets and a common source of annotation confusion.

Genes:
- FCGR3B, CSF3R, CXCR2, CXCR1, MMP9, MMP8, ELANE, PRTN3, CTSG, AZU1, H3C1, H3C2
- H3C3, H3C4, H3C5, H3C6, H3C7, H3C8, H3C9, H3C10, H3C11, H3C12, H3C13, H3C14
- H3C15, H3C16, H3C17, H3C18, H3C19, H3C20, H3C21, LTF, CAMP, LCN2, DEFB1, DEFB4A
- DEFB4B, S100A12, S100A8, S100A9, FCER1G, FPR1, FPR2, ITGAM, ITGAX, CD177, CD55, CD59

### Platelet

Description: Anucleate blood cells derived from megakaryocytes that mediate hemostasis and thrombus formation via granule release and aggregation.

Genes:
- PPBP, PF4, GP1BB, GP5, GP9, THBS1, CXCR4, CD9, CD63, ITGA2B, ITGB3, TUBB1
- GNG11, CMTM5, SPARC, HIST1H2BC, HIST1H4C, HIST1H3A, HIST1H2AE, HIST1H2AC, HIST1H2AD, HIST1H2AG, HIST1H2AH, HIST1H2BB
- HIST1H2BJ, HIST1H2BK, HIST1H2BL, HIST1H2BM, HIST1H2BN, HIST1H2BO, HIST1H2BP, HIST1H2BQ, HIST1H2BR, HIST1H2BS, HIST1H2BT, HIST1H2BU
- HIST1H2BV, HIST1H2BW, HIST1H2BX, HIST1H2BY, HIST1H2BZ

## treg

### Memory_CD4_Tcell

Description: Antigen-experienced CD4+ T cells with enhanced effector functions and tissue-homing capabilities.

Genes:
- IL7R, CD44, CD69, CXCR3, CCR6, ITGAE, ITGA1, GZMK, GZMA, PRF1, NKG7, CST7
- EOMES, TBX21, IFNG, TNF, IL2, CD28, ICOS, PDCD1, CTLA4, TNFRSF9, TNFRSF4, CD40LG
- CD3D, CD3E, CD4, LCK, ZAP70, LAT, THEMIS

### Naive_CD4_Tcell

Description: Resting, antigen-inexperienced CD4+ T cells with high lymph node homing potential and naive TCR signaling capacity.

Genes:
- CCR7, LEF1, TCF7, SELL, IL7R, MAL, CD40LG, ITGB1, CD27, CD28, LTB, LTA
- GIMAP2, GIMAP4, GIMAP5, GIMAP7, GIMAP8, TRAT1, MYC, BACH2, KLF2, KLF4, S1PR1, CD3D
- CD3E, CD4, LAT, ZAP70, LCK, THEMIS

### T_helper_1

Description: CD4+ T helper 1 cells specialized in Th1-type immunity, producing IFN-gamma and TNF-alpha for intracellular pathogen defense.

Genes:
- TBX21, CXCR3, CCR5, IFNG, TNF, IL2, IL12RB1, IL12RB2, STAT1, STAT4, EOMES, GZMB
- GZMA, PRF1, NKG7, CST7, CD40LG, CD69, CD38, CD4, CD3D, CD3E, LCK, ZAP70
- LAT, THEMIS, ICOS, PDCD1, CTLA4, TNFRSF9

### T_helper_17

Description: CD4+ T helper 17 cells producing IL-17 and IL-22, critical for mucosal immunity and autoimmune inflammation.

Genes:
- RORC, CCR6, IL17A, IL17F, IL22, IL23R, IL21, STAT3, AHR, BATF, MAF, CD40LG
- CD69, CD38, CD4, CD3D, CD3E, LCK, ZAP70, LAT, THEMIS, ICOS, PDCD1, CTLA4
- TNFRSF9, TNFRSF4, GZMB, GZMA, PRF1, NKG7

### Treg

Description: CD4+ regulatory T cells expressing FOXP3 that suppress immune responses and maintain self-tolerance.

Genes:
- FOXP3, IL2RA, CTLA4, IKZF2, TNFRSF4, TNFRSF18, TIGIT, LAG3, IKZF3, CCDC88A, SATB1, FAM129C
- CASP4, GZMB, PRF1, GZMA, NKG7, CST7, IL1R1, IL1R2, CD27, CD38, HLA-DRA, HLA-DRB1
- HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, CD74, FCRL3

