# Stage-2 Precomputed Programs

- tissue: PBMC
- n_program_genes: 50
- n_cached_cell_types: 31

## asdc

### ASDC

Description: AXL+SIGLEC6+ dendritic cells (ASDCs) represent a transitional dendritic cell state sharing transcriptional features of both plasmacytoid and conventional dendritic cells.

Genes:
- AXL, SIGLEC6, PPP1R14A, CD22, CX3CR1, CD1C, CLEC10A, FCER1A, ENHO, LILRA3, S100A9, S100A8
- LYZ, C1orf54, GPR137B, MZB1, JCHAIN, LILRB4, ITGAX, CD2, IL3RA, CLEC4C, NRP1, TCF4
- SCT

### cDC2

Description: Type 2 conventional dendritic cells (cDC2s) are the major MHC-II-dependent antigen-presenting myeloid cells in blood, characterized by CD1C and CLEC10A expression.

Genes:
- CD1C, CLEC10A, FCER1A, ENHO, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, HLA-DRB1, CD1E, PKIB, GSN
- CST3, ANXA1, S100A9, S100A8, LYZ, FCN1, CD14, ITGAX, CSF1R, LILRB4

### pDC

Description: Plasmacytoid dendritic cells (pDCs) are specialized type I interferon-producing cells characterized by high expression of CLEC4C, IL3RA, and immunoglobulin-producing machinery.

Genes:
- CLEC4C, IL3RA, LILRA4, TCF4, NRP1, SCT, PACSIN1, PLD4, MAP1A, GZMB, SERPINF1, ITM2C
- MZB1, JCHAIN, DERL3, TXNDC5, IRF7, IRF8, SPIB, LAMP5, PTPRS, APP, SOX4

## b intermediate

### B memory

Description: Antigen-experienced B cells that express CD27 and class-switched immunoglobulins, primed for rapid antibody response upon re-exposure.

Genes:
- MS4A1, CD19, CD27, AIM2, COBLL1, CLECL1, IGHG1, IGHG3, IGHA1, TXNIP, CD80, CD86
- S100A4, S100A6, AHNAK, FCRL1, FCRL3, FCRL5, ITGB2, CD11c, ITGAX, TBX21, ZBTB32, RUNX3
- TNFRSF13B

### B naive

Description: Mature, antigen-inexperienced B cells characterized by high expression of IGHD, TCL1A, and FCER2.

Genes:
- MS4A1, CD19, CD22, TCL1A, FCER2, IL4R, IGHD, IGHM, CD72, YBX3, PLD4, SOX4
- CXCR5, CCR7, SELL, BTG1, LINC00926, CD79A, CD79B, BLNK, HVCN1, MEF2C, SWAP70, ZNF385A
- MYC

### Plasmablast

Description: Highly proliferative, antibody-secreting cells representing the immediate precursors to plasma cells, characterized by high secretory pathway gene expression.

Genes:
- MZB1, PRDM1, IRF4, XBP1, CD38, SDC1, TNFRSF17, IGHG1, IGHG2, IGHG3, IGHA1, IGKC
- IGLC2, IGLC3, JCHAIN, FKBP11, SEC61A1, SSR4, TXNDC5, HERPUD1, DERL3, CREB3L2, SDF2L1, P4HB
- CD24

## b memory

### Atypical Memory B Cell

Description: Also known as age-associated B cells (ABCs), these are CD27-negative, CD11c-positive, and T-bet-positive memory B cells expanded in chronic inflammation, aging, and autoimmune conditions.

Genes:
- ITGAX, TBX21, FCRL5, FCRL3, CD11c, ZEB2, CD86, CD19, MS4A1, GRN, ACTB, HCK
- LST1, Ahnak, S100A6, S100A11, FGR, LYN, CD244, LAIR1, SOX5, TOX, RUNX3, ANXA1
- ANXA2

### Classical Memory B Cell

Description: Classical memory B cells characterized by the expression of CD27 and switched immunoglobulin isotypes (IgG or IgA) that mediate rapid secondary antibody responses.

Genes:
- CD27, CD19, MS4A1, TNFRSF13B, CD38, IGHG1, IGHG3, IGHA1, IGHA2, AIM2, CLEC17A, COBLL1
- FCRL1, FCRL3, FCRL5, CD80, CD86, ITGB2, RUNX2, TXNIP, MARCKS, AHNAK, S100A10, S100A4
- GPR183, CCR7, CD40, NFKBIA, JUNB, FOS

### Naive B Cell

Description: Mature, antigen-inexperienced B cells circulating in PBMCs that express high levels of IgD, IgM, and TCL1A, and lack memory markers like CD27.

Genes:
- IGHD, IGHM, TCL1A, IL4R, FCER2, CD22, CD79A, CD79B, MS4A1, CD19, BACH2, BTG1
- CXCR5, CCR7, SELL, YBX3, PLD4, HVCN1, CD52, BLNK, MEF2C, SWAP70, FAIM, TXNIP

### Plasmablast

Description: Highly proliferative, antibody-secreting cells representing an intermediate stage between activated B cells and terminally differentiated plasma cells, often confused with memory B cells during rapid immune responses.

Genes:
- MZB1, PRDM1, IRF4, XBP1, CD38, SDC1, TNFRSF17, IGHG1, IGHG2, IGHG3, IGHA1, IGHA2
- JCHAIN, TXNDC5, FKBP11, SEC61A1, SSR4, HERPUD1, DERL3, CREB3L2, SDF2L1, MANF, SEL1L, P4HB
- PDIA3, PDIA4, PDIA6

## b naive

### Naive B cell (classical)

Description: Classical resting naive B cells circulating in peripheral blood, characterized by high expression of IGHD, IGHM, TCL1A, and FCER2 (CD23) without activation markers.

Genes:
- MS4A1, CD19, CD22, TCL1A, FCER2, IL4R, IGHD, IGHM, CD79A, CD79B, YBX3, CXCR4
- CCR7, SELL, BTG1, LINC00926, BLNK, CD72, HVCN1, PLD4, P2RX5, CD52, VPREB3, FAM129C
- MEF2C

### Switched Memory B cell

Description: Antigen-experienced B cells that have undergone class-switch recombination to IgG or IgA and lack IgD and IgM expression, representing a common source of false-positive naive annotations if marker thresholds are poorly set.

Genes:
- CD27, IGHG1, IGHG2, IGHA1, IGHA2, CD80, CD86, TNFRSF13B, CLEC17A, COBLL1, AIM2, FCRL3
- FCRL5, S100A4, S100A10, AHNAK, CD99, ITGB1, CD19, MS4A1

### Transitional B cell

Description: Immature B cells recently emigrated from the bone marrow, representing an intermediate developmental stage between pro/pre-B cells and mature naive B cells, marked by high CD38, CD24, and TCL1A.

Genes:
- TCL1A, VPREB3, SOX4, CD24, CD38, PLD4, IGHD, IGHM, MME, ADA, DNTT, CD9
- CD22, FCER2, LINC00926, RAG1, RAG2, CD19, MS4A1, BTG1

### Unswitched Memory B cell

Description: Also known as marginal zone-like B cells, these are antigen-experienced memory B cells that retain expression of both IgD and IgM alongside the memory marker CD27.

Genes:
- CD27, IGHM, IGHD, AIM2, COBLL1, CLEC17A, CD84, CD86, TNFRSF13B, CD80, CD22, MS4A1
- CD19, TXNIP, FCRL1, FCRL3, FCRL5, GPR18, CCR6, MARCKS

## cd14 mono

### Classical Monocyte (CD14++ CD16-)

Description: The major subset of circulating monocytes characterized by high CD14 expression, lack of CD16, and high expression of S100 alarmin proteins, specialized in phagocytosis and pro-inflammatory responses.

Genes:
- CD14, LYZ, S100A8, S100A9, S100A12, VCAN, FCN1, MNDA, CTSS, CD300E, MAFB, GRN
- LGALS3, LGALS1, CSTA, IL1B, CXCL8, CCL3, CCL4, JUNB, FOS, IER3, EIF1, S100A11
- S100A6, S100A4, TYROBP, FCER1G, CFD, SPI1

### Conventional Dendritic Cell 2 (cDC2)

