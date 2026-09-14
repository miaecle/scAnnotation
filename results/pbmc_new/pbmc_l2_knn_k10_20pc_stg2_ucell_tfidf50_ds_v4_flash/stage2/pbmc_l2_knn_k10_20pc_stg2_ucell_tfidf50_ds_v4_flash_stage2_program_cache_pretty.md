# Stage-2 Precomputed Programs

- tissue: PBMC
- n_program_genes: 50
- n_cached_cell_types: 31

## asdc

### ASDC

Description: Atypical dendritic cells expressing AXL and SIGLEC6, with a mixed phenotype resembling both pDC and monocytes, involved in antigen presentation and immune regulation.

Genes:
- AXL, SIGLEC6, IL3RA, CD33, ITGAX, FCGR1A, CSF1R, IRF8, CD4, ITGAM, CXCR3, HLA-DRA
- HLA-DRB1, CD86, CD40, FLT3, LILRA4, CCR7, CCND2, MYCL1, BCL2A1, NFKB1, RELB, TRAF1
- TNFAIP3, IL1R2, TLR7, TLR9, CLEC7A, DUSP2

### Classical Monocyte

Description: Classical monocytes expressing high levels of CD14 and CD163, with potent phagocytic activity and roles in inflammation and antigen presentation.

Genes:
- CD14, CSF1R, CD33, LYZ, S100A8, S100A9, CST3, FCN1, CD68, CD163, CD86, HLA-DRA
- HLA-DRB1, FCGR1A, FCGR2A, FCGR3A, ITGAM, ITGAX, TLR2, TLR4, TLR8, TNF, IL1B, IL6
- CCL2, CCL3, CCL4, CCL7, CCL8, CXCL8

### Conventional Dendritic Cell type 2 (cDC2)

Description: Conventional dendritic cells type 2 expressing CD1c and FCER1A, specialized in presenting antigen to CD4+ T cells and promoting Th2 and Th17 responses.

Genes:
- CD1C, FCER1A, CLEC10A, ITGAX, HLA-DRA, HLA-DRB1, CD86, CD40, FLT3, IRF4, ITGA4, CD11B
- CD33, TLR2, TLR4, TLR6, TLR8, IL6, IL12B, IL23A, TNF, CCL19, CCL22, CCR7
- CD200, CD274, CD80, CD209, FCGR2A, FCGR2B

### Plasmacytoid Dendritic Cell (pDC)

Description: Plasmacytoid dendritic cells expressing CD123 and CD303, specialized in type I interferon production and antiviral immunity.

Genes:
- IL3RA, CLEC4C, GZMB, TCF4, LSP1, IRF7, MYC, BCL11A, SOX4, JCHAIN, TCL1A, MZB1
- DERL3, IRF8, CD4, HLA-DRA, CD86, CD40, TLR7, TLR9, RUNX2, E2F2, CCND2, CCND3
- CDKN1C, IGJ, SPIB, FLT3, CXCR3, CCR10

## b intermediate

### Memory B cell

Description: Antigen-experienced B cells that express CD27 and have undergone class switching, providing rapid recall responses.

Genes:
- MS4A1, CD19, CD27, CD40, CD81, CD83, CR2, FCRL2, FCRL3, FCRL5, HLA-DQA1, HLA-DQB1
- HLA-DRA, HLA-DRB1, IL4R, SWAP70, TNFRSF13B, TNFRSF13C, IRF8, PAX5, CD22, CD72, BLK, LYN
- SYK, PLCG2, PRKCB, NFATC1, NFATC2

### NK cell

Description: Innate lymphoid cells that kill target cells without prior sensitization, expressing cytotoxic granule proteins and killer-cell immunoglobulin-like receptors.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMH, KLRD1, KLRB1, KLRK1, KIR2DL1, KIR3DL1, KLRF1, KLRC1
- KLRC2, FCGR3A, NCAM1, NCR1, NCR3, CASP3, FADD, TNFRSF10A, TNFRSF10B, BID, BAK1, BAX
- CASP8, CASP9, CASP10, APAF1, CYCS, DIABLO

### Naive B cell

Description: Mature B cells that have not encountered antigen, expressing surface IgD and IgM, and are activated upon recognition.

Genes:
- IGHD, IGHM, FCER2, CR2, CD72, CD22, PAX5, EBF1, BACH2, SPIB, IRF4, CD79A
- CD79B, IL4R, CD24, CD38, MZB1, XBP1, PRDM1, JCHAIN, SDC1, CXCR4, TNFRSF17, SLAMF7
- FKBP11, SSR4, SEC61G, NCAM1, NCR1, FCGR3A

### Plasma cell

Description: Terminally differentiated B cells that secrete antibodies, with high expression of CD138 and transcription factor PRDM1.

Genes:
- SDC1, MZB1, XBP1, PRDM1, IRF4, JCHAIN, CD38, CXCR4, TNFRSF17, SLAMF7, FKBP11, SSR4
- SEC61G, IGHG1, IGHA1, IGHM, IGKC, IGLC1, POU2AF1, BCL2A1, MCL1, HSP90B1, HSPA5, PDIA4
- PDIA6, CANX, CALR, TXNDC5, ERO1A, HYOU1

### Transitional B cell

Description: Immature B cells that have recently emigrated from bone marrow, characterized by high expression of CD24 and CD38.

Genes:
- CD24, CD38, MME, VPREB3, IGLL1, IL7R, RAG1, RAG2, DNTTP2, ALDH1A1, TCL1A, CD34
- BACH2, PAX5, EBF1, IRF4, SPIB, CD79A, CD79B, IGHD, IGHM, CD21, CD22, CD72
- BLK, LYN, SYK, PLCG2, PRKCB, NFATC1

## b memory

### Class-switched memory B cells

Description: B cells that have undergone class switch recombination and express CD27, surface IgG/IgA, and memory markers, providing rapid antibody responses upon re-exposure.

Genes:
- CD27, CD40, MS4A1, BANK1, PAX5, CD79A, CD79B, CD19, CD22, CD72, TNFRSF13C, TNFRSF13B
- POU2AF1, SPIB, BCL6, MEF2C, IRF8, EBF1, CD74, HLA-DRA, IGHA1, IGHG1, IGHG2, IGHG3
- IGHG4, IGHM, IGHD, CD83, CD86, ITGAX, CR2

### Naive B cells

Description: Resting B cells expressing both IgM and IgD with high CD23 and low CD27, ready to become activated upon antigen encounter.

Genes:
- IGHD, IGHM, CD27, SELL, CCR7, IL4R, TCL1A, FCER2, CD23, CR2, CD21, CD35
- MS4A1, CD19, CD79A, CD79B, PAX5, BANK1, POU2AF1, SPIB, EBF1, MEF2C, IRF8, CD72
- CD74, HLA-DRA, TNFRSF13C, CD83, CD40, ITGAX

### Non-switched memory B cells

Description: Memory B cells that retain IgD expression along with CD27, often found in the marginal zone and involved in T-independent responses.

Genes:
- CD27, IGHD, CD1C, CD1D, FCER2, CD23, IL4R, CR2, CD21, CD35, MS4A1, CD19
- CD79A, CD79B, PAX5, BANK1, TNFRSF13C, POU2AF1, SPIB, BCL6, MEF2C, IRF8, EBF1, CD72
- CD74, HLA-DRA, IGHM, IGHM, CD83, CD40

### Plasmablasts

Description: Antibody-secreting cells characterized by high CD38 and CD138 expression, proliferative, and with elevated expression of the unfolded protein response genes.

Genes:
- CD38, SDC1, XBP1, PRDM1, JCHAIN, MKI67, CD27, CD28, CD138, CD24, CD9, ITGA4
- ITGB7, CXCR3, CXCR4, SLAMF7, CCR10, TNFRSF17, CD79A, CD79B, MS4A1, CD19, PAX5, BANK1
- IRF4, BCL6, MEF2C, HLA-DRA, CD74, CD83

## b naive

### B memory

Description: Memory B cells are antigen-experienced B cells expressing CD27 and CD24, with class-switched immunoglobulins and rapid recall responses.

Genes:
- CD27, MS4A1, CD79A, CD19, CD24, CD40, ICOSL, CD80, CD86, TNFRSF13C, CD74, HLA-DRA
- HLA-DPB1, HLA-DQB1, CD72, CD37, CD81, CD21, BIRC3, BCL2, BCL2A1, MYD88, LYN, SYK
- PIK3AP1, PTPRC, CD52, BANK1, BCL11A, BLNK, BTLA, CARD11, CCR6, CD1D, CD180, FCRL3
- FCRL5, LAX1, PRDM1, XBP1, MKI67, AICDA, BCL6, CXCR5, CXCR4, IL4R, IL6R

### B naive

Description: Naive B cells are mature, quiescent B lymphocytes expressing high levels of CD20, CD79A/B, and IgD, with no somatic hypermutation or class switching.

Genes:
- MS4A1, CD79A, CD79B, PAX5, HLA-DRA, CD19, CD22, FCER2, IGHD, IGHM, TCL1A, CD37
- CD72, BLK, BACH2, EBF1, VPREB3, CD24, CD21, CD81, CD40, CD80, CD86, ICOSL
- TNFRSF13C, BCL6, BIRC3, MYD88, LYN, SYK, PIK3AP1, CD79A, CD79B, JCHAIN, PTPRC, CD52
- AGT, ARHGAP15, BANK1, BCL11A, BIN1, BLNK, BTLA, CARD11, CCR6, CD1D, CD5, CD151
- CD180

### CD4+ naive T cell

Description: Naive CD4+ T cells are quiescent helper T cells that express CD4, CD28, and lymph node homing receptors CCR7 and CD62L, lacking effector functions.

Genes:
- CD3D, CD3E, CD4, CD28, CCR7, SELL, CD27, IL7R, LEF1, TCF7, MAL, TMSB4X
- FOS, JUN, CD52, PTPRC, BCL2, CD5, CD6, CD8A, CD8B, CD28, CTLA4, ICOS
- TNFRSF4, TNFRSF18, CD27, CD69, IL2RG, IL2RB, CD3G, CD247, ZAP70, LAT, LCK, ITK
- VAV1, CARD11, BCL10, MALT1, NFKB1, NFKBIZ, RELA, REL, JUNB, FOSB, EGR1, EGR2

### CD8+ naive T cell

Description: Naive CD8+ T cells are resting cytotoxic T cell precursors expressing CD8, CD28, and homing receptors CCR7 and CD62L, with no effector molecule expression.

Genes:
- CD3D, CD3E, CD8A, CD8B, CCR7, SELL, CD27, IL7R, LEF1, TCF7, CD28, CD52
- PTPRC, BCL2, CD5, CD6, CD2, CD99, CD3G, CD247, ZAP70, LAT, LCK, ITK
- VAV1, CARD11, BCL10, MALT1, NFKB1, NFKBIZ, RELA, REL, JUNB, FOSB, EGR1, EGR2
- TNFRSF7, IL2RG, IL2RB, CD69, GZMK, GZMM, PRF1, GNLY, NKG7, KLRG1, KLRD1, KLRB1
- KLRC1, KLRK1

### Plasma cell

Description: Plasma cells are terminally differentiated B cells that secrete large amounts of antibodies, characterized by high CD38, CD138, and immunoglobulin gene expression.

Genes:
- CD38, SDC1, MZB1, JCHAIN, XBP1, PRDM1, IRF4, IGHG1, IGHA1, IGLC2, IGKC, TNFRSF17
- SLAMF7, ITGB7, CD138, CD27, CD28, CD19, CD20, HLA-DRA, HLA-DPB1, HLA-DQB1, CD72, CD37
- CD81, BIRC3, BCL2, MYD88, LYN, SYK, PIK3AP1, PTPRC, CD52, BANK1, BCL11A, BLNK
- BTLA, CARD11, CCR6, CD1D, CD180, FCRL3, FCRL5, LAX1, MKI67, AICDA, BCL6, CXCR4
- IL6R

