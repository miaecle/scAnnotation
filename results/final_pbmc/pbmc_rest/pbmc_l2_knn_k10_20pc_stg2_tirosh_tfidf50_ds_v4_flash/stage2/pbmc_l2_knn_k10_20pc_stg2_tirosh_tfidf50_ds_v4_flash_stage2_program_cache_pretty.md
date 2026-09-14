# Stage-2 Precomputed Programs

- tissue: PBMC
- n_program_genes: 50
- n_cached_cell_types: 31

## asdc

### ASDC

Description: AXL+ SIGLEC6+ dendritic cells (ASDC), a distinct DC subset with both myeloid and plasmacytoid features, expressing high levels of AXL, SIGLEC6, and CD1c.

Genes:
- AXL, SIGLEC6, CD1C, FCER1A, CLEC10A, CD1E, CD1A, CD1B, LST1, GPR157, PRSS2, LGALS2
- CLEC4A, CLEC4C, IL3RA, TCF4, PACSIN1, LILRA4, SERPINF1, PLD4, TLR9, TLR7, IRF8, IRF4
- ZEB2

### CD14+ Monocytes

Description: CD14+ classical monocytes expressing high levels of CD14, CD16, and CSF1R, with roles in phagocytosis and inflammation.

Genes:
- CD14, FCGR3A, CSF1R, CD16, CD64, CCR2, CX3CR1, CD11b, ITGAM, CD163, CD68, MARCO
- MSR1, CD36, LRP1, CTSL, CTSB, LYZ, S100A8, S100A9, S100A12, VCAN, FPR1, FPR2
- TLR2, TLR4, IL1B, TNF, IL6, CXCL8

### cDC2

Description: Conventional dendritic cell type 2 (cDC2) expressing CD1c, FCER1A, and CLEC10A, involved in antigen presentation and T-cell activation.

Genes:
- CD1C, FCER1A, CLEC10A, CD1E, CD1D, ITGAX, CD33, CD11C, FSCN1, CCR7, CD40, CD86
- HLA-DRA, HLA-DRB1, CLEC4A, LAMP3, CCL22, CCL17, IL1B, IL6, TNF, CXCL8, CD207, CLEC9A
- XCR1

### pDC

Description: Plasmacytoid dendritic cells (pDC) specialized in type I interferon production, expressing CLEC4C (CD303), LILRA4, and TCF4.

Genes:
- CLEC4C, LILRA4, TCF4, PACSIN1, SERPINF1, PLD4, TLR9, TLR7, IRF8, IRF4, ZEB2, IL3RA
- CD123, CD303, CD304, BCL11A, SPIB, RUNX2, E2-2, TCF4, PTGDR2, CXCR3, CCR5, CCR9
- CLEC9A

## b intermediate

### B intermediate

Description: An intermediate B cell population representing a transitional state between naive and memory B cells, expressing high levels of CD24, CD38, and CD21.

Genes:
- CD27, CD24, CD38, CR2, FCER2, CD40, CD72, CD74, MS4A1, CD79A, CD79B, PAX5
- EBF1, CD19, CD22, IGHD, IGHM, CXCR5, IL4R, TNFRSF13C, TNFRSF13B, CD1D, CD21, CD23
- CD72

### B memory

Description: Memory B cells that have undergone class switching and affinity maturation, expressing CD27 and CD38, and lacking surface IgD.

Genes:
- CD27, CD38, CD24, BCL6, CIITA, ITGAX, CD11c, CD19, MS4A1, CD79A, CD79B, PAX5
- EBF1, CD20, CD22, CD40, TNFRSF13B, TNFRSF13C, BACH2, MEF2B, POU2AF1, POU2F2, IRF4, XBP1
- SDC1

### B naive

Description: Naive B cells that have not yet encountered antigen, characterized by high expression of IgD and IgM, and lacking CD27.

Genes:
- IGHD, IGHM, SELL, CCR7, FCER2, CR2, CD19, MS4A1, CD79A, CD79B, PAX5, EBF1
- CXCR5, CD22, CD20, CD21, CD23, CD24, CD40, IL4R, TNFRSF13C, TNFRSF13B, CD1D, TCL1A
- RNASE6

### Classical monocyte

Description: Classical monocytes are phagocytic cells that circulate in blood, expressing high levels of CD14 and CD16, and are part of the innate immune system.

Genes:
- CD14, FCGR3A, CD33, CD68, CCR2, CSF1R, ITGAM, LYZ, S100A8, S100A9, CD86, TREM1
- TLR2, TLR4, CD11b, CD16, CD163, MERTK, SIGLEC1, CTSS, CTSD, F13A1, CD300E, CCL2
- CXCL8

## b memory

### Atypical memory B cells

Description: CD11c+ T-bet+ memory B cells often expanded in autoimmune diseases and infections, with low CD21 expression.

Genes:
- ITGAX, TBX21, FCRL5, FCRL3, SLC38A1, CXCR3, CD19, MS4A1, CD27, CD24, CD86, CD21
- CD83, TNFRSF1B, BCL2, BCL6, BCL2A1, TNFAIP3, NFKB1, NFKB2, REL, RELA, IKBKB, CHUK
- IKBKG, TLR7, TLR9, MYD88, IRAK1, IRAK4, TRAF6, TICAM1, TICAM2

### Naive B cells

Description: Mature B cells that have not yet encountered antigen, expressing IgM and IgD, with high CD21 and CD23.

Genes:
- IGHD, IGHM, TCL1A, CR2, FCER2, IL4R, CD72, CD24, CD19, MS4A1, CD79A, CD79B
- PAX5, BACH2, IRF8, SPIB, BCL6, BCL2, CD38, CD40, TNFRSF13C, SELL, CCR7, CXCR5
- CD21, PTPRC, BCL11A, EBF1, CD22, CD180

### Plasmablasts

Description: Short-lived antibody-secreting cells derived from activated B cells, characterized by high CD38 and CD138, and low CD20.

Genes:
- CD38, SDC1, XBP1, PRDM1, IRF4, JCHAIN, MZB1, SLAMF7, CD27, CD19, MS4A1, CD79A
- CD79B, IGHG1, IGHA1, IGHM, IGHJ, IGLC, IGKC, PTPRC, CD28, CD44, CD62L, CXCR4
- CCR10, TNFRSF17, TNFRSF13B, TNFRSF13C, AICDA, BCL2, BCL2L1, MCL1, MYC, HSP90B1, HSPA5, PDIA4
- DERL3, UGGT1, EDEM1, EDEM2, EDEM3, SEL1L, SYVN1, HERPUD1, ATF4, ATF6, XBP1, ERN1
- EIF2AK3, PPP1R15A

### Switched memory B cells

Description: Memory B cells that have undergone class-switch recombination, expressing IgG, IgA, or IgE, and are CD27+ IgD-.

Genes:
- CD27, CD24, CD83, CD86, COCH, NOSIP, BANK1, CXCR5, SELL, CD40, TNFRSF13B, TNFRSF13C
- TNFSF8, ICAM1, LTB, PTPN22, MAP4K1, SLC2A5, PIM2, SH3BGRL2, TRAF3, TNFAIP3, BCL2, BCL6
- BCL2L1, MYB, IRF8, SPIB, PAX5, CD19, MS4A1, CD79A, CD79B

### Unswitched memory B cells

Description: Memory B cells that retain IgM and IgD, typically CD27+ IgD+, and are involved in T-independent responses.

Genes:
- CD27, IGHD, IGHM, CD24, CD19, MS4A1, CD79A, CD79B, TCL1A, CR2, FCER2, IL4R
- CD72, BACH2, PAX5, IRF8, SPIB, BCL6, BCL2, MAPK1, PTPRC, CD40, TNFRSF13C, CD83
- CD86, SELL, CXCR5, CCR7, CD38, CD21

## b naive

### B memory

Description: Memory B cells expressing CD27 and class-switched immunoglobulins, providing anamnestic responses.

Genes:
- MS4A1, CD79A, CD79B, CD27, CD40, CD80, CD83, TCF4, BCL6, AIM2, IGHA1, IGHG1
- CD22, CXCR5, BCL11A, SPIB, PAX5, EBF1, CD19, CR2, BACH2, CD72, BLK, FCRL4
- FCRL5, SWAP70, P2RX5, TNS3, STAP1, HLA-DQA1, HLA-DQB1, HLA-DRA, CD74, JCHAIN

### B naive

Description: Naive B cells expressing surface IgM and IgD, with high levels of CD20 and naive markers.

Genes:
- MS4A1, CD79A, CD79B, IGHD, FCER2, IL4R, TCL1A, CD22, CXCR5, PTPN1, BCL11A, SPIB
- PAX5, EBF1, VPREB3, CD19, CR2, BACH2, CD72, BLK, FCRL1, FCRL2, FCRL3, FCRL4
- FCRL5, SWAP70, P2RX5, TNS3, STAP1, HLA-DQA1, HLA-DQB1, HLA-DRA, CD74

### CD4+ naive T

Description: Naive helper T cells expressing CD4, CD62L, and CCR7, responsible for adaptive immune responses.

Genes:
- CD3E, CD4, SELL, CCR7, LEF1, TCF7, IL7R, CD27, CD28, PECAM1, KLF2, CAMK4
- MYC, FOXP1, BCL11B, TCF12, IKZF1, IKZF2, IKZF3, CD5, CD6, CD96, THEMIS, SGK1
- ZNF831, MAL, RGS1, TOX, GATA3, STAT5A, STAT5B

### CD8+ naive T

Description: Naive cytotoxic T cells expressing CD8, CD62L, and CCR7, capable of differentiating into effector cells.

Genes:
- CD3E, CD8A, CD8B, SELL, CCR7, LEF1, TCF7, IL7R, CD27, CD28, PECAM1, KLF2
- CAMK4, MYC, FOXP1, BCL11B, TCF12, IKZF1, IKZF2, IKZF3, CD5, CD6, CD96, THEMIS
- SGK1, ZNF831, MAL, RGS1, TOX, EOMES, TBX21

### Plasma cell

Description: Terminally differentiated B cells secreting antibodies, characterized by high CD38 and expression of XBP1.

Genes:
- SDC1, MZB1, XBP1, PRDM1, CD38, JCHAIN, IGHG1, IGHA1, IGHM, IGKC, IGLC, SEC61B
- DERL3, HERPUD1, PDIA4, PDIA6, HSP90B1, HSPA5, CRELD2, SEL1L, EDEM1, SYVN1, BIRC3, CD79A
- CD79B, MS4A1, CD19, CD27

## cd14 mono

### Classical monocytes

Description: Classical CD14++ monocytes are highly phagocytic and express high levels of CD14 and pro-inflammatory cytokines, serving as the predominant monocyte subset in peripheral blood.