Description: A major myeloid dendritic cell subset in blood that shares many myeloid markers with CD14+ monocytes but is distinguished by high CD1C, FCER1A, and HLA class II expression, specialized in CD4+ T-cell priming.

Genes:
- CLEC10A, FCER1A, CD1C, ENHO, PKIB, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, HLA-DRB1, CD74, CPVL
- GSN, PLD4, IL3RA, CD1E, CD2, CX3CR1, S100A10.1, RUNX3, IRF4, ZBTB46

### Intermediate Monocyte (CD14++ CD16+)

Description: A transitional monocyte population expressing both CD14 and CD16 (FCGR3A) with highly elevated antigen presentation machinery (HLA class II genes) and inflammatory cytokine capacity.

Genes:
- CD14, FCGR3A, HLA-DRA, HLA-DRB1, HLA-DPB1, HLA-DQA1, CD74, AIF1, FTL, FTH1, COTL1, LST1
- IFITM3, IFITM2, S100A8, S100A9, LYZ, VNN2, MARCO, CD40, ITGAX, CLEC10A, CD86, TNF
- IL1B

### Non-classical Monocyte (CD14dim CD16++)

Description: A patrolling monocyte subset characterized by low CD14 and high CD16 (FCGR3A) expression, involved in vascular surveillance and antiviral responses.

Genes:
- FCGR3A, LST1, AIF1, MS4A7, CX3CR1, HES4, CKLF, TCF7L2, RHOC, C1QA, C1QB, C1QC
- IFITM1, IFITM2, IFITM3, LILRB2, LILRA3, SIGLEC10, SPN, CSF1R, SMIM25, MTSS1, CD300C, PECAM1

## cd16 mono

### CD14+ Classical Monocyte

Description: The major classical monocyte subset in PBMCs, characterized by high CD14 expression, low CD16 expression, and high phagocytic and inflammatory potential.

Genes:
- CD14, S100A9, S100A8, S100A12, VCAN, FCN1, LYZ, CD300E, CD163, FPR1, FPR2, CSF3R
- NAMPT, CLEC12A, IL1B, CXCL8, S100A11, ANXA1, LGALS3, GRN, CD68

### CD16+ Non-classical Monocyte

Description: The primary non-classical monocyte subset in PBMCs, characterized by high expression of FCGR3A (CD16), CX3CR1, and patrolling behavior along the vascular endothelium.

Genes:
- FCGR3A, MS4A7, LST1, AIF1, CX3CR1, HES4, TCF7L2, RHOC, IFITM3, C1QA, C1QB, C1QC
- LYN, COTL1, SPI1, CSF1R, CD300A, CD300C, SIGLEC10, PECAM1, LILRB1, LILRB2, FGR, S100A8
- S100A9

### Intermediate Monocyte

Description: A transitional monocyte state expressing both CD14 and CD16, characterized by high expression of MHC class II genes and antigen presentation machinery.

Genes:
- CD14, FCGR3A, HLA-DRA, HLA-DRB1, HLA-DPB1, HLA-DQA1, CD74, S100A8, S100A9, S100A12, GRN, AIF1
- LST1, COTL1, FCN1, VCAN, LYZ, ANXA1, CLEC10A, CD86

### Non-classical Dendritic Cell (cDC2/DC3)

Description: A conventional dendritic cell subset in PBMCs that can be confused with CD16+ monocytes due to overlapping HLA-DR and myeloid marker expression, but distinguished by CD1C and FCER1A.

Genes:
- FCER1A, CLEC10A, CD1C, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, CD2, CX3CR1, CD1E, ENHO, PKIB
- PLD4, RUNX3, FLT3, ZBTB46, CSF2RB, CD86, CD80, CD40

## cd4 ctl

### CD4+ Cytotoxic T Lymphocytes (CD4+ CTL)

Description: A rare subset of CD4+ T cells in PBMCs that express cytotoxic molecules and lineage transcription factors typically associated with CD8+ T cells and NK cells.

Genes:
- GZMB, PRF1, NKG7, GNLY, FGFBP2, GZMH, CX3CR1, TBX21, ZEB2, ADGRG1, S1PR5, PRF1
- KLRD1, KLRG1, CD244, SPON2, CLIC3, CST7, HOPX, EOMES, RUNX3, CCL5, CCL4, CD8A
- CD8B

### CD4+ Effector Memory T Cells (TEM)

Description: Antigen-experienced CD4+ T cells lacking lymph node homing receptors that can express lower levels of granzymes (primarily GZMK) without full cytotoxic differentiation.

Genes:
- CD4, IL7R, LTB, CCR6, ANXA1, S100A4, S100A10, CD2, CD3D, CD3E, CD3G, GZMK
- DUSP2, FOS, JUN, KLRB1, CD52, IL32, GIMAP5, GIMAP7, CORO1A, CXCR3

### CD8+ Effector Memory T Cells (TEMRA)

Description: Terminally differentiated CD8+ T cells that re-express CD45RA and exhibit high cytotoxic potential, frequently transcriptionally confused with CD4+ CTLs.

Genes:
- CD8A, CD8B, GZMH, GZMB, PRF1, NKG7, GNLY, FGFBP2, CX3CR1, KLRG1, FCGR3A, S1PR5
- TBX21, EOMES, ZEB2, ADGRG1, SPON2, CLIC3, CST7, CCL5, CCL4, GZMM, KLRD1, CD244

### Natural Killer (NK) Cells

Description: Innate lymphoid cells that share a highly overlapping cytotoxic gene expression profile with CD4+ CTLs but lack CD3 and CD4 expression.

Genes:
- NCAM1, NCR1, NCR3, FCGR3A, KLRF1, KLRC1, KLRD1, KLRG1, NKG7, GNLY, PRF1, GZMB
- GZMA, SPON2, FGFBP2, CST7, CLIC3, CD160, XCL1, XCL2, S1PR5, HOPX, RUNX3, EOMES

## cd4 naive

### CD4+ Central Memory T cells (Tcm)

Description: An antigen-experienced CD4+ T cell subset that retains lymph node homing receptors CCR7 and SELL but downregulates naive-specific transcription factors like LEF1 while upregulating memory-associated genes like S100A4 and IL32.

Genes:
- CCR7, SELL, CD27, IL7R, LTB, CD4, TRAC, TRBC2, CD3D, CD3E, ANXA1, IL32
- S100A4, S100A10, GIMAP7, GIMAP4, CD52, AQTAP, FOS, JUN, DUSP1

### CD4+ Naive T cells (True)

Description: Bonafide resting CD4+ naive T cells characterized by high expression of lymph node homing receptors CCR7 and SELL, alongside transcription factors LEF1 and TCF7.

Genes:
- CCR7, LEF1, SELL, TCF7, NOSIP, MAL, LDHB, CD27, IL7R, FLT3LG, MYC, EEF1A1
- RPS27, RPL13, RPL3, RPS3A, RPS18, RPL21, BTG1, CD4, TRAC, TRBC1, TRBC2, CD3D
- CD3E, CD3G, TXNIP, S1PR1, KLF2, LINC00861

### CD4+ Stem Cell Memory T cells (Tscm)

Description: A rare, long-lived memory T cell subset that shares naive-like markers such as CCR7 and CD27 but is distinguished by the acquisition of memory markers like CD95 (FAS) and CXCR3.

Genes:
- CCR7, LEF1, SELL, TCF7, CD27, IL7R, FAS, CD44, IL2RB, CXCR3, KLRG1, GZMK
- S1PR1, KLF2, CD4, TRAC, TRBC2, MYC, TXNIP, LTB, CD3D, CD3E, RUNX3, EOMES

### CD8+ Naive T cells

Description: A major neighboring cytotoxic lineage subset that shares the core naive transcriptional program (CCR7, LEF1, SELL) but is distinguished by the expression of CD8A and CD8B instead of CD4.

Genes:
- CD8A, CD8B, CCR7, LEF1, SELL, TCF7, NOSIP, MAL, LDHB, CD27, FLT3LG, GIMAP5
- GIMAP4, CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, S1PR1, KLF2, TXNIP

## cd4 proliferating

### CD4+ Proliferating T cells (MKI67+)

