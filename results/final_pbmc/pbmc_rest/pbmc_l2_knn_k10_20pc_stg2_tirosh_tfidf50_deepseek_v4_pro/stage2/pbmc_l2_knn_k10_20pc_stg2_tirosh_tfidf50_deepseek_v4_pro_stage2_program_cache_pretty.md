# Stage-2 Precomputed Programs

- tissue: PBMC
- n_program_genes: 50
- n_cached_cell_types: 31

## asdc

### AXL+ SIGLEC6+ dendritic cell (ASDC)

Description: AXL and SIGLEC6 double-positive dendritic cells that share features with plasmacytoid DCs, involved in type I interferon production and T-cell activation.

Genes:
- AXL, SIGLEC6, IL3RA, CLEC4C, NRP1, TCF4, BCL11A, SOX4, LILRA4, PACSIN1, C12orf75, LINC00996
- SERPINF1, MZB1, DERL3, IRF7, IRF8, TLR7, TLR9, CCR7, CXCR3, GZMB, PRDM1, PTPRS
- EGR1, JUNB, FOS, SLC15A4, FUT4, PTCRA

### CD1c+ conventional dendritic cell 2 (cDC2)

Description: Professional antigen-presenting cells that prime CD4+ T cells, characterized by CD1c and high levels of MHC class II and Fc receptors.

Genes:
- CD1C, FCER1A, FCGR2B, SIRPA, CLEC10A, CD1E, FCGR2A, CD5, ITGAX, ITGAM, CD33, CD163
- HLA-DRA, HLA-DRB1, CD4, TRAF1, ETS2, TWIST1, FLT3, CX3CR1, CCR7, CD40, CSF1R, CD74
- HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, CD86, CD80

### CLEC9A+ conventional dendritic cell 1 (cDC1)

Description: Dendritic cells specialized in cross-presentation of exogenous antigens to CD8+ T cells, marked by CLEC9A and XCR1.

Genes:
- CLEC9A, XCR1, CADM1, BATF3, IRF8, ID2, THBD, CLEC6, WDFY4, CST3, NDST2, CLNK
- KCNIP3, ZBTB46, FLT3, HLA-DRA, HLA-DRB1, BTLA, SLAMF7, CD80, CD86, CD40, TLR3, CXCL10
- CCL22, CCL17, XCL1, XCL2, KIAA1328, LAMP3

### Plasmacytoid dendritic cell (pDC)

Description: Specialized dendritic cells producing high levels of type I interferons upon viral sensing, characterized by expression of CD123, BDCA2, and BDCA4.

Genes:
- IL3RA, CLEC4C, NRP1, TCF4, BCL11A, LILRA4, IRF7, IRF8, TLR7, TLR9, GZMB, SPIB
- SERPINF1, CD300C, CD2, SLC15A4, FUT4, PTCRA, PTGDR, CCR2, CXCR3, SOX4, PACSIN1, C12orf75
- LINC00996, DERL3, MZB1, RUNX2, ZNF683, PTPRS

### Pre-dendritic cell (pre-DC)

Description: Early precursors of conventional dendritic cells that express CD5 and CD33, with potential to differentiate into cDC1 and cDC2.

Genes:
- CD5, CD33, CX3CR1, CD2, CD7, SPN, FLT3, IL3RA, CD34, KIT, GATA2, SPI1
- IRF8, ID2, AXL, TCF4, SOX4, LILRA4, BCL11A, SLC15A4, FUT4, PTCRA, PTGDR, CCR2
- C12orf75, LINC00996, ZNF683, RUNX2, MZB1, DERL3

## b intermediate

### CD14+ Monocytes

Description: Classical monocytes that migrate to tissues, expressing CD14 and high levels of myeloid-specific genes.

Genes:
- CD14, LYZ, CST3, S100A8, S100A9, S100A12, FCN1, VCAN, CLEC4E, CLEC5A, TLR2, TLR4
- CD36, ITGAM, ITGB2, CD68, CSF1R, LILRB2, LILRA2, MS4A7, MMP9, FPR1, FPR2, IFITM3
- TREM1, CD163, SELL, CCR2, CX3CR1, IL1B, TNF, IL6, CCL2, CCL3, CCL4, SERPINB2
- THBS1, VIM, ANXA1, LGALS3

### CD4+ T cells

Description: Helper T lymphocytes orchestrating adaptive immunity, expressing CD4 and TCR components.

Genes:
- CD3D, CD3E, CD3G, CD4, IL7R, TRAC, TRBC1, TRBC2, LCK, LAT, ZAP70, CD2
- CD28, CTLA4, ICOS, PDCD1, TIGIT, CD40LG, IFNG, IL2, TNF, LTB, RGS1, CCR7
- SELL, LEF1, TCF7, MAL, GIMAP5, GIMAP4, GIMAP7, CXCR4, CXCR3, CCR5, CXCR6, TBX21
- GATA3, RORC, BCL6, PRDM1, MAF

### Memory B cells

Description: Antigen-experienced B cells expressing CD27 and class-switched immunoglobulins, poised for rapid recall responses.

Genes:
- CD27, TNFRSF13B, AIM2, CD80, CD86, FAS, IL21R, CD38, CD24, CD1D, BATF, IRF4
- PRDM1, PAX5, MS4A1, CD19, CD22, IGHG1, IGHG2, IGHG3, IGHG4, IGHA1, IGHA2, IGKC
- ZBTB32, LMO2, CXCR3, CXCR4, CCR6, CXCR5, ICOS, CD44, CD55, IL4R, TXNIP, MZB1
- SDC1, XBP1, HLA-DRA, HLA-DRB1

### Naive B cells

Description: Resting naive B cells expressing surface IgM and IgD, with high MS4A1 and TCL1A, awaiting antigen encounter.

Genes:
- MS4A1, CD19, CD22, CD79A, CD79B, CD74, HLA-DRA, HLA-DRB1, IGHM, IGHD, TCL1A, FCER2
- BANK1, PAX5, EBF1, ADAM28, LILRB1, CD1C, CLECL1, FCRL1, FCRL2, BLNK, STAP1, IGKC
- IGLC2, CD37, CD40, TRAF3IP2, IRF8, SPIB, BCL11A, POU2AF1, PTPN6, CXCR5, CCR7, SELL
- CXCR4, MGAT4A, RAG1, RAG2

### Plasmablasts

Description: Antibody-secreting cells with high SDC1 and ER stress response genes, representing the effector arm of humoral immunity.

Genes:
- SDC1, MZB1, XBP1, PRDM1, IRF4, CD27, CD38, TNFRSF17, SLAMF7, CD79A, CD79B, IGHG1
- IGHA1, IGKC, JCHAIN, SSR4, DERL3, FKBP11, HSP90B1, PDIA4, PDIA6, PPIB, CANX, CALR
- MANF, SDF2L1, EDEM1, ERN1, ATF6, CREB3L2, SEC61A1, SEC11C, SPCS1, SRPRB, KLF2, CXCL10
- ST6GAL1, B4GALT1, MGAT5, LMAN1

## b memory

### Atypical memory B cells

Description: Atypical CD27- IgD- memory B cells expressing FCRL4 and ITGAX, often expanded in chronic infections.

Genes:
- BANK1, CD19, CD22, CD38, CD79A, CD79B, CR2, CXCR3, FCRL4, FCRL5, GPR183, IRF4
- ITGAX, MS4A1, PAX5, TBX21, TNFRSF13B, ZBTB32

### B memory (switched)

Description: Switched memory B cells expressing isotype-switched immunoglobulins (e.g., IgG, IgA) and memory marker CD27.

Genes:
- AICDA, BANK1, CD19, CD22, CD27, CD38, CD40, CD79A, CD79B, CR2, FAIM3, GPR183
- IGHA1, IGHG1, IGHG2, IL6R, IRF4, MS4A1, PAX5, PDE4D, TNFRSF13B, ZEB2

### B memory (unswitched)

Description: Unswitched IgM+ IgD+ memory B cells that retain CD27 expression without class switching.

Genes:
- BANK1, CD19, CD22, CD27, CD38, CD40, CD79A, CD79B, CR2, FAIM3, GPR183, IGHD
- IGHM, IL6R, IRF4, MS4A1, PAX5, SELL, TNFRSF13B, ZEB2

### Naive B cells

Description: Mature naive B cells that have not encountered antigen, expressing IgD, IgM, and lacking CD27.

Genes:
- BACH2, CD19, CD22, CD24, CD38, CD40, CD72, CD79A, CD79B, CR2, CXCR5, FCER2
- GPR183, IGHD, IGHM, IL4R, MS4A1, PAX5, SELL, TCL1A

### Plasma cells

Description: Terminally differentiated antibody-secreting cells with high CD38, CD27, and CD138 expression.

Genes:
- CD27, CD38, DERL3, FKBP11, HSP90B1, IGHA1, IGHG1, IGHM, IGJ, IRF4, MZB1, PDIA4
- PRDM1, SDC1, SEC11C, SLAMF7, SPCS2, SSR4, TNFRSF17, XBP1

## b naive

### B memory

Description: Antigen-experienced B cells expressing CD27, capable of rapid response, including class-switched and unswitched subsets.

Genes:
- CD19, MS4A1, CD22, CD79A, CD79B, CD27, CD38, CD80, CD86, FAS, TNFRSF13B, IL21R
- ITGA4, CD44, MYBL1, ZBTB32, SOX5, CD70, CCR6, CXCR3, TLR7, TLR9, CD40

### B naive

Description: Mature resting naive B cells expressing high levels of IGHM and IGHD, lacking CD27 expression.

Genes:
- IGHM, IGHD, MS4A1, CD19, CD22, CD79A, CD79B, FCER2, SELL, CCR7, CXCR4, TCL1A
- IL4R, BANK1, BACH2, PAX5, EBF1, TCF4, LEF1, CD72, RALGPS2, SWAP70, TNFRSF13C, CR2
- BTG2, CD37, POU2AF1

### Plasmablast

Description: Antibody-secreting cells with high expression of PRDM1, XBP1, and SDC1, downregulating pan-B cell markers.