## cd14 mono

### CD16+ NK cell

Description: CD16+ NK cells are innate lymphoid cells expressing the Fc receptor CD16, enabling antibody-dependent cellular cytotoxicity.

Genes:
- NKG7, GNLY, GZMB, PRF1, KLRD1, KLRC1, KLRC2, KLRK1, FCGR3A, NCAM1, CD244, CD247
- ZAP70, LAT, LCK, ITK, TNFRSF18, IL2RB, IL15RA, IL2RG, STAT4, STAT5A, STAT5B, EOMES
- TBX21, RUNX3, GATA3, CST7, CTSW

### CD1c+ dendritic cell

Description: CD1c+ (cDC2) dendritic cells are myeloid antigen-presenting cells specializing in activating CD4+ T cells and priming Th2 responses.

Genes:
- CD1C, FCER1A, CLEC10A, CD1E, CD1A, CD1B, FCGR2B, FSCN1, CCR7, LAMP3, IRF4, IRF8
- ID2, ZBTB46, FLT3, CSF2RA, CCL17, CCL22, CD80, CD86, HLA-DRA, HLA-DPB1, HLA-DQB1, CD40
- IL12B, IL23A, IL6, TNF, IL1B, CXCL8

### classical monocyte

Description: Classical monocytes are the most abundant monocyte subset, characterized by high CD14 expression, lack of CD16, and strong phagocytic activity.

Genes:
- S100A8, S100A9, S100A12, LYZ, FCN1, CST3, CD14, CCR2, SELL, VCAN, PSAP, CTSS
- CSF1R, FCGR1A, CLEC7A, CLEC4E, CD33, CD86, MNDA, TYMP, CD300E, C5AR1, FPR1, FPR2
- THBS1, PLAUR, SERPINA1

### intermediate monocyte

Description: Intermediate monocytes co-express CD14 and CD16, and are involved in antigen presentation and pro-inflammatory cytokine production.

Genes:
- CD14, FCGR3A, HLA-DRA, CD74, CTSS, CD86, IL1B, TNF, CCL3, CCL4, CXCL8, NFKB1
- NFKB2, REL, IRAK2, MYD88, TLR4, TLR2, TREM1, IL6, IL10, LYZ, S100A8, S100A9
- FCGR1A

### non-classical monocyte

Description: Non-classical monocytes are patrolling monocytes with high CD16 and low CD14, surveying the vasculature and responding to nucleic acids.

Genes:
- FCGR3A, CDKN1C, LST1, RHOC, GPR183, LILRB2, LILRB3, SLAMF7, CX3CR1, NR4A1, MARCKS, FES
- FCER1G, HCST, TYROBP, IFITM3, CLIC3, DUSP1, JUN, FOS, ZFP36, BTG2, EGR1, EGR2
- KLF2

## cd16 mono

### CD16+ Dendritic cells

Description: CD16+ dendritic cells are a subset of conventional dendritic cells that express CD16 and are involved in antigen cross-presentation and activation of T cells.

Genes:
- FCGR3A, TSPAN14, CLEC10A, FCER1A, CD1C, BATF3, IRF8, CLEC9A, XCR1, CADM1, FLT3, ZBTB46
- CCR7, LAMP3, IL3RA, CD80, CD86, HLA-DRA, HLA-DRB1, CD74, CD40, ICOSLG, CD83, CCL19
- CCL21, IL12B, IL23A, TNF, IFNA1, IFNB1

### Classical monocytes

Description: Classical monocytes are CD14++CD16- cells that are phagocytic and produce high levels of pro-inflammatory cytokines, migrating to sites of infection.

Genes:
- CD14, S100A8, S100A9, S100A12, VCAN, LYZ, FCN1, CST3, CD68, CTSS, CTSD, CLEC7A
- ITGAM, CD64, CCR2, CXCL8, IL1B, TNF, CCL3, CCL4, PLIN2, LIPA, NPC2, PSAP
- GRN, C3, CFD, CD163, MSR1, MARCO

### Intermediate monocytes

Description: Intermediate monocytes are CD14+CD16+ cells that exhibit both pro-inflammatory and anti-inflammatory properties, with high expression of HLA-DR and co-stimulatory molecules.

Genes:
- FCGR3A, CD14, S100A8, S100A9, S100A12, VCAN, FOS, JUNB, CXCL2, CXCL8, IL1B, TNF
- CCL3, CCL4, CCR2, CST3, HLA-DRA, HLA-DRB1, CD74, FCGR1A, ANXA2, ITGAM, CTSS, LST1
- AIF1, RBP7, MNDA, CD86, FCER1G, LYZ

### NK cells

Description: NK cells are innate lymphoid cells that kill infected or transformed cells and produce cytokines such as IFN-γ, with CD56dimCD16+ being the most cytotoxic subset.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMA, GZMK, GZMH, KLRD1, KLRB1, KLRK1, KLRC1, KIR2DL1
- KIR2DL3, KIR3DL1, NCR1, NCR3, FCGR3A, CD247, CD3E, CD8A, CD8B, CD2, CD244, SH2D1A
- IL2RB, IL12RB2, IFNG, TNFRSF10B, FASLG, TGFB1

### Non-classical monocytes

Description: Non-classical monocytes are CD16+CD14- patrolling monocytes that survey the endothelium and produce TNF-α, IL-1β, and reactive oxygen species.

Genes:
- FCGR3A, MS4A7, LST1, AIF1, HES4, IFITM3, COTL1, CSF1R, RHOC, TCF7L2, DUSP1, FOS
- JUNB, MAFB, CTSW, CDKN1C, RBM47, STAB1, FGR, SLC7A7, S100A12, S100A9, CXCL16, LILRA5
- IL1RN, FOLR3, FCN1, PLIN2, LIPA, NPC2

## cd4 ctl

### CD4 CTL (Effector)

Description: Cytotoxic CD4+ T cells with high expression of granzymes and perforin, mediating direct cytotoxicity.

Genes:
- GZMB, PRF1, GNLY, GZMA, NKG7, FGFBP2, CTSW, GZMH, CST7, CCL5, CD4, KLRG1
- CX3CR1, ZNF683, HOPX, MYBL1, TBX21, EOMES, ID2, RUNX3, IL2RB, LAG3, TIGIT, GZMK
- KLRD1, KLRF1, KLRB1, CD28, CD27, IL7R

### CD4 CTL (Memory)

Description: Memory-like cytotoxic CD4+ T cells with lower cytotoxic potential but expressing IL7R and CD27, capable of recall responses.

Genes:
- IL7R, CD27, GZMK, GZMA, CTSW, CCL5, KLRB1, CD28, TCF7, LEF1, SELL, CCR7
- CD4, IL2RG, JAK3, BACH2, MYC, FOS, JUN, NFKB1, BCL2, MCL1, ICOS, TNFRSF4
- TNFRSF18, TIGIT, LAG3, HAVCR2, PDCD1, CTLA4

### CD8+ CTL (Effector Memory)

Description: Cytotoxic CD8+ T cells expressing CD8A/B, granzymes, and perforin, commonly confused with CD4 CTL due to shared cytotoxic markers.

Genes:
- CD8A, CD8B, GZMB, PRF1, GNLY, NKG7, GZMK, GZMA, CCL5, CST7, KLRG1, CX3CR1
- CD244, EOMES, TBX21, ZNF683, HOPX, MYBL1, RUNX3, ID2, IL2RB, LAG3, TIGIT, PDCD1
- CTLA4, HAVCR2, CD160, TNFRSF9, CCR5, CCR7

### NK Cells (CD56dim)

Description: Natural killer cells with high cytotoxic activity, expressing NKG7, GNLY, and FCGR3A, often confused with CD4 CTL due to similar effector molecule expression.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMA, KLRD1, KLRF1, FCGR3A, CD247, NCR1, KIR2DL1, KIR3DL1
- KIR2DS4, KLRC1, KLRC2, KLRK1, HLA-DOB, IFNG, TNF, CSF2, IL2RB, IL18RAP, TBX21, EOMES
- ZNF683, CST7, CTSW, FGFBP2, CCL4, CCL3

### γδ T Cells

Description: Gamma-delta T cells expressing T cell receptor gamma and delta chains, sharing cytotoxic granule genes with CD4 CTL.

Genes:
- TRGC1, TRGC2, TRDV2, TRDV1, GZMA, GZMB, NKG7, CCL5, KLRD1, KLRG1, KLRB1, CD7
- CD3E, CD3D, CD3G, TCRGC1, TCRGC2, TCRDV2, EOMES, TBX21, ZNF683, ID2, RUNX3, MYBL1
- HOPX, CST7, CTSW, FGFBP2, GNLY, PRF1

## cd4 naive

### CD4 Central Memory

Description: CD4+ central memory T cells patrol secondary lymphoid organs, retain CCR7 expression, and exhibit rapid recall responses with upregulation of IL7R and CD44.

Genes:
- CCR7, CD44, IL7R, CD27, CD28, BCL2, STAT4, STAT6, GATA3, JUN, FOS, DUSP1
- MYC, MCL1, SOD1, GPX1, TXN, NFKBIA, ZFP36, JUND

### CD4 Naive

Description: CD4+ naive T cells are quiescent cells that express naive markers such as CCR7, SELL, and LEF1, and are primed for activation upon antigen encounter.

Genes:
- CCR7, SELL, LEF1, TCF7, IL7R, CD27, CD28, BCL2, KLF2, FOXP1, ID3, MYC
- ETS1, MAL, SATB1, LDHB, TMSB10, RPL13, CTLA4, DUSP2, S100A8, S100A9

### CD8 Naive

Description: CD8+ naive T cells are cytotoxic precursors that express CD8A and CD8B along with naive markers like CCR7 and SELL, awaiting activation.

Genes:
- CD8A, CD8B, CCR7, SELL, LEF1, TCF7, CD27, CD28, IL7R, BCL2, KLF2, FOXP1
- ID3, MYC, ETS1, MAL, SATB1, LDHB, TMSB10, RPL13

### NK cells

Description: Natural killer cells are innate lymphoid cells that produce cytotoxic granules and express NKG7, GNLY, and PRF1, mediating rapid immune surveillance.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMA, GZMH, GZMM, KLRD1, KLRB1, KLRC1, KLRF1, KIR2DL3
- KIR3DL1, NCR1, NCR3, FCGR3A, CD247, CTSW, FGFBP2, SPON2

## cd4 proliferating

### CD4_Tcm_Proliferating

Description: Proliferating CD4+ central memory T cells expressing high levels of IL7R, CCR7, and SELL, with cell cycle markers.

Genes:
- IL7R, CCR7, SELL, LEF1, TCF7, MKI67, TOP2A, STMN1, PCNA, CENPF, BIRC5, AURKA
- UBE2C, CDK1, CCNB1, CCNA2, CDC20, NUSAP1, RRM2, TYMS, CD3D, CD3E, CD4, CD28
- ICOS, BCL2, MYC, EZH2, DNMT1, HMGB2, H2AFZ, SMC4, SMC2, NASP, LMNB1, KIF2C
- KIF11, KIF20B, ASPM, CENPE, BUB1, BUB1B, MAD2L1, PLK1, AURKB, SGO1, NCAPG, NCAPH
- TOP2B

### CD4_Tem_Proliferating

Description: Proliferating CD4+ effector memory T cells enriched for cytotoxicity-associated transcripts such as GZMA, GZMK, and PRF1, along with cell cycle genes.