Genes:
- CD14, FCGR1A, S100A8, S100A9, LYZ, CCL3, CCL4, CST3, CTSS, MNDA, CD33, CSF1R
- CEBPB, VCAN, FTH1, TCF4, MPEG1, CD68, AIF1, CXCL8, IL1B, TNF, NFKB1, IREB2
- MSRB1, CD163, CD163L1, PLAUR, TPM2, ACTB, GAPDH, HPRT1, B2M, RPLP0, PPIA, PGK1
- ENO1, LDHA, TKT, TALDO1, G6PD

### Intermediate monocytes

Description: Intermediate CD14++CD16+ monocytes exhibit a pro-inflammatory profile with high antigen presentation capacity and are expanded in inflammatory conditions.

Genes:
- CD14, FCGR3A, HLA-DRA, HLA-DRB1, CD86, ITGAM, ITGAX, CCR2, CX3CR1, TLR4, TLR2, IL6
- IL10, CCL2, CCL7, CCL8, CCL13, CXCL1, CXCL2, CXCL3, CXCL5, IL1RN, TNFAIP3, NFKBIZ
- JUN, FOS, EGR1, ATF3, DUSP1, SOCS3, PPP1R15A, GADD45B, IER3, RGS1, RGS2, RGS16
- ZFP36, TRAF1, BCL3, NFKBIE

### Myeloid dendritic cells (cDC2 - CD1c+)

Description: CD1c+ myeloid dendritic cells are potent antigen-presenting cells that express CD1c and FCER1A, and are specialized in activating CD4+ T cells.

Genes:
- CD1C, FCER1A, CLEC10A, CD209, CD1E, CD1A, CD1B, CD1D, CLEC4A, CLEC4C, CLEC7A, CLEC11A
- CLEC12A, CLEC14A, CLEC18A, CLEC2B, CLEC4D, CLEC4E, CLEC5A, CLEC6A, CLEC9A, ITGAX, ITGAM, CD86
- HLA-DRA, HLA-DRB1, HLA-DQB1, HLA-DPB1, HLA-DMA, HLA-DMB, CD40, CD80, CCR7, CCL17, CCL22, CXCL16
- FLT3, IRF4, IRF8, ZBTB46, BATF3, ID2, TCF4, SPI1, CEBPA, CEBPB, MAFB, MAF

### Non-classical monocytes

Description: Non-classical CD14+CD16++ monocytes patrol the vasculature, express low levels of CD14, and are involved in wound healing and antiviral responses.

Genes:
- FCGR3A, CX3CR1, ITGAL, ITGB2, CDKN1C, LST1, AIF1, KCTD12, SIGLEC10, FOLR3, RPS6, PABPC1
- EIF4G2, EIF4A1, EIF3E, RPL7, RPL10, RPS3, RPS4X, RPS5, RPS6, RPS9, RPS12, RPS15
- RPS16, RPS18, RPLP0, RPL3, RPL4, RPL6, RPL8, RPL9, RPL11, RPL12, RPL13, RPL15
- RPL18, RPL19, RPL21, RPL23, RPL27, RPL28, RPL30, RPL31, RPL32, RPL34, RPL35, RPL36
- RPL37, RPL38

### Plasmacytoid dendritic cells

Description: Plasmacytoid dendritic cells are specialized in type I interferon production in response to viral infections and express high levels of IL3RA and CLEC4C.

Genes:
- IL3RA, CLEC4C, TCF4, IRF7, IRF8, SPIB, EBF1, PAX5, PTPRC, CD123, HLA-DRA, HLA-DRB1
- HLA-DQB1, HLA-DPB1, HLA-DMA, HLA-DMB, CD86, CD40, CD80, CCR7, CCL17, CCL22, CXCL10, CXCL11
- CXCL9, IFIH1, DDX58, TLR7, TLR9, MYD88, IRAK1, IRAK4, TRAF6, NFKB1, RELA, JUN
- FOS, ATF2, CREB1, STAT1, STAT2, STAT3, STAT4, STAT5A, STAT5B, STAT6, IRF1, IRF2
- IRF3, IRF5, IRF6, IRF9

## cd16 mono

### CD14+ Monocyte (Classical)

Description: Classical monocytes expressing high levels of CD14, with strong phagocytic and antimicrobial functions.

Genes:
- CD14, LYZ, S100A8, S100A9, S100A12, FCN1, CST3, CTSS, CD68, FOS, JUN, NFKBIA
- TNFAIP3, IL1B, TNF, CCL3, CCL4, CCL2, CXCL8, PLBD1, LST1, RPS11, RPS12, RPS18
- RPL13A, RPL32, RPS27A, RPL37, RPL38, RPS29

### CD16+ Monocyte (Non-classical)

Description: Non-classical monocytes expressing high levels of FCGR3A (CD16) and low levels of CD14, involved in patrolling and pro-inflammatory responses.

Genes:
- FCGR3A, MS4A7, LILRB2, LST1, RHOC, CDKN1C, CFD, HES4, C1QA, CTSD, CTSS, FCER1G
- IFITM3, TNF, CX3CR1, S100A12, S100A8, S100A9, LYPD2, MYO1F, NCF1, NCF2, NCF4, RAC2
- RPS6, TYROBP, FOSB, JUNB, EGR1, DUSP1

### Intermediate Monocyte (CD14+CD16+)

Description: Intermediate monocytes co-expressing CD14 and CD16, bridging classical and non-classical monocytes with roles in inflammation and antigen presentation.

Genes:
- CD14, FCGR3A, MS4A7, LILRB2, LYZ, S100A8, S100A9, S100A12, FCN1, CST3, CTSS, CD68
- TNF, IL1B, CCL3, CCL4, CX3CR1, MYO1F, NCF1, NCF2, RAC2, FOSB, JUNB, EGR1
- DUSP1, LYPD2, CFD, HES4, C1QA, CTSD

### Natural Killer (NK) Cell

Description: Natural killer cells expressing NKG7 and granzymes, with cytotoxic function and CD16-mediated antibody-dependent cellular cytotoxicity.

Genes:
- NKG7, GZMB, GZMA, PRF1, KLRD1, KLRB1, KLRF1, KLRC1, KLRK1, CD247, CD3E, CD3D
- CD2, FCGR3A, NCAM1, NCR1, NCR3, TYROBP, FGFBP2, CCL5, CX3CR1, XCL1, XCL2, GNLY
- SPON2, TRDC, TRGC2, SH2D1B, WARS

### Plasmacytoid Dendritic Cell (pDC)

Description: Plasmacytoid dendritic cells expressing CLEC4C (BDCA-2) and IL3RA (CD123), specialized in type I interferon production in response to viral infections.

Genes:
- CLEC4C, IL3RA, LILRA4, TCF4, BCL11A, IRF4, IRF7, IRF8, SPIB, IL7R, CD2AP, MPEG1
- GZMB, SERPINF1, PLD4, SCL25A, SPCS3, TGFBI, PTPRS, FAM46C, TNFRSF9, CD226, BEX3, SAMD9
- RAB7B, LAMP5, PPP1R14A, RGS13, PTGER4, AP1S3

## cd4 ctl

### CD4 CTL

Description: CD4+ cytotoxic T lymphocytes that express both CD4 and a range of cytotoxic molecules such as granzymes and perforin.

Genes:
- CD4, GZMA, GZMB, GZMH, GZMK, GZMM, PRF1, GNLY, NKG7, KLRD1, KLRB1, KLRK1
- KLRC1, KLRC2, KLRG1, CTSW, CST7, CCL4, CCL5, CX3CR1, FGFBP2, LAG3, IFNG, TNF
- FASLG, CD70, CD40LG, EOMES, TBX21, ZNF683, HOPX, ID2, ID3

### CD8 CTL

Description: CD8+ cytotoxic T lymphocytes expressing CD8, granzymes, and perforin, specialized for killing infected cells.

Genes:
- CD8A, CD8B, GZMA, GZMB, GZMK, GZMH, PRF1, GNLY, NKG7, KLRD1, KLRB1, KLRK1
- KLRC1, KLRC2, KLRG1, CCL4, CCL5, CX3CR1, FGFBP2, EOMES, TBX21, ZNF683, IFNG, TNF
- FASLG, CTSW, CST7, MYO7A, PRDM1, RUNX3

### NK cells

Description: Natural killer cells expressing CD16 and CD56, with potent cytotoxic activity and without prior sensitization.

Genes:
- FCGR3A, NCAM1, KIR2DL1, KIR2DL2, KIR2DL3, KIR3DL1, KIR3DL2, NCR1, NCR3, NCR2, CD244, CD226
- KLRC1, KLRC2, KLRD1, KLRK1, NKG7, GNLY, PRF1, GZMB, GZMA, GZMH, GZMK, CST7
- CTSW, IFNG, TNF, IL2RB, IL18R1, IL12RB2, ZEB2, EOMES, TBX21, TCF7

### NKT cells

Description: Invariant natural killer T cells that co-express T cell receptor and NK cell markers, recognizing lipid antigens via CD1d.

Genes:
- CD3D, CD3E, KLRB1, NKG7, GNLY, PRF1, GZMB, GZMA, GZMK, GZMH, CST7, CTSW
- IFNG, TNF, FASLG, CCL4, CCL5, CD4, ZBTB16, IL18R1, IL12RB2, ID2, EOMES, TBX21
- RUNX3, STAT4, CD27, CD28

### γδ T cells

Description: Gamma-delta T cells expressing γδ T cell receptor, bridging innate and adaptive immunity with rapid cytotoxic responses.

Genes:
- TRGC1, TRGC2, TRDC, TRDV1, TRDV2, CD3D, CD3E, KLRK1, NKG7, GNLY, PRF1, GZMB
- GZMA, GZMK, CST7, CTSW, IFNG, TNF, CCL4, CCL5, EOMES, TBX21, RUNX3, STAT4
- IL7R, CD27, CD28, KLRB1

## cd4 naive

### CD4+ Central Memory T cell

Description: Central memory CD4+ T cells expressing CCR7 and CD45RO, with high ANXA1 and LGALS3.

Genes:
- CCR7, IL7R, ANXA1, LGALS3, CD44, KLRB1, CD28, CD27, PTPRC, CD4, CD3E, CD3D
- CD3G, CD247, LEF1, TCF7, MAL, FOXP1, BACH2, SATB1, TXNIP, BTG2, MYC, KLF2
- BCL2, AKT1, FOXO1, JUN, FOS, EGR1

### CD4+ Effector Memory T cell

Description: Effector memory CD4+ T cells lacking CCR7, expressing KLRG1 and cytolytic molecules like GZMA and IFNG.

Genes:
- KLRG1, GZMA, GZMB, GZMK, EOMES, TBX21, IFNG, PRF1, NKG7, CST7, CCL5, CD44
- CD27, IL7R, CD4, CD3E, CD3D, CD3G, CD247, PTPRC, FASLG, GZMH, GZMM, GNLY
- KLRD1, KLRK1, KLRC1, KLRC2, KIR2DL4, KIR3DL1