Genes:
- SDC1, TNFRSF17, SLAMF7, XBP1, PRDM1, IRF4, ELL2, MZB1, JCHAIN, IGJ, DERL3, SEC11C
- SSR4, FKBP11, CD38, CD27, CD9, CD44, ITGA4, CCR10, CXCR4

### Transitional B

Description: Immature recent bone marrow emigrants with a CD24hiCD38hi phenotype and expression of CD10, CD5, and surrogate light chain VPREB3.

Genes:
- CD19, MS4A1, CD22, CD79A, CD79B, IGHM, IGHD, CD24, CD38, MME, CD5, VPREB3
- CD1C, SPIB, ST3GAL6, CD9, TCL1A, SOX4, IL10, TGFB1, ID2, LMO2, BCL2, CXCR5
- CD44

## cd14 mono

### Classical Monocyte

Description: Classical CD14++CD16- monocytes with high phagocytic and inflammatory capacity.

Genes:
- S100A8, S100A9, S100A12, LYZ, CD14, VCAN, FCN1, CST3, TYROBP, ITGAM, CSF1R, MNDA
- AIF1, CYBB, S100A4, SERPINA1, CHI3L1, FGL2, IFITM3, IL1B, IL8, CCL3, CCL4, TNFAIP3
- PLBD1, GCA, MS4A6A, CLEC4E, CLEC5A, TLR2

### Intermediate Monocyte

Description: CD14++CD16+ intermediate monocytes bridging classical and non-classical subsets, with antigen presentation and pro-inflammatory functions.

Genes:
- CD14, FCGR3A, HLA-DQA1, HLA-DQB1, HLA-DRB1, HLA-DRB5, CD74, CTSL, CCL2, CCR2, CD36, ITGAX
- STAT1, IRF5, TLR5, PTGER2, PECAM1, CD99, CLEC2B, PLAUR, LILRB2, TREM1, CLEC7A, CCR5
- CX3CR1, ADAM19, ITGAM, LST1, AIF1, MNDA

### NK Cell

Description: Natural killer cells with high cytotoxicity and expression of CD16 (FCGR3A) and CD56 (NCAM1), often confused with non-classical monocytes.

Genes:
- NKG7, GNLY, GZMB, PRF1, KLRD1, KLRF1, FCGR3A, NCAM1, NCR1, CD160, KIR2DL1, KIR2DL3
- KIR3DL1, KIR2DS4, SH2D1B, CD244, CD2, CD247, ZAP70, SLAMF6, KLRC1, KLRC2, KLRK1, LAG3
- CX3CR1, ITGAL, IL2RB, B3GAT1, GZMA, GZMH

### Non-classical Monocyte

Description: CD14dimCD16++ patrolling monocytes that survey vasculature and possess high antiviral and complement-related gene expression.

Genes:
- FCGR3A, LILRA2, CDKN1C, ITGAL, TNFRSF1B, CX3CR1, ADAM17, LILRB2, KLRF1, SLAMF7, CMKLR1, PLAC8
- ZEB2, TCF7L2, EMP1, ENO1, ITGB2, SPN, S100A4, S100A6, CLEC4A, HMOX1, VIM, TMEM176A
- TMEM176B, LST1, MTSS1, C1QB, C1QA, C1QC

### cDC2 Dendritic Cell

Description: Type 2 conventional dendritic cells (cDC2) expressing CD1c and CLEC10A, specialized in antigen presentation to CD4 T cells.

Genes:
- CD1C, CLEC10A, FCER1A, ITGAX, SIRPA, CSF1R, FLT3, IRF4, ID2, CLEC4A, CLEC4C, CLEC12A
- FCGR2B, LILRA3, LILRB4, TRAF1, NFKB1, ETS1, BATF3, SPI1, CD40, CCR7, HLA-DPA1, HLA-DQA1
- HLA-DQB1, HLA-DRB1, CLECL1, TLR2, TLR4, CD86

## cd16 mono

### CD1c+ Dendritic Cells

Description: CD1c+ conventional dendritic cells type 2 specialized in antigen presentation to CD4+ T cells.

Genes:
- CD1C, FCER1A, CLEC10A, CLEC4A, CLEC12A, SIRPA, ITGAX, HLA-DQA1, HLA-DQB1, HLA-DRA, CD74, CSRP1
- IRF4, KLF4, ZEB2, LY86, CD1A, CD83, CCR7, FSCN1, FLT3, KIT, CIITA, CD40
- ICAM1, LAMP3, LY75, VIM, ILT3, CLEC7A

### CD56dim CD16+ NK cells

Description: Cytotoxic CD56dim CD16+ natural killer cells mediating antibody-dependent cellular cytotoxicity and direct killing.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMH, KLRF1, KLRD1, NCR1, KLRK1, KLRB1, CD7, SH2D1B
- TBX21, EOMES, ZBTB16, NCAM1, FCGR3A, ADGRE5, KLRC1, KIR2DL1, KIR2DL3, KIR3DL1, CD160, KLRC2
- KIR3DL2, RAC2, RHOC, ITGB2, CD47, LAMP1

### Classical Monocytes

Description: CD14+ CD16- phagocytic monocytes that respond to bacterial infection and chemokine signals.

Genes:
- CD14, CCR2, S100A8, S100A9, LYZ, VCAN, CD36, CLEC4E, FCN1, S100A12, LILRB4, ITGAM
- CSF1R, PECAM1, SELL, CD44, ANXA2, ANXA3, LGALS2, CLEC5A, TLR2, TLR4, CD68, CTSB
- CTSD, CTSL, PSAP, GRN, CEBPA, MNDA

### Intermediate Monocytes

Description: CD14+ CD16+ pro-inflammatory monocytes with high MHC-II expression, producing cytokines upon stimulation.

Genes:
- CD14, FCGR3A, VCAN, THBS1, IL1B, NLRP3, TNF, CD74, HLA-DRA, HLA-DRB1, CD36, CCR2
- S100A8, S100A9, LYZ, CSF1R, ITGAM, ANXA1, LGALS9, TIMP1, SERPINA1, PLAUR, CLEC5A, CXCL8
- PTGS2, IL6, IL1A, CCL20, EREG, CD68

### Non-classical Monocytes

Description: CD14low CD16+ patrolling monocytes that survey endothelium and respond to viral infection.

Genes:
- FCGR3A, CX3CR1, CDKN1C, NR4A1, KLF2, LST1, IFITM3, TMEM176B, WARS, SPN, AIF1, LILRB2
- S100A4, S100A6, ITGAL, ITGAM, LYZ, CD68, CTSZ, ANXA1, PECAM1, SIGLEC10, ADGRE2, VIM
- RHOC, CSF1R, LYN, ZEB2, FGL2, LGALS3

## cd4 ctl

### CD4+ Cytotoxic Effector Memory

Description: Effector memory CD4+ T cells with cytotoxic potential, expressing granzyme K and retaining some memory markers like TCF7 and IL7R.

Genes:
- CD4, GZMK, GZMA, NKG7, CST7, CCL5, CXCR3, TBX21, TCF7, IL7R, ITGB1, CD44
- CD40LG, IFNG, TNF, LTB, GZMM, CTSW, CCR5, PRDM1, CXCR4, ICOS, PDCD1, CCL4
- CCL3

### CD4+ Cytotoxic TEMRA

Description: Terminally differentiated CD4+ T cells that re-express CD45RA and have high cytotoxic effector capacity, marked by granzyme B and perforin expression.

Genes:
- CD4, GZMB, PRF1, GNLY, FGFBP2, SPON2, TBX21, EOMES, CX3CR1, S1PR5, KLRG1, CRTAM
- NKG7, CST7, CCL5, GZMH, RUNX3, ZEB2, KLRC1, KLRD1, CD160, ITGAX, ADGRG1, PRSS23
- GZMA, CTSW, IFNG, TNF, CCL4

### CD8+ Cytotoxic T cell

Description: CD8+ T cells with cytotoxic function, highly expressing granzyme B, perforin, and NK cell-like receptors; often confused with CD4+ CTLs due to shared effector molecules.

Genes:
- CD8A, CD8B, GZMB, PRF1, GNLY, NKG7, CST7, CCL5, GZMH, FGFBP2, SPON2, TBX21
- EOMES, CX3CR1, S1PR5, KLRG1, CRTAM, RUNX3, ZEB2, KLRC1, KLRD1, CD160, ITGAX, PRSS23
- ADGRG1, GZMA, CTSW, IFNG, TNF, CCL4, CXCR3

### NK cell

Description: Innate lymphoid cells lacking T cell receptors, expressing natural cytotoxicity receptors (NCRs), KIRs, and high levels of NKG7 and granzymes; can be misannotated as T cells if CD3 information is missing.

Genes:
- NKG7, GNLY, PRF1, GZMB, KLRF1, KLRC1, KLRD1, KLRB1, NCAM1, NCR1, FCGR3A, SH2D1B
- CD244, XCL1, XCL2, CCL5, CX3CR1, TBX21, EOMES, ITGAX, CD160, PRSS23, GZMA, CTSW
- KIR2DL1, KIR2DL3, KIR3DL1, KIR3DL2, KLRC2, KLRC3, KLRK1, CD7, CD2, ADGRG1

## cd4 naive

### CD4 Central Memory (Tcm)

Description: Central memory CD4+ T cells that home to lymph nodes, expressing CCR7 and CD62L and ready for rapid differentiation.

Genes:
- GPR183, S1PR1, IL7R, CD27, CD28, CD40LG, CCR7, SELL, KLF2, ETS1, SATB1, BCL2
- CD4, CD3D, CD3E, CD247, TRAC, TRBC2, SPOCK2, RCAN3, PIK3IP1, LAT, ANKRD44, ZNF831
- DUSP5, JUNB, TCF7, LEF1, MAL, ITM2A, GIMAP5, GIMAP7, GIMAP1, GIMAP4, SH2D1A, TOB1
- RGS10, LGALS1, PTGER4, AQP3

### CD4 Naive T cell (Mature)

Description: Mature naive CD4+ T cells that have undergone peripheral homeostatic proliferation, characterized by high expression of TCF7, LEF1, and CCR7, and low CD31.