Description: Activated CD4+ T cells undergoing active clonal expansion and cell cycle progression, characterized by high expression of proliferation markers and canonical CD4+ T cell lineage genes.

Genes:
- MKI67, TOP2A, CENPF, CDK1, NUSAP1, BIRC5, CCNB1, CCNB2, CCNA2, CDC20, CDCA8, CDCA3
- AURKA, AURKB, PLK1, UBE2C, CENPE, CENPM, KPNA2, TPX2, SMC4, HMGB2, CD4, IL7R
- CD3D, CD3E, CD3G

### CD8+ Proliferating T cells

Description: Proliferating cytotoxic CD8+ T cells that share cell-cycle machinery with proliferating CD4+ T cells but are distinguished by the expression of CD8 co-receptors and cytolytic effector molecules.

Genes:
- MKI67, TOP2A, CENPF, CDK1, NUSAP1, BIRC5, CD8A, CD8B, GZMB, PRF1, NKG7, GNLY
- CD3D, CD3E, CD3G, CCNB1, CCNA2, CDC20, CDCA8, AURKB, HMGB2, CST7, FGFBP2

### Plasmablasts

Description: Rapidly proliferating, antibody-secreting B-cell precursors that can be confused with proliferating T cells due to shared high expression of cell-cycle genes, but are distinguished by massive immunoglobulin and secretory pathway expression.

Genes:
- MZB1, PRDM1, IRF4, XBP1, CD38, SDC1, IGHM, IGHA1, IGHG1, IGKC, IGLC2, MKI67
- TOP2A, CENPF, CDK1, NUSAP1, BIRC5, TXNDC5, SSR4, FKBP11, SEC61A1, HERPUD1

### Proliferating NK cells

Description: A rare, highly active population of proliferating Natural Killer cells expressing cell-cycle genes alongside NK-specific receptors and cytotoxic mediators, while lacking CD3 expression.

Genes:
- MKI67, TOP2A, CENPF, CDK1, NUSAP1, BIRC5, NCAM1, KLRD1, KLRF1, NKG7, GNLY, GZMB
- PRF1, FCGR3A, SPON2, CST7, CCNB1, CCNA2, CDC20, CDCA8, AURKB

## cd4 tcm

### CD4+ Central Memory T cells (CD4+ TCM)

Description: Antigen-experienced CD4+ T cells that express lymph node homing receptors CCR7 and CD62L (SELL) and possess high proliferative capacity.

Genes:
- CCR7, SELL, TCF7, IL7R, CD4, MAL, LEF1, CD27, CD28, LTB, MYC, NOSIP
- LDHB, GIMAP5, GIMAP7, EEF1A1, TPT1, IL2, CD3D, CD3E, CD3G, FLT3LG, S1PR1, S1PR4
- ITGB1

### CD4+ Effector Memory T cells (CD4+ TEM)

Description: Antigen-experienced CD4+ T cells that have lost CCR7 and CD62L expression, allowing them to home to peripheral tissues to exert immediate effector functions.

Genes:
- IL7R, CD4, ITGB1, S100A4, S100A6, S100A10, ANXA1, LGALS1, CD52, GZMA, GZMK, FGFBP2
- LYAR, KLRG1, CX3CR1, CCL5, CD2, CD3D, CD3E, CD3G, IL32, CORO1A, ACTG1

### CD4+ Naive T cells

Description: Antigen-inexperienced CD4+ T cells characterized by high expression of CCR7, SELL, and LEF1, but lacking memory markers like CD45RO or ITGB1.

Genes:
- CCR7, SELL, LEF1, TCF7, CD4, IL7R, MAL, CD27, NOSIP, LDHB, GIMAP5, GIMAP4
- EEF1B2, RPL13, RPS18, S1PR1, CD3D, CD3E, CD3G, FLT3LG

### Regulatory T cells (Treg)

Description: A specialized lineage of CD4+ T cells dedicated to suppressing immune responses, uniquely characterized by the expression of FOXP3 and high levels of CD25 (IL2RA).

Genes:
- FOXP3, IL2RA, IKZF2, CTLA4, TIGIT, TNFRSF4, TNFRSF18, BATF, CD4, IL7R, LAIR2, RTKN2
- FCRL3, CD109, SOCKS3, CD3D, CD3E, CD3G, MAL, GIMAP5

## cd4 tem

### CD4+ Central Memory T cells (CD4 TCM)

Description: Antigen-experienced CD4+ T cells that retain homing capacity to secondary lymphoid organs via CCR7 and CD62L (SELL) expression, representing a major transitional state often confused with TEM.

Genes:
- IL7R, LTB, CCR7, SELL, CD27, CD4, MAL, TCF7, LEF1, CD3D, CD3E, CD3G
- CD52, GIMAP5, GIMAP7, NOSIP, S100A4, S100A10, S100A6, ANXA1, EEF1A1, TPT1

### CD4+ Cytotoxic T cells (CD4 CTL)

Description: A highly differentiated, cytotoxic subset of CD4+ T cells expressing granzymes, perforin, and NK-associated receptors, frequently misclassified as CD8+ T cells or NK cells.

Genes:
- GZMB, PRF1, NKG7, GNLY, FGFBP2, GZMH, CCL5, CST7, CD4, CD3D, CD3E, CD2
- KLRG1, CX3CR1, ZEB2, TBX21, ADGRG1, PRF1, SPON2, GZMA, HLA-C, B2M

### CD4+ Effector Memory T cells (CD4 TEM)

Description: Antigen-experienced CD4+ T cells residing in or circulating through PBMCs that lack CCR7 and SELL expression but express effector-associated genes and tissue-homing receptors.

Genes:
- IL7R, LTB, CD4, CCR6, GPR183, ANXA1, S100A4, S100A10, S100A6, CD52, CD2, CD3D
- CD3E, CD3G, KLRB1, FOS, JUN, DUSP1, ZFP36, IFNG, CCL5, GZMK, CXCR3, CD44

### CD8+ Effector Memory T cells (CD8 TEM)

Description: Antigen-experienced CD8+ T cells with cytotoxic potential that lack CD4 expression, representing a common source of lineage misclassification for CD4 TEM cells.

Genes:
- CD8A, CD8B, GZMK, CCL5, NKG7, CST7, EOMES, DUSP2, CD2, CD3D, CD3E, CD3G
- LYAR, GZMA, KLRG1, CXCR3, CD247, HCST, S100A4, S100A10, FGFBP2

### Regulatory T cells (Treg)

Description: An immunosuppressive CD4+ T cell subset characterized by high expression of FOXP3 and CD25 (IL2RA) that can be transcriptionally similar to activated CD4 TEM cells.

Genes:
- FOXP3, IL2RA, IKZF2, CTLA4, TIGIT, TNFRSF4, TNFRSF18, BATF, IL10, CD4, CD3D, CD3E
- CD3G, IL7R, LAIR2, RTKN2, FCRL3, S100A4, S100A6, S100A10

## cd8 naive

### CD4+ Naive T cells

Description: Antigen-inexperienced helper T cells that share naive homing markers with CD8+ naive cells but are distinguished by CD4 expression and the absence of CD8 lineage markers.

Genes:
- CD4, CCR7, LEF1, SELL, TCF7, MAL, LDHB, CD27, CD28, IL7R, NOSIP, FLT3LG
- EEF1A1, RPS3, RPL13A, BTG1, TXNIP, GIMAP5, ANXA1, TRABD2B

### CD8+ Central Memory T cells

Description: Antigen-experienced CD8+ T cells that retain lymph node homing capacity while displaying intermediate effector potential and rapid recall capabilities.

Genes:
- CCR7, SELL, CD27, IL7R, CD8A, CD8B, LTB, GZMK, FGFBP2, KLRG1, CXCR3, EOMES
- DUSP1, FOS, JUN, ZFP36, S100A4, S100A6, CD44, ANXA2

### CD8+ Early Effector Memory T cells

Description: Transitional CD8+ memory T cells that have lost naive markers like CCR7 and LEF1, initiating expression of cytotoxic granzymes and tissue-homing chemokine receptors.

Genes:
- CD8A, CD8B, GZMK, LYAR, EOMES, CXCR3, KLRG1, CD27, LTB, DUSP2, NKG7, CST7
- GZMA, PRF1, CCL5, FGFBP2, HCST, CD160, KLRD1, KLRG1