### CD8+ Naive T cell

Description: Naive CD8+ T cells with high expression of CD8A, CD8B, and CCR7, SELL, and IL7R.

Genes:
- CD8A, CD8B, CD8B2, CD28, CD27, IL7R, CCR7, SELL, LEF1, TCF7, MAL, PTPRC
- CD3E, CD3D, CD3G, CD247, FOXP1, BACH2, SATB1, TXNIP, BTG2, MYC, KLF2, BCL2
- AKT1, FOXO1, JUN, FOS, EGR1, DUSP1

### Naive CD4+ T cell

Description: Quiescent CD4+ T cells expressing CD45RA and CCR7, with high expression of IL7R and SELL, and lacking effector molecules.

Genes:
- CCR7, SELL, LEF1, TCF7, IL7R, MAL, PTPRC, CD4, CD3E, CD3D, CD3G, CD247
- FOXP1, BACH2, SATB1, TXNIP, BTG2, MYC, KLF2, BCL2, AKT1, FOXO1, JUN, FOS
- EGR1, DUSP1, ZFP36, SPOCK2, RGCC, LMNA

### Recent thymic emigrant (RTE) CD4+

Description: Recent thymic emigrant subset of naive CD4+ T cells expressing CD31 (PECAM1) and high levels of PTK7.

Genes:
- PECAM1, PTK7, CXCR4, CD4, CCR7, SELL, IL7R, LEF1, TCF7, MAL, FOXP1, BACH2
- SATB1, TXNIP, BTG2, MYC, KLF2, BCL2, AKT1, FOXO1, JUN, FOS, EGR1, DUSP1
- ZFP36, SPOCK2, RGCC, LMNA, CD3E, CD3D

## cd4 proliferating

### CD4 Memory

Description: Antigen-experienced CD4+ T cells that provide rapid recall responses, expressing IL7R and homing to lymph nodes and tissues.

Genes:
- IL7R, S100A4, ANXA1, GPR183, TNFRSF4, CD44, SPOCK2, FNIP1, LAG3, BACH2, CTLA4, ICOS
- TIGIT, PDCD1, FASLG, CD40LG, CXCR5, BCL6, TOX2, MYO1E, PTPN22, SLC2A3, NCF1, VAV2
- DUSP6

### CD4 Naive

Description: CD4+ T cells that have not encountered antigen, characterized by high expression of SELL and CCR7, recirculating through lymph nodes.

Genes:
- SELL, CCR7, TCF7, LEF1, CD27, CD28, MAL, KLF2, ACTN1, PIK3IP1, IL7R, FOXO1
- PDE3B, LDHB, TRAV1-2, TRBV9, AQP3, FBXO7, S100A10, PPP1R14B, ARL4C, SELPLG, CD55, C2ORF88
- TSPAN5

### CD4 Regulatory

Description: Immunosuppressive CD4+ T cells that express FOXP3 and CD25, maintaining self-tolerance and controlling immune responses.

Genes:
- FOXP3, IL2RA, CTLA4, IKZF2, TNFRSF18, TNFRSF4, LAIR2, LAG3, TIGIT, IL10, TGFB1, ENTPD1
- NT5E, CD74, SOCS2, BATF, IRF4, MYO1E, SATB1, FOSL2, ETS1, ZNF331, LAMP2, RAB27A
- GZMB

### CD8 Proliferating

Description: Proliferating CD8+ cytotoxic T cells undergoing cell division, marked by high expression of MKI67 and STMN1, often expanding during immune responses.

Genes:
- MKI67, STMN1, CD8A, CD8B, GZMK, GZMH, NKG7, CCL5, CST7, PRF1, GNLY, HLA-DRA
- HLA-DRB1, CD38, BIRC5, TYMS, TOP2A, CENPF, NUSAP1, RRM2, PCNA, CDK1, CCNB1, AURKB
- PLK1

### NK cells

Description: Innate lymphoid cells that kill infected or transformed cells without prior sensitization, expressing NKG7 and cytotoxic granules.

Genes:
- NKG7, GNLY, PRF1, GZMB, KLRD1, NCR1, KLRF1, KIR2DL1, KIR2DL3, KIR3DL1, IL2RB, FCGR3A
- CD16, CD56, NCAM1, XCL1, XCL2, SH2D1B, SLAMF7, KLRC1, KLRC2, KLRK1, ZEB2, TBX21
- EOMES

## cd4 tcm

### CD4 Naive

Description: Naive CD4+ T cells are antigen-inexperienced, express high levels of CD45RA and lymph node homing receptors, and have limited effector function.

Genes:
- CCR7, SELL, LEF1, TCF7, FOXP1, IKZF2, MAL, GIMAP4, GIMAP7, GPR183, KLF2, S1PR1
- PTPRC, CD3D, CD3E, CD3G, CD4, LCK, ZAP70, LAT, ITK, PRKCA, CAMK4, NFATC1
- NFATC2, JUN, FOS, CCR9, CD45RA, CD62L, CD27, CD28, CCR4, CCR6, CXCR3, CXCR4
- CXCR5, IL2RA, IL7R, IL2RG, STAT5A, STAT5B, MYC, BACH2, BTLA, CD40LG, ICOS, TNFRSF4
- TNFRSF8, TNFRSF9, TNFRSF18

### CD4 TCM

Description: CD4+ central memory T cells express lymph node homing markers (CCR7, SELL) and have memory function with high proliferative capacity.

Genes:
- IL7R, SELL, CCR7, BCL2, CD28, FOXP1, LEF1, TCF7, IKZF2, MAL, GIMAP4, GIMAP7
- GPR183, KLF2, S1PR1, PTPRC, CD3D, CD3E, CD3G, CD4, LCK, ZAP70, LAT, ITK
- PRKCA, CAMK4, NFATC1, NFATC2, JUN, FOS

### CD4 TEM

Description: CD4+ effector memory T cells are antigen-experienced, lack lymph node homing molecules, and produce effector cytokines such as IFN-γ and TNF.

Genes:
- GZMA, GZMK, PRF1, IFNG, TNF, CCL5, CCL4, CCL3, XCL1, XCL2, KLRB1, KLRG1
- NKG7, FGFBP2, GNLY, S100A4, S100A6, S100A10, S100A11, ANXA1, ANXA2, ANXA3, ANXA5, ANXA6
- ANXA7, ANXA8, ANXA9, ANXA10, ANXA11, ANXA13, ANXA14, ANXA15, ANXA16, ANXA17, ANXA18, ANXA19
- ANXA20, ANXA21, ANXA22, ANXA23, ANXA24, ANXA25, ANXA26, ANXA27, ANXA28, ANXA29, ANXA30, ANXA31
- ANXA32, ANXA33

### CD8 TCM

Description: CD8+ central memory T cells are antigen-experienced, express lymph node homing markers, and have memory function with proliferative potential.

Genes:
- IL7R, SELL, CCR7, BCL2, CD28, FOXP1, LEF1, TCF7, IKZF2, MAL, GIMAP4, GIMAP7
- GPR183, KLF2, S1PR1, PTPRC, CD3D, CD3E, CD3G, CD8A, CD8B, LCK, ZAP70, LAT
- ITK, PRKCA, CAMK4, NFATC1, NFATC2, JUN, FOS, EOMES, TBX21, PRDM1, KLF1, KLF3
- KLF4, KLF5, KLF6, KLF7, KLF8, KLF9, KLF10, KLF11, KLF12, KLF13, KLF14, KLF15
- KLF16, KLF17

### Treg

Description: Regulatory T cells suppress immune responses and express FOXP3, high levels of CD25, and inhibitory molecules like CTLA4.

Genes:
- FOXP3, IL2RA, CD25, CTLA4, TIGIT, IKZF2, IKZF4, TNFRSF4, TNFRSF18, TNFRSF9, CD39, ENTPD1
- GITR, LAG3, PDCD1, CD274, ICOS, CD28, TGFB1, IL10, IL35, EBV, IL2RB, IL2RG
- STAT5A, STAT5B, STAT3, SMAD3, SMAD7, SOCS1, SOCS3, CISH, PIM1, PIM2, PIM3, FOXO1
- FOXO3, FOXO4, BACH2, HELIOS, NRP1, CCR4, CCR6, CCR7, CCR8, CCR9, CXCR3, CXCR4
- CXCR5, CXCR6

## cd4 tem

### CD4 TEM Th1

Description: CD4+ effector memory T cells polarized toward Th1, characterized by expression of IFN-γ, TBX21, and CXCR3, involved in cell-mediated immunity.

Genes:
- TBX21, IFNG, CXCR3, CCR5, STAT4, IL12RB2, HLA-DRB1, CCL5, GZMK, PRDM1, EOMES, RUNX3
- CD38, KLRG1, CXCL10, IL18R1, IL12RB1, TNF, LTB, LTA, FASLG, GZMA, GZMH, CCL4
- CCL3, CXCL9, STAT1, IRF1, HLA-DRA, CD69

### CD4 TEM Th17

Description: CD4+ effector memory T cells polarized toward Th17, characterized by expression of IL-17A, RORC, CCR6, and IL-23R, involved in neutrophil recruitment and autoimmune inflammation.

Genes:
- RORC, IL17A, IL17F, CCR6, CCL20, IL23R, STAT3, IRF4, AHR, CD161, KLRB1, IL22
- IL26, CSF2, IL1R1, IL6R, TGFB1, TNF, LTA, LTB, CCL3, CCL4, CST7, GZMB
- FASLG, CD40LG, ICOS, EBI3, IL12A, IL17RA

### CD4 TEM Th2

Description: CD4+ effector memory T cells polarized toward Th2, characterized by expression of IL-4, IL-5, IL-13, GATA3, and CCR4, promoting humoral and allergic responses.

Genes:
- GATA3, IL4, IL5, IL13, CCR4, CCR8, STAT6, IL10, IL2, CSF2, CD200, TNFSF4
- IL1RL1, IL17RB, IL25, CCL17, CCL22, IL9, IL6, CTSC, MAF, IRF4, BATF, ETS1
- MYB, CD27, CD28, ICOS, OX40, TRAF1

### CD4 TEM Treg

Description: CD4+ effector memory regulatory T cells, characterized by FOXP3, CD25, and CTLA4 expression, suppressing immune responses and maintaining self-tolerance.

Genes:
- FOXP3, IL2RA, CTLA4, TNFRSF18, IKZF2, IKZF4, ENTPD1, NT5E, LRRN3, FOXP3, TIGIT, CD27
- CD28, IL10, TGFB1, CCR4, CCR8, STAT5A, STAT5B, TNFSF4, BATF, IRF4, MYB, ETS1
- IL2, IL4, IL13, MIR155, CTLA4, ICOS

### CD8 TEM