Genes:
- CD4, CD3D, CD3E, CD247, TRAC, TRBC2, CCR7, LEF1, TCF7, SELL, MAL, CAMK4
- IL7R, CD27, CD28, ITM2A, SATB1, ETS1, BCL2, SPOCK2, TSHZ2, FAM177A1, PASK, SARAF
- S1PR1, RCAN3, P2RY8, GIMAP5, GIMAP7, GIMAP1, GIMAP4, KLF2, CD40LG, PIK3IP1, ANKRD44, EVI2A
- LAT, TCF7L2, ZNF831, SAMD3

### CD4 Recent Thymic Emigrant

Description: Recent thymic emigrant CD4+ T cells newly exported from the thymus, distinguished by high expression of PECAM1 (CD31) and PTK7.

Genes:
- PECAM1, PTK7, CDKN1A, CD4, CD3D, CD3E, CD247, TRAC, TRBC2, CCR7, LEF1, TCF7
- SELL, MAL, CAMK4, IL7R, CD27, CD28, ITM2A, SATB1, ETS1, BCL2, SPOCK2, S1PR1
- RCAN3, GIMAP5, GIMAP7, GIMAP1, GIMAP4, KLF2, CD40LG, PIK3IP1, LAT, TCF7L2, ZNF831, SAMD3
- DUSP5, JUNB, LRRN3, RHOH

### CD4 Stem Cell Memory (Tscm)

Description: Stem cell memory CD4+ T cells with self-renewal capacity and high CD95 (FAS) expression, bridging naive and memory phenotypes.

Genes:
- FAS, CD4, CD3D, CD3E, CD247, TRAC, TRBC2, CCR7, SELL, TCF7, LEF1, IL7R
- CD27, CD28, BCL6, MYB, ID3, CXCR3, GPR183, KLF2, ETS1, SATB1, MAL, CD40LG
- PIK3IP1, LAT, SPOCK2, RCAN3, S1PR1, BCL2, ITM2A, GIMAP5, GIMAP7, GIMAP1, GIMAP4, ANKRD44
- ZNF831, DUSP5, JUNB, TCF7L2

### CD8 Naive T cell

Description: Naive CD8+ T cells not yet encountered antigen, marked by CD8A/CD8B and absence of effector molecules.

Genes:
- CD8A, CD8B, CD3D, CD3E, CD247, TRAC, TRBC2, CCR7, SELL, TCF7, LEF1, MAL
- CAMK4, ITM2A, SATB1, ETS1, KLF2, BCL2, CD27, CD28, IL7R, NKG7, PIK3IP1, LAT
- SPOCK2, RCAN3, S1PR1, P2RY8, GIMAP5, GIMAP7, GIMAP1, GIMAP4, ANKRD44, EVI2A, ZNF831, SAMD3
- DUSP5, JUNB, TCF7L2, LRRN3

## cd4 proliferating

### B Proliferating cell

Description: Proliferating B cells with expression of CD79A/MS4A1 and cell cycle genes.

Genes:
- CD79A, CD79B, MS4A1, CD19, PAX5, BCL11A, CD22, CD37, BANK1, IGHD, IGHM, CD24
- MKI67, TOP2A, PCNA, BIRC5, CDC20, CCNB1, CDK1, AURKA, KIF11, UBE2C, CENPF, NUSAP1
- PTTG1, RRM2, TYMS, ASPM, PBK, PLK1

### CD4 Proliferating T cell

Description: Proliferating CD4+ T cells expressing cell cycle genes and CD4 co-receptor.

Genes:
- CD4, CD3D, CD3E, CD3G, CD28, IL7R, TRAC, TRBC1, CD2, CD5, LCK, LAT
- IL2RG, MKI67, TOP2A, PCNA, BIRC5, CDC20, CCNB1, CDK1, AURKA, KIF11, UBE2C, CENPF
- NUSAP1, PTTG1, RRM2, TYMS, HMMR, ASPM, PBK, PLK1

### CD8 Proliferating T cell

Description: Proliferating CD8+ T cells characterized by cytotoxic lineage markers and cell cycle genes.

Genes:
- CD8A, CD8B, CD3D, CD3E, CD3G, CD2, LCK, LAT, GZMK, CCL5, KLRG1, MKI67
- TOP2A, PCNA, BIRC5, CDC20, CCNB1, CDK1, AURKA, KIF11, UBE2C, CENPF, NUSAP1, PTTG1
- RRM2, TYMS, HMMR, ASPM, PBK, PLK1

### Monocyte Proliferating cell

Description: Proliferating monocytes or myeloid cells marked by CD14 and S100 family genes.

Genes:
- CD14, LYZ, S100A8, S100A9, S100A12, CD68, CSF1R, FCGR3A, VCAN, CD33, ITGAM, ITGAX
- MKI67, TOP2A, PCNA, BIRC5, CDC20, CCNB1, CDK1, AURKA, KIF11, UBE2C, CENPF, NUSAP1
- PTTG1, RRM2, TYMS, HMMR, ASPM, PBK, PLK1

### NK Proliferating cell

Description: Proliferating natural killer cells expressing granzyme and perforin along with proliferation markers.

Genes:
- NKG7, GNLY, KLRF1, KLRD1, NCAM1, CD247, CD2, NCR1, PRF1, GZMB, FCGR3A, MKI67
- TOP2A, PCNA, BIRC5, CDC20, CCNB1, CDK1, AURKA, KIF11, UBE2C, CENPF, NUSAP1, PTTG1
- RRM2, TYMS, HMMR, ASPM, PBK, PLK1

## cd4 tcm

### CD4 Naive

Description: Naive CD4+ T cells that have not encountered antigen, characterized by high CCR7, SELL, and LEF1 expression, and no effector cytokines.

Genes:
- CCR7, LEF1, TCF7, SELL, IL7R, CD27, CD28, CD45RA, PTPRC, BCL2, KLF2, S1PR1
- MAL, IGF1R, CCR9, ITGB7, CD62L, SELL, CD127, IL7R, CD27, TNFSF8, LTB, HOPX
- ADCY7, CRIP1, LDHB

### CD4 TCM Tfh-like

Description: Central memory CD4+ T cells with a follicular helper phenotype, expressing CXCR5 and BCL6, and specialized in B cell help.

Genes:
- CXCR5, BCL6, ICOS, PDCD1, IL21, CXCL13, SH2D1A, MAF, IL6ST, CD200, BTLA, CD84
- SLAMF6, ASCL2, TOX2, STAT1, IRF4, BATF, TIGIT, CD28, CTLA4, CD40LG, CCR7, SELL
- TCF7

### CD4 TCM Th1-like

Description: Central memory CD4+ T cells polarized towards a type 1 helper phenotype, expressing TBX21 and CXCR3, and capable of producing IFN-γ.

Genes:
- CXCR3, TBX21, IFNG, IL18R1, CRTAM, CCR5, IL12RB2, EOMES, PRDM1, STAT4, CXCL10, CCL5
- GNLY, NKG7, KLRD1, ZBTB32, S1PR5, GZMM, XCL1, FASLG, LYAR, ADGRG1, KLRG1, LAG3
- HAVCR2

### CD4 TCM Th17-like

Description: Central memory CD4+ T cells with a Th17 polarization signature, marked by RORC, CCR6, and production of IL-17 and IL-22.

Genes:
- RORC, CCR6, IL17A, IL17F, IL22, CCL20, IL23R, CD161, KLRB1, AHR, RORA, MAF
- CCR4, IL26, CSF2, IL4I1, CTSH, FURIN, SLC4A4, TNFRSF9, IL21, CXCL13, BATF, IRF4
- STAT3

### CD4 TEM

Description: Effector memory CD4+ T cells that have lost CCR7 and SELL, and express cytotoxic molecules and tissue-homing receptors.

Genes:
- KLRG1, GZMA, PRF1, CX3CR1, CD44, CCR5, EOMES, KLRC1, NKG7, GNLY, IL2RB, IL15RA
- S1PR5, TBX21, PRDM1, FASLG, IFNG, CCL4, CCL3, ZEB2, ADGRG1, HAVCR2, LAG3, CTSW
- CST7

## cd4 tem

### CD4 Central Memory

Description: CD4+ T central memory cells expressing lymphoid homing receptors CCR7 and SELL, retaining ability to proliferate.

Genes:
- CCR7, SELL, TCF7, LEF1, GPR183, CD28, IL6ST, CD27, BACH2, SATB1, MAL, GIMAP4
- GIMAP7, IL7R, ETS1, MYC, SOCS3, RGS10, TOB1, BCL2, TSC22D3

### CD4 TEM Activated

Description: CD4+ effector memory T cells showing recent activation, with upregulated MHC class II, CD69, and pro-inflammatory cytokines.

Genes:
- HLA-DRA, HLA-DRB1, HLA-DPB1, CD74, CD38, CD69, CD40LG, IFNG, TNF, IL2, LTA, NFKBIA
- TNFAIP3, GADD45B, DUSP2, FOS, JUN, FOSB, ATF3, EGR1, IL2RA, RELB

### CD4 TEM Cytotoxic

Description: CD4+ effector memory T cells with cytotoxic potential, expressing granzymes, perforin, and chemokines.

Genes:
- GZMA, GZMH, GZMK, PRF1, NKG7, GNLY, CCL5, CST7, FGFBP2, CX3CR1, ADGRG1, KLRC1
- KLRD1, CRTAM, ZNF683, TBX21, IFNG, CCL4, HOPX, SH2D1B, APOBEC3G, CTSC, PTMS, S1PR5
- KLRF1

### CD4 TEM Resting

Description: CD4+ effector memory T cells in a quiescent state, expressing memory maintenance genes like IL7R and LTB.

Genes:
- IL7R, LTB, TXNIP, MAL, KLRB1, GIMAP4, GIMAP5, GIMAP7, ANXA1, LGALS1, S100A4, S100A6
- FYN, ARL4C, RGS1, TSC22D3, CD27, TNFRSF25, TMIGD2, LRRN3, PTGER2, ETS1

### CD8 Effector Memory

Description: CD8+ effector memory T cells with high cytotoxicity, expressing CD8A/B and granzyme B.