### CD8+ Naive T cells

Description: Quiescent, antigen-inexperienced CD8+ T cells characterized by high expression of lymph node homing receptors and transcription factors maintaining naive pluripotency.

Genes:
- CCR7, LEF1, SELL, TCF7, NOSIP, MAL, LDHB, CD27, CD28, IL7R, FLT3LG, MYC
- EEF1A1, RPS6, RPL13, RPL21, BTG1, JUNB, CD8A, CD8B, TXNIP, SCML1, PIK3IP1, GIMAP5

## cd8 proliferating

### CD4+ Proliferating T cells

Description: Proliferating helper or regulatory T cells undergoing clonal expansion, sharing the same cell-cycle signature as proliferating CD8+ T cells but distinguished by CD4 expression and often enriched for Treg markers like FOXP3 and IL2RA in PBMCs.

Genes:
- MKI67, TOP2A, CD4, CD3D, CD3E, CD3G, IL2RA, FOXP3, PCNA, CENPF, TYMS, CCNB1
- CCNB2, CCNA2, CDK1, NUSAP1, BIRC5, UBE2C, HMGB2, STMN1, TUBA1B, TUBB, H2AFZ, DUT
- RRM2, SMC4, KIF23, ASPM, TPX2, CDCA8

### CD8+ Proliferating T cells

Description: Highly proliferative CD8+ T cells undergoing active cell cycle (S/G2/M phases) in response to antigen stimulation, characterized by high expression of mitotic and DNA replication machinery alongside CD8 lineage markers.

Genes:
- MKI67, TOP2A, PCNA, CENPF, CD8A, CD8B, CD3D, CD3E, CD3G, TYMS, CCNB1, CCNB2
- CCNA2, CDK1, NUSAP1, BIRC5, UBE2C, HMGB2, STMN1, TUBA1B, TUBB, H2AFZ, DUT, RRM2
- MAD2L1, BUB1, CENPE, CENPM, SMC4, KIF2C, KIF11, KIF23, ASPM, DLGAP5, TPX2, CDCA8
- CDCA3, AURKA, PLK1, CEP55

### Non-proliferating Effector CD8+ T cells

Description: Terminally differentiated cytotoxic CD8+ T cells that share high expression of cytolytic effector molecules with proliferating CD8+ T cells but are completely quiescent and lack cell-cycle entry markers like MKI67 and TOP2A.

Genes:
- CD8A, CD8B, CD3D, CD3E, GZMB, GZMH, PRF1, GNLY, NKG7, FGFBP2, FCGR3A, CX3CR1
- KLRG1, TBX21, ZEB2, S100A4, CCL5, CCL4, CST7, PRF1, GZMA, LYAR, IL7R, LTB

### Proliferating NK cells

Description: A rare, highly active cytotoxic innate lymphoid population undergoing proliferation, sharing cell-cycle genes with proliferating CD8+ T cells but lacking CD3/CD8 lineage markers while expressing NK-specific receptors and cytolytic molecules.

Genes:
- MKI67, TOP2A, NCAM1, NKG7, GNLY, PRF1, GZMB, GZMA, KLRD1, KLRF1, FCGR3A, CENPF
- PCNA, TYMS, CCNB1, CDK1, NUSAP1, BIRC5, UBE2C, STMN1, TUBA1B, TUBB, RRM2, CST7
- SPON2, FGFBP2, CLIC3, HOPX, SMC4, BUB1B

## cd8 tcm

### CD4+ Central Memory T cells (CD4+ Tcm)

Description: CD4+ helper T cells with lymph node homing capacity that can be easily misidentified as CD8+ Tcm due to shared expression of memory and homing markers if CD4/CD8 lineage-specific transcripts are weakly captured.

Genes:
- CD4, IL7R, CCR7, SELL, TCF7, CD27, CD28, LTB, LDHB, MAL, GIMAP5, GIMAP4
- ANXA1, IL6R, S1PR1, CD40LG, TNFRSF4, ICOS, CREM, FOS

### CD8+ Central Memory T cells (CD8+ Tcm)

Description: Antigen-experienced CD8+ T cells that traffic through secondary lymphoid organs, characterized by high expression of lymph node homing receptors CCR7 and SELL (L-selectin) alongside memory marker IL7R.

Genes:
- CCR7, SELL, TCF7, LEF1, IL7R, CD27, CD28, LTB, MYC, NOSIP, MAL, LDHB
- CD8A, CD8B, FLT3LG, GIMAP5, GIMAP7, BCL2, S1PR1, EEF1A1

### CD8+ Effector Memory T cells (CD8+ Tem)

Description: Antigen-experienced CD8+ T cells that home to peripheral tissues and exhibit immediate effector function, characterized by the downregulation of CCR7/SELL and upregulation of granzymes and cytolytic transcripts.

Genes:
- GZMK, GZMA, CCL5, EOMES, CD8A, CD8B, DUSP2, LYAR, CD2, CD96, KLRG1, NKG7
- CST7, PRF1, FGFBP2, GZMB, TBX21, CX3CR1, S1PR5, ZEB2

### CD8+ Naive T cells

Description: Mature but antigen-inexperienced CD8+ T cells that share homing markers with Tcm but express higher levels of naive-associated transcription factors and ribosomal proteins, while lacking memory activation signatures.

Genes:
- CCR7, SELL, TCF7, LEF1, IL7R, CD8A, CD8B, IL6R, CD27, BTG1, TOB1, S1PR1
- EEF1B2, RPS27, RPL32, RPL13, RPS18, RPS6, RPL21, RPL18A

## cd8 tem

### CD8+ Effector Memory T Cells (CD8 TEM)

Description: Antigen-experienced CD8+ T cells residing in peripheral blood that lack CCR7 and CD45RA, characterized by high expression of GZMK and CCL5.

Genes:
- GZMK, CCL5, EOMES, CXCR3, CD8A, CD8B, CD3D, CD3E, CD3G, LYAR, DUSP2, KLRG1
- GZMA, FGFBP2, S100A4, ANXA1, IL7R, LTB, CD2, CD27, CD44, ZNF683, RUNX3, ID2

### CD8+ Naive T Cells

Description: Antigen-inexperienced CD8+ T cells characterized by high expression of lymph node homing receptors CCR7 and SELL, and transcription factors TCF7 and LEF1.

Genes:
- CCR7, SELL, LEF1, TCF7, CD27, IL7R, MAL, CD8A, CD8B, CD3D, CD3E, CD3G
- NOSIP, LDHB, EEF1A1, RPS3A, RPL13, RPL21, LTB, MYC

### CD8+ Terminal Effector T Cells (CD8 TEMRA)

Description: Terminally differentiated effector memory CD8+ T cells that re-express CD45RA and exhibit high cytotoxic activity with elevated expression of GZMB, PRF1, and GNLY.

Genes:
- GZMB, PRF1, GNLY, NKG7, FGFBP2, FCGR3A, CX3CR1, KLRD1, KLRG1, ADGRG1, ZEB2, TBX21
- S100A4, SPON2, CLIC3, S100A6, PRF1, GZMH, CD244, KLRF1, CD8A, CD8B

### Gamma-Delta T Cells (gdT)

Description: A specialized T cell lineage expressing gamma and delta T-cell receptor chains that often exhibits a cytotoxic or memory-like transcriptional profile overlapping with CD8+ TEM.

Genes:
- TRDC, TRGC1, TRGC2, TARBP1, GNLY, NKG7, GZMB, GZMK, KLRB1, CD160, KLRC1, KLRD1
- ZNF683, S100A4, CCL5, CD3D, CD3E, CD3G, IL7R, RUNX3

### Natural Killer Cells (NK)

Description: Innate lymphoid cells that share a highly overlapping cytotoxic gene expression profile with CD8+ TEMRA cells but lack CD3 and T-cell receptor complex genes.

Genes:
- NCAM1, NKG7, GNLY, PRF1, GZMB, KLRD1, KLRF1, FCGR3A, SPON2, FGFBP2, CST7, CLIC3
- HOPX, S100A4, CD160, XCL1, XCL2, KLRC1, KLRC2, KLRG1, IL2RB

## cdc1

