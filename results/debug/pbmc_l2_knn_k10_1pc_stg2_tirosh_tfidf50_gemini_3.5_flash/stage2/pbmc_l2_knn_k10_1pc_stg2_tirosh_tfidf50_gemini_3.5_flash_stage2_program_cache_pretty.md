# Stage-2 Precomputed Programs

- tissue: PBMC
- n_program_genes: 50
- n_cached_cell_types: 31

## asdc

### ASDC

Description: AXL+ SIGLEC6+ dendritic cells (ASDC) represent a transitional dendritic cell state sharing transcriptional features of both plasmacytoid and conventional dendritic cells.

Genes:
- AXL, SIGLEC6, PPP1R14A, CD22, CX3CR1, CD1C, CLEC10A, FCER1A, LILRA4, IL3RA, CLEC4C, NRP1
- TCF4, SCT, RUNX2, GZMB, CLIC2, APP, SPI1, IRF8, IRF4, HLA-DQA1, HLA-DQB1, HLA-DPA1
- HLA-DPB1, HLA-DRB1, CD86, CD40, ITGAX, ZBTB46

### cDC1

Description: Conventional type 1 dendritic cells (cDC1s) are a rare myeloid dendritic cell subset specialized in cross-presentation of extracellular antigens to CD8+ T cells.

Genes:
- CLEC9A, CADM1, XCR1, WDFY4, BATF3, IRF8, ID2, CPVL, C1orf54, CLNK, APP, HLA-DQA1
- HLA-DPB1, HLA-DRB1, FLT3, BTLA, S100A4, DPP4, ANPEP, CD40

### cDC2

Description: Conventional type 2 dendritic cells (cDC2s) are the major population of myeloid dendritic cells in human blood, specialized in MHC class II antigen presentation and CD4+ T cell activation.

Genes:
- CD1C, CLEC10A, FCER1A, ENHO, PKIB, COBLL1, HLA-DQA1, HLA-DQB1, HLA-DRB1, HLA-DPA1, HLA-DPB1, CD1E
- GSN, ANXA1, S100A9, S100A8, LYZ, CST3, FCN1, ITGAX, CSF1R, SIRPA, CD86, CD2
- CX3CR1

### pDC

Description: Plasmacytoid dendritic cells (pDCs) are specialized, round-shaped immune cells that secrete massive amounts of type I interferons in response to viral infections.

Genes:
- LILRA4, CLEC4C, IL3RA, TCF4, NRP1, SCT, GZMB, IRF7, IRF8, PACSIN1, PLD4, MAP1A
- LAMP5, SPIB, PTGDS, SOX4, CCDC50, DERL3, MZB1, JCHAIN, TXNIP, APP, SERPINF1, ITM2C
- SPIB

## b intermediate

### B memory

Description: Antigen-experienced B cells that express CD27 and switched immunoglobulin isotypes, representing the mature end of the spectrum that intermediate B cells are transitioning toward.

Genes:
- MS4A1, CD19, CD27, AIM2, COBLL1, CLEC17A, IGHG1, IGHG3, IGHA1, IGHA2, TXNIP, CD80
- CD86, TNFRSF13B, S100A4, AHNAK, FCRL1, FCRL3, FCRL5, ITGB2, CD44

### B naive

Description: Mature, antigen-inexperienced B cells characterized by high expression of IGHD, IGHM, and TCL1A, which can be confused with intermediate B cells due to overlapping naive marker expression.

Genes:
- MS4A1, CD19, IGHD, IGHM, TCL1A, IL4R, FCER2, CD22, CD79A, CD79B, BACH2, CXCR5
- CCR7, YBX3, PLD4, HVCN1, SELL, CD24, BLNK, BTG1, SWAP70, LINC00926

### Plasmablast

Description: Highly active, antibody-secreting B cell precursors characterized by downregulation of MS4A1 (CD20) and massive upregulation of endoplasmic reticulum stress and secretory pathway genes.

Genes:
- MZB1, PRDM1, IRF4, XBP1, CD38, SDC1, TNFRSF17, IGHG1, IGHG2, IGHG3, IGHA1, IGKC
- IGLC2, IGLC3, JCHAIN, FKBP11, SEC61A1, SSR4, DERL3, HERPUD1, TXNDC5

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

Description: Classical resting naive B cells circulating in peripheral blood, characterized by high expression of IGHD, TCL1A, and FCER2 (CD23).

Genes:
- MS4A1, CD19, CD22, FCER2, TCL1A, IL4R, IGHD, IGHM, CD72, CD79A, CD79B, HVCN1
- CXCR5, CCR7, SELL, BLNK, BTG1, YBX3, PLD4, LINC00926, SWAP70, FAIM, CD52, MARCKS
- P2RX5

### Switched Memory B cell

Description: Antigen-experienced B cells that have undergone class-switch recombination to IgG or IgA and lack IGHD and IGHM expression.

Genes:
- MS4A1, CD19, CD27, CD38, IGHG1, IGHG2, IGHA1, IGHA2, TXNIP, FCRL5, CD83, CD86
- CLEC16A, CD24, AHNAK, S100A10, S100A4, ITGB2, LST1, AIF1, COBLL1, CD44

### Transitional B cell

Description: Immature B cells recently emigrated from the bone marrow to the peripheral blood, representing an intermediate developmental stage between pro/pre-B cells and mature naive B cells.

Genes:
- MS4A1, CD19, TCL1A, IGHD, IGHM, VPREB3, SOX4, CD24, CD38, CD9, PLD4, ADA
- MME, DNTT, RAG1, RAG2, CD72, IL4R, FCER2, LINC00926

### Unswitched Memory B cell

Description: Memory B cells that have undergone antigen selection but retain IgM and IgD expression, sharing high transcriptional similarity and marker expression with naive B cells but distinguished by CD27.