Description: CD8+ effector memory T cells, cytotoxic lymphocytes expressing granzymes, perforin, and IFN-γ, targeting infected or malignant cells.

Genes:
- CD8A, CD8B, GZMK, GZMH, GZMA, GZMB, PRF1, NKG7, CCL5, CCL4, CCL3, CXCR3
- CCR5, TBX21, EOMES, KLRK1, KLRD1, KLRC1, KLRG1, FASLG, IFNG, TNF, LTA, LTB
- HLA-DRB1, CD69, CD38, CD27, CD28, CD44

### NK cells

Description: Natural killer cells, innate lymphoid cells with cytolytic activity, expressing NKG7, perforin, and granzymes, involved in early defense against tumors and viruses.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMA, GZMH, KLRD1, KLRC1, KLRK1, NKG2D, CD94, KLRC2
- KLRC3, KIR2DL1, KIR2DL2, KIR3DL1, CD16, FCGR3A, CD56, NCAM1, CX3CR1, CCL5, CCL4, CCL3
- IFNG, TNF, LTA, IL2RB, IL12RB2, EOMES

## cd8 naive

### CD4 Naive

Description: Naive CD4+ T cells that circulate through lymph nodes and differentiate into helper T cell subsets upon activation.

Genes:
- CD4, CCR7, SELL, LEF1, TCF7, IL7R, CD27, CD28, BCL2, MAL, FOXP1, LDHB
- KLF2, S1PR1, FOXO1, CD3D, CD3E, CD3G, ZAP70, LCK, ITK, SH2D1A, TNFRSF4, TNFRSF18
- IKZF2, IKZF3

### CD8 Memory

Description: Memory CD8+ T cells with cytotoxic potential and expression of chemokine receptors, enabling rapid response to secondary infections.

Genes:
- GZMK, GZMA, GZMH, PRF1, GNLY, NKG7, CCL5, CXCR3, KLRG1, EOMES, TBX21, ZEB2
- S1PR1, IL32, IFNG, CD69, HLA-DRA, CD44, ITGA1, MYO1F, ANKRD11, SYNE1, F11R, JAK3
- STAT4

### CD8 Naive

Description: Naive CD8+ T cells expressing CCR7 and CD45RA, responsible for lymph node homing and long-term persistence.

Genes:
- CCR7, LEF1, TCF7, SELL, CD27, CD28, IL7R, BCL2, MAL, FOXP1, LDHB, KLF2
- S1PR1, FOXO1, EOMES, CAMK4, IGFBP4, TXK, ITGA6, LMNA, PHLDA1, CD8A, CD8B

### NK cells

Description: Natural killer cells that mediate innate cytotoxicity through secretion of perforin and granzymes, and express activating receptors.

Genes:
- NKG7, GNLY, PRF1, GZMB, FGFBP2, CLIC3, KLRD1, KLRK1, NCR1, NCR3, FCGR3A, CTSW
- ADGRG1, KLRB1, CD247, SPON2, NCAM1, GZMA, GZMH, CCL3, CCL4, CCL5, CSF1, XCL1
- XCL2

## cd8 proliferating

### CD4 Proliferating

Description: Proliferating CD4+ T cells with high expression of cell cycle and proliferation markers (MKI67, TOP2A) along with CD4 and CD3 complex genes, often confused with CD8 Proliferating.

Genes:
- MKI67, TOP2A, PCNA, TYMS, STMN1, CD4, CD3D, CD3E, CD3G, UBE2C, CENPF, BIRC5
- AURKA, AURKB, CCNB1, CCNB2, CDC25C, PLK1, KIF11, KIF23, KIF20A, NUSAP1, DLGAP5, HMMR
- CKS1B, CKS2, RRM2, TK1, DHFR, TYMS, FOXM1, MYBL2, E2F1, E2F2, E2F8, CDKN3
- GINS2, SKA1, SKA3, SPC25, MAD2L1, MELK, PBK, NEK2, TTK, TPX2, PRC1, KIFC1

### CD8 Effector Memory

Description: CD8+ effector memory T cells expressing cytotoxic molecules (GZMK, GZMB, PRF1) and chemokines (CCL5) with a memory-associated phenotype.

Genes:
- GZMK, GZMB, PRF1, NKG7, CCL5, CD8A, CD8B, CD3D, CD3E, CD3G, KLRK1, KLRC1
- KLRD1, KLRB1, EOMES, TBX21, ZEB2, HOPX, CX3CR1, FASLG, IFNG, IL2RB, IL7R, CD44
- CD27, CCR5, CCR7, SELL, TCF7, LEF1, BCL2, MAL, GZMA, GZMH, CTSW, CST7
- FGFBP2, SPON2, GNLY, TNF, TNFRSF9, CD69, HLA-DRB1, HLA-DQA1, HLA-DPA1, HLA-DRA

### CD8 Naive

Description: Naive CD8+ T cells characterized by high expression of homing markers CCR7, SELL, and transcription factors TCF7, LEF1, with low cytotoxic molecule expression.

Genes:
- CCR7, SELL, TCF7, LEF1, CD8A, CD8B, CD3D, CD3E, CD3G, IL7R, CD27, BCL2
- MAL, FOXP1, SOX4, KLF2, ETS1, MYC, BACH2, SATB1, CD28, CD5, CD6, CD96
- ITGA4, ITGB1, CXCR4, CD62L, CARD11, S1PR1, KLRG1, GPR183, PTPRC, CD45RA, CD45RO, CD95
- CD58, CD2, CD7, CD27, CD28, CD127

### CD8 Proliferating

Description: Proliferating CD8+ T cells with high expression of cell cycle and proliferation markers (MKI67, TOP2A) along with CD8 and CD3 complex genes.

Genes:
- MKI67, TOP2A, PCNA, TYMS, STMN1, CD8A, CD8B, CD3D, CD3E, CD3G, UBE2C, CENPF
- BIRC5, AURKA, AURKB, CCNB1, CCNB2, CDC25C, PLK1, KIF11, KIF23, KIF20A, NUSAP1, DLGAP5
- HMMR, CKS1B, CKS2, RRM2, TK1, DHFR, TYMS, FOXM1, MYBL2, E2F1, E2F2, E2F8
- CDKN3, GINS2, SKA1, SKA3, SPC25, MAD2L1, MELK, PBK, NEK2, TTK, TPX2, PRC1
- KIFC1

### NK

Description: Natural killer cells expressing cytotoxic granules (NKG7, GNLY, PRF1) and various killer cell lectin-like receptors, with high expression of FCGR3A (CD16).

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMA, GZMH, KLRD1, KLRC1, KLRK1, KLRB1, NCR1, NCR3
- FCGR3A, CD160, CD244, CD226, CD96, TIGIT, ITGA2, ITGAL, ITGB2, CX3CR1, CXCR1, CXCR2
- FGFBP2, SPON2, CTSW, CST7, PRSS23, AREG, IFNG, TNF, TNFRSF9, CD69, HLA-DRB1, HLA-DPA1
- HLA-DRA, IL2RB, IL12RB1, IL15RA, IL18R1, KLRC2, KLRC3, KIR2DL1, KIR2DL2, KIR3DL1, KIR3DL2

## cd8 tcm

### CD4 TCM

Description: Central memory CD4+ T cells; provide helper functions and express lymph node homing markers.

Genes:
- CD4, CCR7, SELL, CD27, CD28, IL7R, TCF7, LEF1, MAL, BCL11B, CD3D, CD3E
- CD40LG, IL2RA, FOXP1, FYB1, LDHB, LITAF, CD5, CD6, LCK, ITK, THEMIS, PTPN22
- S1PR1

### CD8 Naive

Description: Naive CD8+ T cells; antigen-inexperienced, express lymph node homing receptors and lack effector molecules.

Genes:
- CCR7, SELL, CD27, CD28, IL7R, TCF7, LEF1, MAL, BCL11B, CD5, CD6, CD8A
- CD8B, CD3E, CD3D, LCK, ITK, THEMIS, PTPN22, LDHB, LITAF, S1PR1, MIR21, IL2RG
- BCL2, MCL1

### CD8 TCM

Description: Central memory CD8+ T cells; express lymph node homing markers (CCR7, SELL) and retain proliferative capacity.

Genes:
- CCR7, SELL, CD27, CD28, IL7R, TCF7, LEF1, MAL, BCL11B, CD3D, CD3E, CD8A
- CD8B, LCK, ZAP70, ITK, MYC, STAT5A, EOMES, LDHB, LITAF, CD5, CD6, THEMIS
- PTPN22, S1PR1, MIR21, IL2RG, BCL2, MCL1

### CD8 TEM

Description: Effector memory CD8+ T cells; exhibit immediate cytotoxic functions and express granzymes and perforin.

Genes:
- GZMB, GZMA, GZMK, PRF1, GNLY, NKG7, CX3CR1, KLRG1, FGFBP2, CCL5, CST7, CCL4
- EOMES, TBX21, ZEB2, HOPX, ID2, DUSP4, MYO1F, COTL1, ACTN1, KLRK1, CD160, FCGR3A
- LAG3

### NK cells

Description: Natural killer cells; innate lymphoid cells with cytotoxic activity against infected or transformed cells.

Genes:
- NKG7, GNLY, GZMB, PRF1, KLRD1, KLRF1, KLRK1, NCR1, NCR3, CD247, CD2, FCGR3A
- NCAM1, XCL1, XCL2, CCL3, CCL4, GZMA, GZMK, CST7, SH2D1B, EOMES, TBX21, ZEB2
- HOPX

## cd8 tem

### CD8 CM

Description: CD8 central memory T cells characterized by lymph node homing and self-renewal capacity with expression of CCR7 and CD62L.

Genes:
- SELL, CCR7, IL7R, TCF7, LEF1, BCL2, CD28, CD27, IL2RA, IL2RB, CD62L, CD45RA
- CD45RO, CD95, CD122, CD127, CXCR4, CXCR5, CCR6, LEF1, FOXP1, MYB, MYC, ETS1
- KLF2, FOXO1, BACH2, STAT5B, ICOS, TNFRSF4, TNFRSF18, TNFRSF9, CD40LG, IFNG, IL2, CSF2
- LTB, TNF, CCL4, CCL3

### CD8 Naive

Description: CD8 naive T cells that are antigen-inexperienced with high expression of lymph node homing markers and transcription factors TCF7 and LEF1.

Genes:
- SELL, CCR7, IL7R, TCF7, LEF1, CCR9, CXCR3, CD28, CD27, CD62L, CD45RA, CD45RO
- CD127, KLF2, FOXO1, ETS1, MYC, BACH2, FOXP1, MYB, STAT5A, STAT5B, ICOS, TNFRSF4
- TNFRSF18, S1PR1, GPR183, CAMK4, IL7R, IL2RG, JAK3, SOS1, GRB2, PTPRC, CD3E, CD3D
- CD3G, CD8A, CD8B, CXCR4