Genes:
- PRDM1, GZMA, GZMK, KLRG1, EOMES, TBX21, CCL5, CST7, NKG7, GZMB, GNLY, PRF1
- HLA-DRA, CD38, MKI67, TOP2A, STMN1, PCNA, CENPF, BIRC5, AURKA, UBE2C, CDK1, CCNB1
- CCNA2, CDC20, NUSAP1, RRM2, TYMS, CD3D, CD3E, CD4, CD27, CD28, ICOS, MYC
- EZH2, DNMT1, HMGB2, H2AFZ, SMC4, SMC2, NASP, LMNB1, KIF2C, KIF11, KIF20B, ASPM
- CENPE

### CD4_Treg_Proliferating

Description: Proliferating regulatory T cells expressing canonical markers FOXP3, IL2RA, and CTLA4 along with cell cycle machinery.

Genes:
- FOXP3, IL2RA, CTLA4, TNFRSF18, TIGIT, IKZF2, IKZF4, IL10, TGFB1, ENTPD1, CD39, CD73
- CD3D, CD3E, CD4, MKI67, TOP2A, STMN1, PCNA, CENPF, BIRC5, AURKA, UBE2C, CDK1
- CCNB1, CCNA2, CDC20, NUSAP1, RRM2, TYMS, MYC, EZH2, DNMT1, HMGB2, H2AFZ, SMC4
- SMC2, NASP, LMNB1, KIF2C, KIF11, KIF20B, ASPM, CENPE, BUB1, BUB1B, MAD2L1, PLK1
- AURKB

### CD8_Proliferating

Description: Proliferating CD8+ T cells with high expression of cytotoxic effectors like GZMB and PRF1, along with cell cycle genes.

Genes:
- CD8A, CD8B, GZMB, PRF1, NKG7, GNLY, GZMH, GZMK, CCL5, CST7, EOMES, TBX21
- KLRG1, CD3D, CD3E, MKI67, TOP2A, STMN1, PCNA, CENPF, BIRC5, AURKA, UBE2C, CDK1
- CCNB1, CCNA2, CDC20, NUSAP1, RRM2, TYMS, CD28, ICOS, MYC, EZH2, DNMT1, HMGB2
- H2AFZ, SMC4, SMC2, NASP, LMNB1, KIF2C, KIF11, KIF20B, ASPM, CENPE, BUB1, BUB1B
- MAD2L1

### NK_Cells

Description: Natural killer cells expressing abundant cytotoxic granules and NK-associated receptors such as NKG7, GNLY, and KLRD1, with minimal CD3 expression.

Genes:
- NKG7, GNLY, GZMB, PRF1, GZMH, GZMK, KLRD1, CD94, NKG2A, NKG2C, NCAM1, FCGR3A
- CD16, CD56, KIR2DL1, KIR3DL1, KLRF1, KLRK1, NCR1, NCR3, CD244, CD226, CD96, TNFRSF9
- IL2RB, IL12RB2, IL18RAP, IFNG, TNF, CCL3, CCL4, XCL1, XCL2, FGFBP2, SPON2, CX3CR1
- FCER1G, TYROBP, HCST, CD3E, CD3D, CD3G, EOMES, TBX21, ZEB2, ID2, NFIL3, PRDM1
- AHR, MYC

## cd4 tcm

### CD4 Naive

Description: Naive CD4+ T cells, which have not encountered antigen and express high levels of CCR7 and CD45RA.

Genes:
- CCR7, SELL, TCF7, LEF1, MAL, CD28, CD27, IL7R, CD3D, CD3E, CD4, CD5
- CD6, CD2, CD96, LAIR1, KLRB1, GATA3, BCL11B, ETS1, FOXO1, FOXP1, MYC, KLF2
- KLF3, KLF6, JUN, FOS, NR4A1, NR4A2, NR4A3, ZFP36, DUSP1, DUSP2, DUSP4, MAPK1
- MAPK3, AKT1, AKT2, RPS6KB1, EIF4E, EIF4B, EIF4A1, EIF4G1, PABPC1, PABPC4, POLR2A, POLR2B
- POLR2C, POLR2D

### CD8 TCM

Description: Central memory CD8+ T cells, which circulate through lymph nodes and provide rapid recall responses.

Genes:
- CD8A, CD8B, GZMK, GZMM, NKG7, CCL4, CCL5, XCL1, XCL2, CXCR4, SELL, CCR7
- CD27, CD28, IL7R, TCF7, LEF1, BCL6, EOMES, TBX21, RUNX3, ZEB2, ID2, ID3
- MYB, STAT3, STAT4, STAT5A, STAT5B, JUN, FOS, NR4A1, NR4A2, NR4A3, KLF2, KLF6
- ZFP36, DUSP1, DUSP2, DUSP4, DUSP6, MAPK1, MAPK3, MAP2K1, MAP2K2, AKT1, AKT2, AKT3
- MTOR, RPS6KB1

### Th1

Description: T helper 1 cells, which produce interferon-gamma and promote cell-mediated immunity against intracellular pathogens.

Genes:
- IFNG, TBX21, CXCR3, CCR5, IL12RB2, STAT4, IL18R1, IL18RAP, LAG3, HLA-DRB1, HLA-DRA, CD38
- CD26, KLRG1, PRF1, GZMB, GZMA, CCL4, CCL5, XCL1, XCL2, CD40LG, TNF, LTB
- LTA, IL2, CSF2, IL3, IL13, IL10, IL21, BCL6, MYB, RUNX3, EOMES, ID2
- ZEB2, GATA3, STAT1, IRF1, NFKB1, RELA, JUN, FOS

### Th17

Description: T helper 17 cells, which produce interleukin-17 and are involved in inflammation and autoimmunity.

Genes:
- IL17A, IL17F, RORC, CCR6, IL23R, STAT3, BATF, IRF4, RORA, AHR, IL1R1, IL6R
- TGFBR2, CASP8, BIRC3, CCL20, CCL22, CD161, KLRB1, PTGDR2, IL26, IL22, CSF2, TNF
- LIF, IL21, IL2, ICOS, CD40LG, CD28, CTLA4, SLC2A1, SLC16A3, LACTB, ZNF683, MAF
- RUNX1, ETS1, LEF1, TCF7, MYC, KLF2, ZFP36, DUSP6, MAPK1

### Treg

Description: Regulatory T cells, which suppress immune responses and maintain self-tolerance.

Genes:
- FOXP3, IL2RA, CTLA4, TIGIT, IKZF2, IKZF4, CD27, CD127, GITR, TNFRSF4, TNFRSF18, LRRC32
- LAG3, HLA-DRA, HLA-DRB1, CCR4, CCR8, CD39, ENTPD1, CD73, NT5E, IL10, TGFB1, IL35
- EBI3, IL12A, STAT5A, STAT5B, BACH2, MIR146A, MIR155, SOCS1, SOCS3, FOXP3, CD3D, CD3E
- CD4, CD2, CD5, CD6, CD96, CD226, CD200, CD200R1, LAIR1, KLRB1, KLRD1, KLRG1

## cd4 tem

### CD4 TCM

Description: CD4+ central memory T cells, expressing CCR7 and CD62L, providing rapid recall responses upon antigen re-encounter.

Genes:
- CCR7, SELL, CD27, CD28, TCF7, LEF1, IL7R, MAL, MYC, CXCR4, CCR4, IL2RG
- BIRC3, ICOS, TNFRSF25, TNFRSF1B, RTKN2, KLRG1, GPR183, P2RY10, S1PR1, KLF2, FOXO1, SESN3
- BNIP3, TOX2, ID3, ZFP36L2

### CD4 TEM

Description: CD4+ effector memory T cells, characterized by expression of IL7R, absence of CCR7, and production of effector cytokines such as IFN-gamma and TNF-alpha.

Genes:
- IL7R, KLRB1, GZMK, GZMA, CCL5, ANXA1, ITGA4, CXCR3, CCR6, CD40LG, TNFRSF4, TNFRSF18
- KLRG1, GPR56, FASLG, CCL4, CCL3, XCL1, XCL2, PRF1, GZMH, GZMM, CST7, CTSW
- NKG7, GNLY, FGFBP2, IL2RB, IL18RAP

### CD8 TEM

Description: CD8+ effector memory T cells, highly cytotoxic with expression of granzymes and perforin, often expressing NK cell receptors.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMH, GZMK, GZMA, CCL5, FGFBP2, CST7, CTSW, KLRD1
- KLRK1, KLRC1, KLRB1, CD8A, CD8B, ITGB2, ITGAL, CX3CR1, CCR5, GPR56, FCGR3A, FCGR3B
- LILRB1, LILRB2, CD244, CD2, CD7, TIGIT

### Th17

Description: T helper 17 cells, a pro-inflammatory CD4+ subset producing IL-17 and IL-22, involved in mucosal immunity and autoimmunity.

Genes:
- IL17A, IL17F, CCL20, CCR6, RORC, RORA, IL23R, KLRB1, IL1R1, TNFRSF25, IL6ST, STAT3
- IRF4, BATF, MAF, AHR, IKZF3, RUNX1, TOX, CCL3, CCL4, CCL5, CXCL8, CSF2
- IL22, IL26

### Treg

Description: Regulatory T cells, expressing FOXP3 and CD25, suppress immune responses and maintain peripheral tolerance.

Genes:
- FOXP3, IL2RA, CTLA4, TIGIT, IKZF2, IKZF4, CD27, CD28, TNFRSF4, TNFRSF18, TNFRSF9, IL7R
- ENTPD1, IL10, TGFB1, EBI3, LAG3, PDCD1, HLA-DRA, HLA-DRB1, CD74, SOCS2, STAM, ITM2A
- TSC22D3, PIM2

## cd8 naive

### CD4 Naive

Description: Resting CD4+ T cells that have not encountered antigen, characterized by CD4 expression and lymphoid homing markers.

Genes:
- CD4, CCR7, SELL, LEF1, TCF7, IL7R, CD27, CD28, FOXP1, BCL2, MYB, KLF2
- LTB, MAL, CAMK4, TRAT1, ITK, CD40LG, ID3, NRP1, IL2RA, STAT5A, STAT5B, SOCS1
- SOCS3

### CD8 Central Memory

Description: Memory CD8+ T cells with lymph node homing capacity, retaining expression of co-stimulatory molecules and intermediate effector molecules.

Genes:
- CCR7, CD27, CD28, IL7R, BCL2, GPR183, MAL, LTB, TRAF1, ICOS, TNFRSF14, CD44
- CCL5, GZMK, AQP3, CD47, BACH2, MYC, CD200, CD5, CD6, CD82, PLAC8, LBH
- SELL

### CD8 Effector Memory

Description: Memory CD8+ T cells that have lost lymph node homing receptors and express high levels of cytotoxic effector molecules.

Genes:
- GZMB, GZMK, PRF1, NKG7, KLRG1, CX3CR1, CCL4, CCL5, CST7, GNLY, KLRC1, KLRD1
- FCGR3A, B3GAT1, FGFBP2, KLRB1, KLRC2, CCL3, CCL4L2, GZMH, GZMA, IFNG, TNF, KLRG2
- GZMM

### CD8 Naive

Description: Resting CD8+ T cells that have not encountered antigen, characterized by expression of lymph node homing receptors and naive-associated transcription factors.

Genes:
- CCR7, SELL, LEF1, TCF7, IL7R, CD28, FOXP1, BCL2, MYB, KLF2, LTB, MAL
- CAMK4, S1PR1, ADD3, EEF2, LBH, TXNIP, CD72, SH3BGRL3, ARHGEF3, PIK3R1, ACTN1, CORO1A
- VAV1