Genes:
- CD8A, CD8B, GZMB, KLRC2, KLRC3, KLRG1, FCRL6, B3GAT1, CD160, CRTAM, HOPX, CX3CR1
- PRF1, NKG7, GZMH, GZMM, CST7, CCL5, LAG3, TIGIT, HAVCR2, ZNF683, TBX21

## cd8 naive

### CD8 Central Memory

Description: Central memory CD8+ T cells retaining lymph node homing receptors and expressing memory-associated molecules, poised for recall responses.

Genes:
- GPR183, CCR7, SELL, CD27, CD28, IL7R, CD44, ANXA1, LTB, FYB, ITGB1, ICOS
- CTLA4, TNFRSF4, IL2RG, CXCR3, CD2, CD5, CD6, CD58

### CD8 Effector Memory

Description: Effector memory CD8+ T cells with immediate effector functions, migratory capacity to peripheral tissues, and expression of cytotoxic molecules.

Genes:
- CCL5, GZMK, KLRG1, CX3CR1, GNLY, GZMA, PRF1, NKG7, FGFBP2, EOMES, DUSP2, FOS
- JUN, FOSB, ZEB2, S1PR5, ITGAX, IL2RB, CD160, KLRF1, CST7, ADGRG1, CRTAM, GZMH

### CD8 Naive

Description: Naive CD8+ T cells expressing markers of lymph node homing and survival genes, lacking immediate effector function.

Genes:
- LEF1, TCF7, CCR7, SELL, CD27, CD28, IL7R, BACH2, TXNIP, MAL, PIK3IP1, NOSIP
- ACTN1, GRAP2, TXK, SATB1, TSHZ2, TRAT1, P2RY8, IGFBP7, ETS1, FOXP1, RASGRP1, LTB
- CD6, CD5, CD2, CD7, CD8A, CD8B

### CD8 TEMRA

Description: Terminally differentiated effector memory CD8+ T cells re-expressing CD45RA with high cytotoxic potential and NK-like receptors.

Genes:
- GZMB, PRF1, NKG7, FGFBP2, TBX21, KLRD1, KLRC1, TYROBP, FCGR3A, S1PR5, CX3CR1, KLRG1
- GZMH, GNLY, SPON2, KLRF1, ADGRG1, CRTAM, CST7, TGFBR3, FASLG, CCL3

## cd8 proliferating

### CD4+ T Proliferating

Description: Proliferating CD4+ T cells, potentially confused with CD8+ T cells if CD4 or CD8 is uncertain.

Genes:
- CD4, CD3E, CD3G, CD3D, IL7R, CCR7, SELL, LEF1, TCF7, CD27, CD28, BCL11B
- TRAT1, ANXA1, CD2, CD40LG, ICOS, MAL, SATB1, MKI67, PCNA, TOP2A, TYMS, UBE2C
- AURKB, BIRC5, PLK1, RRM2, TK1, CENPF

### CD8+ T Proliferating (Effector-like)

Description: Proliferating CD8+ T cells with an effector/TEMRA phenotype, expressing high levels of cytotoxic molecules (GZMB, PRF1).

Genes:
- GZMB, PRF1, NKG7, CST7, FGFBP2, CX3CR1, TBX21, EOMES, GZMH, GNLY, KLRD1, KLRC1
- CHST12, HOPX, AHR, SPON2, VEGFA, S1PR5, KLRF1, ADGRG1, TYROBP, FCER1G, MKI67, PCNA
- TOP2A, TYMS, UBE2C, AURKB, BIRC5, PLK1

### CD8+ T Proliferating (Memory-like)

Description: Proliferating CD8+ T cells with a memory phenotype, expressing GZMK and CD44.

Genes:
- GZMK, CD44, EOMES, KLRG1, ITGB1, LGALS1, ANXA1, CCL5, XCL1, XCL2, CD2, CD58
- CXCR3, CXCR4, IL7R, CD27, CRIP1, ARL4C, DUSP2, TNFRSF1B, MKI67, PCNA, TOP2A, TYMS
- RRM2, UBE2C, AURKB, BIRC5, PLK1, CENPF

### CD8+ T Proliferating (Naive-like)

Description: Proliferating CD8+ T cells with a naive phenotype, expressing markers like CCR7 and SELL.

Genes:
- CCR7, SELL, LEF1, TCF7, CD27, IL7R, CAMK4, NELL2, BACH2, CD28, SATB1, THEMIS
- MAL, TSHZ2, LTB, PIK3IP1, SAMHD1, MGAT4A, APBB1IP, DPP4, NOSIP, MKI67, PCNA, TOP2A
- TYMS, RRM2, UBE2C, AURKB, BIRC5, PLK1

### NK Proliferating

Description: Proliferating natural killer cells, which share cytotoxic markers with CD8+ T cells and can be misannotated.

Genes:
- NKG7, GNLY, PRF1, GZMB, KLRF1, NCR1, NCR2, NCR3, KLRD1, CD160, CD244, EOMES
- TBX21, CD7, CD2, CD38, CTSS, CHST12, HOPX, AHR, SPON2, MKI67, PCNA, TOP2A
- TYMS, UBE2C, AURKB, BIRC5, PLK1, RRM2

## cd8 tcm

### CD8 TCM

Description: Central memory CD8+ T cells that home to secondary lymphoid organs and provide long-term memory, expressing lymph node homing receptors and costimulatory molecules.

Genes:
- CCR7, SELL, LEF1, TCF7, IL7R, CD27, CD28, MAL, GPR183, PIK3IP1, RCAN3, CAMK4
- SATB1, SAMSN1, MYC, KLF2, S1PR1, CXCR3, ITGA4, CD226, TOB1, ITM2C, RGS10, CMTM6
- ANXA1

### CD8 TEM

Description: Effector memory CD8+ T cells that circulate through non-lymphoid tissues, rapidly producing effector cytokines and cytolytic molecules upon reactivation.

Genes:
- KLRG1, CX3CR1, GZMK, NKG7, CCL5, PRF1, GZMH, CST7, FGFBP2, TBX21, EOMES, ITGAL
- SPON2, PLEK, DUSP2, CD244, KLRD1, GZMA, XCL1, XCL2, HOPX, RGS1, DUSP4, JUNB
- FOSL2

### CD8 TEMRA

Description: Terminally differentiated effector memory CD8+ T cells re-expressing CD45RA with high cytotoxic capacity and expression of NK-like receptors.

Genes:
- B3GAT1, FCGR3A, GZMB, PRF1, GNLY, NKG7, CST7, CX3CR1, KLRG1, KLRD1, KLRC1, TBX21
- ZEB2, EOMES, RUNX3, ADGRG1, FGFBP2, CD244, CD160, KIR2DL1, KIR3DL1, KIR2DS4, LILRB1, SYNE1
- PLEKHF1, RAB27A

### Gamma-delta T cells

Description: Gamma-delta T cells recognizing non-peptide antigens, expressing gamma/delta TCR chains and often possessing innate-like responsiveness.

Genes:
- TRDC, TRGC1, TRGV9, TRDV2, KLRB1, SYK, GZMK, CCL5, NKG7, CST7, GZMA, GZMH
- PRF1, GNLY, TBX21, EOMES, IL2RB, CD160, KLRG1, FYB1, LAT2, LIME1

### NK cells

Description: Natural killer cells, innate lymphoid cells that mediate cytotoxicity and cytokine production, sharing cytolytic molecule expression with CD8 T cells but lacking TCR.

Genes:
- NCAM1, KLRF1, NCR1, NCR3, SH2D1B, SLAMF7, CD160, NKG7, PRF1, GZMB, GNLY, FCGR3A
- KLRD1, KLRC1, KLRB1, TYROBP, CD244, CD226, GZMA, CST7, ADGRG1, FGFBP2, S1PR5, SPON2
- MYOM2, SYNE1, KIR2DL1, KIR3DL1, KIR2DS4, LILRB1, FASLG, CCL5

## cd8 tem

### CD56dim NK cells

Description: Cytotoxic CD56dim natural killer cells, the major circulating NK subset with high antibody-dependent cellular cytotoxicity and killer immunoglobulin-like receptor expression.

Genes:
- KLRF1, NCAM1, NCR1, CD160, KIR2DL3, KIR3DL1, KIR3DL2, GNLY, PRF1, GZMB, SLAMF7, CD244
- IL2RB, KLRC1, KLRC2, KLRD1, TYROBP, HCST, CLIC3, TKTL1, PLAC8, GZMM, FCGR3A, CX3CR1
- TBX21, SPON2, CCL3, CCL4, XCL1, XCL2, B3GNT7, S1PR5

### CD8 TCM

Description: Central memory CD8+ T cells capable of long-term survival, homing to secondary lymphoid organs, and providing recall responses.

Genes:
- CCR7, LEF1, TCF7, SELL, CD27, CD28, IL7R, BCL2, MAL, SLAMF6, TXK, SATB1
- FOXO1, KLF2, PIK3IP1, SESN3, CAMK4, FLT3LG, AQP3, DUSP4, NOSIP, RGS1, RGS10, GPR183
- S1PR1, P2RY8, TNFRSF25, TRAF3IP3, MYB

### CD8 TEM

Description: Effector memory CD8+ T cells with high cytotoxic potential, expressing perforin and granzymes, poised for rapid effector function upon antigen re-encounter.

Genes:
- GZMK, GZMA, CCL5, NKG7, CST7, PRF1, GZMB, CCL4, CXCR4, ITGA1, ITGB1, CRTAM
- BCL2L11, TBX21, EOMES, KLRG1, GZMH, SLAMF7, CD160, CD244, FGFBP2, SPON2, CCL3, XCL1
- XCL2, HOPX, ADAM8, S1PR5, TYROBP, GNLY

### CD8 TEMRA

Description: Terminally differentiated CD8+ effector memory cells re-expressing CD45RA, with high expression of cytotoxic molecules and homing to peripheral tissues.

Genes:
- FCGR3A, CX3CR1, KLRG1, B3GNT7, ZNF683, TBX21, PRF1, GZMB, GZMH, NKG7, CST7, FGFBP2
- SPON2, ADGRG1, MYO1F, RASGRP1, SYNE2, PTPRC, TYROBP, GNLY, CCL3, CCL4, XCL2, S1PR5
- CTSC, S100A4