Genes:
- MS4A1, CD19, CD27, IGHM, IGHD, AIM2, COBLL1, CLEC17A, CD84, TXNIP, LTB, CD52
- MYC, GPR18, CCR6, TNFRSF13B, S100A4, S100A6, FCRL1, FCRL3, CD24

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
- GZMB, PRF1, NKG7, GNLY, FGFBP2, CX3CR1, GZMH, GZMA, PRF1, FCGR3A, SPON2, KLRG1
- KLRD1, ZEB2, TBX21, ADGRG1, S1PR5, CCL5, CCL4, CCL3, CST7, CD244, HOPX, ID2
- RUNX3

### CD4+ Effector Memory T Cells (CD4+ TEM)

Description: Antigen-experienced CD4+ T cells lacking lymph node homing receptors that can express lower levels of granzymes (predominantly GZMK) without full commitment to the classical CD4+ CTL phenotype.

Genes:
- IL7R, LTB, CD4, CCR6, ANXA1, CD52, S100A4, S100A10, S100A6, CD2, CD3E, CD3D
- CD3G, TRAC, GZMK, LYAR, DUSP2, CD27, FOS, JUN

### CD8+ Effector Memory T Cells (CD8+ TEMRA)

Description: Terminally differentiated cytotoxic CD8+ T cells that re-express CD45RA and share an almost identical cytotoxic gene expression profile with CD4+ CTLs, leading to frequent annotation confusion.

Genes:
- CD8A, CD8B, GZMH, GZMB, PRF1, NKG7, GNLY, FGFBP2, CX3CR1, KLRG1, FCGR3A, S1PR5
- ZEB2, TBX21, ADGRG1, CCL5, CCL4, CST7, EOMES, RUNX3, CD244, SPON2, KLRD1, GZMA

### Natural Killer Cells (NK)

Description: Innate lymphoid cells that lack T-cell receptor components (CD3D/E/G) but express high levels of cytotoxic mediators and NK-specific receptors, often transcriptionally overlapping with CD4+ CTLs.

Genes:
- NCAM1, NCR1, NCR3, FCGR3A, NKG7, GNLY, PRF1, GZMB, GZMA, KLRD1, KLRF1, KLRK1
- CD160, XCL1, XCL2, SPON2, FGFBP2, CST7, CLIC3, HOPX, S1PR5, RUNX3, EOMES

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

Description: Activated CD4+ T cells undergoing active clonal expansion and cell cycle progression, characterized by high expression of mitotic and DNA replication machinery.

Genes:
- MKI67, TOP2A, CENPF, CDK1, NUSAP1, BIRC5, CCNB1, CCNB2, CCNA2, CDC20, CDCA8, CDCA3
- AURKA, AURKB, PLK1, UBE2C, CENPE, CENPM, TPX2, KIF11, KIF2C, KIF23, SMC4, SMC2
- DUT, TYMS, RRM2, PCNA, MCM2, MCM4, MCM6, CD4, IL7R, CD3D, CD3E, CD3G

### CD8+ Proliferating T cells

Description: Proliferating CD8+ cytotoxic T cells that share cell-cycle markers with proliferating CD4+ T cells but are distinguished by CD8 co-receptor and cytolytic effector molecule expression.

Genes:
- MKI67, TOP2A, CENPF, CDK1, NUSAP1, BIRC5, CD8A, CD8B, GZMB, PRF1, NKG7, GNLY
- CD3D, CD3E, CD3G, CCNB1, CCNB2, CCNA2, CDC20, CDCA8, AURKB, UBE2C, KIF11, TYMS
- RRM2, PCNA

### Plasmablasts

Description: Highly proliferative, antibody-secreting B-cell precursors that express high levels of immunoglobulin genes and endoplasmic reticulum stress response factors alongside cell-cycle genes.

Genes:
- MZB1, PRDM1, IRF4, XBP1, CD38, SDC1, IGHG1, IGHG2, IGHG3, IGHA1, IGKC, IGLC2
- IGLC3, JCHAIN, MKI67, TOP2A, CENPF, CDK1, NUSAP1, BIRC5, CCNB1, CCNB2, CCNA2, CDC20
- CDCA8

### Proliferating NK cells

Description: A rare, highly active population of natural killer cells undergoing mitotic division, lacking CD3 expression while expressing classic NK lineage and cytotoxic markers.

Genes:
- MKI67, TOP2A, CENPF, CDK1, NUSAP1, BIRC5, NCAM1, KLRD1, KLRF1, NKG7, GNLY, GZMB
- PRF1, FCGR3A, TYROBP, CCNB1, CCNB2, CCNA2, CDC20, CDCA8, AURKB, UBE2C, KIF11

## cd4 tcm

### CD4+ Central Memory T cells (CD4+ TCM)

Description: Antigen-experienced CD4+ T cells characterized by the expression of lymph node homing receptors CCR7 and L-selectin (SELL) along with survival marker IL7R, lacking immediate effector function.

Genes:
- CCR7, SELL, TCF7, LEF1, IL7R, CD4, MAL, CD27, CD28, MYC, NOSIP, LDHB
- EEF1A1, TPT1, IL2, CD3D, CD3E, CD3G, FLT3LG, ITGB1, GIMAP5, GIMAP7, ANXA1, LTB

### CD4+ Effector Memory T cells (CD4+ TEM)

Description: Antigen-experienced CD4+ T cells that have lost CCR7 and SELL expression, allowing them to home to peripheral tissues where they can exert rapid effector functions upon re-stimulation.

Genes:
- S100A4, GZMA, GZMK, FGFBP2, LYAR, ANXA1, CD52, IL32, CD44, ITGB1, LGALS1, CORO1A
- ACTG1, COTL1, LMNA, CD2, CD3E, CD3D, RUNX3, CCL5, NKG7, CST7

### CD4+ Naive T cells

Description: Mature but antigen-unexperienced CD4+ T cells that share many homing markers with TCM cells but express higher levels of naive-specific transcription factors like LEF1 and lack memory activation markers.