## cd8 proliferating

### CD4 Proliferating

Description: Proliferating CD4+ T cells expressing cell cycle genes and CD4, often confused with CD8 proliferating due to shared proliferation signature.

Genes:
- CD4, MKI67, TOP2A, PCNA, TYMS, RRM2, BIRC5, CENPF, STMN1, CDCA8, CKAP2, ASPM
- KIF11, CCNB1, CDC20, AURKA, AURKB, PLK1, BUB1, KIF2C, NEK2, NUSAP1, TONSL, TK1
- DUT, MYC, CD27, CD28, ICOS, IL2RA

### CD8 Effector Memory

Description: Memory CD8+ T cells with effector function, expressing GZMK, GZMB, and NKG7 but retaining some memory markers.

Genes:
- GZMK, GZMA, GZMB, PRF1, NKG7, CCL5, CST7, CTSW, KLRG1, EOMES, TBX21, CX3CR1
- FGFBP2, FCGR3A, HOPX, ZEB2, ID2, PRDM1, KLRD1, KLRK1, CD244, CD160, CD57, B3GAT1
- LAG3, TIGIT, PDCD1, CTLA4, HAVCR2, LILRB1

### CD8 Naive

Description: Naive CD8+ T cells characterized by expression of CCR7, SELL, and TCF7, with low effector molecules.

Genes:
- CCR7, SELL, LEF1, TCF7, IL7R, CD27, CD28, CD5, CD6, KLF2, SATB1, MYB
- FOXP1, BACH2, TCF12, ETS1, BCL11B, SIPR1, MAL, CAMK4, ABLIM1, FLT3LG, LRRN3, NOSIP
- PPP1R16B, CMKLR1, SPOCK2, TGFBR3, PASK, IGFBP4

### CD8 Proliferating

Description: Proliferating CD8+ T cells expressing high levels of cell cycle genes and cytotoxic molecules.

Genes:
- MKI67, TOP2A, CD8A, CD8B, GZMB, PRF1, NKG7, CCL5, GZMK, GZMA, GNLY, CST7
- CTSW, KLRG1, EOMES, TBX21, CX3CR1, FGFBP2, FCGR3A, MYC, PCNA, TYMS, RRM2, BIRC5
- CENPF, STMN1, CDCA8, CKAP2, ASPM, KIF11

### NK cells

Description: Natural killer cells expressing cytotoxic granules and NK-associated receptors, often confused with CD8+ T cells due to shared cytolytic markers.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMA, KLRD1, KLRK1, NCR1, NCAM1, FCGR3A, KLRF1, KLRC1
- KLRC2, KLRC3, KIR2DL1, KIR2DL2, KIR2DL3, KIR3DL1, KIR3DL2, KIR2DS1, KIR2DS2, KIR2DS4, KIR3DS1, CD244
- CD160, CD226, CD96, TIGIT, KLRB1, IL2RB

## cd8 tcm

### CD4 TCM

Description: Central memory CD4+ T cells, expressing high levels of CD40LG and IL7R, providing helper functions.

Genes:
- CD4, CD40LG, IL7R, CCR7, SELL, CD27, CD28, BCL6, TCF7, LEF1, FOXP3, IL2RA
- CTLA4, TNFRSF18, TNFRSF4, ICOS, PDCD1, CD3E, CD3D, CD3G, B2M, HLA-A, HLA-B, HLA-C
- MALAT1, NEAT1, TMSB4X, ACTB, GAPDH, EEF1A1, RPL13A, RPS18, RPLP0, RPS27A, UBB, UBC
- HSP90AB1, HSP90AA1, HSPA8, HSPA1B, HSPA1A, DNAJB1, DNAJA1, CDC37, STIP1, FKBP4, PTGES3, AHSA1
- TTC1, HSPBP1, BAG2, BAG1

### CD8 Naive

Description: Naive CD8+ T cells with no prior antigen experience, expressing CD45RA and CCR7.

Genes:
- CCR7, SELL, LEF1, CD27, CD28, IL7R, FOXP1, TCF7, BCL6, CD3E, CD3D, CD8A
- CD8B, B2M, HLA-A, HLA-B, HLA-C, MALAT1, NEAT1, TMSB4X, ACTB, GAPDH, EEF1A1, RPL13A
- RPS18, RPLP0, RPS27A, UBB, UBC, HSP90AB1, HSP90AA1, HSPA8, HSPA1B, HSPA1A, DNAJB1, DNAJA1
- CDC37, STIP1, FKBP4, PTGES3, AHSA1, TTC1, HSPBP1, BAG2, BAG1

### CD8 TCM (GZMK+)

Description: Central memory CD8+ T cells expressing granzyme K, indicating a more differentiated state with cytolytic potential.

Genes:
- GZMK, KLRG1, CXCR3, CCL5, GZMA, GZMM, PRF1, NKG7, FGFBP2, FCGR3A, KLRD1, KLRF1
- KLRC1, KLRC2, KLRB1, CD2, CD7, CD8A, CD8B, CD3E, CD3D, CD247, ZAP70, LCP2
- ITK, GRAP2, NCK2, VAV1, WAS, ARHGAP25, RHOG, RAC2, CDC42, PAK1, PAK2, MYO9B
- MYH9, MYL12B, MYL6, ACTN4, WDR1, CORO1A, FSCN1, LSP1, PLCG2

### CD8 TCM (IL7Rhi)

Description: Central memory CD8+ T cells with high IL7R expression, exhibiting robust proliferative capacity and memory potential.

Genes:
- IL7R, CCR7, SELL, CD27, CD28, BCL6, TCF7, LEF1, IL2RG, CD3E, CD3D, CD8A
- CD8B, B2M, HLA-A, HLA-B, HLA-C, MALAT1, NEAT1, TMSB4X, ACTB, GAPDH, EEF1A1, RPL13A
- RPS18, RPLP0, RPS27A, UBB, UBC, HSP90AB1, HSP90AA1, HSPA8, HSPA1B, HSPA1A, DNAJB1, DNAJA1
- CDC37, STIP1, FKBP4, PTGES3, AHSA1, TTC1, HSPBP1, BAG2, BAG1

### CD8 TEM

Description: Effector memory CD8+ T cells with immediate effector function, expressing low CCR7 and high cytotoxic molecules.

Genes:
- GZMB, GZMA, GZMH, GZMM, PRF1, NKG7, CCL5, FGFBP2, FCGR3A, KLRG1, KLRD1, KLRC1
- NKG2D, CD2, CD7, CD8A, CD8B, CD3E, CD3D, CD247, ZAP70, LCP2, ITK, GRAP2
- NCK2, VAV1, WAS, ARHGAP25, RHOG, RAC2, CDC42, PAK1, PAK2, MYO9B, MYH9, MYL12B
- MYL6, ACTN4, WDR1, CORO1A, FSCN1, LSP1, PLCG2, ITGAL, ITGB2, CX3CR1

## cd8 tem

### CD4 TEM

Description: CD4+ effector memory T cells, expressing CD27, IL7R, and KLRB1, often confused with CD8 TEM in unsupervised clustering due to similar activation states but lacking CD8 and cytotoxic markers.

Genes:
- IL7R, CCR6, CCR7, CD27, CD28, KLRB1, ANXA1, GATA3, IL2, IL21, CD40LG, ICOS
- TNFRSF4, TNFRSF18, TIGIT, CTLA4, FOXP3, IL10, BCL6, MAF, STAT3, STAT5A, MYC, IRF4
- PRDM1, CXCR5, PD1, LAG3, HAVCR2, CD200

### CD8 CM

Description: CD8+ central memory T cells expressing CCR7, SELL (CD62L), and CD27, with lower cytotoxic gene expression compared to TEM, often confused with CD8 TEM in datasets with poor resolution.

Genes:
- CCR7, SELL, CD27, CD28, IL7R, LTB, LEF1, TCF7, BCL2, MAL, PTPRK, S100A6
- GIMAP6, GIMAP4, GPR183, CXCR3, CXCR4, CXCL13, CCL20, IL17RA, IL17RB, CD8A, CD8B, EOMES
- TBX21, ZNF683, STAT4, PRMT1, ARID5B, MXD3

### CD8 TEM

Description: CD8+ effector memory T cells expressing granzymes K and H, cytotoxic molecules, and lacking CD45RA, with high expression of CCL5 and NKG7.

Genes:
- GZMK, GZMH, CCL5, NKG7, CST7, GZMM, PRF1, GNLY, FGFBP2, CXCR3, CCL4, CCL3
- IFNG, TNF, EOMES, TBX21, KLRG1, CD8A, CD8B, IL7R, CD27, CD28, FASLG, GZMA
- GZMB, KLRD1, KLRK1, NCR3, SH2D1A, CD69

### CD8 TEMRA

Description: Terminally differentiated CD8+ effector memory cells re-expressing CD45RA (TEMRA), with high expression of GZMB, GZMH, PRF1, and NKG7, indicative of strong cytotoxic potential.

Genes:
- GZMB, GZMH, PRF1, NKG7, GNLY, KLRG1, FGFBP2, FCGR3A, CD57, KLRD1, KLRF1, PLAC8
- HOPX, GZMM, CST7, CCL4, CCL3, IFNG, TNF, EOMES, TBX21, CD8A, CD8B, IL2RB
- CX3CR1, ZEB2, TTC38, TNFSF10, CTSW, APOBEC3G

### NK cells

Description: Natural killer cells, particularly the CD56dim subset, expressing high levels of cytotoxic molecules like NKG7, GNLY, PRF1, and GZMB, and lacking CD3 and T cell receptors, thus a common confound with CD8 TEM.

Genes:
- NKG7, GNLY, PRF1, GZMB, KLRD1, KLRF1, KLRK1, NCR1, NCR3, CD160, FCGR3A, CD244
- SH2D1B, CXCR1, CXCR2, FGFBP2, GZMH, GZMM, CST7, CCL4, CCL3, XCL1, XCL2, IL2RB
- IL18RAP, PLAC8, HOPX, SPON2, ZEB2, TTC38

## cdc1

### CD14+ Monocyte

Description: Classical monocytes (CD14+CD16-) involved in phagocytosis, cytokine production, and differentiation into macrophages or dendritic cells in tissues.

Genes:
- CD14, LYZ, S100A8, S100A9, S100A12, FCN1, CSTA, CST3, LILRB2, LILRB1, CLEC7A, CD33
- TYROBP, NCF1, NCF2, CYBB, FCGR2A, IL1B, TNF, CCL2, CCL3, CCL4, CCL7, CCL8
- CXCL2, CXCL3, IL8, SERPINA1, HCK, FGR

### cDC1

Description: Conventional dendritic cells type 1 (cDC1) specialize in cross-presentation of antigens to CD8+ T cells and recognition of intracellular pathogens.

Genes:
- CLEC9A, XCR1, CADM1, BATF3, IRF8, THBD, DNASE1L3, C1orf54, FAM213A, ENTPD1, NLRC5, ID2
- FLT3, BCL2L11, TSPAN6, ITGB7, CD8A, PMEL, PPARG, IDO1, KIT, MYCL, IL12RB2, IL2RB
- IL21R, TNFRSF9, TNFRSF4, CD36, CD207

### cDC2

Description: Conventional dendritic cells type 2 (cDC2) specialize in presenting antigens to CD4+ T cells and sensing extracellular pathogens.

Genes:
- CD1C, FCER1A, CLEC10A, CD1D, FCGR2B, CLEC12A, CLEC4A, CD1E, CD1B, MRC1, SIGLEC10, SIGLEC5
- CCL17, CCL22, IL13RA1, RAB7B, IL1RL1, CXCL8, HLA-DQA1, HLA-DQB1, CD207, CD209, LAMP3, FSCN1
- CCR7, CCL19, IL4I1, IL6, IL10, TNF