## cdc1

### CD14+ Monocyte

Description: Classical monocytes, phagocytic cells involved in inflammation and tissue repair.

Genes:
- CD14, S100A8, S100A9, LYZ, VCAN, CSF1R, CD33, ITGAM, ITGAX, FCN1, CLEC4E, CLEC5A
- CLEC7A, NLRP3, IL1B, IL1R2, CD36, FCGR1A, FCGR2A, CD4, TLR2, TLR4, CLEC12A, CLEC6A
- S100A12, C5AR1, CCR2, MMP9, LGALS2, PLBD1

### Plasmacytoid DC

Description: Plasmacytoid dendritic cells, major producers of type I interferons upon viral infection.

Genes:
- LILRA4, CLEC4C, IL3RA, NRP1, PTCRA, TCF4, IRF7, SPIB, BCL11A, GZMB, LAMP5, RUNX2
- CXCR3, CCR2, ITM2C, PLAC8, DHRS9, MZB1, SEC61G, ATP6V0C, ZEB2, BCLAF1

### cDC1

Description: Conventional dendritic cell type 1, specialized in cross-presentation and anti-viral responses.

Genes:
- THBD, CLEC9A, XCR1, IRF8, BATF3, CADM1, FLT3, ID2, WDFY4, ZNF366, SLAMF7, BTLA
- CD226, TLR3, PTPRS, RAB7B, PPM1N, ACSL1, SNX20, MYO1G, BHLHE41, WFDC1, C1orf54, PLEKHO1
- SLC38A1, DENND1B

### cDC2

Description: Conventional dendritic cell type 2, potent activators of CD4+ T cells.

Genes:
- CD1C, FCER1A, CLEC10A, SIRPA, ITGAX, ANPEP, CD33, CD2, CSF1R, CD4, TLR2, TLR4
- IL6ST, CD300A, CD300LF, DAB2, LILRB2, LILRA1, LILRA2, SIGLEC6, RNASE6, CD1A, PLD4, CCL22

## cdc2

### DC3

Description: Inflammatory CD1c+ dendritic cells co-expressing CD163 and monocyte-related genes, associated with inflammatory conditions.

Genes:
- CD163, MAFB, VCAN, ANXA2, PLBD1, THBS1, CD36, TREM2, LILRA5, SIRPA, CD9, ITGAM
- CST3, LGALS3, SPP1, IL13RA1, CCR2, MERTK, ADAM8, ADAM9, ALOX5AP, ALOX5, FCGR2A, CTSL
- CTSB

### cDC1

Description: Conventional dendritic cell type 1 specializing in cross-presentation of antigens to CD8+ T cells.

Genes:
- CLEC9A, XCR1, CADM1, THBD, BTLA, IRF8, BATF3, ID2, FLT3, TLR3, CLNK, CPVL
- C1orf54, CD226, KLRC1, KLRF1, WDFY4, SNX4, TSPAN33, PLXNC1, SLC24A4, FAM129C, ZBTB46, NDRG2
- GPR56

### cDC2

Description: Conventional dendritic cell type 2 expressing CD1c and involved in priming CD4+ T cell responses and immune regulation.

Genes:
- CD1C, CLEC10A, FCER1A, CD1E, FCGR2B, MS4A6A, HLA-DQA1, HLA-DQB1, HLA-DRB1, HLA-DRB5, ADAMDEC1, PLCG2
- LILRB2, SIRPA, PPARG, CTSH, GPR183, RAB7B, MARCH1, BIRC3, TNFAIP3, EGR1, SYT11, ARL4C
- ZNF331

### pDC

Description: Plasmacytoid dendritic cells that produce large amounts of type I interferon upon viral infection.

Genes:
- LILRA4, CLEC4C, NRP1, IRF7, TCF4, GZMB, SERPINF1, PTPRS, IL3RA, BCL11A, RUNX2, SPIB
- LAMP5, PACSIN1, PPP1R14B, ITM2C, CCDC50, MAPKAPK2, SCT, UGCG, C12orf75, DERL3, P2RY14, PLD4
- SLAMF7

## dnt

### MAIT cells

Description: Innate-like T cells restricted by MR1, recognizing microbial riboflavin metabolites, exhibiting rapid effector responses.

Genes:
- TRAV1-2, SLC4A10, KLRB1, IL18RAP, DPP4, ZBTB16, RORC, CCR6, CXCR6, CD8A, GZMA, GZMK
- PRF1, NKG7, IFNG, CD3D, CD3E, CD3G, CD247, TRAC, TRBC1, TRBC2, ICOS, CTLA4
- CD2, CD5, CD6, CD7, CXCR3, CCR5

### NK cells

Description: Cytotoxic innate lymphoid cells lacking CD3 and TCR, recognizing stressed cells via NK receptors, often confused with DN T cells due to shared cytotoxic markers.

Genes:
- NCAM1, NCR1, NCR3, KLRF1, KLRD1, KLRC1, KLRC2, KIR2DL1, KIR3DL1, GZMA, GZMB, PRF1
- NKG7, CTSW, CST7, SPON2, FCGR3A, CD7, CD2, IFNG, TGFB1, IL2RB, IL15RA, CD160
- GNLY, SH2D1B, B3GAT1, ITGAM, SLAMF7

### Vδ1 γδ T cells

Description: Tissue-resident and memory-like γδ T cells with diverse functions and a less cytotoxic, more regulatory gene signature.

Genes:
- TRDV1, IL7R, KIT, CD69, ITGAE, EOMES, TCF7, LEF1, CCR7, SELL, CD27, CD28
- BCL2, IL2RG, RORA, BCL11B, TCF7L2, CCL4, CCL3, CD3D, CD3E, CD3G, CD247, TRAC
- TRBC1, TRBC2, CD5, CD6, CD7, RGS1

### Vδ2 γδ T cells

Description: Cytotoxic innate-like T cells recognizing phosphoantigens via the Vγ9Vδ2 TCR, prevalent in peripheral blood.

Genes:
- TRGV9, TRDV2, GZMA, GZMB, GZMK, GZMM, PRF1, NKG7, CTSW, CCL5, LTB, KLRD1
- KLRF1, KLRC1, KLRK1, FCGR3A, TBX21, IFNG, CX3CR1, CXCR3, NCR3, HOPX, GZMH, CST7
- CD247, CD2, CD3D, CD3E, CD3G, CD7

## doublet

### Monocyte

Description: True monocyte, often confused with doublets due to high transcript complexity; expressed genes typical of myeloid lineage and innate immune function.

Genes:
- CD14, LYZ, S100A8, S100A9, FCN1, CST3, VCAN, S100A12, CLEC4E, MS4A6A, MNDA, CD68
- ITGAM, TLR2, CD163, CSF1R, FCGR3A, LILRB2, PILRA, CD36, CTSS, HLA-DRB1, HLA-DRA, CD74
- MPEG1, TREM1, NAMPT, MCL1, CYBB, IL1B, CCL3, CCL4, OSM, NLRP3, CXCL8, TNF
- IL6, CD33, CD300LF, ITGAX

### Monocyte-B cell doublet

Description: Doublet combining a monocyte and a B cell, characterized by co-expression of monocyte (CD14, LYZ) and B cell (CD79A, MS4A1) markers.

Genes:
- CD14, LYZ, S100A8, S100A9, FCN1, CST3, VCAN, S100A12, CLEC4E, MS4A6A, MNDA, CD68
- ITGAM, TLR2, CD163, CSF1R, FCGR3A, LILRB2, PILRA, CD36, MS4A1, CD79A, CD79B, BLNK
- PAX5, BANK1, CD19, CD22, CD40, CD72, IGHM, IGHD, IGKC, IGLC2, MZB1, JCHAIN
- TNFRSF17, VPREB3, CD24, CD27, IL4R, CXCR4, CCR7, SELL, CD83, HLA-DRA, HLA-DRB1, CD74
- CD38, CD138

### NK cell-monocyte doublet

Description: Doublet consisting of an NK cell and a monocyte, expressing NK lineage markers (NKG7, GNLY, PRF1) alongside monocyte markers (CD14, LYZ).

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMA, KLRF1, KLRD1, KLRB1, NCR1, NCR3, CD160, CD244
- KLRG1, KLRC1, KLRK1, SH2D1B, EOMES, TBX21, IFNG, TNF, CD14, LYZ, S100A8, S100A9
- FCN1, CST3, VCAN, S100A12, CLEC4E, MS4A6A, MNDA, CD68, ITGAM, TLR2, CD163, CSF1R
- FCGR3A, LILRB2, PILRA, CD36, CTSS, HLA-DRB1, HLA-DRA, CD74, MPEG1, TREM1, NAMPT, MCL1
- CYBB, IL1B

### T cell

Description: Bona fide T cell, distinguishable from T cell-containing doublets by the absence of monocyte/B cell markers; expresses core T cell lineage genes.

Genes:
- CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, CD2, CD7, LCK, ZAP70, CD4, CD8A
- CD8B, CCR7, SELL, CD27, CD28, IL7R, TCF7, LEF1, GZMK, GZMA, PRF1, NKG7
- GNLY, LTB, MALAT1, STAT4, TBX21, EOMES, IFNG, TNF, CCL5, CCL4, CXCR3, CXCR4
- HOPX, TOX, ITGAE, CD69

### T cell-B cell doublet

Description: Doublet formed by a T cell and a B cell, simultaneously expressing T cell (CD3, TRBC) and B cell (CD79A, MS4A1) lineage markers.

Genes:
- CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, CD2, CD7, LCK, ZAP70, MS4A1, CD79A
- CD79B, BLNK, PAX5, BANK1, CD19, CD22, CD40, CD72, IGHM, IGHD, IGKC, IGLC2
- MZB1, JCHAIN, TNFRSF17, VPREB3, CD24, CD27, IL4R, CXCR4, CCR7, SELL, CD83, HLA-DRA
- HLA-DRB1, CD74, CD38, CD138, FCER2, TCL1A, BCL11A, EAF2, IRF8, SPIB, KLF2, MEF2C
- POU2F2, NFKBID

### T cell-monocyte doublet