Genes:
- CCR7, SELL, TCF7, LEF1, IL7R, CD4, MAL, CD27, IL6R, CCR6, TOX, TXNIP
- BTG1, EEF1B2, RPS27, RPL13, RPL32, RPS3A, RPS18, RPL21

### Regulatory T cells (Tregs)

Description: A specialized lineage of CD4+ T cells dedicated to suppressing immune responses and maintaining self-tolerance, characterized by high expression of FOXP3 and IL2RA (CD25).

Genes:
- FOXP3, IL2RA, IKZF2, CTLA4, TNFRSF4, TNFRSF18, TIGIT, LAIR2, IL10, CD4, RTKN2, FCRL3
- AC133893.1, CD109, ICA1, BATF, PRDM1, ANXA2, CAPG, S100A10

## cd4 tem

### CD4+ Central Memory T cells (CD4 TCM)

Description: Antigen-experienced CD4+ T cells that retain lymph node homing receptors CCR7 and CD62L (SELL) and lack immediate cytotoxic effector function.

Genes:
- IL7R, CCR7, SELL, CD27, CD28, LTB, MAL, CD4, GIMAP7, GIMAP5, TCF7, LEF1
- NOSIP, LDHB, CD3D, CD3E, CD3G, EEF1A1, TPT1, MYC

### CD4+ Cytotoxic T Lymphocytes (CD4 CTL)

Description: A highly cytotoxic subset of CD4+ T cells expressing granzyme B, perforin, and NK-associated receptors, often expanded in chronic viral infections.

Genes:
- GZMB, PRF1, GNLY, NKG7, FGFBP2, ADGRG1, CX3CR1, ZEB2, TBX21, EOMES, KLRD1, KLRG1
- SPON2, S100A4, CD244, PRF1, GZMH, CST7, CCL4, CCL5, HLA-C, B2M

### CD4+ Effector Memory T cells (CD4 TEM)

Description: Antigen-experienced CD4+ T cells lacking CCR7 and CD62L but expressing tissue-homing chemokine receptors and effector molecules like GZMK.

Genes:
- COTL1, S100A4, S100A6, ANXA1, IL7R, CD4, LTB, GIMAP7, GIMAP4, GIMAP5, CD52, FGL2
- KLRG1, CXCR3, CCR5, GZMK, GZMA, DASP1, DUSP2, JUNB, FOS, ZFP36, IFNG, CCL5
- CD2, CD3D, CD3E, CD3G, HCST, S100A10

### CD8+ Effector Memory T cells (CD8 TEM)

Description: Antigen-experienced CD8+ T cells that express intermediate levels of cytolytic molecules like GZMK and lack CD4 expression, frequently misclassified as CD4 TEM due to low CD4/CD8 transcript detection.

Genes:
- CD8A, CD8B, GZMK, GZMA, CCL5, NKG7, CST7, EOMES, DUSP2, CD2, CD247, KLRG1
- LYAR, HCST, FGFBP2, GZMH, PRF1, CD3D, CD3E, CD3G

### Natural Killer T cells (NKT)

Description: A specialized T cell lineage sharing properties of both T cells and Natural Killer cells, expressing CD3 alongside NK-associated C-type lectin receptors.

Genes:
- NKG7, GNLY, GZMB, PRF1, KLRB1, KLRC1, KLRD1, CD3D, CD3E, CD3G, CD247, FCER1G
- TYROBP, HCST, ZBTB16, IL2RB, CD160, FGFBP2, S100A4, CST7

## cd8 naive

### CD4+ Naive T cells

Description: A highly transcriptionally similar CD4+ counterpart to CD8+ naive T cells, sharing naive markers like CCR7 and LEF1 but distinguished by CD4 expression and the absence of CD8A/B.

Genes:
- CD4, IL7R, LEF1, SELL, CCR7, TCF7, MAL, NOSIP, LDHB, CD27, GIMAP5, GIMAP4
- LTB, FLT3LG, EEF1A1, RPS27, RPL13, RPL21, CD3D, CD3E, CD3G, S1PR1, TXNIP

### CD8+ Central Memory T cells (Tcm)

Description: Antigen-experienced CD8+ T cells that retain lymph node homing receptors CCR7 and SELL but express higher levels of memory-associated genes like IL7R, S100A4, and immediate-early activation genes.

Genes:
- CCR7, SELL, CD27, IL7R, CD8A, CD8B, LTB, GIMAP5, ANXA1, CD44, S100A4, S100A10
- IL8, CXCR3, CD3D, CD3E, CD3G, ZFP36, FOS, JUN, DUSP1

### CD8+ Naive T cells (True)

Description: True CD8+ naive T cells characterized by high expression of lymph node homing receptors CCR7 and SELL, transcription factors LEF1 and TCF7, and a lack of cytotoxic effector molecules.

Genes:
- LEF1, SELL, CCR7, TCF7, NOSIP, MAL, LDHB, CD27, CD8A, CD8B, IL7R, FLT3LG
- MYC, EEF1A1, RPS27, RPL13, RPL21, LTB, GIMAP5, GIMAP4, TOX, S1PR1, TXNIP, CD3D
- CD3E, CD3G

### CD8+ Stem Cell Memory T cells (Tscm)

Description: A rare, long-lived memory subset that is transcriptionally almost identical to naive CD8+ T cells but distinguished by the upregulation of CXCR3, FAS (CD95), and low levels of effector-associated genes.

Genes:
- CCR7, SELL, TCF7, LEF1, CD27, CD8A, CD8B, IL7R, CXCR3, FAS, IL2RB, KLRG1
- GZMK, EOMES, TBX21, RUNX3, CD3D, CD3E, CD3G, S1PR1

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

### CD4+ Central Memory T cells (CD4 TCM)

Description: A highly transcriptionally similar CD4+ helper T cell subset that is frequently misclassified as CD8+ TCM due to shared memory and homing marker expression profiles.