### pDC

Description: Plasmacytoid dendritic cells (pDC) are specialized in production of type I interferons (IFN-α/β) in response to viral infections.

Genes:
- LILRA4, CLEC4C, IL3RA, SLC23A2, PTCRA, PLD4, MXD1, BCL11A, IRF7, IRF8, TCF4, ZEB2
- RUNX2, TCL1A, SERPINF1, GZMB, LAMP5, ITM2C, SPIB, PIK3AP1, CXCR3, IL18R1, IL18RAP, TLR7
- TLR9, MYCL, E2-2, FLT3, CD4, HLA-DRA

## cdc2

### CD14+ Monocyte

Description: Classical CD14+ monocytes, major population of blood monocytes, expressing high CD14 and low CD16, involved in phagocytosis and inflammatory responses.

Genes:
- CD14, LYZ, S100A8, S100A9, FCGR3A, CSF1R, CX3CR1, CCR2, CD68, CD163, MRC1, ITGAM
- ITGAX, TLR2, TLR4, MYD88, IRAK1, IRAK4, TNF, IL1B, IL6, IL10, CCL2, CCL3
- CCL4, CCL5, CCL7, CCL8, CCL13, CCL14, CCL16, CCL18, CCL19, CCL20, CCL21, CCL22
- CCL23, CCL24, CCL25, CCL26, CCL27, CCL28, CXCL1, CXCL2, CXCL3, CXCL5, CXCL6, CXCL8
- CXCL10, CXCL11

### CD16+ Monocyte

Description: Non-classical CD16+ monocytes, characterized by high FCGR3A and CX3CR1, patrolling vasculature and involved in antiviral responses.

Genes:
- FCGR3A, CD16, CSF1R, CX3CR1, CCR2, CCR5, CXCR4, CD14, CD36, CD32, ITGAM, ITGAX
- TLR4, TLR8, IRF8, IRF5, TNF, IL1B, IL6, IL10, CCL2, CCL3, CCL4, CCL5
- CCL7, CCL8, CCL13, CCL14, CCL16, CCL18, CCL19, CCL20, CCL21, CCL22, CCL23, CCL24
- CCL25, CCL26, CCL27, CCL28, CXCL1, CXCL2, CXCL3, CXCL5, CXCL6, CXCL8, CXCL10, CXCL11
- CXCL16, CLEC4A

### cDC2A

Description: cDC2A (CD1c+ DC subpopulation) characterized by high FCER1A and CD1C expression, specializing in antigen presentation and Th2/Th17 polarization.

Genes:
- FCER1A, CD1C, HLA-DQA1, HLA-DQB1, CD83, CCR7, LAMP3, FSCN1, CD40, CD86, HLA-DMA, HLA-DMB
- HLA-DPA1, HLA-DPB1, CLEC4A, CLEC4C, IRF8, IRF4, ZBTB46, FLT3, CSF2RA, CD4, CD1E, CD1D
- FCER1G, CLEC10A, CD207, CD209, CD1B, CD1A, BATF3, IDO1, IL12B, IL23A, TNF, CCL22
- CCL17, CCL19, CCL21, CCR7, CCR6, CXCR5, CXCR4, CXCR3, CCL5, CCL3, CCL4, CCL2
- CXCL8, CXCL10

### cDC2B

Description: cDC2B (CD1c+ DC subpopulation) characterized by high CLEC10A and lower FCER1A, associated with tolerogenic responses and Th2 induction.

Genes:
- CLEC10A, FCER1A, CD1C, HLA-DQA1, HLA-DQB1, CD163, CD36, CLEC7A, CD206, CCR2, CCR5, CX3CR1
- CD14, CD1E, CD1D, CD207, CD209, CD11B, ITGAM, CSF1R, CSF2RA, FLT3, IRF4, ZBTB46
- CCL22, CCL17, CCL24, CCL26, IL10, TGFB1, IDO1, IL27, IL4I1, MAFB, PPARG, CDKN1C
- SLC40A1, FOLR2, MRC1, MSR1, STAB1, OLR1, SCARB1, SCARB2, CD68, CD11C, ITGAX, CD80
- CD86, CD40

### pDC

Description: Plasmacytoid dendritic cells (pDC) specialized in type I interferon production in response to viral infections, expressing high CLEC4C and IL3RA.

Genes:
- CLEC4C, IL3RA, TCF4, LILRA4, IRF7, IRF8, BCL11A, SPIB, PACSIN1, SERPINF1, PLD4, DERL3
- MPEG1, NFIB, SCN9A, SCT, CLEC10A, CLEC4A, CLEC12A, CXCR3, CXCR4, CCR7, CCL3, CCL4
- CCL5, TNF, IL12A, IL12B, IFNA1, IFNA2, IFNA4, IFNA5, IFNA6, IFNA7, IFNA8, IFNA10
- IFNA13, IFNA14, IFNA16, IFNA17, IFNA21, IFNB1, IFNW1, IFNE1, IFNK, TLR7, TLR9, MYD88
- IRAK1, IRAK4

## dnt

### MAIT cells

Description: Mucosal-associated invariant T (MAIT) cells are innate-like T cells restricted by MR1, producing cytokines upon microbial stimulation.

Genes:
- KLRB1, TRAV1-2, TRAJ33, TRAJ12, TRAJ20, SLC4A10, CCR6, IL18R1, IL18RAP, RORC, ZBTB16, PLAC8
- RBPJ, GZMK, GZMA, NKG7, PRF1, KLRD1, CD3D, CD3E, CD8A, CD8B, CD4, CD7
- CD2, IL7R, ITGA1, ITGAE, CXCR6, CSF2, IFNG, TNF, CCL20, CCL4, CCL5, KLRK1
- HCST, FCRL6, SLAMF7, KLRC1, KLRG1, EOMES, TBX21

### NK cells

Description: Natural killer (NK) cells are innate lymphoid cells that kill infected or transformed cells without prior sensitization.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMA, GZMH, GZMM, KLRD1, KLRK1, KLRC1, KLRC2, KLRF1
- KLRG1, FCER1G, TYROBP, HCST, SLAMF7, CD247, CD3E, CD3D, CD2, CD7, IL2RB, IL12RB2
- IL18RAP, TBX21, EOMES, ZNF683, HOPX, CCL5, CX3CR1, FGFBP2, S1PR5, SPON2, TTC38, PRSS23
- KIR2DL1, KIR2DL3, KIR3DL1, KIR2DS4, KIR3DL2

### NKT-like cells

Description: NKT-like cells are T cells expressing NK cell markers such as CD56 and NKG7, bridging innate and adaptive immunity.

Genes:
- KLRB1, KLRD1, NKG7, PRF1, GZMB, GZMA, GZMK, GNLY, FGFBP2, KLRC1, KLRC2, KLRK1
- CD3D, CD3E, CD2, CD7, IL2RB, IL12RB2, IL18RAP, TBX21, EOMES, ZNF683, HOPX, CCL5
- CX3CR1, CXCR6, ITGAL, ITGB2, FCER1G, TYROBP, HCST, SLAMF7, CRTAM, DUSP2, JUN, FOS
- NFKB1, RELA

### γδ T cells

Description: γδ T cells are a subset of T cells that express a γδ T-cell receptor, involved in innate-like immunity and enriched in tissues.

Genes:
- TRGC1, TRGC2, TRDV2, TRDV3, TRGV9, TRG-AS1, CD3D, CD3E, CD3G, TRDC, KLRD1, NKG7
- GZMA, GZMK, KLRB1, KLRC1, KLRK1, FCER1G, TYROBP, ZAP70, LCK, ITK, CD2, CD7
- IL7R, IL2RB, PRF1, GNLY, GZMB, CD247, PTPRC, CCL5, CX3CR1, FGFBP2, GZMH, GZMM
- KLRF1, KLRC2, KLRG1, S1PR5, TBX21, EOMES, ZNF683, HOPX

## doublet

### Adaptive NK

Description: Adaptive NK cells are a specialized memory-like subset of NK cells that expand in response to viral infections, characterized by expression of KIRs and CD57.

Genes:
- NKG7, GNLY, PRF1, GZMB, KLRD1, KLRK1, FCGR3A, CD2, CD7, IL2RB, KLRC1, KLRC2
- KLRC3, KIR2DL1, KIR2DL2, KIR2DL3, KIR3DL1, KIR3DL2, LILRB1, LILRB2, LILRB4, CD57, B3GAT1, FCGR3B
- PLAC8, ZBTB32, ZNF683, HOPX, KLRC1, KLRG1, CXCR1, CXCR2, CX3CR1, ITGAL, ITGB2, ITGAX
- ITGAM, S1PR5, TNFRSF10C, TNFRSF1B, FASLG, TRAIL, GZMK, GZMH, GZMM, PRSS23, CTSW, CTSWS1
- AIM2

### CD56bright NK

Description: CD56bright NK cells are a subset of natural killer cells characterized by high expression of NCAM1 (CD56) and low expression of FCGR3A (CD16), with a cytokine-producing regulatory phenotype.

Genes:
- NCAM1, KLRB1, GZMB, PRF1, GNLY, NKG7, KLRD1, KLRC1, KLRK1, FCGR3A, CD244, CD2
- CD7, IL2RB, IL18R1, IL18RAP, CXCR3, CCR5, CCR7, SELL, ITGAL, ITGB2, TNFRSF10C, TNFRSF1B
- XCL1, XCL2, CSF2, IFNG, LTA, TNF, FASLG, TRAIL, GZMK, GZMH, GZMM, PRSS23
- CTSW, CTSWS1, MYOM2, AIM2, TGFBR3, SMAD3, STAT4, STAT5A, STAT5B, EOMES, TBX21, ZEB2
- KLF12, SOX4

### CD56dim NK

Description: CD56dim NK cells are a mature, cytotoxic subset of natural killer cells with high FCGR3A (CD16) expression and potent cytotoxic activity.

Genes:
- FCGR3A, NKG7, GNLY, PRF1, GZMB, KLRD1, KLRK1, CD2, CD7, IL2RB, CXCR1, CXCR2
- CX3CR1, ITGAL, ITGB2, ITGAX, ITGAM, S1PR5, KLRG1, KLRC1, KLRC2, KLRC3, KIR2DL1, KIR2DL2
- KIR2DL3, KIR3DL1, KIR3DL2, LILRB1, LILRB2, LILRB4, TNFRSF10C, TNFRSF1B, FASLG, TRAIL, GZMK, GZMH
- GZMM, PRSS23, CTSW, CTSWS1, AIM2, TGFBR3, SMAD3, STAT4, STAT5A, STAT5B, EOMES, TBX21
- ZEB2, KLF12

### CD8+ T cell

Description: CD8+ T cells are cytotoxic T lymphocytes that recognize antigens presented by MHC class I molecules and express CD8A/CD8B and various granzymes and perforin.

Genes:
- CD8A, CD8B, CD3D, CD3E, CD3G, CD247, GZMA, GZMB, GZMK, GZMH, PRF1, GNLY
- NKG7, CCL5, CST7, CTSW, CTSWS1, FASLG, TRAIL, IFNG, TNF, LTA, IL2, IL7R
- CCR7, SELL, LEF1, TCF7, EOMES, TBX21, ZEB2, KLF12, SOX4, MYB, ID2, ID3
- BATF, JUN, FOS, NFKB1, RELA, STAT1, STAT3, STAT5A, STAT5B, STAT6, IRF1, IRF4
- IRF8, NFATC1, NFATC2

### NKT cell