### AS_DC

Description: AXL+SIGLEC6+ dendritic cells, a transitional DC population sharing properties of both plasmacytoid and classical dendritic cells.

Genes:
- AXL, SIGLEC6, PPP1R14A, CD22, CXCR4, SCHIP1, G551, DAB2, CD5, LILRI4, TCF4, IL3RA
- CD1C, CLEC10A, FCER1A, RUNX2, SPIB, CST3, HLA-DPA1, HLA-DPB1

### Intermediate_Monocytes

Description: A subset of monocytes expressing both CD14 and CD16 (FCGR3A) that can be confused with cDCs due to high expression of MHC class II molecules and antigen presentation genes.

Genes:
- CD14, FCGR3A, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, AIF1, FTL, FTH1, LST1, COTL1, S100A8
- S100A9, LYZ, FCN1, GRN, VNN2, CD36, ITGAM, CSF1R

### cDC1

Description: Classical dendritic cell type 1, specialized in cross-presentation of intracellular antigens to CD8+ T cells via the MHC class I pathway.

Genes:
- CLEC9A, XCR1, CADM1, WDFY4, BATF3, FLT3, IDO1, CLNK, CPVL, C1orf54, S100A3, APP
- DPP4, GPR141, KCNK2, PTPN22, S100B, TCF4, IRF8, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, HLA-DRA
- HLA-DRB1

### cDC2

Description: Classical dendritic cell type 2, the major population of myeloid dendritic cells in human blood, highly efficient at presenting extracellular antigens to CD4+ T cells.

Genes:
- CD1C, FCER1A, CLEC10A, SIRPA, COBLL1, ENHO, PKIB, CXCL8, IL1B, S100A9, S100A8, CD1E
- CD2, CD1A, HLA-DQA1, HLA-DQB1, HLA-DRB1, HLA-DRA, CST3, ANXA1, FCN1, LYZ, CSF3R, ITGAM

### pDC

Description: Plasmacytoid dendritic cells, specialized in secreting massive amounts of type I interferons in response to viral nucleic acids.

Genes:
- LILRA4, CLEC4C, PTGDS, TCF4, IRF7, IRF8, GZMB, IL3RA, NRP1, SCT, PLD4, MAP1A
- PACSIN1, SOX4, SPIB, BCL11A, APP, RUNX2, CCDC50, SERPINF1, ITM2C, DERL3, MZB1, JCHAIN

## cdc2

### Classical_Monocytes

Description: A major myeloid lineage in PBMC that is frequently confused with cDC2 due to shared expression of CD1c, CD14, and various S100 alarmin proteins.

Genes:
- CD14, LYZ, S100A9, S100A8, S100A12, FCN1, VCAN, CD300E, CD33, GRN, TYROBP, FCER1G
- CST3, CTSS, MNDA, CFD, SPI1, CEBPD, IER3, MAFB

### Non_Classical_Monocytes

Description: Patrolling monocytes that express CD16 (FCGR3A) and can overlap transcriptionally with cDC2s during automated clustering due to shared myeloid lineage markers.

Genes:
- FCGR3A, MS4A7, LST1, AIF1, CX3CR1, HES4, TCF7L2, RHOC, IFITM3, C1QA, C1QB, C1QC
- CDKN1C, SIGLEC10, LILRB2, LILRA5, SMIM25, MTSS1, C3AR1, PECAM1

### cDC2_A_inflammatory

Description: A subset of classical dendritic cells type 2 (cDC2) characterized by the expression of inflammatory mediators, monocyte-like markers, and rapid response to activation signals.

Genes:
- CD1C, FCER1A, CLEC10A, S100A9, S100A8, LYZ, FCN1, VCAN, CD14, IL1B, CXCL8, CCL3
- CCL4, TNF, NFKBIA, JUN, FOS, IER3, EGR1, CD1e, CD2

### cDC2_B_conventional

Description: The canonical, quiescent subset of cDC2 specialized in antigen presentation, characterized by high expression of MHC class II molecules and classical dendritic cell transcription factors.

Genes:
- CD1C, FCER1A, CLEC10A, HLA-DQA1, HLA-DQB1, HLA-DRB1, HLA-DPA1, HLA-DPB1, CD74, CD86, CD40, FLT3
- ZBTB46, IRF4, CIITA, CD52, ENHO, RUNX3, PKIB, PLD4

## dnt

### Double-negative T cells (dnT)

Description: A rare population of mature T cells lacking both CD4 and CD8 co-receptors, often expressing alpha-beta or gamma-delta T-cell receptors and exhibiting cytotoxic or regulatory functions.

Genes:
- CD3D, CD3E, CD3G, TRADD, TRAC, TRBC1, TRBC2, KLRG1, GZMA, GZMB, PRF1, NKG7
- GNLY, FGFBP2, ADGRG1, ZEB2, TBX21, S100A4, S100A6, IL7R, CD2, CD7, CD247, CST7
- LYAR

### Gamma-delta T cells (gdT)

Description: T cells expressing the gamma-delta TCR chains instead of alpha-beta, which are typically CD4-/CD8- (double-negative) and bridge innate and adaptive immunity.

Genes:
- TRDC, TRGC1, TRGC2, TARBP1, GNLY, NKG7, GZMB, GZMA, PRF1, KLRB1, KLRC1, KLRD1
- CD160, TYROBP, FCER1G, SST, CD3D, CD3E, CD3G, CD247, ZBTB16, IKZF2, RUNX3, HOPX

### Mucosal-Associated Invariant T cells (MAIT)

Description: A specialized population of donor-unrestricted T cells expressing an invariant TCR alpha chain and high levels of KLRB1 (CD161), often presenting as CD8+ or double-negative.

Genes:
- TRAV1-2, KLRB1, SLC4A10, ZBTB16, NCR3, RORC, IL7R, DPP4, GZMK, GZMA, NKG7, CD3D
- CD3E, CD3G, CD247, CD8A, CD8B, CCR6, CXCR6, IKZF2, RUNX3, CEBPB

### Natural Killer cells (NK)

Description: Innate cytotoxic lymphocytes that lack CD3 expression but share a highly overlapping cytotoxic gene expression profile with double-negative T cells.

Genes:
- NCAM1, KLRF1, KLRC1, KLRD1, NKG7, GNLY, PRF1, GZMB, GZMA, FCGR3A, FGFBP2, SPON2
- CD160, XCL1, XCL2, CLIC3, CST7, HOPX, S100A4, S100A6, IL2RB, IL15RA, RUNX3, EOMES

## doublet

### Activated T cell / NK cell (Confused Neighbor)

Description: A highly cytotoxic single T or NK cell that can be misidentified as a doublet due to its high transcriptomic complexity and expression of multiple effector genes.

Genes:
- NKG7, GZMB, GZMA, GNLY, PRF1, CST7, FGFBP2, FCGR3A, SPON2, KLRD1, KLRF1, CD247
- CD8A, CD8B, GZMH, CCL5, CTSWM, HOPX, S100A4, IL32

### B cell - T cell Doublet

Description: An artifactual multicellular aggregate containing both T cells and B cells, characterized by the simultaneous expression of mutually exclusive lineage markers such as CD3 and CD19/CD79A.

Genes:
- CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, CD79A, CD79B, MS4A1, CD19, HLA-DRA, HLA-DRB1
- CD74, LINC00926, BANK1, IL7R, CD4, CD8A, CD8B, LTB, MEF2C, CD2

### Platelet - Monocyte Aggregate

Description: A biological or technical doublet consisting of a monocyte physically associated with platelets, showing co-expression of myeloid markers and platelet-specific transcripts like PPBP and PF4.

Genes:
- CD14, LYZ, S100A8, S100A9, FCN1, VCAN, PPBP, PF4, GNG11, SDPR, TUBB1, CLU
- GP9, ITGA2B, SPARC, TREML1, CST3, TYROBP, FCER1G, HLA-DRA

### T cell - Monocyte Doublet

Description: An artifactual aggregate of a T cell and a monocyte, exhibiting high expression of both T cell receptor complex genes and myeloid-specific S100 family or lysosomal genes.