Genes:
- CD4, IL7R, CD27, SELL, CCR7, LTB, LDHB, MAL, GIMAP5, GIMAP4, ANXA1, S100A4
- S100A6, S100A10, CD52, AARD, TRADD, IL32, CD3D, CD3E

### CD8+ Central Memory T cells (CD8 TCM)

Description: Antigen-experienced CD8+ T cells that retain lymph node homing capacity (CCR7+, SELL+) and high IL7R expression, but show early activation and memory markers.

Genes:
- IL7R, CD27, SELL, CCR7, LTB, CD69, GIMAP5, GIMAP7, ANXA1, CD8A, CD8B, KLRB1
- ZFP36, FOS, JUN, DUSP1, S100A4, S100A10, TXNIP, CD52

### CD8+ Effector Memory T cells (CD8 TEM)

Description: Antigen-experienced CD8+ T cells homing to peripheral tissues, characterized by the downregulation of CCR7/SELL and upregulation of cytolytic mediators like GZMK and GZMA.

Genes:
- GZMK, GZMA, LYAR, CST7, NKG7, CD8A, CD8B, DUSP2, CD2, CD247, KLRG1, EOMES
- CCL5, IFNG, PRF1, FGFBP2, CX3CR1, TBX21, GZMB, ADGRG1

### CD8+ Naive T cells

Description: Quiescent, antigen-inexperienced CD8+ T cells characterized by high expression of lymph node homing receptors and transcription factors like LEF1 and TCF7.

Genes:
- CCR7, LEF1, SELL, TCF7, NOSIP, MAL, LDHB, CD27, IL7R, EEF1A1, RPS3A, RPL13
- RPL21, RPL18A, RPS12, RPS18, BTG1, FLT3LG, MYC, CD8A, CD8B

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

### AS-DCs (Axl+ Siglec-6+ dendritic cells)

Description: A transitional dendritic cell population sharing properties of both pDCs and cDCs, characterized by the expression of AXL, SIGLEC6, and CD22.

Genes:
- AXL, SIGLEC6, PPP1R14A, CD22, SCHIP1, CXF1, LILRI2, DAB2, G5, CD5, IL3RA, CLEC4C
- LILRA4, CD1C, FCER1A, RUNX2, TCF4, CST3, HLA-DQA1, HLA-DQB1

### cDC1 (CLEC9A+ classical dendritic cells)

Description: A rare, specialized subset of dendritic cells highly efficient at cross-presenting extracellular antigens to CD8+ T cells, characterized by the expression of CLEC9A and XCR1.

Genes:
- CLEC9A, XCR1, CADM1, WDFY4, BATF3, FLT3, IDO1, CLNK, C1orf54, CPVL, S100A4, APP
- DPP4, LTC4S, S100B, PPA1, GPR141, KCNK17, MAP1A, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, HLA-DRA
- HLA-DRB1

### cDC2 (CD1C+ classical dendritic cells)

Description: The major population of classical dendritic cells in human blood, specialized in presenting MHC class II antigens to CD4+ T cells and expressing CD1C and FCER1A.

Genes:
- CD1C, FCER1A, CLEC10A, SIRPA, COBLL1, ENHO, PKIB, CXCL8, IL1B, S100A9, S100A8, FCN1
- LYZ, CD14, CSF3R, CST3, HLA-DQA1, HLA-DQB1, HLA-DRB1, HLA-DRA, CD86, CD2, LILRB4, PLD4

### pDC (Plasmacytoid dendritic cells)

Description: Dendritic cell precursors specialized in producing massive amounts of type I interferons in response to viral infections, morphologically resembling plasma cells.

Genes:
- LILRA4, CLEC4C, PTGDS, TCF4, IRF7, IRF8, GZMB, IL3RA, NRP1, SCT, PLD4, PACSIN1
- MAP1A, APP, SOX4, SPIB, BCL11A, RUNX2, SERPINF1, ITM2C, DERL3, MZB1, JCHAIN

## cdc2

### Classical_Monocytes

Description: A major myeloid lineage in PBMC that is frequently confused with cDC2s due to shared expression of CD14, S100 proteins, and other myeloid lineage markers.

Genes:
- CD14, LYZ, S100A9, S100A8, S100A12, FCN1, VCAN, CD300E, CFD, GRN, LGALS3, LGALS1
- CTSS, CSTA, CD68, CSF3R, MAFB, FPR1, MEF2C, SPI1

### cDC1

Description: A rare, distinct conventional dendritic cell subset specialized in cross-presentation of intracellular antigens to CD8+ T cells, sharing general dendritic cell markers with cDC2s.

Genes:
- CLEC9A, XCR1, CADM1, WDFY4, BATF3, IRF8, IDO1, CPVL, C1orf54, APP, ANPEP, DPP4
- HLA-DPA1, HLA-DPB1, HLA-DRA, HLA-DRB1, CD74, BTLA, CLNK, S100A4

### cDC2_A_inflammatory

Description: An inflammatory subtype of classical dendritic cells 2 (cDC2) expressing traditional CD1C and FCER1A markers alongside elevated levels of monocyte-like inflammatory mediators and alarmins.

Genes:
- CD1C, FCER1A, CLEC10A, S100A9, S100A8, LYZ, FCN1, VCAN, CD14, IL1B, CXCL8, CCL3
- CCL4, TNF, NFKB1, JUN, FOS, IER3, EGR1, CD1E, HLA-DQA1, HLA-DQB1, HLA-DRB1

### cDC2_B_conventional

Description: The classic, quiescent subset of cDC2s specialized in antigen presentation, characterized by high expression of MHC class II molecules and specific dendritic cell receptors without inflammatory activation.

Genes:
- CD1C, FCER1A, CLEC10A, ENHO, COBLL1, WDFY4, RUNX3, FLT3, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1
- HLA-DRA, HLA-DRB1, CD74, CPVL, CD2, CX3CR1, G3BP1, PLD4