Description: NKT cells are a heterogeneous population of T cells that express both NK cell markers (NKG7, KLRD1) and T cell markers (CD3), and rapidly produce cytokines upon activation.

Genes:
- NKG7, GNLY, PRF1, GZMB, KLRD1, KLRK1, CD3D, CD3E, CD3G, CD247, CD4, CD8A
- CD8B, FCGR3A, CD2, CD7, IL2RB, CXCR3, CCR5, CCR7, SELL, ITGAL, ITGB2, TNFRSF10C
- TNFRSF1B, FASLG, TRAIL, IFNG, TNF, LTA, IL4, IL13, IL17A, IL17F, IL22, CSF2
- XCL1, XCL2, CTSW, CTSWS1, PRSS23, AIM2, TGFBR3, SMAD3, STAT4, STAT5A, STAT5B, EOMES
- TBX21, ZEB2

## eryth

### Early Erythroblast

Description: Early erythroblast precursors that are actively proliferating and initiating hemoglobin synthesis.

Genes:
- GATA1, KLF1, TAL1, GYPB, GYPC, RHAG, EPOR, TFRC, CDK6, CCND3, MYB, KIT
- FLVCR1, ALAD, UROD, CPOX, PPOX, FECH, SLC25A37, SLC25A38, ABCB10, HEBP1, HEBP2, BLVRB
- HMOX2, HMBS, ALAS2

### Late Erythroblast

Description: Late erythroblasts undergoing enucleation and high hemoglobin production.

Genes:
- HBA1, HBA2, HBB, HBD, HBE1, HBG1, HBG2, GYPA, EPB42, ANK1, SPTB, SPTA1
- SLC4A1, CA1, KEL, RHCE, RHD, DARC, CD47, ALAS2, FECH, SLC25A37, BLVRB, HMOX2
- NFE2

### Megakaryocyte

Description: Megakaryocytes that are platelet precursors, often confused with erythroid cells due to shared early progenitor markers.

Genes:
- ITGA2B, ITGB3, GP9, GP1BA, GP1BB, PF4, PPBP, VWF, CD36, F13A1, THBS1, SELP
- CLEC1B, GATA1, FLI1, NFE2, SLC6A4, TUBB1, HIST1H1C, TIMP3

## gdt

### CD8+ T cell

Description: CD8+ cytotoxic T cells are key adaptive effectors that kill infected or malignant cells via granule exocytosis and cytokine production.

Genes:
- CD8A, CD8B, CD3E, CD3D, CD3G, CD28, CD27, CD45RO, CCR7, SELL, IL7R, TCF7
- LEF1, EOMES, TBX21, PRDM1, ZNF683, GZMK, GZMA, GZMB, GNLY, PRF1, NKG7, CCL5
- CST7, EFF1, KLRG1, KLRD1, KLRK1, FASLG, TNF, IFNG, IL2, IL22, CCL4, XCL1
- XCL2, CCR5, CXCR3, CX3CR1, ITGB1, ITGA4, CD99, PTPRC, CD2, CD5, CD6, CD38
- CD69, HLA-A

### MAIT cell

Description: Mucosal-associated invariant T (MAIT) cells are innate-like T cells recognizing microbial vitamin B2 metabolites, with effector functions including cytokine production and cytotoxicity.

Genes:
- KLRB1, CD161, SLC4A10, TRAV1-2, TRAJ33, TRAJ12, TRBC1, TRBC2, ZBTB16, PLZF, RORC, RORA
- AHR, IL17A, IL17F, IL22, IFNG, TNF, CSF2, CCL20, CXCL13, CCL4, CCL5, GZMA
- GZMB, GZMK, GNLY, PRF1, NKG7, KLRD1, KLRK1, CD8A, CD8B, CD4, CD3E, CD3D
- CD3G, CD27, CD28, CD45RO, CCR7, SELL, IL7R, IL2RB, IL18R1, IL18RAP, IL12RB1, IL12RB2

### NK cell

Description: Natural killer cells are innate lymphoid cells that provide rapid cytotoxicity and cytokine responses against stressed cells without prior sensitization.

Genes:
- NKG7, KLRF1, KLRD1, KLRK1, NCR1, NCR2, NCR3, FCGR3A, CD16, CD56, NCAM1, GZMB
- GZMA, GZMM, PRF1, GNLY, CCL5, XCL1, XCL2, CCL4, IFNG, TNF, CSF2, IL2RB
- IL15RA, IL18RAP, IL12RB2, STAT4, STAT5B, EOMES, TBX21, ZEB2, ID2, BATF, IRF8, TCF7
- LEF1, CD7, CD2, CD11a, CD18, CD94, NKG2A, KIR2DL1, KIR2DL2, KIR3DL1, KIR3DL2

### Vδ1 gdT cell

Description: Vδ1 gamma-delta T cells are less common in PBMC, enriched in tissues, and have diverse TCR specificities with roles in stress surveillance and immune regulation.

Genes:
- TRDC, TRGC1, TRGC2, TRDV1, TRGV1, TRGV2, TRGV3, TRGV4, KLRD1, GZMA, GZMB, GNLY
- PRF1, CCL5, NKG7, CD3E, CD3D, CD3G, CD27, CD28, CD45RO, CCR7, SELL, IL7R
- IL2RB, IL15RA, CX3CR1, KLRG1, EOMES, TBX21, ZEB2, ID2, BATF, IRF4, STAT4, STAT1
- STAT2, IFNG, TNF, CSF2, XCL1, XCL2, KLRB1, KLRK1, NKG2D, NCR2, CD160, FASLG
- TRAIL, TNFSF10

### Vδ2 gdT cell

Description: Vδ2 gamma-delta T cells are the predominant subset in human PBMC, recognizing phosphoantigens and producing cytokines like IFN-γ and TNF-α.

Genes:
- TRDC, TRGC1, TRGC2, TRGV9, TRDV2, KLRD1, GZMA, GZMB, GNLY, PRF1, CCL5, NKG7
- CD3E, CD3D, CD3G, ZAP70, LCK, FYN, ITK, LAT, LCP2, NFATC1, NFKB1, STAT3
- STAT5B, MYC, BCL2, MCL1, BAD, BAK1, BID, BIM, PUMA, NOXA, CASP3, CASP8
- CASP9, CYCS, APAF1, DIABLO, HTRA2, XIAP, BIRC2, BIRC3, TNF, IFNG, IL2RA, IL7R
- CXCR3

## hspc

### Common myeloid progenitor (CMP)

Description: Progenitors committed to myeloid lineages, giving rise to granulocytes, monocytes, and dendritic cells.

Genes:
- CD34, CD33, MPO, CEBPA, SPI1, GATA2, RUNX1, KIT, FLT3, CSF1R, CSF3R, IL3RA
- CD38, CD115, CD116, CD123, CD131, CD13, CD14, CD16low, CD64, CD11b, LYZ, CTSG
- ELANE, PRTN3, AZU1, BPI, LTF, MMP8, MMP9, IL8, CCL3, CXCL8, MYD88, IRF8
- CEBPE, CEBPB, GFI1, LMO4, MITF, MAFB, ETS2, PU.1, FOS, JUNB

### Erythroid progenitor

Description: Progenitors that differentiate into red blood cells, characterized by high expression of hemoglobin genes and erythroid-specific transcription factors.

Genes:
- HBA1, HBA2, HBB, HBD, HBZ, EPOR, GATA1, KLF1, NFE2, TAL1, LMO2, MYB
- ERG, FOG1, BCL11A, SOX6, BAND3, GYPA, GYPB, GYPC, KEL, RHAG, ALAS2, FECH
- UROD, CPOX, PPOX, SLC4A1, XK, ANK1, SPTB, SPTA1, EPB42, DMTN, ADD1, ADD2
- ICAM4, LU, LW, CD235a, CD71, CD36, cKIT, EPO, HIF2A, VEGFA, EPHB4, RHOXF2

### Hematopoietic stem cell (HSC)

Description: Long-term hematopoietic stem cells capable of self-renewal and differentiation into all blood lineages.

Genes:
- CD34, PROM1, FLT3, KIT, TAL1, RUNX1, GATA2, LMO2, MEIS1, HOXA9, MLL, HHEX
- ERG, LYL1, SCL, BMX, MYB, KLF4, JUN, FOS, ETV6, NUP98, HOXB4, CD164
- SPINK2, CD93, CD133, CD38low, THY1, CDCP1, ALDH2, ABCG2, CXCR4, ITGA6, TSPAN7, POU3F1
- SOX4, HMGA2, LIN28B, EZH2, BMI1, PRDM16, CEBPA, SPI1, ID1, ID2, JARID2, MEF2C
- HLF

### Megakaryocyte progenitor

Description: Progenitors that differentiate into megakaryocytes and produce platelets, marked by platelet-specific integrins and granule proteins.

Genes:
- ITGA2B, GP1BA, GP1BB, GP9, PF4, PPBP, TREML1, VWF, SELP, THBS1, CD36, CD41
- CD61, CD42a, CD42b, CD42c, CD42d, ITGA2, ITGB3, FLI1, GATA1, GATA2, NFE2, MEIS1
- PBX1, HOXA9, RUNX1, MYB, ZFP36L2, FOG1, ETS1, ERG, STAT5A, JAK2, MPL, THPO
- CXCR4, MCL1, BCL2, BAX, BID, CASP3, WAS, ARPC1B, TUBB1, MYH9, FLNA, ACTN1

### Pre-B cell

Description: B cell precursors in early development, expressing pre-B cell receptor and recombination machinery, often confused with hematopoietic progenitors due to CD34 positivity.

Genes:
- CD19, CD79A, CD79B, PAX5, EBF1, TCF3, IRF4, IRF8, BCL11A, BLNK, CD34, CD10
- IGLL1, VPREB1, VPREB3, RAG1, RAG2, DNTT, SMARCA4, MYC, MEF2C, FOXO1, ID3, ID2
- LYN, SYK, ZAP70, ITK, LCK, BLK, FYN, HCK, CD22, CD72, CD79, CD81
- CD19low, CD24, CD38, CD40, CD44, CD117, CD133, FLT3, KIT, CXCR4, VLA4, IL7R
- IL2RG

## ilc

### CD4+ T cells

Description: CD4+ T cells are helper T lymphocytes that express CD4 and IL7R, orchestrating adaptive immune responses through cytokine production and B cell help.

Genes:
- CD4, IL7R, CD3E, CD3D, CD3G, CD28, CD40LG, CXCR5, CCR7, SELL, LEF1, TCF7
- FOXP1, BCL11B, GATA3, BCL6, ICOS, PD1, TIGIT, LAG3, CTLA4, CD69, CD44, CD62L
- CD27, CD127, CD25, CD122, CD132, IL2RA, IL2RB, IL2RG, IL4R, IL5RA, IL13RA1, IL13RA2
- IFNGR1, IFNGR2, STAT5A, STAT5B, STAT6, STAT3, STAT1, IRF4, NFATC1, NFATC2, NFKB1, RELA
- JUN, FOS

### ILC1

Description: ILC1 are innate lymphoid cells that produce IFN-gamma and express T-bet, involved in type 1 immunity against intracellular pathogens.

Genes:
- TBX21, EOMES, IFNG, GZMB, NKG7, PRF1, GZMA, GZMK, GZMH, GZMM, GZMH, KLRK1
- KLRD1, KLRC1, KLRC2, KLRB1, KLRF1, KLRG1, NCAM1, CD244, CD160, FCGR3A, FCRL6, IL12RB2
- IL18RAP, IL18R1, IL21R, IL2RB, IL2RG, STAT4, STAT1, IRF1, IRF9, BATF, JUN, FOS
- MAP3K8, NFKB1, RELA, MYC, CCL3, CCL4, CCL5, XCL1, XCL2, GPR56, GPR183, S1PR5
- CXCR3, CXCR6