Description: Doublet arising from a T cell and a monocyte, co-expressing T cell lineage markers (CD3, TRBC) and monocyte lineage markers (CD14, LYZ, S100A8/9).

Genes:
- CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, CD2, CD7, LCK, ZAP70, CD14, LYZ
- S100A8, S100A9, FCN1, CST3, VCAN, S100A12, CLEC4E, MS4A6A, MNDA, CD68, ITGAM, TLR2
- CD163, CSF1R, FCGR3A, LILRB2, PILRA, CD36, CTSS, HLA-DRB1, HLA-DRA, CD74, MPEG1, TREM1
- NAMPT, MCL1, CYBB, IL1B, CCL3, CCL4, OSM, NLRP3, CXCL8, TNF, IL6, CD33
- CD300LF, ITGAX

## eryth

### Early Erythroblast (Basophilic)

Description: Basophilic erythroblasts actively synthesizing hemoglobin, with high expression of globin genes and heme biosynthesis enzymes.

Genes:
- HBA1, HBA2, HBB, HBD, HBG1, HBG2, AHSP, ALAS2, FECH, BLVRB, SLC4A1, GYPA
- GYPB, YIPF1, NUPR1, TFRC, CA1, CA2, ANK1, EPB42, SPTA1, SPTB, TNS1, ADD2
- ALAD, HMBS, UROD, TXNIP

### Erythroid Progenitor (CFU-E/Proerythroblast)

Description: Earliest committed erythroid progenitors expressing stem cell markers and erythroid transcription factors, with low hemoglobin expression.

Genes:
- KIT, CD34, GATA1, TAL1, LMO2, KLF1, MYB, GFI1B, SPI1, CD44, TFRC, EPOR
- FLT3, CD38, HOXB4, HHEX, ETV6, MECOM, RUNX1, ANKRD44, CD164, FAM178B, SMIM1, RHD
- SLC4A1

### Late Erythroblast (Polychromatic/Orthochromatic)

Description: Late-stage erythroblasts undergoing enucleation, enriched in erythroid membrane and cytoskeletal proteins, and high globin expression.

Genes:
- GYPA, GYPB, GYPE, SLC4A1, EPB42, SPTA1, SPTB, ANK1, RHD, RHAG, ICAM4, CD47
- XK, KLF1, AHSP, HBB, HBA1, HBA2, BLVRB, FECH, ALAS2, CA2, CA1, NUPR1
- YIPF1, TMOD1, SELENBP1, TXNIP

### Megakaryocyte/Platelet

Description: Megakaryocytic and platelet lineage cells, potentially confused due to shared hematopoietic origin, expressing hemostatic factors and platelet markers.

Genes:
- PF4, PPBP, GP1BA, GP9, ITGA2B, ITGB3, SELP, VWF, CLEC1B, GP6, F13A1, MPL
- THPO, GATA1, NFE2, RUNX1, PTGS1, ALOX12, TREML1, NRGN, MYL9, ACTA2, TUBB1, PDGFB
- PECAM1, CD9

## gdt

### IL17_gdT

Description: IL-17-producing γδ T cells, often Vδ1+, characterized by expression of IL17A, RORC, and chemokine receptor CCR6.

Genes:
- TRDV1, TRGV4, IL17A, IL17F, IL22, RORC, CCR6, KLRB1, KIT, IL23R, IL1R1, PTGDR
- IL7R, DPP4, ITGAE, CD69, CD44, ANXA1, LGALS1, S100A4, S100A6, S100A11, ID2, NFKBID
- BCL2A1, CCL20, IL26, CCR4, CCR10, AHR

### MAIT_cells

Description: Mucosal-associated invariant T cells with semi-invariant TCR α chain (TRAV1-2/TRAJ33) and expression of KLRB1, ZBTB16, and IL18R1.

Genes:
- TRAV1-2, TRAJ33, TRBV20-1, TRBV6-1, SLC4A10, KLRB1, IL18R1, IL18RAP, ZBTB16, RORC, CCR6, CXCR6
- DPP4, CD27, CD44, CD69, CD101, CD82, ITGAE, GZMA, GZMK, PRF1, NKG7, GNLY
- IFNG, TNF, CCL20, IL17A, IL22, CCR5, CXCR3

### NK_cells

Description: Natural killer cells that share cytotoxic molecules with γδ T cells but are distinguished by expression of NCRs, FCGR3A, and KIRs, without TCR transcripts.

Genes:
- NCR1, NCR2, NCR3, KLRF1, KLRC1, KLRD1, B3GAT1, FCGR3A, NCAM1, IL2RB, KIR2DL1, KIR2DL3
- KIR3DL1, KIR3DL2, CD244, CD226, CD96, TIGIT, CRTAM, PRF1, GZMB, GZMA, NKG7, GNLY
- SPON2, CCL5, XCL1, XCL2, FGFBP2, TWIST1

### cytotoxic_gdT

Description: Cytotoxic Vδ2+ γδ T cells that express high levels of granzymes, perforin, and NK cell receptors, capable of IFN-γ and TNF production.

Genes:
- TRDV2, TRGV9, NKG7, GNLY, PRF1, GZMB, GZMA, GZMH, KLRD1, KLRC1, KLRK1, KLRF1
- CD96, CD244, CRTAM, NCR3, IFNG, TNF, CCL5, CX3CR1, ZBTB16, EOMES, TBX21, RUNX3
- FGFBP2, CST7, KLRG1, CD160, S1PR5, SPON2

## hspc

### Common myeloid progenitor

Description: Common myeloid progenitors giving rise to myelomonocytic and erythro-megakaryocytic lineages.

Genes:
- MPO, ELANE, CTSG, PRTN3, AZU1, GATA1, KLF1, NFE2, AHSP, HBA1, HBB, GYPA
- ITGA2B, GP1BA, GP9, PF4, PPBP, VWF, RUNX1, GATA2, SPI1, CEBPA, CEBPE, IRF8
- KIT, CD34, CD38, LYN, HCK, FCER1G, TAL1, LMO2

### Hematopoietic stem cell

Description: Quiescent, self-renewing hematopoietic stem cells with multi-lineage potential.

Genes:
- HLF, MLLT3, SPINK2, HOPX, CRHBP, AVP, CD34, GATA2, MECOM, MYCT1, MEIS1, MSI2
- ID1, PROM1, PRNP, TGFBI, EGFL7, LMO2, RUNX1, TAL1, LYL1, BCL11A, FLI1, ERG
- HEY1, TEK, ESAM, ANGPT1, KIT, THY1

### Multipotent progenitor

Description: Multipotent progenitors primed for lymphoid and myeloid differentiation.

Genes:
- FLT3, DNTT, LEF1, IL7R, SELL, CXCR4, CD74, HLA-DRA, SPI1, CEBPA, GATA1, CD44
- KIT, ITGA6, ITGB3, CD34, RUNX1, GATA2, LYN, NOTCH1, MYB, MYC, FOXO1, BCL2
- MCL1, CCR7, IL6R, IFITM1

### Plasmacytoid dendritic cell

Description: Plasmacytoid dendritic cells specialized in antiviral responses through type I interferon production.

Genes:
- IL3RA, CLEC4C, TCF4, IRF7, IRF8, TLR7, TLR9, LILRA4, NRP1, PTCRA, SCT, BCL11A
- SEC61B, SERPINF1, GZMB, LAMP5, PLD4, SIGLEC6, CLEC2D, CD2, CD7, ITGAX, ITM2C, TCF7L2
- RUNX2, SPIB, CXCR3, CCR7, TCN2, FCER1A

### Pre-B cell

Description: B cell progenitors expressing early B lineage factors and recombination machinery, present at low frequencies in PBMC.

Genes:
- CD19, CD79A, CD79B, VPREB1, IGLL1, RAG1, RAG2, DNTT, CD24, PAX5, EBF1, TCF3
- LYN, BLK, CD22, CD72, CD37, MS4A1, IL7R, MEF2C, LEF1, CXCR4, CD38, CD27
- CD43, BCL11A, SOX4, ID2

## ilc

### ILC1

Description: Innate lymphoid cells type 1 that produce IFN-gamma and contribute to type 1 immune responses against intracellular pathogens.

Genes:
- IL7R, TBX21, IFNG, KLRB1, IL18R1, CXCR3, IL12RB2, TNFRSF9, RORA, IL2RB, IL2RG, CD27
- CD7, CD69, ITGAE, CXCR6, CCR4, LYAR, KLF2, SELPLG, CST7, S1PR5, PTPRC, ICOS
- TNFRSF4

### ILC2

Description: Innate lymphoid cells type 2 that produce Th2 cytokines (IL-4, IL-5, IL-13) and are involved in allergic responses and helminth defense.

Genes:
- IL1RL1, GATA3, IL5, IL13, IL4, IL9, RORA, PTGDR2, KLRG1, AREG, IL2RB, IL2RG
- IL7R, CD7, CD52, IL17RB, HPGDS, SOCS2, MAF, BCL11B, IL1RAP, IL1R1, TGFB1, VDR

### ILC3

Description: Innate lymphoid cells type 3 that produce IL-17 and IL-22, regulate mucosal barrier integrity and response to extracellular bacteria.

Genes:
- RORC, IL23R, IL17A, IL22, KIT, CCR6, NCR2, LTA, LTB, IL1R1, IL7R, CD7
- KLRB1, CXCR5, CXCL13, TNFRSF4, IL12RB1, CSF2, IL26, TKTL1, AHR, IL17F

### NK cells

Description: Cytotoxic innate lymphoid cells that mediate antiviral and antitumor immunity through perforin-dependent killing.

Genes:
- NKG7, GZMB, PRF1, KLRF1, KLRC1, KLRD1, NCR1, NCR3, NCAM1, FCGR3A, EOMES, TBX21
- CD160, CD244, CD7, CX3CR1, SLAMF7, GNLY, SPON2, CD2, ITGB2, ITGAL, KIR2DL1, KIR2DL3
- KIR3DL1, GZMA, FGFBP2, TYROBP, LCK

## mait

### CD8_TEMRA