Genes:
- CD3D, CD3E, CD3G, TRAC, CD14, LYZ, S100A8, S100A9, S100A12, FCN1, VCAN, CD4
- IL7R, CST3, HLA-DRA, HLA-DRB1, CD74, TYROBP, FCER1G, CTSS, CD2, IL32

## eryth

### Megakaryocytes

Description: Platelet-producing myeloid cells that share a common bipotent progenitor with the erythroid lineage, often sharing marker genes or forming doublets with erythroid cells.

Genes:
- PPBP, PF4, GNG11, TUBB1, SDPR, SPARC, CLU, GP9, GP1BA, ITGA2B, MPIG6B, TREML1
- MYL9, ACTN1, F13A1, HIST1H2AC, GRAP2, SH3BGRL2, CD9, CLEC1B, P2RY12, CMRF35, PRKAR2B, NGF
- RGS18, PLEK

### Normoblasts

Description: Nucleated erythroid precursors that are actively dividing or undergoing differentiation, characterized by the co-expression of hemoglobin genes and cell-cycle markers.

Genes:
- HBA1, HBA2, HBB, GYPA, ALAS2, AHSP, SLC4A1, TFRC, GATA1, KLF1, MKI67, TOP2A
- PCNA, CENPF, CDK1, BIRC5, CCNA2, CCNB1, HIST1H4C, HIST1H1D, HIST1H1E, H4C3, H2AC20, H3C2
- DUT, TYMS, HMGB2, NUSAP1

### Plasmacytoid Dendritic Cells

Description: A specialized dendritic cell subset that can be confused with erythroid cells in low-quality datasets due to shared low-complexity or high mitochondrial/ambient RNA profiles.

Genes:
- LILRA4, CLEC4C, PLD4, PTGDS, GZMB, TCF4, IRF7, IRF8, IL3RA, CD4, NRP1, MAP1A
- SCT, PACSIN1, APP, DERL3, MZB1, SEC61A1, TXNDC5, JCHAIN, SPIB, BCL11A, RUNX2, SERPINF1
- ITM2C

### Reticulocytes

Description: Immature, enucleated red blood cells that still retain ribosomes and high levels of globin transcripts, occasionally found in peripheral blood.

Genes:
- HBA1, HBA2, HBB, HBD, HBM, AHSP, ALAS2, SLC25A37, SLC4A1, GYPA, GYPB, KEL
- EPB42, SPTA1, SPTB, ANK1, ADD2, CA1, CA2, HEMGN, BPGM, BLVRB, TFRC, GATA1
- KLF1, MYL4, APOC1, SNCA

## gdt

### CD8_TEMRA

Description: Terminally differentiated effector memory CD8+ T cells re-expressing CD45RA, which share a highly overlapping cytotoxic gene expression program with gamma-delta T cells.

Genes:
- CD8A, CD8B, TRAC, TRBC1, TRBC2, GZMH, GZMB, PRF1, NKG7, GNLY, FGFBP2, FCGR3A
- CX3CR1, KLRG1, ADGRG1, ZEB2, TBX21, S100A4, CCL5, CCL4, HLA-C, CD52

### MAIT

Description: Mucosal-Associated Invariant T cells expressing the TRAV1-2 TCR alpha chain and high levels of CD161 (KLRB1), sharing semi-invariant characteristics and transcriptional regulators with gamma-delta T cells.

Genes:
- TRAV1-2, KLRB1, SLC4A10, ZBTB16, RORC, IL7R, CCR6, DPP4, GZMK, NCR3, ANXA1, CD161
- FURIN, DUSP1, FOS, JUN, IL18RAP, LTB, CD52, GIMAP4

### NK_CD56dim

Description: Mature cytotoxic Natural Killer cells that lack CD3 expression but share almost the entire non-TCR cytotoxic machinery with Vd2 gamma-delta T cells, leading to frequent doublet or misclassification issues.

Genes:
- NCAM1, FCGR3A, NKG7, GNLY, PRF1, GZMB, GZMA, KLRD1, KLRF1, KLRG1, KLRB1, CD160
- SPON2, FGFBP2, CST7, PRF1, HOPX, CLIC3, S100A4, S100A6, SH2D1B, S100B

### Vd1_gdT

Description: A less common peripheral blood gamma-delta T cell subset expressing the Vd1 chain, often displaying a more naive, memory, or tissue-homing phenotype compared to Vd2 cells.

Genes:
- TRDV1, TRGV4, TRGV2, CD8A, CD8B, LEF1, SELL, CCR7, IL7R, TCF7, MAL, CD27
- CD28, MYC, GIMAP5, GIMAP7, LTB, LDHB, NOSIP, EEF1A1

### Vd2_gdT

Description: The predominant gamma-delta T cell subset in human peripheral blood, characterized by Vd2/Vg9 TCR chain expression and a highly cytotoxic, effector-like transcriptional profile.

Genes:
- TRDV2, TRGV9, GZMB, PRF1, NKG7, GNLY, FGFBP2, FCGR3A, CX3CR1, KLRG1, KLRD1, KLRF1
- CD160, EOMES, TBX21, ZBTB16, IKZF2, S100A4, S100A6, S100A10, LGALS1, ANXA1, HOPX, ADGRG1

## hspc

### CD34+ Early Progenitor (HSPC)

Description: Multipotent hematopoietic stem and progenitor cells characterized by high CD34 expression and the capacity to differentiate into multiple lineages.

Genes:
- CD34, AVVP1, SPINK2, SOX4, GATA2, PRSS57, MYL4, CTSG, AZU1, MPO, ELANE, LYZ
- CD38, CD109, PROM1, CRHBP, HLF, MSI2, MEIS1, RUNX1, GATA1, KLF1, HBBP1, HBD
- HBG1, HBG2, ALAS2, AHSP, GYPA, GYPB

### Granulocyte-Monocyte Progenitor (GMP)

Description: Myeloid-biased progenitor cells transitioning from stem-like states toward mature neutrophils, monocytes, and granulocytes.

Genes:
- MPO, ELANE, AZU1, PRTN3, CTSG, RNASE3, DEFA3, DEFA4, LYZ, CST3, CSF3R, CEBPA
- CEBPD, CEBPE, SPI1, CD33, FCGR3A, FCN1, S100A8, S100A9, S100A12, GNLY

### Megakaryocyte-Erythroid Progenitor (MEP)

Description: Lineage-committed progenitors derived from HSPCs that give rise to erythroid cells and megakaryocytes, characterized by early expression of globin and platelet-specific genes.

Genes:
- GATA1, KLF1, TAL1, ZFPM1, AHSP, ALAS2, GYPA, GYPB, HBD, HBG1, HBG2, HBB
- HBA1, HBA2, CA1, SLC4A1, EPB42, GP1BA, GP9, ITGA2B, MPL, PLEK, PF4, PPBP
- SDPR

### Plasmacytoid Dendritic Cell (pDC)

Description: A specialized dendritic cell lineage producing high levels of type I interferons, often sharing progenitor-like transcriptional signatures with HSPCs.

Genes:
- LILRA4, CLEC4C, IL3RA, TCF4, IRF7, IRF8, PLD4, GZMB, SERPINF1, ITM2C, MAP1A, PACSIN1
- SCT, NRP1, APP, DERL3, MZB1, TXNIP, SPIB, CCDC50

## ilc

### ILC3

Description: Innate lymphoid cells type 3 that express RORC and KIT, producing IL-22 and IL-17 to regulate mucosal immunity and tissue homeostasis.

Genes:
- KIT, IL23R, RORC, AHR, IL1R1, LST1, IL22, CSF2, LTA, LTB, TNFSF11, CD2
- KLRB1, TMEM176A, TMEM176B, PLXND1, GPR183, IL7R, CD4, IKZF3

### MAIT cells

Description: Mucosal-associated invariant T cells that express the semi-invariant TCR alpha chain TRAV1-2 and high levels of KLRB1 (CD161), often transcriptionally mimicking ILCs.

Genes:
- TRAV1-2, KLRB1, SLC4A10, DPP4, ZBTB16, RORC, IL7R, GZMK, NCR3, IKZF2, CD161, CCR6
- CXCR6, ANXA1, LTB, DUSP1, FOS, JUN, CD8A, CD8B

### NK cells