### ILC2

Description: ILC2 are innate lymphoid cells producing type 2 cytokines (IL-13, IL-5) and expressing GATA3, crucial for helminth defense and allergic inflammation.

Genes:
- GATA3, IL13, IL5, IL4, IL9, IL10, CSF2, RORA, RORB, KLRG1, KIT, LILRB2
- LILRA4, FCRL1, FCRL2, FCRL3, FCRL4, FCRL5, FCRL6, CRTH2, PTGDR2, HPGDS, CYSLTR1, CYSLTR2
- TSLP, TSLPR, IL7R, IL13RA1, IL13RA2, IL4RA, IL2RA, IL2RB, IL2RG, STAT6, STAT5A, STAT5B
- GATA1, GATA2, GATA4, GATA6, FOXP1, BCL6, BACH2, ID2, ID3, ETV1, ETV5, NFIL3
- NR3C1, NR4A1, NR4A2

### ILC3

Description: ILC3 are innate lymphoid cells that produce IL-22 and IL-17, express RORγt, and are essential for mucosal immunity and tissue repair.

Genes:
- RORC, IL23R, IL22, IL17A, IL17F, IL26, CCL20, CCR6, KIT, KLRB1, CD117, CD127
- CD25, CD122, CD132, IL7R, IL2RB, IL2RG, STAT3, STAT5, AHR, HIF1A, ARNT, TOX2
- TCF7, ID2, ID3, BATF, JUNB, FOSL2, IRF4, IRF8, MAF, NFKB1, RELA, BCL6
- BCL2, MCL1, PIM1, PIM2, SOCS3, CISH, MAPK1, MAPK3, AKT1, MTOR, RPS6KB1, EIF4EBP1
- LAT, LCK

### NK cells

Description: NK cells are innate lymphocytes with cytotoxic activity, characterized by expression of NKG7, GNLY, and PRF1, and play key roles in tumor surveillance and viral infection.

Genes:
- NCAM1, NKG7, GNLY, PRF1, GZMB, GZMA, GZMK, GZMH, GZMM, KLRK1, KLRD1, KLRC1
- KLRC2, KLRC3, KLRC4, KLRB1, KLRF1, KLRG1, FCGR3A, CD16, CD56, CD57, CD244, CD160
- CD226, CD2, CD28, CD11a, CD11b, CD18, CX3CR1, CXCR1, CXCR2, CXCR3, CXCR4, CCR1
- CCR2, CCR5, CCR7, IL12RB1, IL12RB2, IL15RA, IL2RB, IL2RG, STAT4, STAT5, EOMES, TBX21
- RUNX3, ZEB2

## mait

### CD4+ MAIT

Description: CD4+ mucosal-associated invariant T cells, a minor subset with regulatory-like functions and cytokine production.

Genes:
- CD4, KLRB1, IL18R1, IL18RAP, SLC4A10, TIGIT, GZMK, GZMM, CTSW, DUSP2, LTB, RORA
- CCR6, CXCR6, CD3E, CD3D, CD2, CD7, IL2RA, IL7R, CXCR3, CD28, CD27, PTPRC

### CD8+ MAIT

Description: CD8+ mucosal-associated invariant T cells, abundant in blood, characterized by semi-invariant TCR and production of IL-17A and IFN-γ.

Genes:
- KLRB1, IL18R1, IL18RAP, SLC4A10, TIGIT, GZMK, GZMM, CTSW, DUSP2, CSF2, LTB, RORA
- CCR6, CXCR6, CD8A, CD8B, CD3E, CD3D, CD2, CD7, ITGAE, KLRG1, LAG3, FASLG

### Conventional CD8+ T cell

Description: Conventional CD8+ T cells that recognize peptide-MHC class I, including naive and memory subsets.

Genes:
- CD8A, CD8B, SELL, CCR7, LEF1, TCF7, BCL2, IL7R, CD28, CD27, CD3E, CD3D
- TRAC, TRBC1, TRBC2, CD5, CD6, CD247, CD3G, CD2

### NKT cell

Description: Invariant natural killer T cells expressing semi-invariant TCR and sharing both T cell and NK cell features.

Genes:
- KLRB1, NKG7, GZMB, PRF1, NCAM1, FCGR3A, KLRD1, KLRC1, KLRK1, CD3E, CD3D, ZBTB16
- XCL1, XCL2, CSF2, IL4, IL13, IFNG, CD69, TRAV10

### γδ T cell

Description: T cells bearing γδ T cell receptor, involved in innate-like responses.

Genes:
- TRGC1, TRGC2, TRDV1, TRDV2, TRDD3, CD3E, CD3D, CD2, CD7, CD27, CD28, PTPRC
- FCGR3A, KLRB1, NKG7, GZMB, PRF1, KLRC1, KLRD1, CD160

## nk

### CD56bright NK

Description: CD56bright NK cells are abundant in lymph nodes, produce high levels of cytokines like IFN-gamma, and have low cytotoxic activity.

Genes:
- NCAM1, GZMK, KLRB1, IL7R, CCR7, SELL, XCL1, XCL2, IL2RB, IL18R1, IL12RB2, CSF2
- TNF, IFNG, CCL3, CCL4, CD69, HLA-DRB1, HLA-DPA1, HLA-DPB1, CD44, ITGA4, CD62L, LY9
- CD28, CD27, ICOS, TNFRSF9, TNFRSF4, TNFRSF18, TIGIT, KLRG1, KIR2DL4, KLRC1, KLRC2, KLRC3
- KLRD1, NKG7, GNLY, PRF1

### CD56dim NK

Description: CD56dim NK cells are cytotoxic, express high levels of CD16 (FCGR3A) and KIRs, and are the predominant NK subset in blood.

Genes:
- FCGR3A, KIR2DL1, KIR2DL2, KIR2DL3, KIR3DL1, KIR3DL2, KIR3DL3, KIR2DS1, KIR2DS2, KIR2DS3, KIR2DS4, KIR2DS5
- KIR3DS1, PRF1, GZMB, GZMA, GNLY, NKG7, KLRD1, KLRK1, NCR1, NCR3, CD160, CD226
- DNAM1, CX3CR1, FGFBP2, FCGR3B, FCER1G, TNFRSF10C, AREG, B3GAT1, KLRC1, KLRC2, KLRC3, KLRF1
- KLRG1, SLAMF7, CD244, CD2

### Cytotoxic CD8+ T cells

Description: Cytotoxic CD8+ T cells are antigen-experienced T cells that express CD8 and kill infected or malignant cells, sharing several effector molecules with NK cells.

Genes:
- CD8A, CD8B, CD3D, CD3E, CD3G, GZMK, GZMH, GZMA, GZMB, PRF1, GNLY, NKG7
- CCL5, CX3CR1, KLRG1, KLRD1, KLRK1, FCGR3A, CD7, CD27, CD28, CD45RO, CCR7, SELL
- IL7R, EOMES, TBX21, TOX, TCF7, LEF1, MYC, FOS, JUN, IFNG, TNF, LTA
- LTB, GZMM, GZMA, GZMH, GZMK, GZMB

### NKT cells

Description: NKT cells (natural killer T cells) express both T-cell receptors and NK cell markers, and rapidly produce cytokines upon activation.

Genes:
- CD3D, CD3E, CD3G, CD8A, CD8B, NKG7, GNLY, PRF1, GZMB, KLRB1, KLRG1, KLRD1
- KLRK1, NCR1, NCAM1, FCGR3A, CD160, CD226, CD244, SLAMF7, TRAV1-2, TRAJ33, TRAJ12, SLC4A10
- RORC, PLZF, ZBTB16, IL18R1, IL12RB2, CCR6, CD69, HLA-DRB1, HLA-DPA1, HLA-DPB1, CCL5, CCL4
- IFNG, TNF, CSF2, XCL1, XCL2

## nk proliferating

### Cytotoxic CD8+ T cells

Description: Cytotoxic CD8+ T cells with high expression of granzymes, perforin, and other cytotoxic markers, distinct from NK cells by expression of CD3 and TCR components.

Genes:
- CD8A, CD8B, GZMB, GZMH, GZMK, GZMA, PRF1, NKG7, GNLY, CCL4, CCL5, CX3CR1
- FGFBP2, SPON2, FCGR3A, KLRD1, KLRK1, KLRC1, KLRC2, KLRG1, CD244, CD247, HCST, SH2D1B
- PLAC8, CST7, CTSW, FASLG, IFNG, TNF, TNFRSF1A, TNFRSF4, CD69, CD38, HLA-DRA, HLA-DRB1
- CD74, ITGA4, ITGB1, ITGA2, CD44, SELL, CXCR3, CXCR6, CCR5, CCR7, LAG3, PDCD1
- CTLA4, HAVCR2

### NK CD56bright

Description: Cytokine-producing CD56bright natural killer cells with high expression of NCAM1, GZMK, and chemokine receptors, and low expression of KIRs.

Genes:
- NCAM1, GZMK, GZMA, GZMM, CCL3, CCL4, CCL5, XCL1, XCL2, IL2RB, IL7R, IL12RB2
- IL18R1, IL18RAP, TNFSF10, TNFRSF1A, TNFRSF4, CD44, SELL, CD62L, CCR7, CXCR3, CXCR6, CX3CR1
- ITGA4, ITGB1, ITGA6, ITGA2, CD69, CD38, HLA-DRA, HLA-DRB1, CD74, NCAM1, BACH2, KLRB1
- KLRC1, KLRG1, CD27, CD28, CD3E, CD3D, CD3G, CD8A, CD8B, CD4, GATA3, TOX
- ID2, EOMES

### NK CD56dim

Description: Cytotoxic CD56dim natural killer cells characterized by high expression of FCGR3A (CD16), KIR receptors, and cytotoxic molecules.

Genes:
- FCGR3A, KIR2DL1, KIR2DL3, KIR3DL1, KIR3DL2, KIR2DS1, KIR2DS2, KIR2DS4, KIR3DS1, KLRC1, KLRC2, KLRC3
- KLRK1, NKG7, GNLY, PRF1, GZMB, GZMH, GZMM, FGFBP2, SPON2, CX3CR1, FCER1G, TYROBP
- KLRD1, KLRF1, CD244, CD247, HCST, SH2D1B, PLAC8, CCL4, XCL1, XCL2, CST7, CTSW
- GZMA, GZMK, PRF1, FASLG, IFNG

### NK Proliferating

Description: Proliferating natural killer cells with high expression of cell cycle genes and NK cell markers.

Genes:
- MKI67, TOP2A, TYMS, PCNA, CENPF, STMN1, HMGB2, BIRC5, CDK1, CCNB1, CCNA2, AURKA
- AURKB, PLK1, KIF2C, KIF20A, KIF23, CENPE, CENPA, NUSAP1, H2AFZ, HIST1H4C, HIST1H1B, HIST1H2BJ
- HIST1H2BM, HIST1H3B, HIST1H2AC, HIST1H2AD, HIST1H2AI, HIST1H2BK, HIST1H2BH, HIST1H2BO, HIST1H3D, HIST1H3F, HIST1H3H, HIST1H3I
- HIST1H4A, HIST2H2AB, HIST2H2BE, HIST2H3A, HIST2H3D, HIST2H4A, HIST3H2A, HIST3H2BB, NKG7, GNLY, KLRD1, KLRF1
- KLRK1, NCR1

### Proliferating CD8+ T cells

Description: Proliferating CD8+ T cells with high expression of cell cycle genes and T cell lineage markers.