### CD8 TEM

Description: CD8 effector memory T cells characterized by rapid cytotoxic effector functions and expression of granzymes and perforin.

Genes:
- GZMB, PRF1, NKG7, GNLY, CCL5, GZMK, GZMH, CST7, FGFBP2, KLRG1, CX3CR1, FCGR3A
- KLRD1, KLRF1, HOPX, EOMES, TBX21, ZEB2, ID2, BATF, STAT4, IL2RB, IL7R, CD69
- ITGAE, ITGAL, ITGB2, CD44, S1PR1, MYO1F, ARHGAP15, TAGAP, LAG3, PDCD1, HAVCR2, TIGIT
- CTLA4, GAPDH, ACTB, GZMA

### CD8 TEMRA

Description: CD8 terminally differentiated effector memory cells re-expressing CD45RA, with high expression of KLRG1, CD57, and potent cytotoxicity.

Genes:
- KLRG1, CD57, GZMB, PRF1, NKG7, GNLY, CCL5, FGFBP2, CX3CR1, FCGR3A, EOMES, TBX21
- ZEB2, ID2, HOPX, ARHGAP15, TAGAP, LAG3, PDCD1, HAVCR2, TIGIT, CTLA4, IL2RB, IL7R
- CD44, ITGAE, ITGAL, ITGB2, MYO1F, GZMH, GZMK, CST7, KLRD1, KLRF1, CD69, S1PR1
- STAT4, BATF, GAPDH, ACTB

### NK cells

Description: Natural killer cells characterized by expression of NKG7, GNLY, and FCGR3A, with potent cytotoxic and cytokine-producing functions.

Genes:
- NKG7, GNLY, PRF1, GZMB, FCGR3A, KLRD1, KLRF1, KLRK1, NCR1, NCR3, CD160, CD244
- CD2, CD7, CD56, NCAM1, XCL1, XCL2, CCL5, CXCR1, CXCR2, IL2RB, IL18RAP, IL18R1
- IFNG, TNF, CSF2, CCL3, CCL4, CCL3L1, CCL4L2, GZMK, GZMH, CST7, FGFBP2, HOPX
- EOMES, TBX21, ZEB2, ID2

## cdc1

### CD14+ Monocyte

Description: CD14+ classical monocytes, involved in phagocytosis and inflammatory responses.

Genes:
- CD14, FCGR3A, CSF1R, LYZ, S100A8, S100A9, S100A12, CD163, ITGAM, CCR2, CX3CR1, IDO1
- TREM1, TLR2, TLR4, CD36, CD68, FPR1, FPR2, CEBPB, MAFB, NFKB1, RELA, STAT3
- IRF1

### cDC1

Description: Conventional type 1 dendritic cells, specialized in cross-presentation of antigens to CD8+ T cells.

Genes:
- CLEC9A, XCR1, CADM1, THBD, C1orf54, BATF3, IRF8, IDO1, DNASE1L3, CPVL, SERPING1, KLRB1
- CDKN1C, BCL11B, MYCL1, MICU3, NIBAN1, SAMD10, TRDC, IL7R, CD4, CD8A, GZMK, CCR7
- LAMP3

### cDC2

Description: Conventional type 2 dendritic cells, efficient in MHC-II presentation and CD4+ T cell activation.

Genes:
- FCER1A, CD1C, CLEC10A, CD1E, CD1B, FCGR2B, CD207, IL13RA1, IRF4, ZBTB46, KLF4, CCR2
- CX3CR1, CD40, CD86, HLA-DQA1, HLA-DQB1, HLA-DRB1, CD74, CSF1R

### pDC

Description: Plasmacytoid dendritic cells, specialized in producing type I interferons in response to viral infections.

Genes:
- IL3RA, CLEC4C, LILRA4, TCF4, IRF7, IRF8, BCL11A, SPIB, PLD4, PACSIN3, LRRC26, SLC15A4
- CLIC3, CXCR3, CD303, CD304, TCF4, ZEB2, RUNX2, ID2

## cdc2

### CD14+ Monocytes

Description: CD14+ classical monocytes, phagocytic cells that can differentiate into macrophages or dendritic cells and produce inflammatory cytokines.

Genes:
- CD14, S100A8, S100A9, LYZ, FCN1, CST3, CCR2, CD33, CSF1R, FCGR1A, ITGAM, IL1B
- TNF, CTSS, CTSD, NPC2, LGALS1, LGALS3, ANXA2, HLA-DRA, CD74, PLBD1, TREM1, CLEC7A
- TLR2, TLR4, MYD88, IRAK1

### cDC1

Description: Conventional dendritic cells type 1, expressing CD141 (BDCA-3), specialized in cross-presentation and activation of CD8+ T cells.

Genes:
- CLEC9A, XCR1, THBD, CADM1, IRF8, BATF3, ID3, FLT3, IL12RB2, CCR7, CD207, CD209
- LAMP3, CCL22, IL12A, IL12B, TLR3, TLR7, TLR8, MYCL1, ZBTB46, IFIH1, DDX58, IRF7
- STAT2, NOD2, RIPK2, CARD9

### cDC2

Description: Conventional dendritic cells type 2, expressing CD1c and FcεRI, specialized in antigen presentation to CD4+ T cells.

Genes:
- CD1C, FCER1A, CLEC10A, PKIB, SERPINF1, CACNB3, SLC38A1, LDLRAD4, ENPP6, SUSD6, NIPAL1, GABBR1
- SCN9A, ZBTB46, ID2, IRF4, RAB32, GPR137B, FZD2, PLD4, ITGAX, SIGLEC6, CD97, ILDR2
- TMEM176A, TMEM176B, SPIB, SYK, BLNK

### pDC

Description: Plasmacytoid dendritic cells, major producers of type I interferons in response to viral infection, expressing CD123 and CD303.

Genes:
- IL3RA, CLEC4C, LILRA4, IRF7, IRF8, TCF4, SPIB, PTPRC, CD74, HLA-DRA, BCL11A, RUNX2
- GPR109A, VSTM1, PLAC8, IDO1, MX1, OAS1, OAS3, ISG15, IFI44, RSAD2, IFIT1, IFIT3
- LY6E, SIGLEC1, AIM2, STAT1, STAT3

## dnt

### CD8+ T cells

Description: Cytotoxic T lymphocytes expressing CD8, central to adaptive immune response against intracellular pathogens.

Genes:
- CD8A, CD8B, GZMK, GZMH, PRF1, NKG7, CCL5, GZMA, GZMM, CTSW, GNLY, FGFBP2
- CX3CR1, CD27, CD28, IL7R, EOMES, TBX21, KLRG1, CD244, MYO7A, CMC1, S1PR5, KLRC1
- KLRC2

### MAIT cells

Description: Mucosal-associated invariant T cells, an innate-like T cell subset characterized by semi-invariant TCR and high expression of CD161, involved in antimicrobial immunity.

Genes:
- KLRB1, SLC4A10, IL18R1, RORC, ZBTB16, GZMK, CCR6, CXCR6, ITGA1, ITGAE, CD69, TNFRSF9
- GPR183, LMNA, ANXA1, S1PR5, GZMA, GZMM, PRF1, CTSW, NKG7, GNLY

### NK cells

Description: Natural killer cells, innate lymphoid cells that mediate cytotoxicity against infected or malignant cells without prior sensitization.

Genes:
- NCAM1, NKG7, GNLY, PRF1, GZMB, FCGR3A, KIR2DL4, KIR3DL1, KIR2DL1, KIR3DL2, KLRD1, KLRK1
- KLRC1, KLRC2, KIR2DS4, NCR1, NCR2, NCR3, CD244, CD160, LILRB1, CX3CR1, FGFBP2, SPON2
- GZMH, GZMM, CTSW, CCL3, CCL4, XCL1, XCL2

### γδ T cells

Description: Gamma-delta T cells, a subset of T cells expressing gamma-delta T cell receptor, with roles in innate and adaptive immunity.

Genes:
- TRDC, TRGC1, TRGC2, TRDV1, TRDV2, KLRK1, KLRD1, FCGR3A, CD160, GNLY, NKG7, PRF1
- GZMB, GZMA, GZMM, CTSW, CD27, CD28, IL2RB, CX3CR1, FGFBP2, LAG3, KIR2DL4, KIR3DL1
- KLRC1, KLRC2

## doublet

### B cell

Description: Antibody-producing B lymphocyte with MHC class II expression.

Genes:
- MS4A1, CD79A, CD79B, PAX5, EBF1, BANK1, CD19, CD72, VPREB3, BLNK, IGHM, IGHD
- TCL1A, CD22, FCER2, CR2, CD74, HLA-DRA, HLA-DRB1, CD24

### CD14+ Monocyte

Description: Classical monocyte expressing CD14 and high levels of phagocytosis-related genes.

Genes:
- CD14, FCGR3A, CTSS, CSF1R, LYZ, CST3, S100A9, S100A8, VCAN, IL1B, CD68, CTSD
- PSAP, MPEG1, FTH1, FTL, CYBB, NCF2, LST1, AIF1

### CD8+ T cell

Description: Cytotoxic T lymphocyte with effector functions and granzyme production.

Genes:
- CD8A, CD8B, GZMK, GZMB, PRF1, NKG7, KLRD1, KLRC1, EOMES, TBX21, CCL5, GZMH
- GZMA, GNLY, FGFBP2, CCL4, CCL3, XCL1, XCL2, CD3D

### NK cell

Description: Natural killer cell with innate cytotoxic activity and interferon-gamma production.

Genes:
- NKG7, GNLY, PRF1, GZMB, KLRD1, KLRB1, KLRC1, KLRF1, FCGR3A, NCAM1, CD160, CD244
- XCL1, XCL2, CCL5, FGFBP2, SPON2, KLRC2, KLRK1, NCR1

### Plasmacytoid dendritic cell

Description: Type I interferon-producing dendritic cell with plasmacytoid morphology.

Genes:
- IL3RA, CLEC4C, TCF4, LILRA4, IRF7, IRF8, TLR7, TLR9, MX1, OAS1, IFIT1, IFIT3
- ISG15, SERPING1, SPIB, BCL11A, CCR7, CD68, CD123, HLA-DRA

## eryth

### Erythroblast

Description: Mature erythroblasts with high hemoglobin synthesis and enucleation markers, representing the final stage of erythroid development.

Genes:
- HBA1, HBA2, HBB, HBD, HBE1, HBG1, HBG2, CA1, SLC4A1, GYPA, GYPB, GYPE
- TFRC, ALAS2, EPB42, AHSP, SPTA1, SPTB, ANK1, ADD2, DMTN, RHAG, RHCE, KCNH2
- WDR52

### Erythroid Progenitor

Description: Early committed erythroid progenitor cells with high expression of erythroid transcription factors and transferrin receptor, precursor to mature erythroblasts.