## dnt

### Double-negative T cells (dnT)

Description: Mature T cell receptor alpha-beta bearing T cells that lack both CD4 and CD8 co-receptors, often exhibiting a naive or central memory-like transcriptional profile in healthy PBMCs.

Genes:
- TRATC1, TRAC, TRBC1, TRBC2, CD3D, CD3E, CD3G, CD2, CD5, CD7, CD27, IL7R
- LTB, LDHB, MAL, CD28, LEF1, NOSIP, FYB1, LCK, ZAP70, ITK, TCF7

### Gamma-delta T cells (gdT)

Description: T cells expressing the gamma-delta T-cell receptor that lack CD4 and CD8, frequently confused with dnT cells due to their double-negative surface phenotype but distinguished by cytotoxic and NK-like gene expression.

Genes:
- TRDC, TRGC1, TRGC2, TARBP1, GNLY, NKG7, GZMB, GZMA, PRF1, KLRB1, KLRC1, KLRD1
- KLRG1, CD160, TYROBP, FCER1G, HOPX, S100A4, CST7, ZBTB16, S100A6, ANXA1

### Mucosal-Associated Invariant T cells (MAIT)

Description: A specialized population of donor-unrestricted T cells expressing the TRAV1-2 TCR alpha chain and high levels of KLRB1 (CD161), which are often CD8-negative or double-negative.

Genes:
- TRAV1-2, KLRB1, SLC4A10, ZBTB16, NCR3, RORC, IL18RAP, IL23R, GZMK, DUSP2, CD161, LTB
- CD2, CD3E, CD3D, CD3G, RUNX3, FOS, JUN, IL7R

### Natural Killer cells (NK)

Description: Innate lymphoid cells lacking CD3 expression that share a highly overlapping cytotoxic gene signature with double-negative T cells and gamma-delta T cells.

Genes:
- NCAM1, NKG7, GNLY, PRF1, GZMB, GZMA, FCGR3A, KLRD1, KLRF1, KLRC1, KLRB1, CD160
- HOPX, CST7, SPON2, CLIC3, S100A4, PRF1, FGFBP2, S100A6, TYROBP, FCER1G

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

Description: Terminally differentiated effector memory CD8+ T cells re-expressing CD45RA, which share an almost identical cytotoxic gene expression program with effector gamma-delta T cells.

Genes:
- CD8A, CD8B, TRAC, TRBC1, TRBC2, FGFBP2, FCGR3A, CX3CR1, GZMB, PRF1, GNLY, NKG7
- KLRG1, EOMES, TBX21, ZEB2, ADGRG1, S100A4, S100A6, CST7

### MAIT

Description: Mucosal-Associated Invariant T cells that express the TRAV1-2 TCR alpha chain and high levels of KLRB1 (CD161), frequently confused with gdT cells due to shared semi-invariant TCR features and cytotoxic profiles.

Genes:
- TRAV1-2, KLRB1, SLC4A10, ZBTB16, RORC, IL7R, DPP4, GZMK, GZMA, NCR3, IKZF2, CD161
- CCR6, CXCR6, ANXA1, CD2, CD5, CD6, RUNX3, LTB, IL32

### NK_CD56dim

Description: Mature cytotoxic Natural Killer cells that share a highly overlapping transcriptional signature of cytolytic effector molecules and homing receptors with Vd2 gamma-delta T cells.

Genes:
- NCAM1, FCGR3A, FGFBP2, CX3CR1, PRF1, GZMB, GZMA, GNLY, NKG7, KLRD1, KLRF1, KLRG1
- SPON2, CLIC3, CST7, HOPX, ZEB2, TBX21, S100A4, S100A6, PRF1

### Vd1_gdT

Description: A minor gamma-delta T cell subset in peripheral blood that often exhibits a naive, memory, or mucosal-associated invariant-like phenotype with tissue-homing potential.

Genes:
- TRDV1, TRGV4, TRGV2, CD8A, CD8B, IL7R, CCR7, SELL, LEF1, TCF7, CD27, CD28
- LTB, IL32, GZMK, GZMA, KLRB1, CD161, ZBTB16, RUNX3, CD5, CD6

### Vd2_gdT

Description: The predominant gamma-delta T cell subset in human peripheral blood, characterized by Vd2/Vg9 TCR chain expression, cytotoxic effector function, and responsiveness to phosphoantigens.

Genes:
- TRDV2, TRGV9, GZMB, PRF1, GNLY, NKG7, FGFBP2, FCGR3A, CX3CR1, KLRG1, KLRD1, KLRF1
- CD160, EOMES, TBX21, ZBTB16, PLCG2, S100A4, S100A6, S100A10, S100A11, ANXA1, LGALS1, CD52
- SST

## hspc

### CD34+ Granulocyte-Monocyte Progenitor (GMP)

Description: A myeloid-biased progenitor population in the HSPC compartment committed to generating granulocytes and monocytes, characterized by high expression of primary granule proteins.

Genes:
- CD34, SPINK2, MPO, ELANE, PRTN3, AZU1, CTSG, RNASE2, RNASE3, LYZ, CST3, CSF3R
- CEBPA, CEBPD, CD38, CD14, FCN1, GRN, SERPINB1, CALR

### CD34+ Megakaryocyte-Erythroid Progenitor (MEP)

Description: A committed progenitor subtype derived from HSPCs that gives rise to the megakaryocytic and erythroid lineages, characterized by the co-expression of CD34 and early erythroid/megakaryocytic transcription factors.

Genes:
- CD34, SPINK2, GATA1, GATA2, KLF1, MYB, TFRC, GYPA, GYPB, ALAS2, HBD, HBB
- HBA1, HBA2, PLEK, ITGA2B, GP9, TUBB1, PF4, SDPR, CD9, MPL, VWF, PBX1

### Hematopoietic Stem Cell / Multipotent Progenitor (HSC/MPP)