Description: Terminally differentiated effector memory CD8+ T cells re-expressing CD45RA, with high expression of KLRG1, CD57 (B3GAT1), and granzymes B and K, and NK-like receptors, resembling effector cells.

Genes:
- CD8A, CD8B, KLRG1, B3GAT1, GZMB, PRF1, GNLY, TBX21, EOMES, ZEB2, CX3CR1, FCGR3A
- NKG7, CTSW, CCL5, GZMA, S1PR5, FGFBP2, CCL4, HOPX, KLRC1, KIR2DL3, KIR3DL1, CD3D
- CD3E, CD7, GZMH, ADGRG1, ZNF683, TGFBR3

### MAIT_activated

Description: Activated mucosal-associated invariant T cells upregulating early activation markers CD69 and CD25 (IL2RA), along with effector molecules granzyme B, perforin, IFN-γ, and TNF, while retaining core MAIT markers.

Genes:
- KLRB1, IL18R1, ZBTB16, RORC, DPP4, CCR6, SLC4A10, GZMK, CXCR6, GPR18, CD27, GATA3
- IL7R, KLRG1, KLRC1, CTSW, NKG7, GZMA, TRAV1-2, MYO1F, ITM2C, SYNE2, SCML4, PTGDR
- SAMD3, ANXA1, HMGB2, CD69, IL2RA, HLA-DRA, GZMB, PRF1, IFNG, TNF, CD8A, CD8B
- CD38, FAS, TNFSF10

### MAIT_resting

Description: Resting mucosal-associated invariant T cells expressing canonical semi-invariant TCR Vα7.2, high CD161 (KLRB1), IL-18Rα, PLZF (ZBTB16), and chemokine receptor CCR6, typically CD8+.

Genes:
- KLRB1, IL18R1, ZBTB16, RORC, DPP4, CCR6, SLC4A10, GZMK, CXCR6, GPR18, CD27, GATA3
- IL7R, KLRG1, KLRC1, NCR3, CTSW, NKG7, GZMA, TRAV1-2, MYO1F, ITM2C, SYNE2, SCML4
- PTGDR, SAMD3, ANXA1, HMGB2, S100A4, CD8A, CD8B

### Vd2_gdT

Description: Vδ2+ γδ T cells, the predominant γδ subset in blood, expressing Vγ9 (TRGV9), Vδ2 (TRDV2), CD161, NK receptors, and effector molecules, responding to phosphoantigens.

Genes:
- TRDV2, TRGV9, CD160, KLRB1, NKG7, GNLY, GZMA, GZMB, PRF1, CX3CR1, FCGR3A, KLRG1
- KLRC1, TBX21, EOMES, ZEB2, ZNF683, CCL5, CST7, KIR2DL4, KIR3DL2, CD3D, CD3E, CD7
- TRGC1, GZMK, IFNG, TNF, CCL4, ADGRG1

### iNKT

Description: Invariant natural killer T cells restricted by CD1d, expressing the canonical Vα24-Jα18 TCR (TRAV10/TRBV25-1), very high PLZF, and innate-like cytokines, with CD4+ or double-negative phenotype.

Genes:
- TRAV10, TRBV25-1, ZBTB16, KLRB1, IL18R1, GATA3, CD4, CCR6, RORC, IL7R, CXCR6, PTGDR2
- CTSH, CAPN3, SYNE2, PLCG2, CD27, ITM2C, S100A4, ANXA1, LGALS1, VIM, PTMA, HMGB2
- MALAT1, IL4, IL13, GZMA, NKG7, CTSW, CCL5

## nk

### Adaptive NK

Description: Memory-like NK cell subset, often CD57+ and NKG2C+, arising in response to CMV infection with enhanced antibody-dependent responses.

Genes:
- KLRC2, B3GAT1, FCGR3A, PRF1, GZMB, GNLY, NKG7, KIR2DL1, KIR2DL3, KIR3DL1, KIR3DL2, CD2
- CD244, CD160, TYROBP, SH2D1B, IL2RB, CX3CR1, ZEB2, FGFBP2

### CD56bright NK

Description: Immunoregulatory NK cell subset with high cytokine production and low cytotoxicity, characterized by CD56bright, CD62L, and NKG2A expression.

Genes:
- NCAM1, KLRC1, KLRD1, SELL, CCR7, GZMK, IL7R, CD27, LTB, XCL1, XCL2, GPR183
- MYB, TCF7, LEF1, ETS1, CST7, CXCR3, CD2, CD44, ITGAX, TNF

### CD56dim NK

Description: Cytotoxic NK cell subset with high perforin, granzyme, and CD16 expression, mediating ADCC and natural killing.

Genes:
- FCGR3A, PRF1, GZMB, GZMH, GZMA, GNLY, NKG7, KLRF1, CX3CR1, CXCR1, TBX21, EOMES
- KIR2DL1, KIR2DL3, KIR3DL1, KIR3DL2, FGFBP2, ZEB2, CRYBG1, CD244, CD160, ITGB2, KLRG1, CD58
- IL2RB, CCL4, CCL5, IFNG, CTSW

### Effector CD8+ T cells

Description: Cytotoxic CD8+ T lymphocytes with high perforin, granzymes, and NK-cell receptors, functioning in adaptive immune responses.

Genes:
- CD3D, CD3E, CD3G, CD8A, CD8B, TRAC, TRBC1, GZMB, PRF1, GNLY, NKG7, KLRG1
- KLRC1, KLRD1, B3GAT1, CCL4, CCL5, IFNG, CX3CR1, CD2, GZMH, GZMA, FGFBP2, TBX21
- EOMES

### NKT cells

Description: Innate-like T cells expressing invariant TCR (Va24-Ja18) and recognizing lipid antigens via CD1d, sharing NK cell features.

Genes:
- CD3D, CD3E, CD3G, TRAC, TRBC1, NCAM1, ZBTB16, KLRB1, CD4, CD8A, GZMB, PRF1
- GNLY, NKG7, GZMK, IL7R, CXCR3, CCR6, CD27, CD44, KLRD1, KLRC1, IL2RB, CD160
- KLRF1

## nk proliferating

### CD56bright NK

Description: CD56bright NK cells are immature, cytokine-producing natural killer cells that reside primarily in secondary lymphoid tissues and are abundant in peripheral blood, expressing high levels of NCAM1 and CD62L.

Genes:
- CCL5, CCR7, CD2, CD27, CD44, CD69, CD7, CXCR3, CXCR6, GZMK, IL15RA, IL2RB
- IL2RG, IL7R, ITGA4, ITGB7, KIT, KLRB1, MYC, NCAM1, SELL, TCF7, TNFRSF1B, XCL1
- XCL2

### CD56dim NK

Description: CD56dim NK cells are mature, cytotoxic natural killer cells that mediate antibody-dependent cellular cytotoxicity and direct killing, characterized by high FCGR3A and perforin expression.

Genes:
- B3GAT1, CCL3, CCL4, CX3CR1, FCER1G, FCGR3A, FGFBP2, GNLY, GZMB, HOPX, ITGAM, KLRC1
- KLRD1, KLRF1, KLRG1, LAMP1, NKG7, PRF1, RUNX3, S100A4, S1PR5, SPON2, STMN1, SYNE1
- TBX21

### NKT cells

Description: NKT cells are a unique T lymphocyte population that co-expresses T cell receptor and NK cell markers, bridging innate and adaptive immunity, and can be mistaken for NK cells.

Genes:
- CCL5, CD2, CD247, CD3D, CD3E, CD3G, CD4, CD44, CD7, CXCR3, EOMES, GNLY
- GZMA, IFNG, IL2RB, IL2RG, IL7R, ITGA4, ITGB7, KLRB1, NKG7, TBX21, TRAC, TRBC2
- ZBTB16

### Proliferating CD8+ T cells

Description: Proliferating CD8+ T cells are activated cytotoxic T lymphocytes undergoing cell division, marked by CD3, CD8, and cell cycle genes, often confused with proliferating NK cells due to shared cytolytic molecules.

Genes:
- AURKB, BIRC5, CCNA2, CCNB1, CD2, CD247, CD28, CD3D, CD3E, CD3G, CD8A, CD8B
- CDC20, CDK1, CENPF, GNLY, GZMA, GZMH, MAD2L1, MKI67, NKG7, PCNA, PLK1, PRF1
- TOP2A, TRAC, TRBC2, TUBB, TYMS

## nk_cd56bright

### CD8_T_cells

Description: CD8+ T lymphocytes expressing CD3, CD8 chains, and T cell receptor, capable of cytotoxic function upon antigen recognition.

Genes:
- CD3D, CD3E, CD3G, CD8A, CD8B, TRAC, TRBC2, CD28, CD27, LCK, LAT, ITK
- ZAP70, CD5, CD6, CD7, GZMK, PRF1, NKG7, KLRG1, CX3CR1, CCR7, SELL, IL7R
- IFNG, TNF, CCL4, CCL5, GZMA, GNLY, EOMES, TBX21, CD2

### NK_CD56bright

Description: CD56bright natural killer cells with high proliferative and cytokine-producing capacity, low cytotoxicity, and expression of NKG2A, CD62L, and IL-7R.

Genes:
- NCAM1, SELL, IL7R, KIT, KLRC1, GZMK, XCL1, XCL2, CCL4, CCL3, MYC, EOMES
- TCF7, LEF1, TNFRSF4, CD44, ITGA4, ITGB1, CXCR3, CCR7, KLRD1, IL2RB, IL15RA, TNFSF10
- IFNG, TNF, CD2, CD7, KLRB1, RGS1

### NK_CD56dim

Description: CD56dim natural killer cells representing the major cytotoxic NK population with high ADCC activity, expressing CD16, KIRs, and granzymes.

Genes:
- FCGR3A, PRF1, GZMB, GZMA, GNLY, NKG7, CST7, KLRF1, KLRG1, KIR2DL1, KIR2DL3, KIR3DL1
- KIR3DL2, LILRB1, TBX21, CX3CR1, ITGAL, S1PR5, CRIP1, AKR1C3, LGALS1, ADGRE5, KIR2DL4, KIR2DS1
- KIR2DS2, KIR2DS4, CD160, FGFBP2, SPON2, CLIC3

## pdc

### ASDC