Description: Cytotoxic innate lymphocytes that share many transcriptional features with ILCs but are distinguished by high expression of perforin, granzymes, and killer cell lectin-like receptors.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMA, KLRD1, KLRF1, KLRG1, FCGR3A, NCAM1, CD244, CST7
- HOPX, SPON2, CLIC3, S1PR5, FGFBP2, PRF1, GZMM, CTS6, CD160, XCL1, XCL2, KLRC1
- KLRC2

### gamma-delta T cells

Description: T cells expressing the gamma-delta TCR chains that exhibit innate-like rapid effector functions and overlap significantly with ILC and NK cell transcriptional profiles.

Genes:
- TRDC, TRGC1, TRGC2, TARBP1, CD160, KLRG1, KLRC2, KLRC3, GZMB, GZMA, GNLY, NKG7
- PRF1, SST, CD8A, CD8B, RUNX3, IKZF2, ZBTB16, IL7R

## mait

### Effector Memory CD8+ T cells

Description: A major CD8+ T cell population in PBMCs that lacks TRAV1-2 and SLC4A10 but shares high expression of cytotoxic molecules and chemokine receptors with MAIT cells, leading to frequent misannotation.

Genes:
- CD8A, CD8B, GZMK, GZMH, GZMB, PRF1, NKG7, EOMES, TBX21, CD27, LTB, CXCR3
- CCL5, CST7, LYAR, FGFBP2, KLRG1, CD244, S100A4, S100A6

### MAIT CD4- CD8- (DN)

Description: A double-negative (CD4- CD8-) subset of MAIT cells in PBMCs that shares core MAIT transcriptional programs but lacks CD8 co-receptor expression.

Genes:
- TRAV1-2, TRAJ33, KLRB1, SLC4A10, ZBTB16, RORC, IL7R, DPP4, IKZF2, IL18RAP, CCR6, CD161
- GZMK, FASLG, TNFSF10, RUNX3, CD2, CD3D, CD3E, CD3G

### MAIT CD8+

Description: The predominant subset of mucosal-associated invariant T (MAIT) cells in human peripheral blood, characterized by CD8 expression, semi-invariant TCR alpha chain, and high levels of IL-18R1 and CD161.

Genes:
- TRAV1-2, TRAJ33, KLRB1, SLC4A10, ZBTB16, RORC, CD8A, CD8B, IL7R, DPP4, NCR3, GZMK
- GZMB, PRF1, NKG7, GNLY, FGFBP2, FCGR3A, CX3CR1, KLRG1, KLRD1, HCST, CD244, CD161

### Natural Killer (NK) cells

Description: Innate lymphoid cells that share high expression of CD161 (KLRB1), C-type lectin receptors, and cytotoxic effector genes with MAIT cells, but lack CD3 and TCR expression.

Genes:
- NCAM1, NCR1, FCGR3A, NKG7, GNLY, PRF1, GZMB, GZMA, KLRD1, KLRF1, KLRG1, CD160
- XCL1, XCL2, SPON2, FGFBP2, CST7, CLIC3, HOPX, S100A4

## nk

### CD56bright CD16minus NK

Description: The cytokine-producing, immunomodulatory NK cell subset in PBMCs, characterized by high CD56 expression, low or absent CD16, and high expression of GZMK and chemokines like XCL1.

Genes:
- NCAM1, SELL, IL7R, GZMK, KLRC1, XCL1, XCL2, CSF2, IFNG, TNF, LTB, CD27
- IL2RB, CAPG, RUNX2, TCF7, SOX4, MYC, GPR183, CCR7

### CD56dim CD16plus NK

Description: The major cytotoxic NK cell subset in peripheral blood, characterized by high expression of CD16 (FCGR3A), perforin, and granzymes, specialized in rapid target cell lysis.

Genes:
- FCGR3A, FGFBP2, CX3CR1, PRF1, GZMB, GZMH, SPON2, KLRF1, KLRG1, S1PR5, ADGRG1, CLIC3
- NKG7, GNLY, CST7, TBX21, ZEB2, PRF1, HCST, CD244, KLRD1, KLRD1, PTGDR, S100A4

### CD8plus Effector T cells

Description: A major T cell population in PBMCs that shares cytotoxic machinery with NK cells but is distinguished by the expression of the T-cell receptor complex and CD8 co-receptors.

Genes:
- CD8A, CD8B, CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, GZMK, GZMA, EOMES, RUNX3
- CD27, LTB, DUSP2, CD2, IL7R, KLRG1, CXCR3, CCL5

### Gamma-Delta T cells

Description: An unconventional T cell lineage expressing gamma and delta TCR chains that bridges innate and adaptive immunity, often sharing transcriptional profiles and marker genes with NK cells.

Genes:
- TRDC, TRGC1, TRGC2, CD3D, CD3E, CD2, KLRB1, KLRC2, KLRC3, NKG7, GNLY, GZMB
- GZMH, SST, TARDBP, CD160, ZBTB16, IKZF2, LEF1, CD244

## nk proliferating

### NK CD56bright

Description: An immunomodulatory, cytokine-producing NK cell subset characterized by high CD56 (NCAM1) expression, low cytotoxicity, and lack of CD16 (FCGR3A).

Genes:
- NCAM1, SELL, KLRC1, GZMK, IL7R, LTB, XCL1, XCL2, CSF2, IFNG, TNFSF10, CAPG
- CD44, RUNX2, GPR183, IL2RB, CD2, CD27, CST7, CTS1

### NK CD56dim

Description: The mature, highly cytotoxic majority NK cell subset in peripheral blood, characterized by high CD16 (FCGR3A) and granzyme/perforin expression.

Genes:
- FCGR3A, FGFBP2, CX3CR1, PRF1, GZMB, GZMA, GNLY, NKG7, KLRF1, KLRG1, SPON2, CLIC3
- S100A4, S100A6, PRF1, ADGRG1, ZEB2, TBX21, HOPX, CST7

### NK Proliferating

Description: A rare, actively cycling natural killer cell population in PBMCs characterized by high expression of proliferation markers alongside cytotoxic effector molecules.

Genes:
- MKI67, TOP2A, CENPF, PCNA, CDK1, BIRC5, CCNB1, CCNA2, NUSAP1, UBE2C, HMGB2, STMN1
- TYMS, DUT, RRM2, CEP55, KIF2C, KIF11, AURKA, AURKB, PLK1, CENPE, CENPA, NKG7
- GNLY, PRF1, GZMB, FGFBP2, FCGR3A, KLRD1

### T Proliferating

Description: Actively dividing T cells (often CD8+ or gamma-delta T cells) that share a strong mitotic signature with proliferating NK cells but are distinguished by T-cell receptor complex expression.

Genes:
- MKI67, TOP2A, CENPF, PCNA, CDK1, BIRC5, CCNB1, CCNA2, NUSAP1, UBE2C, HMGB2, STMN1
- TYMS, DUT, RRM2, CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, CD8A, CD8B, IL7R
- CD4, LTB, LDHB, TUBA1B, TUBB, H2AFZ

## nk_cd56bright

### MAIT_cells

Description: Mucosal-associated invariant T cells that share high expression of CD161 (KLRB1) and IL-7R with CD56bright NK cells, often leading to annotation confusion.

Genes:
- TRAV1-2, KLRB1, SLC4A10, ZBTB16, RORC, IL7R, DPP4, NCR3, GZMK, CD161, CCR6, ANXA1
- CD8A, CD8B, RUNX3, IKZF2, FURIN, DUSP2, IL18RAP, LTB

### NK_CD56bright_canonical

Description: Canonical CD56bright NK cells characterized by high cytokine production capacity, expression of homing receptors like CD62L (SELL), and low baseline cytotoxicity.

Genes:
- NCAM1, SELL, IL7R, GZMK, KLRC1, KLRD1, LTB, IL2RB, CD44, XCL1, XCL2, CSF2
- IFNG, TNF, CD2, CD27, TCF7, CCR7, RUNX2, ZBTB16, MYC, GPR183, CAPG, SOX4

### NK_CD56dim

Description: The major mature cytotoxic NK cell subset in peripheral blood, characterized by high CD16 (FCGR3A) and perforin/granzyme B expression.