Description: The most primitive, self-renewing, and multipotent compartment of HSPCs in circulation, characterized by high CD34 expression and stemness-associated transcription factors.

Genes:
- CD34, AVVP, SPINK2, MLLT3, MECOM, HLF, CRHBP, HOPX, GATA2, PRSS57, CD52, CD109
- PROM1, CYTL1, SMIM24, CLEC11A, MYCN, CTSG, ANGPT1, RBPMS

### Plasmacytoid Dendritic Cell (pDC)

Description: A mature peripheral immune cell type often confused with HSPCs due to shared expression of CD34-adjacent progenitor markers like CD123 (IL3RA) and high transcriptional activity, specializing in rapid type I interferon production.

Genes:
- CLEC4C, LILRA4, PLD4, TCF4, IRF7, IRF8, GZMB, IL3RA, NRP1, SCT, PACSIN1, MAP1A
- APP, SERPINF1, ITM2C, DERL3, MZB1, TXNIP, SPIB, RUNX2

## ilc

### ILC3

Description: A rare subset of innate lymphoid cells in PBMC characterized by the expression of RORC, KIT (CD117), and the IL-23 receptor, involved in mucosal immunity and tissue homeostasis.

Genes:
- KIT, IL23R, AHR, RORC, IL1R1, LST1, IL4I1, TMEM176A, TMEM176B, PLXDC2, CD200, TNFSF11
- LIF, CSF2, KLRB1, CD161, GPR183, PTGDR2, IL17F, IL22

### MAIT cells

Description: Mucosal-associated invariant T cells that express a semi-invariant T-cell receptor and share phenotypic markers with ILCs, such as CD161 (KLRB1) and IL-7R, leading to frequent misclassification.

Genes:
- TRAV1-2, KLRB1, SLC4A10, DPP4, ZBTB16, RORC, IL7R, NCR3, GZMK, LTB, CD8A, CD8B
- IKZF2, CCR6, CXCR6, ANXA1, IL18RAP, FURIN, DUSP2, GZMA

### NK cells

Description: Cytotoxic innate lymphoid cells that share many marker genes with ILCs but are distinguished by high expression of perforin, granzymes, and killer cell lectin-like receptors.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMA, KLRD1, KLRF1, KLRG1, CD244, CD160, FCGR3A, FGFBP2
- SPON2, CST7, CLIC3, HOPX, S1PR5, PRF1, GZMM, CTS6, IL2RB, NCR3, NCR1, XCL1
- XCL2

### gamma-delta T cells

Description: T cells expressing the gamma-delta TCR that exhibit innate-like rapid effector functions and share transcriptional profiles with both NK cells and helper ILCs.

Genes:
- TRDC, TRGC1, TRGC2, TARBP1, CD160, KLRG1, KLRC1, KLRC2, KLRC3, GNLY, NKG7, GZMB
- GZMA, CD8A, CD8B, SST, EOMES, TBX21, RUNX3, ZBTB16

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

### CD56bright CD16low NK cells

Description: An immunomodulatory NK cell subset in PBMCs characterized by high cytokine production (e.g., IFN-gamma, TNF) upon stimulation, high expression of CD56 (NCAM1) and CD62L (SELL), and low cytotoxicity.

Genes:
- NCAM1, SELL, IL7R, GZMK, KLRC1, XCL1, XCL2, CSF2, IFNG, TNF, LTB, IL2RB
- CD2, CD44, TCF7, RUNX2, CAPG, SOX4, GPR183, MYC

### CD56dim CD16plus NK cells

Description: The major cytotoxic NK cell subset in peripheral blood, characterized by high expression of CD16 (FCGR3A), perforin, granzymes, and chemotactic receptors for homing to inflamed tissues.

Genes:
- FCGR3A, FGFBP2, CX3CR1, PRF1, GZMB, GZMH, SPON2, KLRG1, ADGRG1, S1PR5, CLIC3, GSTP1
- NKG7, GNLY, KLRD1, KLRF1, KLRM1, CD244, ZEB2, TBX21, PRF1, HCST, S100A4, S100A6

### CD8plus Effector Memory T cells

Description: A T cell population commonly confused with NK cells due to shared expression of cytotoxic molecules (granzymes, perforin) and killer lectin-like receptors, but distinguished by the expression of the T-cell receptor complex and CD8.

Genes:
- CD8A, CD8B, CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, GZMK, GZMA, CCL5, EOMES
- DUSP2, CD27, LTB, IL7R, KLRG1, CXCR3, CD247, HCST

### Gamma-Delta T cells

Description: A specialized T cell lineage expressing gamma-delta TCRs that shares transcriptional profiles with NK cells, including high expression of cytotoxic mediators and NK receptors, often leading to misclassification.

Genes:
- TRDV2, TRGV9, TRDC, TRGC1, TRGC2, CD3D, CD3E, CD247, KLRB1, NKG7, GNLY, GZMB
- GZMH, CD160, KLRC2, KLRC3, ZBTB16, IKZF2, HOPX, S100A4

## nk proliferating

### CD56bright NK

Description: An immature, immunomodulatory NK cell subset in PBMCs characterized by high surface expression of CD56, low cytotoxicity, and high cytokine production capacity.

Genes:
- NCAM1, SELL, KLRC1, IL7R, GZMK, LTB, IL2RB, CD2, KLRC2, XCL1, XCL2, CSF2
- IFNG, TNFSF10, CAPG, RUNX2, CD44, CST7, GZMA, PRF1

### CD56dim NK

Description: The mature, highly cytotoxic majority NK cell subset in PBMCs characterized by high CD16 (FCGR3A) expression and abundant cytolytic granules.

Genes:
- FCGR3A, FGFBP2, CX3CR1, GZMB, PRF1, GNLY, NKG7, KLRF1, KLRG1, SPON2, CLIC3, S100A4
- S100A6, PRF1, CST7, ADGRG1, ZEB2, TBX21, HOPX, S100B

### NK Proliferating