Genes:
- GATA1, KLF1, TFRC, GYPA, AHSP, ALAS2, EPB42, SPTA1, SPTB, ANK1, ADD2, DMTN
- MPP1, ICAM4, RHAG, CA1, SLC4A1, HBA1, HBA2, HBB, HBD, HBE1, HBG1, HBG2
- BCL11A, MYB, KIT, CD34, GATA2, TAL1

### Megakaryocyte

Description: Megakaryocytic cells expressing platelet-specific markers and transcription factors regulating megakaryopoiesis, commonly confused with erythroid cells due to shared GATA1 expression.

Genes:
- PF4, PPBP, ITGA2B, ITGB3, GP1BA, GP1BB, GP5, GP6, GP9, VWF, F13A1, MPL
- PLEK, TUBB1, CLU, APOE, SPARC, SERPINE1, THBS1, PDGFA, PDGFB, HIST1H2AC, HIST1H4C, FOXP1
- FLI1, GATA1, NFE2, MEIS1, HOXA9

### Platelet

Description: Platelet fragments expressing megakaryocytic and granule marker genes, often contaminating PBMC single-cell data and confused with erythroid cells.

Genes:
- PPBP, PF4, GP9, ITGA2B, ITGB3, VWF, SELP, CLEC1B, GP1BA, GP5, F13A1, MPL
- TUBB1, SPARC, CD9, MYL9, ACTN1, TAGLN2, ARHGEF12, PTPRJ

## gdt

### CD8+ T cells

Description: CD8+ T cells are cytotoxic T lymphocytes that recognize peptide antigens presented by MHC class I, playing a central role in adaptive immunity.

Genes:
- CD8A, CD8B, CD3E, CD3D, CD3G, CD247, CD28, CD27, CCR7, SELL, TCF7, LEF1
- EOMES, TBX21, PRF1, GZMB, GZMH, GZMK, GZMM, GZMA, GNLY, NKG7, CST7, KLRG1
- KLRK1, KLRC1, KLRC2, KLRD1, NCR3, FCGR3A, FGFBP2, SPON2, CX3CR1, S1PR5, IL2RB, CCL5
- CCL4, CCL3, XCL1, XCL2, CTSW, ADGRG1, CRTAM, CD38, HLA-DRA, HLA-DRB1, MKI67, TOP2A
- BIRC5, CENPF

### MAIT cells

Description: Mucosal-associated invariant T (MAIT) cells are an innate-like T cell subset that recognizes microbial vitamin B metabolites presented by MR1, expressing CD161 and semi-invariant TCR.

Genes:
- KLRB1, CD161, TRAV1-2, TRAJ33, TRAJ12, TRAJ20, TRAJ30, TRAJ34, TRAJ38, TRAJ52, TRAV26-1, TRAV26-2
- TRBV6-1, TRBV6-2, TRBV6-3, TRBV6-4, TRBV6-5, TRBV6-6, TRBV6-7, TRBV6-8, TRBV6-9, TRBV20-1, TRBV28, TRBV29-1
- TRBV30, RORC, RORA, CCR6, IL23R, IL18R1, IL12RB1, KIT, CSF1R, GATA3, CXCR6, CD4
- CD8A, CD8B, CCL20, CCL4, CCL5, XCL1, XCL2, IFNG, TNF, IL17A, IL22, CSF2
- PRF1, GZMB, GZMK

### NK cells

Description: Natural killer (NK) cells are innate lymphoid cells that kill infected or tumor cells without prior sensitization, characterized by expression of CD56 and CD16.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMA, GZMH, GZMK, GZMM, KLRD1, KLRC1, KLRC2, KLRC3
- KLRK1, NCR1, NCR2, NCR3, FCGR3A, CD16, CD56, NCAM1, CD2, CD7, CD5, CD247
- ZAP70, TYROBP, KIR2DL1, KIR3DL1, KIR2DS1, KIR2DS2, KIR2DS4, KIR3DL2, KIR3DS1, LILRB1, LILRA1, KLRF1
- KLRJ1, SPON2, S1PR5, CX3CR1, FGFBP2, ADGRG1, CTSW, CCL5, CCL4, CCL3, XCL1, XCL2
- IL2RB, IL12RB2, IL18R1

### Vδ1 T cells

Description: Vδ1 T cells are a less abundant PBMC gamma-delta subset that often reside in tissues and exhibit regulatory and cytotoxic functions, with a naïve/memory phenotype.

Genes:
- TRDC, TRGC1, TRDV1, KLRD1, KLRB1, CD161, CD8A, CD8B, CD56, NCAM1, GZMK, GZMA
- GZMM, CCL5, CCL4, CCL3, XCL1, XCL2, IL7R, CD27, CD28, CD44, CD62L, SELL
- CCR7, TCF7, LEF1, MYC, BATF, EOMES, TBX21, ZNF683, HOPX, ID2, ID3, KLF2
- KLF6, ETS1, FLI1, RUNX3, RORA, RORC, AHR, CD96, TIGIT, LAG3, PDCD1, HAVCR2
- CTLA4, ICOS

### Vδ2 T cells

Description: Vδ2 T cells are the predominant gamma-delta T cell subset in human peripheral blood, characterized by expression of Vδ2 TCR chain and high cytotoxic activity against microbes and tumors.

Genes:
- TRDC, TRGC2, TRDV2, TRGV9, KLRD1, KLRF1, KLRJ1, PRF1, GZMB, GZMA, GZMH, GNLY
- NKG7, FCGR3A, CD16, CX3CR1, FGFBP2, SPON2, S1PR5, ZBTB16, LILRB1, KIR2DL1, KIR3DL1, KIR2DL3
- KIR2DS1, KIR2DS3, KIR2DS4, KIR3DL2, KIR3DS1, IL2RB, CCL5, CCL4, CCL3, XCL1, XCL2, CTSW
- GZMM, GZMK, GZML, ADGRG1, CRTAM, CD2, CD7, CD5, CD3E, CD3D, CD3G, CD247
- ZAP70, LCK

## hspc

### CMP

Description: Common myeloid progenitors committed to myeloid lineage (monocytes, granulocytes, erythrocytes, megakaryocytes).

Genes:
- CD33, CSF1R, IL3RA, FCGR2A, CEBPA, SPI1, MYB, MPO, AZU1, ELANE, PRTN3, CTSG
- LYZ, S100A8, S100A9, CEBPB, FCN1, CD14, CLEC12A, ITGAM, ITGAX, FCGR1A, FCGR3B, NCF1
- NCF2, CYBB, MMP9, CR1, CD68, ADGRE1

### HSC

Description: Self-renewing hematopoietic stem cells giving rise to all blood lineages.

Genes:
- CD34, PROM1, KIT, FLT3, ALCAM, CD93, ENG, THY1, ITGA6, MLLT3, HOPX, HHEX
- GATA2, RUNX1, MYB, TAL1, LMO2, GFI1, MEIS1, HOXA9, JARID2, ERG, MECOM, HLF
- ANGPT1, PROCR, KDR, FUT4, CD164, CD55

### MPP

Description: Multipotent progenitors with limited self-renewal and multilineage differentiation capacity.

Genes:
- CD34, KIT, FLT3, MME, DNTT, VPREB1, IGLL1, IL7R, DPP4, SPINK2, LTB, CYTL1
- SOX4, HMGB2, STMN1, TOP2A, MKI67, CDK1, CENPF, CKS1B, TYMS, PCNA, PCLAF, CDCA5
- NUSAP1, UBE2C, CCNA2, CCNB1, BUB1, KIF11

### Monocyte

Description: Circulating monocytes, innate immune phagocytes with pro-inflammatory and anti-inflammatory functions.

Genes:
- CD14, FCGR3A, CD68, CSF1R, CD163, CX3CR1, S100A8, S100A9, LYZ, CD33, CLEC12A, ITGAM
- ITGAX, FCGR1A, FCGR2A, FCGR3B, NCF1, NCF2, CYBB, MMP9, CR1, ADGRE1, FPR1, FPR2
- CCR2, CCRL2, CD36, MSR1, TREM2, OLR1

### Pre-B cell

Description: Early B cell progenitor undergoing immunoglobulin gene rearrangement.

Genes:
- CD19, CD79A, CD79B, VPREB1, IGLL1, DNTT, PAX5, EBF1, TCF3, IRF4, BACH2, POU2F2
- SPIB, ID3, SWAP70, BLK, CD22, CD72, CD38, MS4A1, CD37, CD52, IGHM, IGHD
- CXCR4, CD40, CD86, HLA-DRB1, CD74, HLA-DRA

## ilc

### ILC1

Description: Innate lymphoid cell type 1 involved in type 1 immunity, producing interferon-gamma and requiring T-bet.

Genes:
- IL7R, KLRB1, TBX21, IFNG, GZMB, PRF1, GNLY, NKG7, CCL5, CST7, LAMP1, FASLG
- IL12RB2, IL18RAP, CXCR3, KLRK1, NCR1, NCR3, CD247, EOMES, ID2, MYC, KLF2, RORA
- ETS1

### ILC2

Description: Innate lymphoid cell type 2 involved in type 2 immunity, producing IL-5 and IL-13, dependent on GATA3.

Genes:
- GATA3, PTGDR2, KLRG1, IL13, IL5, IL9, CRLF2, IL1RL1, IL17RB, CD200R1, AREG, CCR4
- CCR8, HPGD, PPARG, NR3C1, TCF7, BATF, IRF4, GATA1, MAF, NFIL3, TOX, PRDM1
- GADD45A

### ILC3

Description: Innate lymphoid cell type 3 involved in mucosal immunity, producing IL-22 and IL-17, dependent on RORγt.

Genes:
- RORC, IL22, IL23R, KIT, NCR2, CD96, AHR, IL1R1, IL7R, CCR6, CCR7, CD117
- GZMK, LILRA4, TNFRSF4, TNFRSF18, TNFRSF9, CD127, ID2, EOMES, ZEB2, TOB1, BCL11B, BATF
- NFIL3

### NK cells

Description: Natural killer cells, cytotoxic innate lymphocytes that kill infected or transformed cells, often confused with ILC1 due to shared markers.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMH, GZMK, KLRD1, KLRK1, NCR1, NCR3, FCGR3A, NCAM1
- CD244, CD247, KLRC1, KLRC2, KLRC3, KLRAP1, SPON2, CCL4, CCL3, XCL1, XCL2, FGFBP2
- LAG3

## mait

### CD8+ T cell

Description: Conventional cytotoxic CD8+ T cells that mediate adaptive immunity, characterized by expression of CD8A, CD8B, and effector molecules such as GZMB and PRF1.

Genes:
- CD8A, CD8B, GZMA, GZMB, GZMH, GZMK, PRF1, NKG7, GNLY, CCL5, CST7, FGFBP2
- EOMES, TBX21, ZEB2, MYBL1, KLRK1, KLRC1, KLRD1, CD27, CD28, CD3E, CD3D, CD247