Genes:
- MKI67, TOP2A, TYMS, PCNA, CENPF, STMN1, HMGB2, BIRC5, CDK1, CCNB1, CCNA2, AURKA
- AURKB, PLK1, KIF2C, KIF20A, KIF23, CENPE, CENPA, NUSAP1, H2AFZ, HIST1H4C, HIST1H1B, HIST1H2BJ
- HIST1H2BM, HIST1H3B, HIST1H2AC, HIST1H2AD, HIST1H2AI, HIST1H2BK, HIST1H2BH, HIST1H2BO, HIST1H3D, HIST1H3F, HIST1H3H, HIST1H3I
- HIST1H4A, HIST2H2AB, HIST2H2BE, HIST2H3A, HIST2H3D, HIST2H4A, HIST3H2A, HIST3H2BB, CD8A, CD8B, CD3D, CD3E
- CD3G, TRAC, TRBC1, TRBC2

## nk_cd56bright

### CD56bright NK

Description: Cytokine-producing NK cells with low cytotoxicity, expressing high levels of CD56 and lacking CD16.

Genes:
- GZMK, XCL1, XCL2, IL7R, SELL, KLRB1, CCR7, CD44, CD27, IL2RB, IL18RAP, CXCR3
- TNFRSF4, TNFRSF9, ICOS, GZMA, BACH2, TCF7, LEF1, MYC, JUN, FOSB, EGR1, DUSP1
- NR4A2, SOCS3, IL2RA, IL9R, CCR5, CXCR6

### CD56dim NK

Description: Cytotoxic NK cells expressing CD16 and low CD56, predominant in peripheral blood.

Genes:
- FCGR3A, KLRF1, KLRG1, HAVCR2, PRF1, GZMB, GZMH, NKG7, GNLY, KLRD1, KLRC1, KLRK1
- SH2D1B, FGFBP2, SPON2, CX3CR1, ITGAL, ITGB2, CD2, CD7, KLRC3, KLRC4, KIR2DL4, KIR3DL1
- KIR3DL2, KIR2DS4, CD226, CD244, CD16, GZMM

### CD8+ cytotoxic T

Description: Cytotoxic T cells expressing CD8, responsible for killing infected cells via perforin and granzymes.

Genes:
- CD8A, CD8B, GZMB, GZMH, GZMA, PRF1, NKG7, GNLY, KLRD1, KLRC1, CD3D, CD3E
- CD3G, CD247, CD2, CD7, FASLG, IFNG, TNF, CCL5, XCL1, XCL2, CTSW, CST7
- GZMM, GZMK, KLRK1, KLRB1, EOMES, TBX21

### NKT

Description: Innate-like T cells expressing both T cell receptor and NK cell markers, capable of rapid cytokine production.

Genes:
- CD3D, CD3E, CD3G, CD247, KLRB1, KLRK1, NKG7, ZBTB16, IL18R1, PRF1, GZMB, GZMK
- IL4, IFNG, PTGDR2, CCR6, CXCR6, IL17RB, RORC, TBX21, EOMES, CD4, CD8A, CD8B
- TRAV10, TRBV25-1, TRAJ18, KIR3DL1, KIR2DL4

## pdc

### CD14+ Monocyte

Description: Classical monocytes expressing high levels of CD14, involved in phagocytosis, inflammation, and recruitment to tissues.

Genes:
- CD14, S100A8, S100A9, CSF1R, CD163, CD68, FCGR3A, FCGR2A, ITGAM, ITGAX, CCR2, CX3CR1
- LYZ, LST1, AIF1, FPR1, FPR2, TLR2, TLR4, MYD88, IRAK1, IRAK4, TRAF6, NLRP3
- IL1B, IL6, TNF, CCL2, CCL3, CCL4, CXCL8, IL10

### cDC2

Description: Conventional dendritic cell type 2, specialized in antigen presentation to CD4+ T cells and expressing high levels of CD1c and FcεRI.

Genes:
- CD1C, FCER1A, CLEC10A, CD1E, CLEC4A, CD1B, CD1A, ITGAX, ITGAM, HLA-DQA1, HLA-DQB1, HLA-DRA
- HLA-DRB1, CD86, CD40, CCR7, CCL22, CCL17, IL4I1, IRF4, ZEB2, KLF4, AP1B1, MARCH1
- FLT3, CSF1R, CD32, FCGR2A, CD64, FCGR1A

### pDC CD2+

Description: A subset of pDC with higher CD2 and CD5 expression, showing reduced type I interferon production but enhanced antigen-presenting capacity.

Genes:
- CD2, CD5, CD6, LTK, ITGA4, IL3RA, TCF4, IRF8, IRF7, CLEC4C, LILRA4, SERPINF1
- PLAC8, UGCG, NR4A2, SCT, BCL11A, GPM6B, RUNX2, PTCRA, E2-2, CCR5, CXCR3, ICOS
- CD83, CD86, HLA-DRA, HLA-DRB1, CD40, BTLA, ILT7

### pDC CD2-

Description: Classical pDC subset with strong type I interferon response and high expression of TLR7, TLR9, and IRF7.

Genes:
- CLEC4C, LILRA4, IRF7, IRF8, SERPINF1, PLAC8, UGCG, TCF4, NR4A2, SCT, BCL11A, GPM6B
- RUNX2, PTCRA, E2-2, IL3RA, CD123, TLR7, TLR9, MYD88, IRAK4, IRAK1, TRAF6, IFIH1
- DDX58, MX1, OAS1, OAS2, OAS3, ISG15, IFI44L, RSAD2, IFIT1, IFIT2, IFIT3, IFITM1
- IFITM2, IFITM3, BST2, CD83

## plasmablast

### Memory B Cell

Description: Antigen-experienced B cell that persists long-term and expresses CD27 and class-switched immunoglobulin, but lacks plasma cell markers.

Genes:
- CD27, CD19, MS4A1, CXCR5, CR2, TNFRSF13C, POU2AF1, BACH2, BCL6, AICDA, IL4R, IRF8
- PAX5, EBF1, CD79A, CD79B, HLA-DRA, HLA-DRB1, HLA-DQB1, HLA-DQA1, CD74, IGHM, IGHD, IGHG1
- IGHG3, IGHA1, IGHE, FCER2, SWAP70, TCF4

### Naive B Cell

Description: Mature B cell that has not encountered antigen, expressing high levels of IgD and IgM along with B-cell markers and lacking CD27.

Genes:
- IGHD, IGHM, CD19, MS4A1, CD22, CR2, TNFRSF13C, FCER2, CD79A, CD79B, PAX5, EBF1
- POU2AF1, BACH2, BCL6, IRF8, IL4R, HLA-DRA, HLA-DRB1, HLA-DQB1, HLA-DQA1, CD74, CXCR4, CXCR5
- CCR7, SELL, KLF2, TCL1A, IGBP1, BANK1

### Plasma Cell

Description: Non-proliferative, terminally differentiated antibody-secreting cell with high expression of CD138 (SDC1) and absence of MKI67.

Genes:
- SDC1, XBP1, CD38, IRF4, PRDM1, JCHAIN, IGHG1, IGHG3, IGHA1, IGHA2, IGHM, DERL3
- SSR4, HSP90B1, HSPA5, PDIA4, PDIA6, DNAJB9, EDEM1, HYOU1, MANF, PPIB, CANX, CALR
- PDIA3, ERP29, ERP44, TXNDC5, SDF2L1, TNFRSF17

### Plasmablast

Description: A proliferating B cell that secretes antibodies, characterized by high expression of cell cycle genes, endoplasmic reticulum stress genes, and immunoglobulin chains.

Genes:
- MKI67, XBP1, SDC1, CD38, IRF4, PRDM1, JCHAIN, IGHG1, IGHG3, IGHA1, IGHA2, IGHM
- DERL3, SSR4, HSP90B1, HSPA5, PDIA4, PDIA6, DNAJB9, EDEM1, HYOU1, MANF, PPIB, CANX
- CALR, PDIA3, ERP29, ERP44, TXNDC5, SDF2L1

## platelet

### Activated Platelets

Description: Activated platelets undergo degranulation and shape change, upregulating adhesion molecules and procoagulant factors.

Genes:
- SELP, CD63, THBS1, SERPINE1, IL1B, CCL5, CXCL4, PDGFB, LAMP1, LAMP2, ITGA2B, ITGB3
- PF4, PPBP, VWF, CLU, CD36, CD9, GNAS, GNG11, PLEK, MYL9, TPM2, ACTB
- ARHGEF6

### Megakaryocytes

Description: Megakaryocytes are bone marrow-derived precursor cells that produce platelets, characterized by high expression of cytoskeletal and platelet-specific genes.

Genes:
- VWF, MYL9, TPM2, ITGA2B, GP1BA, PF4, PPBP, FLI1, GATA1, RUNX1, MPL, THPO
- NFE2, DIAPH1, MYH9, CLU, CD36, CD9, GNAS, GNG11, PLEK, TUBB1, GP9, SDPR
- ACTB

### Resting Platelets

Description: Resting platelets are small anucleate cell fragments involved in hemostasis, characterized by high expression of alpha-granule proteins and platelet-specific integrins.

Genes:
- PPBP, PF4, SDPR, TUBB1, GP9, GP1BA, ITGA2B, ITGB3, CLU, CD36, CD9, GNAS
- GNG11, PLEK, ARHGEF6, RUNX1, GATA1, FLI1, MYL9, TPM2, ACTB, HIST1H2AC, CALM1, PDGFA
- VWF

## treg

### Activated Treg

Description: Activated regulatory T cells with high FOXP3 and IL2RA expression, expressing co-inhibitory molecules and cytokines like IL10 and TGFB1.

Genes:
- FOXP3, IL2RA, CTLA4, TNFRSF18, TNFRSF4, ICOS, TIGIT, BATF, IKZF2, IL2RB, TNFRSF9, CCR8
- ENTPD1, LAG3, PDCD1, CD27, CD28, IL10, TGFB1, CCL5, GZMA, PRF1, EOMES, TBX21
- CXCR3, CCR5, IL12RB2, IFNG, STAT1, STAT4

### CD8+ effector T cell

Description: Activated CD8+ effector T cells with cytotoxic markers such as granzymes, perforin, and interferon-gamma, targeting infected or malignant cells.

Genes:
- CD8A, CD8B, GZMA, GZMB, GZMK, GZMH, PRF1, GNLY, NKG7, CCL5, CCL4, CCL3
- IFNG, TNF, FASLG, EOMES, TBX21, ZEB2, ID2, RUNX3, CST7, KLRK1, KLRC1, KLRD1
- CD69, CD44, IL2RB, IL12RB2, IL18R1, IL18RAP

### Naive CD4+ T cell

Description: Naive CD4+ T cells that have not yet encountered antigen, expressing CCR7 and CD45RA, and capable of differentiating into various helper subsets.

Genes:
- CCR7, SELL, IL7R, TCF7, LEF1, CD27, CD28, CD40LG, IL2, IFNG, IL4, IL5
- IL13, IL17A, IL17F, IL22, IL9, IL21, GATA3, RORC, TBX21, STAT6, STAT3, STAT1
- MAF, AHR, BATF, IRF4, NFATC1, NFATC2

### Resting Treg

Description: Resting regulatory T cells with moderate FOXP3 and IL2RA expression, maintaining immune homeostasis without high activation markers.

Genes:
- FOXP3, IL2RA, CTLA4, TNFRSF18, TNFRSF4, ICOS, TIGIT, BATF, IKZF2, IL2RB, TNFRSF9, CCR8
- ENTPD1, LAG3, PDCD1, CD27, CD28, IL10, TGFB1, CCL5, GZMA, PRF1, EOMES, TBX21
- CXCR3, CCR5, IL12RB2, IFNG, STAT1, STAT4