Description: A rare, actively cycling natural killer cell population in PBMCs characterized by high expression of proliferation markers alongside cytotoxic effector molecules.

Genes:
- MKI67, TOP2A, CENPF, PCNA, CDK1, BIRC5, CCNB1, CCNA2, NUSAP1, UBE2C, HMGB2, STMN1
- TYMS, DUT, RRM2, CEP55, AURKB, KIF2C, CENPE, CENPA, NKG7, GNLY, GZMB, PRF1
- KLRD1, FGFBP2, FCGR3A, CST7

### T Proliferating

Description: Actively dividing T cells in PBMCs that share cell-cycle machinery with proliferating NK cells but are distinguished by the expression of CD3 and T-cell receptor complex genes.

Genes:
- MKI67, TOP2A, CENPF, PCNA, CDK1, BIRC5, CCNB1, CCNA2, NUSAP1, UBE2C, HMGB2, STMN1
- TYMS, CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, CD8A, CD8B, IL7R, CD4, LDHB

## nk_cd56bright

### MAIT_cells

Description: Mucosal-associated invariant T cells that share many phenotypic markers with NK cells, such as CD161 (KLRB1) and IL-18 receptors, often leading to annotation confusion in high-throughput single-cell datasets.

Genes:
- TRAV1-2, KLRB1, SLC4A10, DPP4, RORC, IL7R, NCR3, GZMK, CD8A, CD8B, IKZF2, ZBTB16
- CCR6, CXCR6, ANXA1, IL18R1, IL23R, FURIN, DUSP4, CD161

### NK_CD56bright_canonical

Description: The canonical cytokine-producing NK cell subset in PBMCs, characterized by high expression of NCAM1 (CD56), homing receptors like SELL (L-selectin), and GZMK, while lacking high levels of cytolytic granzyme B and perforin.

Genes:
- NCAM1, SELL, IL7R, GZMK, KLRC1, KLRD1, LTB, IL2RB, CD2, CD27, XCL1, XCL2
- CSF2, IFNG, TNF, FOS, JUN, ZBTB16, TCF7, CCR7, RUNX2, MYC, GPR183, CD44
- IL18RAP

### NK_CD56dim_mature

Description: The major cytotoxic NK cell subset in peripheral blood, characterized by high expression of FCGR3A (CD16), CX3CR1, and high levels of cytolytic effector molecules like GZMB and PRF1.

Genes:
- FCGR3A, FGFBP2, CX3CR1, GZMB, PRF1, GNLY, NKG7, KLRF1, KLRG1, SPON2, ADGRG1, ZEB2
- TBX21, S1PR5, CLIC3, CST7, CD244, PRF1, GZMA, HLA-C, IL32, HCST

### T_gd

Description: Gamma-delta T cells that express cytotoxic machinery and NK-associated receptors, frequently overlapping transcriptionally with both CD56dim NK cells and cytotoxic CD8+ T cells.

Genes:
- TRDC, TRGC1, TRGC2, TARBP1, CD160, KLRG1, KLRC2, KLRC3, GZMB, GNLY, NKG7, PRF1
- S1PR5, CD8A, CD8B, RUNX3, EOMES, HOPX, ZNF683, IL2RB

## pdc

### AS-DC (AXL+ SIGLEC6+ transitional DC)

Description: A transitional dendritic cell population sharing properties of both pDCs and cDCs, characterized by high expression of AXL, SIGLEC6, and antigen-presentation machinery.

Genes:
- AXL, SIGLEC6, SIGLEC1, CD2, CD5, CX3CR1, PPP1R14A, LILRI4, S100A10, S100A4, CD22, CD86
- HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, HLA-DRB1, CD1C, FCER1A, CLEC10A, ENHO, FGR, LST1, AIF1
- COBLL1, RUNX3, MS4A7, CSF1R

### Classical pDC (CLEC4C+ LILRA4+)

Description: Classical plasmacytoid dendritic cells specialized in rapid, massive secretion of type I interferons in response to viral nucleic acids.

Genes:
- CLEC4C, LILRA4, IL3RA, TLR7, TLR9, TCF4, IRF7, IRF8, NRP1, PLD4, MAP1A, GZMB
- SERPINF1, ITM2C, PACSIN1, LAMP5, SCT, APP, SPIB, PTGDS, SOX4, BCL11A, RUNX2, TXNIP
- C1orf186, PTPRS, DERL3, MZB1, SEC61A1, HERPUD1

### Pre-B Cells

Description: B cell progenitors that can be confused with pDCs due to shared expression of lymphoid-associated genes, SOX4, and certain surface markers.

Genes:
- VPREB1, VPREB3, IGLL1, DNTT, ADA, CD19, MS4A1, CD24, CD79A, CD79B, EBF1, PAX5
- SOX4, MME, IL7R, RAG1, RAG2, STAP1, BLNK, CD38, TCL1A, HMGB3, DTL, DIAPH3

### cDC1 (CLEC9A+ CADM1+)

Description: Conventional dendritic cell type 1 specialized in cross-presentation of intracellular antigens to CD8+ T cells.

Genes:
- CLEC9A, CADM1, XCR1, WDFY4, BATF3, IRF8, ID2, FLT3, CPVL, C1orf54, CLNK, APP
- S100A3, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, HLA-DRA, HLA-DRB1, CD74, IFI30, LY86, GSN, BTLA
- SNX22

## plasmablast

### Activated B Cell

Description: Mature B cells undergoing activation and clonal expansion in response to antigen stimulation, showing upregulation of activation markers, costimulatory molecules, and NF-kB pathway genes.

Genes:
- CD19, MS4A1, CD79A, CD79B, CD83, CD86, CD40, NFKB1, NFKB2, REL, EBI3, MYC
- CCND2, MIR155HG, FCRL3, FCRL5, CLEC17A, TRAF1, TNFAIP3, NFKBIZ, JUN, FOS, IER3, CD69
- GPR183, SLAMF1