### Gamma-delta T cell

Description: T cells expressing gamma-delta TCR (TRDC, TRGC1/2) that function in innate immunity, often found in tissues, and can be confused with MAIT cells due to overlapping cytotoxicity markers.

Genes:
- TRDC, TRGC1, TRGC2, GZMA, GZMM, GZMK, NKG7, GNLY, KLRB1, KLRG1, CD3E, CD3D
- CD27, CD28, CXCR3, CCR6, PRF1, CST7, FGFBP2, CCL5

### MAIT

Description: Mucosal-associated invariant T cells, a subset of innate-like T cells that express a semi-invariant TCR (TRAV1-2/TRAJ33) and recognize bacterial metabolites, characterized by high expression of KLRB1, IL18R1, and SLC4A10.

Genes:
- SLC4A10, KLRB1, IL18R1, CCR6, CXCR6, TRAV1-2, TRAJ33, RORC, ZBTB16, GPR55, NCR3, LST1
- KLRG1, GZMK, NKG7, GNLY, PRF1, GZMA, CST7, CCL5

### NKT cell

Description: Invariant natural killer T cells that recognize glycolipid antigens presented by CD1d, defined by expression of ZBTB16, TRAV10, and TRAJ18, and share some markers with MAIT cells.

Genes:
- ZBTB16, TRAV10, TRAJ18, CD1D, KLRB1, IL18R1, CCR6, CXCR6, GZMA, GZMB, PRF1, NKG7
- GNLY, RORC, GPR55, NCR3, KLRG1, CST7, CCL5, CD3E, CD3D

## nk

### CD56bright NK

Description: CD56bright NK cells are cytokine-producing, immunoregulatory NK cells with high expression of CD56, NKG2A, and CD94, and low cytotoxicity.

Genes:
- KLRC1, KLRC2, KLRC3, KLRD1, NCAM1, CD3Z, FCER1G, TYROBP, KLRB1, IL7R, GZMK, GZMB
- PRF1, CCL3, CCL4, XCL1, XCL2, SELL, KIT, IL2RB, IL12RB2, CCR7, CD62L, CD44
- CD27, CD28, CD69, CD94, NKG2A, NKG2C, NKG2D, NKG2E, NKp46, NKp30, NKp44, DNAM1
- TIGIT, 2B4, NTB-A, CRACC, CD244, CSF1, CCL5, XCL1, XCL2, GZMH, GZMA, GZMK

### CD56dim NK

Description: CD56dim NK cells are highly cytotoxic, CD16-positive NK cells that mediate antibody-dependent cellular cytotoxicity and express killer immunoglobulin-like receptors.

Genes:
- CD16, FCGR3A, KIR2DL1, KIR2DL2, KIR2DL3, KIR3DL1, KIR3DL2, KLRD1, NKG2A, NKG2C, NKG2D, GZMB
- PRF1, GZMA, GZMH, GNLY, FASLG, TNFSF10, CCL3, CCL4, CCL5, XCL1, XCL2, CST7
- CTSW, MYBL1, PTGDR2, LPXN, SPON2, KLRC1, KLRF1, KLRG1, CD57, B3GAT1, CD38, CD11b
- ITGAM, CD2, CD7, SH2D1B, TBX21, EOMES, ZEB2, ID2, NFIL3

### CD8+ TEMRA

Description: CD8+ TEMRA cells are terminally differentiated effector memory T cells re-expressing CD45RA, with high cytotoxic potential and expression of NK-like receptors.

Genes:
- CD8A, CD8B, CD3D, CD3E, CD3G, NKG7, GZMB, PRF1, GZMA, GZMH, GNLY, FASLG
- CCL5, XCL1, XCL2, CCL4, CST7, CTSW, MYBL1, SPON2, KLRC1, KLRD1, KLRG1, CD57
- B3GAT1, CD27, CD28, CD44, CD62L, SELL, CCR7, TCF7, LEF1, EOMES, TBX21, ZEB2
- ID2, RUNX3, GZMK, GZMM

### NKT cell

Description: NKT cells are a subset of T cells that co-express NK cell markers and a semi-invariant T-cell receptor, recognizing lipid antigens presented by CD1d.

Genes:
- CD3D, CD3E, CD3G, TRDC, TRGC1, TRGC2, TRDV2, KCNA3, KLRB1, NKG7, GZMB, PRF1
- GZMA, GZMH, GNLY, IFNG, IL4, IL13, CCL5, XCL1, XCL2, CCL3, CCL4, CD69
- CD38, CD56, NCAM1, CD27, CD28, CD95, FAS, TRAV1-2, TRAJ33, TRAV10, TRBV25-1, IL18RAP
- IL12RB2, ZBTB16, PLZF, TOX2, ID2, NFIL3, EOMES, TBX21, GATA3, RORC, BCL6

## nk proliferating

### CD8+ T cells (activated)

Description: Activated CD8+ T cells are cytotoxic T lymphocytes that proliferate and produce effector molecules, often confused with NK cells due to shared markers like GZMB and PRF1.

Genes:
- CD8A, CD8B, CD3D, CD3E, CD3G, GZMB, GZMK, GZMA, PRF1, GNLY, NKG7, CCL5
- CCL4, CCL3, IFNG, TNF, IL2, CD69, HLA-DRA, HLA-DRB1, CD38, CD74, CXCR3, CCR5
- CCR7, SELL, CD44, CD27, CD28, CD95, FAS, PDCD1, LAG3, TIGIT, HAVCR2, CTLA4
- ICOS, KLRG1, CD57, B3GAT1, EOMES, TBX21, RUNX3, STAT4, STAT1, IRF1, MX1, ISG15
- IFI44L

### NK CD56bright

Description: CD56bright NK cells are abundant in lymph nodes and produce abundant cytokines such as IFN-gamma and TNF-alpha, with lower cytotoxicity.

Genes:
- GZMK, XCL1, XCL2, CCL3, CCL4, KLRC1, KLRB1, IL2RB, GZMB, PRF1, KLRD1, NCAM1
- CD62L, SELL, FCGR3A, KIR2DL4, KIR3DL1, KIR2DS4, KIR2DS2, KIR3DL2, KIR2DS1, KIR2DL1, KIR2DS3, KIR2DS5
- KIR3DL3, KIR2DL5A, KIR2DL5B, KIR2DS3, KIR2DS5, KIR3DS1, KIR2DL4, KIR3DL1, KIR2DS4, KIR2DS2, KIR3DL2, KIR2DS1
- KIR2DL1, KIR2DS3, KIR2DS5, KIR3DL3, KIR2DL5A, KIR2DL5B, CD27, IL7R, TNFRSF9, TNFRSF4, CD44, CD62L

### NK CD56dim

Description: CD56dim NK cells are highly cytotoxic and constitute the majority of circulating NK cells, expressing high levels of CD16 and perforin.

Genes:
- KLRF1, PRF1, GZMB, GNLY, NKG7, KLRD1, FCGR3A, CD16, KIR2DL1, KIR2DL2, KIR2DL3, KIR3DL1
- KIR2DS1, KIR2DS2, KIR3DS1, KIR2DL4, KIR3DL2, KIR2DS4, KIR2DS3, KIR2DS5, KIR3DL3, KIR2DL5A, KIR2DL5B, CD57
- B3GAT1, LAG3, TIGIT, HAVCR2, PDCD1, CD38, CD74, HLA-DRA, HLA-DRB1, CX3CR1, NKG2C, KLRC2
- NKG2E, KLRC3, KLRG1, CD226, CD244, CD2, CD7, CD11b, ITGAM, CD18, ITGB2, CD95
- FAS

### NK Proliferating

Description: Proliferating NK cells are actively cycling, expressing high levels of cell cycle-related genes such as MKI67 and TOP2A, and are typically a small subset in PBMC.

Genes:
- MKI67, TOP2A, CENPF, BIRC5, CCNB1, CCNB2, CDK1, AURKA, AURKB, PLK1, CDC20, KIF11
- KIF23, KIF2C, KIFC1, TTK, NEK2, NUF2, NDC80, ASPM, BUB1, BUB1B, CASC5, CDCA8
- CENPA, CENPE, CENPI, CENPW, DLGAP5, ECT2, HMMR, KIF14, KNL1, MELK, NCAPG, NCAPG2
- NCAPH, NUSAP1, PRC1, RACGAP1, SGOL1, SGOL2, SKA1, SKA3, SPAG5, SPC25, STMN1, TACC3
- TPX2, TUBB

### NKT cells

Description: NKT cells are a subset of T cells that express both T cell receptors and NK cell markers, capable of rapid cytokine production and often misidentified as NK cells.

Genes:
- CD3D, CD3E, CD3G, TRBC1, TRBC2, TRAV10, TRAV20, TRAV29, TRAV36, TRDV2, TRDV3, TCRGC1
- TCRGC2, KLRB1, NKG7, GNLY, GZMB, PRF1, IFNG, IL4, IL13, CCL3, CCL4, CCL5
- XCL1, XCL2, CD56, NCAM1, CD161, KLRB1, CD94, KLRD1, NKG2A, KLRC1, NKG2C, KLRC2
- NKG2E, KLRC3, CD69, CD44, CD62L, SELL, CD27, CD28, CD95, FAS, PDCD1, GITR
- TNFRSF18, ICOS

## nk_cd56bright

### CD8_T_cell

Description: Cytotoxic T lymphocytes expressing CD8 and CD3, with T cell receptor complex genes, involved in adaptive immune response.

Genes:
- CD8A, CD8B, CD3E, CD3D, CD3G, TRAC, TRBC1, TRBC2, GZMK, GZMM, KLRG1, EOMES
- TBX21, CXCR3, CCR5, CD27, CD28, IL7R, CCR7, SELL, LEF1, TCF7, PRF1, GZMH
- NKG7

### NKT_cell

Description: Innate-like T lymphocytes that express both T cell and NK cell markers, notably KLRB1 and ZBTB16, and recognize lipid antigens via CD1d.

Genes:
- KLRB1, ZBTB16, CD3E, CD3D, CD3G, TRAT1, IL4, IFNG, GZMB, PRF1, NKG7, GNLY
- SPON2, KLRK1, KLRD1, CTSW, ID2, IL18RAP, TRAV10, TRAJ18

### NK_CD56bright

Description: Cytokine-producing NK cells characterized by high CD56 expression, low CD16, and expressing KIT and IL7R, with a regulatory/immature phenotype.

Genes:
- NCAM1, GZMK, KIT, IL7R, CCR7, SELL, LEF1, TCF7, XCL1, XCL2, CCL3, CCL4
- CD27, BCL2, GPR56, CXCR3, CXCR4, CD44, IL2RB, IL12RB2, CCR5, CD62L, CD127, CD117

### NK_CD56dim