Genes:
- FCGR3A, FGFBP2, CX3CR1, GZMB, PRF1, NKG7, GNLY, KLRF1, KLRG1, SPON2, ADGRG1, S1PR5
- ZEB2, TBX21, PRF1, CLIC3, CST7, HOPX, S100A4, S100A6, ANXA1, CD247

### gamma_delta_T_cells

Description: Unconventional T cells expressing the gamma-delta T-cell receptor that share cytotoxic and NK-like receptor profiles, frequently misannotated as NK cells.

Genes:
- TRDC, TRGC1, TRGC2, TARBP1, CD160, KLRB1, KLRC2, KLRC3, GZMB, GNLY, NKG7, CD8A
- CD8B, EOMES, RUNX3, S1PR5, ZNF683, IKZF2, FYN, LCK

## pdc

### Axl+ Siglec6+ dendritic cell (AS-DC)

Description: A transitional dendritic cell population sharing features of both pDCs and conventional DCs, characterized by high expression of AXL and SIGLEC6.

Genes:
- AXL, SIGLEC6, PPP1R14A, CD2, CX3CR1, CD5, IL1R2, LST1, FGR, MS4A6A, CD1C, CLEC10A
- FCER1A, ENHO, S100A9, S100A8, LYZ, C1orf54, RUNX3, DIPK2A, LILRB2, ITGAX

### Classical pDC

Description: Classical plasmacytoid dendritic cells specialized in rapid, massive secretion of type I interferons in response to viral nucleic acids.

Genes:
- CLEC4C, LILRA4, PTGDS, GZMB, TCF4, IRF7, IRF8, IL3RA, NRP1, PLD4, SCT, MAP1A
- APP, PACSIN1, SOX4, SPIB, BCL11A, RUNX2, TXNIP, SERPINF1, ITM2C, DERL3, LAMP5, CCDC50
- PTPRS

### Pre-B cell

Description: Developing B cell progenitors that can contaminate PBMC fractions and share several transcriptional regulators and surface markers with pDCs.

Genes:
- VPREB1, VPREB3, DNTT, MME, CD19, MS4A1, CD24, CD79A, CD79B, SOX4, ADA, RAG1
- RAG2, EBF1, PAX5, IL7R, STAP1, SPRY1, BLNK, CD38

### cDC1

Description: Conventional type 1 dendritic cells specialized in cross-presentation of intracellular antigens to CD8+ T cells.

Genes:
- CLEC9A, CADM1, XCR1, WDFY4, BATF3, FLT3, IDO1, CPVL, CLNK, S100B, C12orf75, APP
- DPP4, LTA4H, ANPEP, GPR141, KCNK17, PPM1N, SNX22, B3GAT2

## plasmablast

### Activated B Cell

Description: A transitional B cell state undergoing activation that shares some activation markers with plasmablasts but retains high expression of pan-B-cell markers and MHC class II.

Genes:
- CD19, MS4A1, CD79A, CD79B, CD22, CD83, CD86, MYC, CCND2, EBI3, CLEC17A, FGR
- NFKB1, REL, JUN, FOS, DUSP1, DUSP2, IER3, CD40, TNFRSF13B, HLA-DRA, HLA-DQA1, HLA-DQB1

### IgA Plasmablast

Description: A mucosal-homing subtype of antibody-secreting cells in PBMC characterized by high expression of IgA heavy chains and J-chain.

Genes:
- IGHA1, IGHA2, IGHG1, IGHG2, JCHAIN, MZB1, PRDM1, IRF4, XBP1, SEC61A1, SSR4, FKBP11
- TXNDC5, DERL3, HERPUD1, SDF2L1, CREB3L2, CD38, SDC1, TNFRSF17, SLAMF7, CD27, ITGA4, CXCR4

### IgG Plasmablast

Description: A systemic-homing subtype of antibody-secreting cells in PBMC characterized by high expression of IgG heavy chains and endoplasmic reticulum stress response genes.

Genes:
- IGHG1, IGHG2, IGHG3, IGHG4, JCHAIN, MZB1, PRDM1, IRF4, XBP1, SEC61A1, SSR4, FKBP11
- TXNDC5, DERL3, HERPUD1, SDF2L1, CREB3L2, CD38, SDC1, TNFRSF17, SLAMF7, CD27, ITGA4, CXCR4

### Plasmacytoid Dendritic Cell

Description: A distinct lineage of dendritic cells that can be confused with plasmablasts due to shared high secretory capacity, ER-related gene expression, and CD4/CD38 expression.

Genes:
- CLEC4C, LILRA4, IL3RA, TCF4, IRF7, IRF8, GZMB, NRP1, PACSIN1, PLD4, MAP1A, SCT
- APP, SOX4, SPIB, BCL11A, RUNX2, TXNIP, CD4, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1

## platelet

### Megakaryocyte-like Platelets

Description: Classic platelet population in PBMCs characterized by high expression of megakaryocyte-lineage transcripts, clotting factors, and cytoskeletal proteins involved in activation.

Genes:
- PPBP, PF4, GNG11, TUBB1, SDPR, SPARC, CLU, GP9, GP1BA, ITGA2B, MPIG6B, TREML1
- F13A1, MYL9, ACTB, TMSB4X, HIST1H2AC, P2RY12, NRGN, GRAP2, SH3BGRL3, CD9, CLEC1B, RGS18
- PRKAR2B

### Plasmacytoid Dendritic Cells

Description: A rare immune cell type in PBMCs often confused with platelets in low-quality single-cell datasets due to shared ambient RNA contamination or overlapping low-complexity transcriptomic profiles.

Genes:
- LILRA4, CLEC4C, TCF4, IL3RA, SCT, NRP1, PLD4, MAP1A, GZMB, SERPINF1, ITM2C, SPIB
- IRF7, IRF8, PACSIN1, APP, SOX4, DERL3, MZB1, TXNIP, JCHAIN, C1QA, C1QB

### Platelet-Monocyte Aggregates

Description: Physical doublets or biological aggregates of monocytes and platelets that exhibit a hybrid transcriptomic signature containing both myeloid and megakaryocytic marker genes.

Genes:
- CD14, LYZ, S100A8, S100A9, S100A12, FCN1, VCAN, PPBP, PF4, GNG11, TUBB1, GP9
- ITGA2B, CD9, CST3, GRN, TYROBP, FCER1G, MS4A6A, CTSS, LST1, AIF1, CFD

## treg

### CD4+ Memory T cell

Description: Antigen-experienced CD4+ helper T cells that share many activation and memory markers with Effector Tregs but lack the lineage-defining FOXP3 expression.

Genes:
- IL7R, S100A4, S100A10, S100A6, ANXA1, CD4, CD3D, CD3E, CD3G, CD44, LTB, IL32
- GIMAP7, AOP2, LGALS1, CD52, FOS, JUN, DUSP1, ZFP36

### CD4+ Naive T cell

Description: A major neighboring CD4+ T cell subset that can be confused with Naive Tregs due to shared naive marker expression but lacks FOXP3 and IL2RA.

Genes:
- CCR7, LEF1, SELL, TCF7, MAL, CD27, IL7R, CD4, LDHB, NOSIP, EEF1B2, FLT3LG
- GIMAP5, GIMAP1, BTG1, MYC, S100A10, S100A4, CD3D, CD3E

### Effector Treg

Description: Highly suppressive, activated regulatory T cells expressing high levels of FOXP3, CTLA4, and various HLA class II and TNF receptor superfamily molecules.

Genes:
- FOXP3, IL2RA, IKZF2, PRDM1, HLA-DRB1, HLA-DRA, CD74, ICOS, TNFRSF4, TNFRSF9, TNFRSF18, CTLA4
- TIGIT, LAG3, HAVCR2, MAF, MYO1G, ANXA1, LGALS1, S100A4, S100A6, CD147, IL1RL1, CCR4

### Naive Treg

Description: Resting or naive regulatory T cells characterized by the co-expression of FOXP3 and IL2RA alongside classical naive T cell markers like CCR7 and SELL.

Genes:
- FOXP3, IL2RA, CCR7, LEF1, SELL, TCF7, IL7R, CD4, MAL, CD27, NOSIP, LDHB
- EEF1A1, FM04, CCR6, GIMAP5, GIMAP7, MYC, BTG1, FLT3LG