Description: Axl+SIGLEC6+ dendritic cells with overlapping features of pDC, cDC2, and monocytes.

Genes:
- AXL, SIGLEC6, CD22, CD33, CCR7, LAMP3, CD40, CD83, CD86, BCL2A1, ID3, TGFB1
- IL15, FLT3, ZBTB46, IRF4, CSF2RA, IL3RA, CLEC10A, CD1C, FCER1A, CD14, CD163, SLC11A1
- VCAN, FCGR3A, ITGAM, CD68, LGALS3, LGALS1, EMP1, ANPEP, CD36

### cDC1

Description: Conventional type 1 dendritic cells specialized in cross-presentation and CD8+ T cell priming.

Genes:
- CLEC9A, XCR1, CADM1, BTLA, CD226, THBD, BATF3, IRF8, ID2, ZBTB46, FLT3, C1orf54
- WDFY4, CLNK, CYTH4, SNX3, AP1S3, TAP1, TAP2, PSMB8, PSMB10, HLA-DPA1, HLA-DQA1, HLA-DRA
- CD74, LGALS2, SMIM5, STX11, CPVL, BRI3, PRDX1, NDUFA4L2

### cDC2

Description: Conventional type 2 dendritic cells that promote CD4+ T cell responses and express CD1c and FCER1A.

Genes:
- CD1C, FCER1A, CLEC10A, CD1A, CD1B, CD1E, SIRPA, CCL17, CCL22, IRF4, NOTCH2, KLF4
- FLT3, ZBTB46, CSF1R, LILRB2, LILRA2, LILRB1, CD14, CD163, MRC1, CD36, ITGAX, ITGAM
- CST3, CTSB, CTSD, CTSL, GPNMB, TREM2, CD300LF, IL13RA1, IL4I1

### pDC (CD2+)

Description: Activated plasmacytoid dendritic cells expressing CD2 and CD5 with higher immunogenic potential.

Genes:
- CD2, CD5, CD300A, CD80, CD86, CD83, CCR7, IL7R, ICOS, CD38, SLAMF7, SLAMF1
- CD40, CD274, CCL17, CCL22, CXCL10, IFIT1, IFIT2, IFIT3, ISG15, MX1, OAS1, IFITM1
- IRF7, STAT1, STAT2, IFI44L, IFI6, RSAD2, TNFSF10, CCL3, CCL4, XCL1

### pDC (CD2-)

Description: Resting plasmacytoid dendritic cells with high expression of TCF4 and low activation markers.

Genes:
- CLEC4C, NRP1, IL3RA, LILRA4, TCF4, RUNX2, BCL11A, SPIB, IRF7, IRF8, GZMB, PPP1R14B
- MAP1A, SERPINF1, ITM2C, MZB1, DERL3, SEC61B, SPCS3, PLD4, LAMP5, GNG11, SCT, PTCRA
- CCDC50, LYN, BLNK, CD300LG, PLEK, SLC15A4, TLR7, TLR9, CIITA

## plasmablast

### Memory B cell

Description: Antigen-experienced B cells expressing CD27 and MS4A1 (CD20), lacking plasmablast/plasma cell transcription factors PRDM1 and XBP1, poised for recall responses.

Genes:
- MS4A1, CD27, CD24, BANK1, FCRL5, PAX5, BACH2, CCR7, SELL, CD40, TNFRSF13B, CD79A
- CD79B, CD22, CD72, CD83, AICDA, BATF, CD19, CR2, CD1C, SPIB, BCL11A, TCF4
- IRF8, POU2F2, EBF1, GPR183, CXCR5, CD200, IGHG1, IGLC2

### Plasma cell

Description: Terminally differentiated, long-lived antibody-secreting cells with higher expression of SDC1 (CD138) and CXCR4, retaining ER stress and UPR features.

Genes:
- SDC1, TNFRSF17, CD38, CXCR4, XBP1, PRDM1, IRF4, MZB1, DERL3, SEC11C, SSR4, FKBP11
- PDIA4, HSP90B1, PPIB, JCHAIN, IGHA1, IGHG1, IGHG2, IGLC2, IGKC, CD27, SLAMF7, POU2AF1
- ITGA4, EAF2, ELL2, HERPUD1, CRELD2, MANF, SSR2, DNAJB11, HSPA5, P4HB, LMAN1, SEC24D
- SEC23B, SAR1B, CTSC, LAPTM5

### Plasmablast

Description: Antibody-secreting cells characterized by high expression of endoplasmic reticulum stress and unfolded protein response genes, producing immunoglobulins without extensive proliferation.

Genes:
- MZB1, XBP1, PRDM1, IRF4, DERL3, SEC11C, SSR4, FKBP11, PDIA4, HSP90B1, PPIB, SDF2L1
- TXNDC5, JCHAIN, IGHA1, IGHG1, IGHG2, IGLC2, IGKC, CD27, CD38, TNFRSF17, SLAMF7, POU2AF1
- ITGA4, SDC1, EAF2, ELL2, HERPUD1, CRELD2, MANF, SSR2, DNAJB11, HSPA5, P4HB, LMAN1
- SEC24D, SEC23B, SAR1B

### Proliferating Plasmablast

Description: Actively dividing plasmablasts that co-express cell cycle genes alongside unfolded protein response and immunoglobulin secretory machinery.

Genes:
- MKI67, TOP2A, PCNA, BIRC5, CDK1, CCNB1, CCNB2, CCNA2, AURKB, BUB1, UBE2C, CENPF
- NUSAP1, KIF11, ASPM, CENPE, TPX2, CDC20, STMN1, HMMR, MZB1, XBP1, PRDM1, IRF4
- DERL3, SEC11C, SSR4, FKBP11, PDIA4, HSP90B1, PPIB, JCHAIN, IGHA1, IGHG1, IGLC2, IGKC
- CD27, CD38, TNFRSF17, SLAMF7

## platelet

### Activated Platelet

Description: Platelets showing transcriptional signatures of activation, degranulation, and cytoskeletal rearrangement.

Genes:
- SELP, CD63, SPARC, TSPAN9, GNA15, RGS18, ACTN1, MYH9, TLN1, FLNA, PLEK, VCL
- GPX1, PRDX2, TXN, HSPA5, HSPA8, SLC3A2, LAMP2, CD151, CD9, PECAM1, ITGB1, ITGAV
- TGFB1, MMP2, TIMP1, SERPINE1, CCL5, ALOX12

### Megakaryocyte

Description: Large nucleated platelet precursors often confused with platelets but distinguishable by higher expression of nuclear transcription factors and adhesion molecules.

Genes:
- VWF, GP1BA, ITGA2B, GP9, PF4, PPBP, TUBB1, CLEC1B, GATA1, ZFPM1, NFE2, RUNX1
- FLI1, MAFB, MPL, CXCR4, PECAM1, CD63, TYROBP, FCER1G, LILRB2, LILRA6, ITGB3, GP5
- GP6, TSPAN9, CD151, CD9, CD36, HLA-A

### Resting Platelet

Description: Inactive circulatory platelets expressing high levels of platelet-specific genes and lacking activation markers.

Genes:
- PF4, PPBP, GP9, ITGA2B, ITGB3, GP1BA, GP5, TUBB1, CLEC1B, CLU, F13A1, TIMP3
- RGS10, PTGS1, TREML1, GNG11, SDPR, HIST1H2AC, CAVIN2, MPP1, MYL9, NRGN, ODC1, GP6
- LY6G6F, PEAR1, PTCRA, CMTM5, P2RY12, GAS2L1, TUBA4A, SNCA, CD36

## treg

### Activated CD4+ T cells (non-Treg)

Description: Conventional CD4+ T cells recently stimulated, producing effector cytokines and cytotoxic molecules, often confused with Tregs due to shared activation markers.

Genes:
- IL2, IFNG, TNF, CD40LG, CCL3, CCL4, CCL5, XCL1, CD69, CD38, HLA-DRA, HLA-DRB1
- CD74, CD83, ICAM1, CD44, CXCR3, CCR5, CXCR6, IL21, IL4, IL13, GZMA, GZMK
- PRF1

### Effector Treg

Description: Highly suppressive Tregs that have undergone full activation, equipped with an array of immunomodulatory molecules and poised for rapid effector function.

Genes:
- FOXP3, IL2RA, CTLA4, TIGIT, ICOS, TNFRSF18, ENTPD1, NT5E, HLA-DRA, CD74, BATF, IRF4
- MAF, IL10, LAG3, HAVCR2, CD38, CD69, CCR4, CCR8, IL1R2, PTGER2, PTGER4, GITR
- TNFRSF4

### Follicular helper T cells (Tfh)

Description: Specialized CD4+ T cells that provide help to B cells in germinal centers, circulating forms of which can resemble Tregs phenotypically.

Genes:
- CXCR5, PDCD1, ICOS, BCL6, MAF, IL21, CXCL13, BTLA, CD200, CD40LG, SLAMF6, SH2D1A
- TOX, TOX2, BATF, IRF4, STAT1, STAT3, IL6ST, IL2RA, CD69, CD38, HLA-DRA, CD74
- CCR7

### Memory Treg

Description: Antigen-experienced Tregs that recirculate through peripheral tissues, expressing high levels of inhibitory receptors and homing molecules for non-lymphoid sites.

Genes:
- CD44, TIGIT, CTLA4, ICOS, TNFRSF18, ENTPD1, NT5E, HLA-DRA, HLA-DRB1, CD74, CCR6, CXCR3
- GZMK, PDCD1, LAG3, TNFRSF4, TNFRSF9, CD38, CD69, CCR4, CCR8, IL1R2, IL1RL1, PTGER2
- PTGER4

### Naive Treg

Description: Resting Tregs that have not yet encountered their cognate antigen, characterized by lymph node homing markers and high expression of transcription factors maintaining quiescence.

Genes:
- CCR7, SELL, TCF7, LEF1, CD27, IL7R, BACH2, KLF2, S1PR1, MAL, ADRB2, SOCS3
- BCL2, LTB, RGS10, CD28, ITGB7, NOSIP, AES, LRRN3, PTPRC, TSC22D3, ARHGAP45, CREM
- FOXP1