Description: Cytotoxic NK cells with high CD16 expression, low CD56, and expressing granzymes and perforin, constituting the majority of peripheral blood NK cells.

Genes:
- FCGR3A, KLRD1, KLRK1, PRF1, GZMB, GZMH, GZMM, GNLY, NKG7, FGFBP2, SPON2, CST7
- CLIC3, KLRF1, KLRG1, CD57, B3GAT1, CD160, CD247, ZEB2, TBX21, EOMES, SH2D1B, KTN1
- PPP1R9A

## pdc

### CD14+ monocyte

Description: Classical monocytes expressing CD14 and FcγRIIIa, key in innate immunity and often confused with pDCs in flow cytometry.

Genes:
- CD14, FCGR3A, CSF1R, CD68, LYZ, S100A8, S100A9, VCAN, CTSS, CTSD, CST3, CD163
- CCL2, CXCL8, IL1B, TNF, NFKB1, REL, MYD88, TLR2, TLR4, CD33, CEBPB, MAFB
- SEPP1, F13A1, CD36, LPL, MARCO, MSR1

### cDC2

Description: Conventional dendritic cells type 2, highly expressing CD1c and FCER1A, specialized in antigen presentation to CD4+ T cells.

Genes:
- CD1C, FCER1A, CLEC10A, FSCN1, CCR7, LAMP3, CD83, CD86, HLA-DQA1, HLA-DQB1, HLA-DRA, CD40
- IRF4, ZEB2, KLF4, NOTCH2, IRF8, ID2, TRAF3, NPL, RBPJ, BCL6, MIR155HG, CSF2RA
- CSF2RB, IL4I1, ALOX15, SIGLEC1, CD1D, KIT

### pDC_activated

Description: Activated plasmacytoid dendritic cells with high expression of GZMB and IRF7, producing type I interferons upon viral stimulation.

Genes:
- GZMB, IRF7, LILRA4, CLEC4C, IL3RA, TCF4, BCL11A, PLD4, SERPINF1, PTCRA, RUNX2, SCT
- NXPH2, SMPD3, MAP1B, RAB33A, DPP3, JCHAIN, IRF8, SPIB, TNFRSF21, TLR9, TLR7, MYO1E
- CD2, FCER1A, CLEC10A, CCL5, CXCR3, IFIT1

### pDC_resting

Description: Resting plasmacytoid dendritic cells with high expression of CLEC4C and IL3RA, involved in antiviral IFN production.

Genes:
- LILRA4, CLEC4C, IL3RA, TCF4, BCL11A, PLD4, SERPINF1, PTCRA, RUNX2, SCT, NXPH2, SMPD3
- MAP1B, RAB33A, DPP3, JCHAIN, IRF8, SPIB, TNFRSF21, TLR9, TLR7, MYO1E, CD2, FCER1A
- CLEC10A

## plasmablast

### Memory B cell

Description: Memory B cells are long-lived B cells expressing CD27, CD19, MS4A1, and class-switched or unswitched immunoglobulins, along with activation markers and transcription factors like BCL6.

Genes:
- CD27, CD19, MS4A1, CD79A, CD79B, PAX5, HLA-DRA, HLA-DRB1, HLA-DQB1, HLA-DPB1, CD22, FCER2
- CD80, CD86, ICOSLG, BIRC3, NFKB1, REL, RELB, TNFRSF13C, CD40, BACH2, BCL6, MYC
- MCL1, BCL2, BCL2A1, TCF3, IGHM, IGHD

### Naive B cell

Description: Naive B cells are resting B cells expressing surface IgM and IgD, along with CD19, MS4A1, PAX5, and TCL1A, but lacking CD27 and CD38.

Genes:
- CD19, MS4A1, CD79A, CD79B, PAX5, HLA-DRA, HLA-DRB1, HLA-DQB1, HLA-DPB1, CD22, FCER2, CD40
- BACH2, BCL6, MCL1, BCL2, BCL2A1, TCF3, IGHD, IGHM, TCL1A, BANK1, CD72, CD81
- CD9, CD37, CR2, IL4R, IL6R, IL10RA

### Plasma cell

Description: Plasma cells are terminally differentiated antibody-secreting cells with high SDC1, PRDM1, XBP1, and immunoglobulin heavy chains, and they lack proliferation markers like MKI67.

Genes:
- SDC1, CD38, PRDM1, XBP1, IRF4, MZB1, FKBP11, SEC61B, SSR4, JCHAIN, IGHA1, IGHG1
- IGHA2, IGHG3, IGHG4, IGHM, IGHD, MCL1, TXN, HSP90B1, PDIA4, PPIB, CALR, CANX
- BIRC5, TOP2A, CENPF, AURKA, PLK1, CCNB1, CDK1, UBE2C, HMGB2, STMN1, TYMS, PCNA
- RAN, H2AFZ, HIST1H4C, HIST1H2BK

### Plasmablast

Description: Plasmablasts are proliferating antibody-secreting B cell precursors that highly express PRDM1, XBP1, IRF4, and MKI67, along with cell cycle genes and immunoglobulin chains.

Genes:
- MKI67, PRDM1, IRF4, XBP1, MZB1, CD38, JCHAIN, SDC1, IKZF3, ELL2, SEC61B, SSR4
- FKBP11, TXN, HSP90B1, PDIA4, PPIB, CALR, CANX, MCL1, BIRC5, TOP2A, CENPF, AURKA
- PLK1, CCNB1, CDK1, UBE2C, HMGB2, STMN1, TYMS, PCNA, RAN, H2AFZ, HIST1H4C, HIST1H2BK
- TUBA1B, TUBB4B, ACTB, GAPDH

## platelet

### Activated Platelet

Description: Platelets that have undergone degranulation and shape change, expressing activation markers like P-selectin and CD63.

Genes:
- SELP, CD63, THBS1, F13A1, SERPINE1, PLAUR, VWF, ITGA2B, ITGB3, PF4, PPBP, SPARC
- TUBB1, MYL9, STOM, CLU, GP1BA, GP9, CD9, PCP4

### Erythrocyte

Description: Red blood cells, enucleated cells expressing hemoglobin genes and membrane proteins, often contaminating PBMC preparations.

Genes:
- HBA1, HBA2, HBB, HBD, ALAS2, GYPA, GYPB, GYPC, SLC4A1, EPB42, ANK1, SPTB
- SPTA1, ADD2, TMOD1, KEL, RHAG, AQP1, CA1, HBA1

### Megakaryocyte

Description: Bone marrow precursor of platelets, occasionally found in PBMC, expressing high levels of platelet-specific genes and cell cycle markers.

Genes:
- GP1BA, ITGA2B, ITGB3, PF4, PPBP, MKI67, TOP2A, CENPF, BIRC5, AURKB, PLK1, CDK1
- CCNB1, CCNB2, KIF20A, KIF11, TTK, NUSAP1, SMC4, KIF2C

### Resting Platelet

Description: Inactive platelets circulating in blood, expressing alpha-granule proteins and surface receptors.

Genes:
- PPBP, PF4, GP1BA, GP9, ITGA2B, ITGB3, CD9, CLU, SPARC, TUBB1, STOM, MYL9
- SYNGR1, GP5, GP6, PCP4, PRKAR2B, NRGN, RGS18, MALAT1

## treg

### CD4+ Conv T

Description: Conventional CD4+ T cells are a heterogeneous population of helper T cells that do not express FOXP3 at high levels and include Th1, Th2, Th17, and Tfh subsets with diverse cytokine profiles.

Genes:
- CD4, CD3E, IL7R, CD28, CD40LG, ICOS, CCR7, SELL, CD45RA, CD45RO, LEF1, TCF7
- BCL6, CXCR5, PD1, ICOSLG, CD200, CD27, CD62L, CCR4, STAT4, STAT6, GATA3, TBX21
- RORC, FOXP3low, IL2, IFNG, IL4, IL5, IL13, IL17A, IL21, IL22, TNF, CSF2
- CCL5, XCL1, XCL2, CD69

### CD8+ T

Description: CD8+ T cells are cytotoxic T lymphocytes that are primarily responsible for killing infected or malignant cells, expressing CD8 and containing perforin and granzymes.

Genes:
- CD8A, CD8B, CD3E, CD3D, CD3G, CD28, CD27, CCR7, SELL, CD45RA, CD45RO, GZMK
- GZMH, GZMB, PRF1, NKG7, GNLY, KLRD1, KLRG1, KLRB1, KLRC1, KLRC2, KLRF1, EOMES
- TBX21, ZEB2, ID2, TCF7, LEF1, CD127, IL7R, CD62L, CD44, CCL5, XCL1, XCL2
- FASLG, CD95, CD122, CD132, CD25

### Effector Treg

Description: Effector Treg cells are highly suppressive regulatory T cells with a CD45RA-FOXP3hi phenotype, expressing elevated levels of activation markers, costimulatory molecules, and effector cytokines such as IL-10 and TGF-beta.

Genes:
- FOXP3, IL2RA, CTLA4, IKZF2, IKZF4, TNFRSF18, TNFRSF9, TIGIT, LAG3, CD27, CD127low, CD45RO
- CD44, CCR4, CCR8, GITR, OX40, 4-1BB, PD1, BLIMP1, IRF4, BATF, MAF, PRDM1
- EOMES, TBX21, CXCR3, CCR6, IL10, TGFB1, IL35, GZMB, PRF1, FASLG, CD95, CD122
- CD132, CD25hi, CD39, CD73

### Naive Treg

Description: Naive Treg cells are a subset of regulatory T cells with a CD45RA+FOXP3lo phenotype, expressing high levels of CCR7 and CD62L for lymphoid homing and low levels of activation markers.

Genes:
- CD45RA, CCR7, SELL, FOXP3, IL2RA, CTLA4, CD27, CD62L, LEF1, TCF7, FOXP1, SATB1
- CD28, ICOS, TNFRSF9, TIGIT, CD4, CD3E, CD3D, CD3G, IL7R, MAL, KLF2, S1PR1
- GATA3, BCL2, MYC, IL2RB, STAT5A, STAT5B, SOCS2, SOCS3, CD127, CD45RO, CD44, CD25
- CD122, CD132, CD154, CD40LG

### Th17

Description: Th17 cells are a subset of CD4+ T cells characterized by expression of RORC and production of IL-17A and IL-17F, playing a key role in mucosal immunity and autoimmune inflammation.

Genes:
- CD4, CD3E, RORC, IL17A, IL17F, IL22, IL23R, CCR6, CCR4, CD161, IL1R1, IL1R2
- TGFBR1, TGFBR2, STAT3, BATF, IRF4, MAF, AHR, HIF1A, IL26, CCL20, CCR10, CD146
- CD49f, CD54, CD95, CD127, IL7R, CD28, ICOS, PD1, CTLA4, FOXP3low, TNF, CSF2
- IL6R, IL21, S100A4, S100A6