### Memory B Cell

Description: Antigen-experienced B cells that persist long-term in the circulation, characterized by CD27 expression and somatic hypermutation without active high-rate antibody secretion.

Genes:
- CD19, MS4A1, CD79A, CD79B, CD27, AIM2, CLEC17A, TNFRSF13B, COBLL1, FCRL4, FCRL5, CD80
- CD86, ITGB2, AHNAK, S100A4, S100A10, TXNIP, CD24, LINC00926, BANK1, MARCKS, GPR183

### Plasma Cell

Description: Fully terminally differentiated, non-proliferative antibody-secreting cells that express high levels of CD138 (SDC1) and BCMA (TNFRSF17) with massive immunoglobulin production.

Genes:
- SDC1, CD38, TNFRSF17, PRDM1, XBP1, IRF4, MZB1, SSR4, JCHAIN, IGKC, IGHG1, IGHG2
- IGHG3, IGHG4, IGHA1, IGHA2, TXNDC5, FKBP11, HSP90B1, DERL3, SEC11C, EMP3, GPX1, SLAMF7
- CD27, FCRL5, TNFRSF13B, SDF2L1, CREB3L2, HERPUD1

### Plasmablast

Description: Highly proliferative, antibody-secreting immature B cells in the peripheral blood that express high levels of endoplasmic reticulum stress genes and immunoglobulin transcripts.

Genes:
- MZB1, SSR4, PRDM1, IRF4, XBP1, SEC61B, FKBP11, TXNDC5, DERL3, HERPUD1, SDF2L1, TENT5C
- CREB3L2, MANF, SEL1L, HSP90B1, CANX, CALR, PDIA3, PDIA4, PDIA6, PPIB, B2M, CD38
- SDC1, TNFRSF17, IGHM, IGHA1, IGHA2, IGHG1, IGHG2, IGHG3, IGKC, IGLC2, IGLC3, JCHAIN

## platelet

### Megakaryocyte-like Platelets

Description: Platelets and rare circulating megakaryocyte progenitors characterized by high expression of classical platelet activation, adhesion, and structural genes.

Genes:
- PPBP, PF4, GNG11, TUBB1, SDPR, SPARC, GP9, GP1BA, GP1BB, GP5, ITGA2B, ITGB3
- MPL, TREML1, CLU, F13A1, MYL9, HIST1H2AC, ACTB, TMSB4X, CD9, PECAM1, CLEC1B, PTGS1
- RAP1B

### Plasmacytoid Dendritic Cells

Description: A neighboring immune cell type in PBMCs that can be confused with platelets due to shared expression of certain surface markers or low RNA content in high-throughput droplet sequencing.

Genes:
- LILRA4, CLEC4C, PTGDS, GZMB, TCF4, IRF7, IRF8, SCT, NRP1, IL3RA, MAP3K7IP2, PLD4
- PACSIN1, SOX4, SPIB, APP, RUNX2, SERPINF1, ITM2C, DERL3, MZB1, TXNIP

### Platelet-Monocyte Aggregates

Description: A common technical artifact or biological doublet in PBMC datasets where physical adherence of platelets to CD14+ monocytes results in a hybrid transcriptional profile.

Genes:
- CD14, LYZ, S100A8, S100A9, S100A12, FCN1, VCAN, PPBP, PF4, GNG11, SDPR, GP9
- ITGA2B, CD9, CST3, CD68, TYROBP, FCER1G, LST1, AIF1, SPI1, MNDA

### Platelet-T Cell Aggregates

Description: A common technical artifact or biological doublet in PBMC datasets where platelets adhere to T lymphocytes, leading to co-detection of T-cell receptor and platelet-specific transcripts.

Genes:
- CD3D, CD3E, CD3G, TRAC, IL7R, CD4, CD8A, PPBP, PF4, GNG11, SDPR, GP9
- ITGA2B, CD9, CD2, CD5, CD7, LTB, LDHB, MAL, FYB1, HCST

## treg

### CD4+ Memory T cell

Description: Antigen-experienced CD4+ helper T cells that lack high FOXP3 expression but share activation and memory markers with Effector Tregs, leading to potential annotation overlap.

Genes:
- IL7R, S100A4, S100A6, CD44, ANXA1, LMNA, CD52, FOS, JUN, DUSP1, GIMAP7, GIMAP4
- LTB, CD4, AOP2, IL32, CD2, CD3E, CD3D, CD3G

### CD4+ Naive T cell

Description: A major neighboring CD4+ T cell subset that lacks FOXP3 and IL2RA expression but shares naive homing markers like CCR7 and SELL, often causing misclassification with Naive Tregs.

Genes:
- CCR7, SELL, LEF1, TCF7, MAL, IL7R, CD27, CD28, NOSIP, LDHB, FLT3LG, S1PR1
- EEF1B2, TPT1, BTG1, MYC, JUNB, FOS, CD45RA, GIMAP5

### Effector Treg

Description: Highly suppressive, activated regulatory T cells that express high levels of immune checkpoints, TNF receptor superfamily members, and HLA class II molecules.

Genes:
- FOXP3, IL2RA, IKZF2, CTLA4, TIGIT, ICOS, TNFRSF4, TNFRSF9, TNFRSF18, HLA-DRA, HLA-DRB1, CD147
- LGALS1, ANXA1, MYO1G, IL1RL1, CCR4, CCR8, PRDM1, MAF, IRF4, S100A4, S100A6

### Naive Treg

Description: Resting or naive regulatory T cells characterized by the co-expression of FOXP3 and IL2RA alongside lymphoid homing markers like CCR7 and SELL.

Genes:
- FOXP3, IL2RA, CCR7, SELL, LEF1, TCF7, IL7R, MAL, CD62L, CD45RA, BACH2, NOSIP
- TXNIP, S1PR1, BTG1, EEF1A1, LDHB, CCR6, TNFRSF25, SATB1

