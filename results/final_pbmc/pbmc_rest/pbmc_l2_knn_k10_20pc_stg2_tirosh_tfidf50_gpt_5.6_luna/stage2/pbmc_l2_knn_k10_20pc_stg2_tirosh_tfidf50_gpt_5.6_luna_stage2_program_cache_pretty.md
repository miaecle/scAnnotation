# Stage-2 Precomputed Programs

- tissue: PBMC
- n_program_genes: 50
- n_cached_cell_types: 31

## asdc

### AXL+ SIGLEC6 dendritic cells (ASDC)

Description: A rare human dendritic-cell population marked by AXL and SIGLEC6 that shares antigen-presentation features with conventional DCs but is transcriptionally distinct from pDCs.

Genes:
- AXL, SIGLEC6, SIGLEC1, CD5, CD2, CD22, LILRB4, GZMB, FCER1A, CD1C, CLEC10A, CD86
- GPR183, CSTA, CST3, LILRA1, CTSS, CD74, HLA-DRA, HLA-DPA1, HLA-DPB1, HLA-DMA, HLA-DMB, HLA-DQB1

### CD1C+ conventional dendritic cells (cDC2)

Description: The major blood conventional dendritic-cell population, specialized for antigen uptake and presentation and characterized by CD1C, FCER1A, CLEC10A, and CD1E.

Genes:
- CD1C, FCER1A, CLEC10A, CD1E, CD1D, CD1B, CST3, CSTA, COTL1, CLEC12A, FCGR2A, CYTH4
- CD86, CTSS, CD74, HLA-DRA, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, HLA-DMA, HLA-DMB, GPR183, CCDC50

### Monocyte-derived dendritic cells / DC3-like cells

Description: An inflammatory monocyte-related dendritic-cell state with enhanced phagocytic and myeloid programs that can overlap phenotypically with ASDCs and cDC2s.

Genes:
- CD14, FCGR3A, CD163, CD36, MS4A7, LILRB1, LILRB3, FCER1G, TYMP, CTSD, CTSS, LGALS3
- SERPINA1, S100A10, CFD, SAT1, CTSD, IFITM3, LST1, FCGR2A, CD68, CD86, HLA-DRA, CD74

### Plasmacytoid dendritic cells

Description: Type I interferon-producing dendritic cells specialized for sensing nucleic acids and expressing CLEC4C, IL3RA, TCF4, and GZMB.

Genes:
- GZMB, CLEC4C, IL3RA, TCF4, GZMB, JCHAIN, SERPINF1, PTCRA, PLD4, PACSin1, IRF7, IRF8
- TLR7, TLR9, GZMB, IGJ, LILRB4, TPM4, BCL11A, SMPD3, CYB5R3, PTPRS, HLA-DRA, GZMB

## b intermediate

### B intermediate

Description: An intermediate mature B-cell state with transitional-like TCL1A and CD24 expression alongside established B-cell receptor and antigen-presentation programs.

Genes:
- TCL1A, IGHD, IGHM, CD24, FCER2, IL4R, CD38, MS4A1, CD79A, CD74, HLA-DRA, CD37
- CD22, BANK1, BLK, RALGPS2, VPREB3, FCRL1, HVCN1, AFF3, BACH2, SPIB, LTB, MEF2C
- IGKC

### Naive B cell

Description: Antigen-inexperienced mature B cells express predominantly IgD and IgM with strong lymphoid-homing and quiescent B-cell receptor programs.

Genes:
- IGHD, IGHM, TCL1A, FCER2, IL4R, MAL, HVCN1, LTB, CCR7, SELL, BACH2, MEF2C
- RALGPS2, BANK1, BLK, AFF3, SPIB, FCRL1, CD22, CD79A, MS4A1, CD74, HLA-DRA, CD37
- IGKC

### Plasmablast

Description: Highly antibody-secreting B-cell descendants with plasma-cell differentiation, unfolded-protein-response, and abundant immunoglobulin-production programs.

Genes:
- MZB1, JCHAIN, XBP1, SEC11C, DERL3, SSR4, FKBP11, MANF, CD38, SDC1, TNFRSF17, PRDM1
- IRF4, CD27, IGHG1, IGHG3, IGHA1, IGKC, CD79A, MALAT1, HSP90B1, CALR, PDIA4, PPIB
- TXNDC5

### Transitional B cell

Description: Recently emigrated or transitional B cells retain immature TCL1A, CD24, and CD38 features while beginning mature B-cell receptor differentiation.

Genes:
- TCL1A, IGHD, IGHM, CD24, CD38, FCER2, IL4R, IGLL1, VPREB3, SOX4, MAL, BACH2
- HVCN1, RAG1, RAG2, EBF1, BCL11A, CD79A, MS4A1, CD74, HLA-DRA, CD37, BANK1, BLK
- IGKC

### Unswitched memory B cell

Description: Mature antigen-experienced B cells that retain unswitched IgM or IgD and display CD27, complement-receptor, and memory-associated activation programs.

Genes:
- CD27, IGM, IGHD, AIM2, TNFRSF13B, CD44, CD21, CR2, FCRL2, FCRL1, BANK1, BLK
- MS4A1, CD79A, CD37, CD22, CD74, HLA-DRA, CD82, CD40, CD83, LTB, CD86, IGKC
- CD19

## b memory

### Atypical memory B cell

Description: A chronically stimulated, often CD11c-positive memory B-cell state marked by TBX21, FCRL5, ITGAX, and altered innate-like signaling.

Genes:
- TBX21, FCRL5, ITGAX, FCRL3, SIGLEC6, CD11C, CD86, LILRB1, TLR7, TLR10, ITGAM, CXCR3
- ZEB2, IFITM3, LGALS3, CTSD, FCER1G, TYROBP, MS4A1, CD79A, CD74, HLA-DRA, CD27, TNFRSF13B

### Class-switched memory B cell

Description: Antigen-experienced B cells that have undergone immunoglobulin class switching and commonly express CD27 together with IGHG or IGHA transcripts.

Genes:
- CD27, TNFRSF13B, IGHG1, IGHG2, IGHG3, IGHA1, IGHA2, MS4A1, CD79A, CD74, HLA-DRA, HLA-DPA1
- HLA-DPB1, CD37, CD22, CD40, BANK1, BLNK, HVCN1, SPIB, BACH2, AIM2, TCL1A, CD83

### IgM memory B cell

Description: Unswitched memory B cells retain IGHM and often IGHD while displaying a CD27-positive antigen-experienced phenotype.

Genes:
- CD27, IGHM, IGHD, MS4A1, CD79A, CD74, HLA-DRA, HLA-DPA1, HLA-DPB1, CD37, CD22, BANK1
- BLNK, HVCN1, SPIB, BACH2, TNFRSF13B, AIM2, CD40, FCER2, LTB, MAL, AQP3, CD52

### Naive B cell

Description: A commonly confused neighboring B-cell population consisting of antigen-inexperienced cells that express TCL1A, IGHD, IGHM, and FCER2 and generally lack strong memory markers such as CD27.

Genes:
- TCL1A, IGHD, IGHM, FCER2, IL4R, MAL, AQP3, CCR7, LTB, IGKC, MS4A1, CD79A
- CD74, HLA-DRA, HLA-DPA1, HLA-DPB1, CD37, CD22, BANK1, BLNK, HVCN1, SPIB, BACH2, B2M

## b naive

### Mature naive B cell

Description: Mature antigen-inexperienced B cells characterized by strong IGHD, TCL1A, FCER2, and IL4R expression together with a conventional B-cell receptor program.

Genes:
- TCL1A, IGHD, IGHM, FCER2, IL4R, MS4A1, CD79A, CD79B, CD37, CD22, HLA-DRA, HLA-DPA1
- HLA-DPB1, CD74, BANK1, BLK, SPIB, HVCN1, FCRL1, BACH2, AFF3, GPR183, VPREB3, EBF1
- MEF2C, RALGPS2, PAX5, TNFRSF13C

### Plasmablast

Description: Highly antibody-secreting B-lineage cells with plasmablast differentiation, unfolded-protein-response, immunoglobulin, and secretory machinery programs.

Genes:
- MZB1, JCHAIN, XBP1, PRDM1, IRF4, SEC11C, DERL3, FKBP11, TNFRSF17, CD38, CD27, SDC1
- IGHG1, IGHG3, IGHA1, IGKC, IGLC2, IGLC3, MZB1, SSR4, SEC61A1, MANF, TXNDC5, HSPA5
- DNAJB9, P4HB, DDIT3, CD74

### Transitional B cell

Description: Recently bone-marrow-derived B cells with elevated CD24, CD38, TCL1A, and immature-associated CD10 expression while retaining an IgM-rich B-cell program.

Genes:
- TCL1A, CD24, CD38, IGHM, IGHD, MS4A1, CD79A, CD79B, CD37, CD22, HLA-DRA, HLA-DPA1
- HLA-DPB1, CD74, IL4R, FCER2, TNFRSF13C, CD10, MME, VPREB3, BACH2, EBF1, SPIB, BLK
- BANK1, HVCN1, MAL, TCL1B

### Unswitched memory B cell

Description: Antigen-experienced, generally IgM- or IgD-positive memory B cells marked by CD27, TNFRSF13B, FCRL2, and increased activation and antigen-presentation programs.

Genes:
- CD27, TNFRSF13B, FCRL2, FCRL1, CD44, CD82, AIM2, IGHM, IGHD, MS4A1, CD79A, CD79B
- CD37, CD22, HLA-DRA, HLA-DPA1, HLA-DPB1, CD74, CD40, BANK1, CD48, LTB, COTL1, GPR183
- TNFRSF13C, CD19, FCER2, FCRL3

## cd14 mono

### CD1C-Positive Conventional Dendritic Cell

Description: CD1C-positive conventional dendritic cells are professional antigen-presenting cells that can resemble monocytes but preferentially express CD1C, FCER1A, CLEC10A, and MHC-II genes.

Genes:
- CD1C, FCER1A, CLEC10A, CST3, HLA-DRA, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, CD74, GPR183, CLEC12A
- CD1E, IRF4, CCDC50, CADM1, CD83, SPIB, HLA-DMA, HLA-DMB, COTL1, FCER1G, LYZ, CTSS

### Classical CD14 Monocyte

Description: Classical monocytes are highly phagocytic CD14-high cells enriched for S100A8/S100A9, FCN1, VCAN, and inflammatory innate immune programs.

Genes:
- LYZ, S100A8, S100A9, CTSD, CTSS, FCN1, VCAN, TYMP, CTSC, LGALS3, LILRB1, FCER1G
- TYROBP, AIF1, MNDA, SERPINA1, S100A10, SAT1, FPR1, CFD, LGALS9, SLC11A1, MS4A6A, IFITM3

### Inflammatory CD14 Monocyte

Description: Inflammatory CD14 monocytes represent an activated classical-monocyte state with strong cytokine, NF-kB, stress-response, and S100A8/S100A9 expression.

Genes:
- S100A8, S100A9, S100A12, IL1B, CXCL8, TNF, CCL3, CCL4, NLRP3, PTGS2, NAMPT, PLAUR
- FOS, JUN, NFKBIA, IER3, DUSP1, CTSD, CTSS, FCN1, VCAN, LYZ, MNDA, SLC11A1

### Intermediate CD14-FCGR3A Monocyte

Description: Intermediate monocytes coexpress CD14 and FCGR3A and show antigen-presentation, interferon-response, and transitional monocyte programs.

Genes:
- CD14, FCGR3A, MS4A7, LST1, IFITM3, IFITM1, IFITM2, LILRB1, LILRA1, SERPINA1, LGALS3, IFI30
- SAT1, CTSD, CTSS, FCER1G, TYROBP, AIF1, LGALS9, CFD, MS4A6A, IFITM5, CTSC, LYZ

### Nonclassical FCGR3A Monocyte

Description: Nonclassical monocytes are FCGR3A-high patrolling cells with reduced S100A8/S100A9 expression and enhanced adhesion, surveillance, and interferon-associated programs.

Genes:
- FCGR3A, MS4A7, LST1, IFITM3, IFITM1, IFITM2, LILRB1, LILRA1, SIGLEC10, IFITM5, LGALS3, IFI30
- CFD, SERPINA1, LGALS9, RHOC, SAT1, CTD-2006K23.1, FCER1G, TYROBP, AIF1, CTSS, MS4A6A, LYZ

## cd16 mono

### CD1C+ conventional dendritic cells

Description: Antigen-presenting conventional dendritic cells expressing CD1C, FCER1A, CLEC10A, and abundant MHC class II machinery that can resemble FCGR3A-positive monocytes.

Genes:
- CD1C, FCER1A, CLEC10A, CD1E, CST3, HLA-DRA, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, GPR183, CD74
- COTL1, CLEC12A, IRF4, CSF1R, LILRB1, FCER1G, LST1, LYZ

### Classical CD14+ monocytes

Description: Inflammatory CD14-high monocytes characterized by S100A8/S100A9, VCAN, FCN1, and strong phagocytic and innate immune programs.

Genes:
- CD14, S100A8, S100A9, VCAN, FCN1, CTSD, CTSS, CTSB, LGALS3, S100A10, LYZ, TYMP
- MNDA, FCER1G, AIF1, LST1, CTSD, FTH1, FTL, LGALS1

### FCGR3A+ non-classical monocytes

Description: Patrolling CD16-positive monocytes enriched for FCGR3A, MS4A7, LST1, LILRB1, and CDKN1C that survey vascular endothelium and participate in tissue surveillance.

Genes:
- FCGR3A, MS4A7, LST1, IFITM3, IFITM1, IFITM2, LILRB1, LILRA1, IFITM, CFD, CDKN1C, IFITM?

### Intermediate CD14+FCGR3A+ monocytes

Description: Transitional monocytes co-expressing CD14 and FCGR3A with heightened antigen-presentation and inflammatory potential relative to non-classical monocytes.

Genes:
- CD14, FCGR3A, LST1, MS4A7, LILRB1, FCER1G, AIF1, CTSS, CTSD, TYMP, LGALS3, IFITM3
- IFITM1, IFITM2, SERPINA1, SAT1, IFI30, S100A10, CTSB, MNDA

## cd4 ctl

### Activated or effector-memory CD4 T cell

Description: A conventional CD4 T-cell population with helper or activation programs, typically marked by CD4, IL7R, CCR7, and activation-associated genes rather than dominant cytotoxic machinery.

Genes:
- CD4, CD3D, CD3E, TRAC, TRBC1, TRBC2, IL7R, LTB, MALAT1, MAL, LTB, IL32
- CCR7, LTB, MAL, NOSIP, LTB, MHCN1, LST1, ICOS, TNFRSF4, TNFRSF18, CTLA4, IL2RA

### Cytotoxic CD4 T cell

Description: A clonally expanded CD4 T-cell population with strong cytotoxic effector programs, commonly expressing CCL5, NKG7, granzymes, and perforin.

Genes:
- CD4, CD3D, CD3E, TRBC1, TRBC2, CCL5, NKG7, GZMK, GZMH, GNLY, PRF1, CTSW
- KLRD1, KLRB1, CST7, LST1, FGFBP2, GZMB, CCL4, CCL4L2, CCL3, HLA-C, TYROBP, TRAC

### Cytotoxic CD8 T cell

Description: A CD8 T-cell cytotoxic population characterized by CD8A/CD8B expression together with perforin, granzymes, NKG7, and inflammatory chemokines.

Genes:
- CD8A, CD8B, CD3D, CD3E, TRAC, TRBC1, TRBC2, CCL5, NKG7, GNLY, PRF1, GZMB
- GZMH, GZMK, CTSW, CST7, FGFBP2, KLRD1, CCL4, CCL4L2, CCL3, HLA-C, CD27, CD8A

### Natural killer cell

Description: An innate cytotoxic lymphocyte population with high KLRD1, TYROBP, FCER1G, GNLY, and PRF1 and little or no conventional T-cell receptor expression.

Genes:
- KLRD1, KLRB1, FCGR3A, TYROBP, TRAC, NKG7, GNLY, PRF1, GZMB, GZMH, CTSW, CST7
- FGFBP2, XCL1, XCL2, CCL5, CCL4, CCL4L2, TRDC, TYROBP, FCER1G, S1PR5, KLRC1, KLRF1

## cd4 naive

### CD4 Central Memory

Description: Recirculating antigen-experienced CD4 T cells that retain CCR7-dependent lymphoid homing while expressing IL7R and memory-associated S100A4 and IL32.

Genes:
- IL7R, CCR7, LTB, MAL, TCF7, LEF1, AQP3, S100A4, IL32, GPR183, LTBR, MALAT1
- FYB1, TRABD2A, NOSIP, PIK3IP1, TXNIP, LDHB, LIME1, ETS1, THEMIS, BACH2, LTB, TRBC1

### CD4 Effector Memory

Description: Antigen-experienced CD4 T cells with reduced naive-cell quiescence and increased tissue-recirculation, helper, and cytokine-response programs.

Genes:
- IL7R, S100A4, IL32, LTB, AQP3, GPR183, KLRB1, CCR6, RORA, CXCR4, ANXA1, LTBR
- GPR183, CD40LG, TNFRSF4, ICOS, MALAT1, FYB1, TRBC1, TRBC2, LST1, IL32, LTB, AQP3

### CD4 Naive

Description: Antigen-inexperienced conventional CD4 T cells characterized by CCR7, TCF7, LEF1, IL7R, and strong lymphoid-homing and quiescence programs.

Genes:
- CCR7, LTB, MAL, LEF1, TCF7, IL7R, NOSIP, PIK3IP1, BACH2, SATB1, BCL11B, MALAT1
- AQP3, TXNIP, LIME1, TRABD2A, ETS1, THEMIS, FYB1, LDHB, MIR155HG, LTBR, TRBC1, TRBC2

### CD8 Naive

Description: Antigen-inexperienced CD8 T cells that resemble CD4 naive cells transcriptionally but are distinguished by CD8A/CD8B expression and a cytotoxic-lineage T-cell program.

Genes:
- CD8A, CD8B, CCR7, LTB, MAL, LEF1, TCF7, IL7R, NOSIP, PIK3IP1, BACH2, SATB1
- BCL11B, AQP3, TXNIP, LIME1, TRABD2A, ETS1, THEMIS, FYB1, LDHB, MIR155HG, TRBC1, TRBC2

### Regulatory T Cell

Description: Suppressive CD4 T cells defined by FOXP3, high IL2RA and CTLA4, and activation or checkpoint-associated markers such as TIGIT and TNFRSF4.

Genes:
- FOXP3, IL2RA, CTLA4, IKZF2, TNFRSF4, TNFRSF18, TIGIT, LAYN, BATF, IL32, DUSP4, RTKN2
- CCR7, IL7R, LTB, MALAT1, BACH2, SATB1, ICOS, LAIR2, COTL1, TNFRSF9, GZMK, ENTPD1

## cd4 proliferating

### Activated or memory CD4 T cells

Description: Non-cycling activated or memory CD4 T cells that may be mistaken for a proliferating CD4 population when activation markers are prominent.

Genes:
- IL7R, CCR7, LTB, MAL, LEF1, NOSIP, S100A4, LTB, IL32, CD40LG, ICOS, CXCR5
- PDCD1, HLA-DRA, HLA-DRB1, IL2RA, TNFRSF4, CD3D, CD3E, TRBC1, TRBC2, TRAC, MALAT1

### Proliferating CD4 T cells

Description: Cycling helper T cells undergoing active cell division while retaining a CD4 T-cell receptor program.

Genes:
- MKI67, TOP2A, TUBA1B, HMGB2, TYMS, UBE2C, CENPF, CENPA, STMN1, TUBB, CDC20, CDK1
- CCNB1, CCNB2, NUSAP1, ASPM, PCLAF, TTK, BIRC5, KIF11, KIF20A, KIF2C, CD3D, CD3E
- TRBC1, IL7R

### Proliferating CD8 T cells

Description: Cycling cytotoxic T cells distinguished from proliferating CD4 cells by CD8 expression and elevated effector molecules such as CCL5, NKG7, and granzymes.

Genes:
- MKI67, TOP2A, TYMS, UBE2C, CENPF, STMN1, BIRC5, CDK1, CCNB1, NUSAP1, PCLAF, CD8A
- CD8B, CCL5, NKG7, GZMK, GZMH, GZMA, LST1, TRBC1, TRBC2, CD3D, CD3E, TRAC

### Proliferating NK cells

Description: Cycling natural killer cells that can be confused with proliferating T cells because of shared cell-cycle genes but show strong innate cytotoxic and NK-receptor programs.

Genes:
- MKI67, TOP2A, TYMS, UBE2C, CENPF, STMN1, BIRC5, CDK1, CCNB1, NUSAP1, PCLAF, NKG7
- GNLY, PRF1, GZMB, GZMH, KLRD1, FCGR3A, TYROBP, TRAC, TRBC1, XCL1, XCL2, KLRB1

### Proliferating regulatory T cells

Description: Activated proliferating CD4 regulatory T cells characterized by FOXP3, high-affinity IL-2 signaling, and suppressive checkpoint receptors.

Genes:
- FOXP3, IL2RA, CTLA4, TIGIT, IKZF2, TNFRSF4, TNFRSF18, LRRC32, BATF, ICOS, IL32, HLA-DRA
- MKI67, TOP2A, TYMS, UBE2C, CENPF, STMN1, BIRC5, CD3D, CD3E, TRBC1, TRAC, LAYN

## cd4 tcm

### CD4 Naive

Description: Naive CD4 T cells are antigen-inexperienced lymphocytes marked by strong CCR7/SELL trafficking, TCF7/LEF1 stem-like programs, and low effector-gene expression.

Genes:
- CCR7, SELL, TCF7, LEF1, MAL, NOSIP, LTB, AQP3, IL7R, MALAT1, BACH2, KLF2
- LTBR, TRABD2A, TXNIP, PIK3IP1, FYB1, TRAT1, BCL11B, ETS1, CCR7, CD27, LDHB, NOSIP

### CD4 TCM

Description: CD4 central-memory T cells retain lymphoid-homing and self-renewal programs while expressing IL7R and CCR7 with limited cytotoxic differentiation.

Genes:
- IL7R, LTB, CCR7, TCF7, LEF1, AQP3, MAL, NOSIP, TRAT1, PTPRCAP, FYB1, LTBR
- PIK3IP1, TRABD2A, TXNIP, KLF2, BACH2, ETS1, CD27, IL32, MALAT1, BCL11B, LAT, CD4

### CD4 TEM

Description: CD4 effector-memory T cells have experienced antigen and show reduced naive-homing features with increased IL7R, S100A4, GZMK, and inflammatory effector activity.

Genes:
- IL7R, S100A4, IL32, GZMK, LTB, LTB, CCL5, CD3D, CD3E, TRBC1, TRBC2, LST1
- AQP3, S100A10, ANXA1, IFITM1, IFITM2, IFITM3, COTL1, MALAT1, PTPRCAP, FYB1, TRAT1, CD27

### CD8 T

Description: CD8 T cells are cytotoxic T lymphocytes distinguished from CD4 memory cells by CD8A/B and stronger granule-mediated cytotoxic, chemokine, and NK-receptor programs.

Genes:
- CD8A, CD8B, CCL5, NKG7, CTSW, GZMK, GZMH, GZMB, PRF1, GNLY, KLRD1, KLRB1
- FGFBP2, CCL4, CCL4L2, CCL3, LST1, TRBC1, TRBC2, CD3D, CD3E, CD3G, LAG3, KLRG1
- HLA-B

### Regulatory T

Description: Regulatory T cells suppress immune responses through FOXP3-driven regulatory circuitry and high expression of IL2RA, CTLA4, TIGIT, and TNFRSF18.

Genes:
- FOXP3, IL2RA, CTLA4, TIGIT, IKZF2, TNFRSF18, TNFRSF4, IL32, LAYN, BATF, LRRC32, ICOS
- IL7R, MIR155HG, DUSP4, TNFRSF9, RTKN2, C15orf48, LAIR2, CARD11, CD3D, CD3E, TRBC1, TRBC2

## cd4 tem

### CD4 central memory T cells

Description: A frequently confused neighboring population with less differentiated lymphoid-memory features, retaining CCR7, SELL, TCF7, LEF1, and stronger lymph-node homing characteristics than CD4 effector memory cells.

Genes:
- CCR7, SELL, LTB, MAL, IL7R, LTBR, MALAT1, NOSIP, TRAT1, LEF1, TCF7, MIR155HG
- LINC02446, TXNIP, BCL11B, CCR6, BACH2, BCL2, NOSIP, PIK3IP1

### CD8 effector memory T cells

Description: A common neighboring cytotoxic T-cell population that can resemble CD4 effector memory cells but is distinguished by CD8A/CD8B and stronger NKG7, PRF1, GNLY, GZMH, or FGFBP2 expression.

Genes:
- CD8A, CD8B, NKG7, CCL5, GZMK, GZMH, PRF1, GNLY, CCL4, CCL4L2, KLRD1, KLRB1
- CTSW, FGFBP2, KLRG1, CD3D, CD3E, TRBC1, TRBC2, IL32

### GZMK+ CD4 effector memory T cells

Description: A common circulating CD4 effector-memory population characterized by GZMK, IL7R, and memory-associated chemokine receptor expression, often representing antigen-experienced but non-cytotoxic T cells.

Genes:
- GZMK, IL7R, LTB, MAL, MALAT1, LINC02446, TRAT1, LTBR, NOSIP, GPR183, ICOS, CD27
- MIR155HG, TNFRSF4, CXCR4, CXCR5, CCL5, IL32, LST1, KLRB1

### Th1-like CD4 effector memory T cells

Description: An inflammatory CD4 memory subset with Th1 polarization and enhanced type-1 cytokine and cytotoxic effector programs, frequently marked by CXCR3, TBX21, IFNG, and CCL5.

Genes:
- TBX21, IFNG, CXCR3, CCL5, NKG7, GZMK, PRF1, GNLY, CCL4, CCL4L2, HLA-DRA, HLA-DPB1
- IL12RB2, STAT4, KLRD1, CD40LG, TNFRSF9, MIR155HG, IL32, TRBC2

### Th17-like CD4 effector memory T cells

Description: A mucosal-homing CD4 effector-memory population with Th17-associated transcriptional features including CCR6, KLRB1, RORA, IL23R, and occasional IL17A or IL17F expression.

Genes:
- KLRB1, CCR6, RORA, IL7R, IL23R, CCL20, RORC, IL17A, IL17F, KLRB1, MIR4435-2HG, AQP3
- LINC00861, LTB, MAL, GPR183, CCR4, TNFRSF4, BATF, MIR155HG

## cd8 naive

### CD4 Naive T Cell

Description: Naive helper-lineage T cells that closely resemble naive CD8 cells transcriptionally but generally lack strong CD8A and CD8B expression.

Genes:
- CCR7, LTB, IL7R, MAL, TCF7, LEF1, AQP3, NOSIP, CCR6, MALAT1, CD27, CD28
- TRAT1, THEMIS, BCL11B, SATB1, IL2RG, TRBC1, TRBC2, CD3D, CD3E, CD3G, LTB, IL32

### CD8 Central Memory

Description: Antigen-experienced CD8 T cells retaining CCR7-dependent lymphoid recirculation and substantial proliferative potential.

Genes:
- IL7R, CCR7, LTB, MAL, TCF7, LEF1, AQP3, CD27, CD28, IL2RG, MALAT1, NOSIP
- TRAT1, THEMIS, BCL11B, SATB1, CD8A, CD8B, LTB, TRBC1, TRBC2, CD3D, CD3E, IL32

### CD8 Effector Memory GZMK+

Description: Memory-like CD8 T cells with tissue-experienced and moderate cytotoxic programs dominated by GZMK rather than granzymes B or H.

Genes:
- GZMK, IL7R, LTB, IL32, CD3D, CD3E, CD3G, TRBC1, TRBC2, CD8A, CD8B, CCL5
- NKG7, LST1, AQP3, CD27, CD28, LTB, MALAT1, KLRB1, S100A4, TNFAIP3, HLA-B, HLA-C

### CD8 Naive

Description: Antigen-inexperienced CD8 T cells with lymphoid-homing, quiescence, and T-cell stemness programs.

Genes:
- CCR7, LTB, IL7R, MAL, TCF7, LEF1, MALAT1, AQP3, NOSIP, BCL11B, SATB1, LST1
- CD27, CD28, TRAT1, THEMIS, CCR6, CD8A, CD8B, TRBC2, TRBC1, CD3D, CD3E, CD3G

### Cytotoxic CD8 T Cell

Description: Differentiated CD8 T cells with strong granule-mediated cytotoxicity and partial NK-cell receptor expression.

Genes:
- NKG7, CCL5, GZMB, GZMH, GNLY, PRF1, GZMA, GZMK, KLRD1, KLRB1, KLRG1, FCGR3A
- CTSW, FGFBP2, TRBC1, TRBC2, CD3D, CD3E, CD8A, CD8B, CST7, TYROBP, HCST, XCL1
- XCL2

## cd8 proliferating

### Cycling CD4 T cells

Description: A proliferating helper-lineage T-cell population that can resemble cycling CD8 T cells but preferentially expresses CD4, IL7R, CCR7, LTB, and MAL.

Genes:
- CD3D, CD3E, CD3G, TRBC1, TRBC2, CD4, IL7R, LTB, MAL, CCR7, MKI67, TOP2A
- TYMS, STMN1, TUBA1B, HMGB2, UBE2C, BIRC5, PCLAF, CENPF, NUSAP1, TPX2, AURKB, CDC20
- CCNB1, CCNA2, CDK1, RRM2, TK1, PTTG1

### Cycling CD8 T cells

Description: CD8 T cells undergoing active cell division, marked by strong S-phase and mitotic programs alongside CD3 and CD8 expression.

Genes:
- CD3D, CD3E, CD3G, TRBC1, TRBC2, CD8A, CD8B, MKI67, TOP2A, TYMS, STMN1, TUBA1B
- HMGB2, UBE2C, BIRC5, PCLAF, CENPF, NUSAP1, TPX2, AURKB, CDC20, CCNB1, CCNA2, CDK1
- CENPA, TTK, KIF11, KIF20A, RRM2, TK1, PTTG1, GTSE1

### Cycling NK cells

Description: Proliferating innate cytotoxic lymphocytes that resemble cycling CD8 T cells but show stronger NK-associated genes including NKG7, GNLY, FCGR3A, XCL1, and XCL2.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMH, CTSW, FCGR3A, TRAC, CD3D, CD3E, MKI67, TOP2A
- TYMS, STMN1, TUBA1B, HMGB2, UBE2C, BIRC5, PCLAF, CENPF, NUSAP1, TPX2, AURKB, CDC20
- CCNB1, CCNA2, CDK1, KIF11, RRM2, TK1, XCL1, XCL2

### Cycling effector CD8 T cells

Description: Proliferating cytotoxic CD8 T cells that combine a strong cell-cycle program with effector molecules such as CCL5, NKG7, granzymes, and perforin.

Genes:
- CD3D, CD3E, TRBC1, TRBC2, CD8A, CD8B, MKI67, TOP2A, STMN1, TYMS, NKG7, CCL5
- GNLY, GZMK, GZMA, CTSW, PRF1, GZMB, HLA-DRA, IFITM1, IFITM3, BIRC5, UBE2C, CENPF
- CCNB1, CDK1, TUBA1B, HMGB2, PCLAF, NUSAP1

## cd8 tcm

### CD8 central memory T cells

Description: Long-lived antigen-experienced CD8 T cells with lymphoid-homing and self-renewal features that retain CCR7, IL7R, and TCF7 expression.

Genes:
- CCR7, IL7R, LTB, TCF7, LEF1, MAL, NOSIP, LTB, AQP3, MALAT1, BACH2, SATB1
- TRBC1, TRBC2, CD3D, CD3E, CD3G, LST1, LTBR, ICOS

### CD8 effector memory T cells

Description: Antigen-experienced CD8 T cells with reduced lymphoid homing and increased cytotoxic effector programs, commonly marked by CCL5, GZMK, and NKG7.

Genes:
- CCL5, GZMK, NKG7, CST7, FGFBP2, GZMH, GZMA, PRF1, CTSW, KLRD1, KLRB1, CD8A
- CD8B, TRBC1, TRBC2, CD3D, CD3E, CD3G, IL32, LST1

### CD8 naive T cells

Description: Antigen-inexperienced CD8 T cells characterized by strong CCR7, TCF7, LEF1, MAL, and lymphoid-homing programs with minimal cytotoxic gene expression.

Genes:
- CCR7, LTB, TCF7, LEF1, MAL, NOSIP, BACH2, SATB1, MALAT1, IL7R, LTBR, AQP3
- CCR7, TRBC1, TRBC2, CD3D, CD3E, CD3G, CD27, LINC00861

### MAIT cells

Description: Innate-like T cells enriched for the semi-invariant TRAV1-2 receptor and mucosal-associated cytotoxic and NK-receptor programs.

Genes:
- TRAV1-2, SLC4A10, KLRB1, NKG7, CCL5, GZMK, GZMA, KLRD1, CTSW, CST7, IL32, LTB
- CD8A, CD8B, TRBC1, TRBC2, CD3D, CD3E, CD3G, MTRNR2L8

### Natural killer cells

Description: Cytotoxic innate lymphocytes that can be mistaken for activated CD8 T cells but typically show strong GNLY, FCGR3A, TYROBP, and NK-receptor expression with limited TCR-chain expression.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMH, FGFBP2, KLRD1, FCGR3A, TYROBP, TRAC, KLRF1, XCL1
- XCL2, CTSW, CST7, CCL5, S1PR5, HCST, CD247, TRBC2

## cd8 tem

### CD4 effector memory T cell

Description: Conventional antigen-experienced CD4 T cells that can overlap with CD8 TEM but are distinguished by CD4-associated expression and generally weaker cytotoxic programs.

Genes:
- CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, IL7R, LTB, MAL, MALAT1, LTB, IL32
- LTB, CCR7, LTB, MIR155HG, LTB, GZMK, IL32, LTB, MAL, LTB, CD4, LTB
- AQP3

### CD8 effector memory (CD8 TEM)

Description: Antigen-experienced CD8 T cells with a circulating effector-memory phenotype, typically marked by GZMK, CCL5, CD8A/CD8B, and moderate cytotoxic gene expression.

Genes:
- CD3D, CD3E, CD3G, TRBC1, TRBC2, CD8A, CD8B, GZMK, CCL5, NKG7, LST1, LTB
- IL7R, MALAT1, MAL, LTB, IL32, GZMA, CST7, HCST, CD247, TRAC, LIME1, CD27
- TXNIP

### CD8 effector memory RA (CD8 TEMRA)

Description: Highly differentiated cytotoxic CD8 T cells lacking naive markers and expressing strong effector molecules such as FGFBP2, GNLY, GZMB, and PRF1.

Genes:
- CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, CD8A, CD8B, FGFBP2, GNLY, GZMB, GZMH
- NKG7, PRF1, CCL5, CTSW, KLRD1, FCGR3A, TYROBP, HCST, CD247, CST7, GZMA, B2M
- HLA-B

### MAIT cell

Description: Innate-like T cells enriched for the TRAV1-2 program and mucosal-associated markers, with variable CD8 expression and rapid cytotoxic effector potential.

Genes:
- TRAV1-2, KLRB1, SLC4A10, ZBTB16, RORA, KLRD1, NKG7, GZMK, GZMA, CCL5, CST7, IL7R
- CCR6, CXCR6, SLC7A5, LTB, IL32, CD3D, CD3E, TRAC, CD8A, HCST, KLRC4, KLRF1
- CTSW

### Natural killer cell

Description: Cytotoxic lymphocytes that resemble CD8 TEMRA cells but generally lack a coherent T-cell receptor complex and show strong KLRD1, TYROBP, and GNLY expression.

Genes:
- NKG7, GNLY, KLRD1, FCGR3A, TYROBP, TRAC, CD3D, CD3E, CD247, HCST, KLRF1, KLRC1
- XCL1, XCL2, PRF1, GZMB, GZMH, CTSW, FGFBP2, CST7, CCL5, S1PR5, TRBC1, B2M
- HLA-B

## cdc1

### DC3

Description: DC3 cells are monocyte-like dendritic cells with mixed antigen-presenting and inflammatory myeloid programs and are a frequent cDC2 or monocyte annotation confounder.

Genes:
- CD14, CD163, FCGR3A, LILRA1, LILRB1, LILRB3, MS4A7, CTSD, CTSB, TYMP, LGALS3, SAT1
- FCN1, S100A8, S100A9, CTSS, CST3, LYZ, IFITM3, SERPINA1, AIF1, CFD, CD36, ITGAX
- CLEC12A

### cDC1

Description: Conventional type 1 dendritic cells specialized for cross-presentation and priming of cytotoxic T-cell responses, marked by CLEC9A and XCR1.

Genes:
- CLEC9A, XCR1, BATF3, IRF8, CADM1, WDFY4, DNASE1L3, THBD, CLU, C1orf54, SNX22, IDO1
- DPP4, CPNE3, CST3, FCER1A, CD74, HLA-DRA, HLA-DPA1, HLA-DPB1, HLA-DQB1, HLA-DMA, HLA-DMB, CTSS
- GPR183

### cDC2

Description: Conventional type 2 dendritic cells are CD1C-positive antigen-presenting cells that promote helper T-cell and mucosal immune responses.

Genes:
- CD1C, CLEC10A, FCER1A, CD1E, COTL1, CST3, CLEC12A, CSF2RA, ITGAX, CD1D, GPR183, CD86
- CD40, HLA-DRA, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, HLA-DMA, HLA-DMB, CTSS, CSTA, LILRB1, CD74
- LY86

### pDC

Description: Plasmacytoid dendritic cells specialize in type I interferon production and express CLEC4C, IL3RA, GZMB, and TCF4 rather than the canonical cDC1 program.

Genes:
- GZMB, GZMB, GZMB, GZMB, TCF4, GZMB, CLEC4C, IL3RA, GZMB, JCHAIN, GZMB, IRF7
- IRF8, PLD4, SERPINF1, PTCRA, TLR7, TLR9, GZMB, IFITM1, IFITM3, IFI6, ISG15, GZMB
- IGJ

## cdc2

### AXL+ SIGLEC6+ dendritic cells

Description: AXL-positive SIGLEC6-positive dendritic cells are a transitional or DC5-like population sharing features of cDC2 and plasmacytoid dendritic cells.

Genes:
- AXL, SIGLEC6, CD2, CD5, CD22, COTL1, GZMB, LILRA4, TCF4, IRF7, SERPINF1, PLD4
- GZMB, PTCRA, IL3RA, CLEC4C, IRF8, TCL1A, HLA-DRA, GPR183, CD1C, FCER1A, CST3, LST1

### CD14+ CD1C+ DC3

Description: DC3 cells are a CD1C-positive dendritic population with a monocyte-like inflammatory program and enhanced expression of CD14, CD163, and CD36.

Genes:
- CD14, CD163, CD36, CD1C, CLEC10A, FCER1A, CD1E, CLEC12A, S100A10, FCGR2A, MS4A7, LILRB1
- LILRB3, CTSD, CTSL, TYMP, THBD, CD86, CD81, LGALS3, S100A11, CSTA, IFITM3, HLA-DRA
- CD74

### CD14+ classical monocytes

Description: Classical monocytes are phagocytic myeloid cells that can resemble inflammatory DC3 cells but are distinguished by strong LYZ, S100A8, S100A9, FCN1, and VCAN expression.

Genes:
- LYZ, S100A8, S100A9, CTSD, CTSS, FCN1, VCAN, CTSL, LGALS3, S100A10, TYMP, FCGR3A
- MS4A7, LILRB1, LILRB3, CTSD, AIF1, FCER1G, TYROBP, LGALS9, IFITM3, FCGR2A, CTSD, MNDA
- SERPINA1

### CD1C+ CLEC10A+ cDC2

Description: Canonical blood cDC2 cells specialized for antigen presentation and priming of CD4 T-cell responses, characterized by CD1C, CLEC10A, and FCER1A expression.

Genes:
- CD1C, CLEC10A, FCER1A, CD1E, CST3, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, HLA-DRA, HLA-DRB1, HLA-DMA
- HLA-DMB, GPR183, CD74, CTSS, IRF4, CLEC12A, CD86, CSTA, PLD4, LILRB1, SERPINF1, CCL22

### Plasmacytoid dendritic cells

Description: Plasmacytoid dendritic cells are antiviral interferon-producing cells defined by GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, and GZMB.

Genes:
- GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB
- GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB, GZMB

## dnt

### Conventional DN alpha-beta T cells

Description: Conventional CD4−CD8− alpha-beta T cells retain a naive or central-memory T-cell program without strong cytotoxic or innate-like receptor expression.

Genes:
- TRAC, TRBC1, TRBC2, CD3D, CD3E, CD3G, CD247, LCK, LAT, TRAT1, MAL, IL7R
- CCR7, LTB, MALAT1, NOSIP, PTPRCAP, FYB1, LEF1, TCF7, LTB, IL32

### Gamma-delta T cells

Description: Gamma-delta T cells express rearranged gamma-delta receptors and commonly show an innate-like cytotoxic program with NK-associated receptors.

Genes:
- TRDC, TRGC1, TRGC2, TRDV2, TRGV9, KLRD1, KLRC1, KLRF1, NKG7, GNLY, GZMB, GZMH
- FGFBP2, CCL5, CTSW, PRF1, FCER1G, TYROBP, CST7, CD3D, CD3E, CD247

### MAIT cells

Description: MAIT cells are semi-invariant MR1-restricted T cells enriched for TRAV1-2, SLC4A10, KLRB1, ZBTB16, and mucosal antibacterial effector features.

Genes:
- TRAV1-2, SLC4A10, KLRB1, ZBTB16, RORA, CCR6, IL7R, IL18RAP, IL18R1, KLRD1, KLRC1, NKG7
- GZMK, CCL5, KLRF1, NCR3, TRAC, TRBC1, CD3D, CD3E, CD247

### NKT-like T cells

Description: NKT-like T cells are CD3-positive T lymphocytes with a strong NK-receptor and cytotoxic effector program, often resembling NK cells in PBMC datasets.

Genes:
- TRAC, TRBC1, TRBC2, CD3D, CD3E, CD3G, CD247, KLRD1, KLRC1, KLRF1, NKG7, GNLY
- CCL5, GZMB, GZMH, PRF1, CTSW, CST7, FGFBP2, XCL1, XCL2, FCGR3A

### Natural killer cells

Description: NK cells are the principal neighboring population confused with dnT cells because of shared cytotoxic and NK-receptor programs, but they generally lack a coherent surface T-cell receptor complex.

Genes:
- NKG7, GNLY, KLRD1, FCGR3A, TYROBP, FCER1G, TRAC, TRBC1, CD3D, CD3E, KLRF1, KLRC1
- KLRC2, XCL1, XCL2, CCL5, GZMB, GZMH, PRF1, CTSW, FGFBP2, CST7

## doublet

### B_cell_monocyte_doublet

Description: A mixed B-cell and monocyte profile combining B-cell receptor/MHC-II genes with lysosomal and myeloid genes.

Genes:
- CD79A, MS4A1, CD37, CD74, HLA-DRA, HLA-DPA1, CD79B, BANK1, CD22, CD83, CD48, LTB
- LYZ, LST1, FCER1G, TYROBP, CTSS, AIF1, LGALS3, FCN1, CTSD, IFITM3

### Platelet_monocyte_doublet

Description: A platelet-containing myeloid doublet marked by platelet granule and integrin genes together with a monocyte LYZ/LST1 inflammatory program.

Genes:
- PPBP, PF4, NRGN, GNG11, RGS18, SDPR, GP9, ITGA2B, ITGB3, PF4V1, TUBB1, NCOA4
- LYZ, LST1, S100A8, S100A9, CTSS, FCER1G, TYROBP, AIF1, LGALS3, FCN1

### T_cell_NK_cell_doublet

Description: A mixed lymphocyte profile showing a T-cell receptor/CD3 program together with cytotoxic NK-cell genes.

Genes:
- CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, IL7R, LTB, MALAT1, NKG7, GNLY, PRF1
- GZMB, GZMH, CTSW, KLRD1, FCER1G, TYROBP, CCL5, XCL1, XCL2, KLRB1

### T_cell_monocyte_doublet

Description: A mixed T-cell and myeloid profile characterized by CD3/TRAC expression alongside monocyte genes such as LYZ, LST1, and S100A8/S100A9.

Genes:
- CD3D, CD3E, CD3G, TRAC, TRBC1, IL7R, LTB, MALAT1, IL32, LST1, S100A8, S100A9
- LYZ, CTSS, FCN1, LGALS3, TYMP, CTSD, FCER1G, TYROBP, AIF1, LGALS9

## eryth

### Erythroblast (immature erythroid)

Description: Immature erythroid cells actively undergoing hemoglobinization and red-cell membrane assembly, characterized by erythroid transcription factors, transferrin receptor, and heme-biosynthetic genes.

Genes:
- TFRC, CD36, GATA1, KLF1, TAL1, NFE2, EPOR, ALAS2, AHSP, GYPA, HBB, HBA1
- HBA2, CA1, SLC4A1, EPB42, ANK1, SPTA1, SPTB, RHAG, FECH, PPOX, UROD, HMBS
- BCL11A, TRIM10

### Mature erythrocyte

Description: Highly differentiated enucleated red blood cells dominated by globin transcripts and specialized cytoskeletal, membrane, and ion-transport components.

Genes:
- HBB, HBA1, HBA2, GYPA, SLC4A1, CA1, EPB42, ANK1, SPTA1, SPTB, RHAG, RHD
- GYPB, GYPE, AQP1, TMOD1, ELL2, TRIM10, PIEZO1, ATP1B1, BPGM, P4HA2

### Platelet/megakaryocyte

Description: Platelet-lineage cells involved in hemostasis, distinguished from erythroid cells by platelet granule, integrin, and megakaryocytic cytoskeletal programs.

Genes:
- PPBP, PF4, NRGN, GNG11, RGS18, SDPR, CLU, GP9, ITGA2B, ITGB3, GP1BA, GP1BB
- TUBB1, CAVIN2, FERMT3, RGS10, PFN1, ACTB, TLN1, GNAQ, PLEK, NBEAL2, SELP, F13A1

### Reticulocyte (late erythroid)

Description: Late erythroid cells retaining residual biosynthetic activity while expressing abundant hemoglobin and mature erythrocyte membrane proteins.

Genes:
- HBB, HBA1, HBA2, AHSP, ALAS2, GYPA, CA1, SLC4A1, EPB42, ANK1, SPTA1, SPTB
- RHAG, RHD, GYPB, TRIM10, PIEZO1, ATP1B1, BNIP3L, FECH, PPOX, UROD, HMBS, TFRC

## gdt

### Cytotoxic γδ T cells

Description: Activated γδ T cells with strong granule-mediated cytotoxicity and NK-like effector programs, often spanning both Vδ1 and Vδ2 compartments.

Genes:
- TRDC, TRGC1, TRGC2, CD3D, CD3E, CD3G, CD247, NKG7, GNLY, GZMB, GZMH, GZMK
- GZMA, PRF1, CTSW, CCL5, KLRD1, KLRC1, KLRB1, FCGR3A, XCL1, XCL2, LST1, TYROBP
- TRBC2

### MAIT cells

Description: MR1-restricted innate-like T cells that can resemble γδ T cells through KLRB1, SLC4A10, ZBTB16, and cytotoxic gene expression.

Genes:
- TRAV1-2, SLC4A10, KLRB1, ZBTB16, RORA, IL7R, CCR6, KLRD1, NKG7, GZMK, GZMA, CCL5
- CTSW, TRAC, TRBC1, TRBC2, CD3D, CD3E, CD3G, CD247, KLRF1, FCER1A, LTB, IL32

### NK cells

Description: Cytotoxic innate lymphocytes commonly confused with γδ T cells because of overlapping NK-receptor, granzyme, perforin, and NKG7 programs but lacking a γδ T-cell receptor program.

Genes:
- KLRD1, NCR1, NCR3, KLRF1, FCGR3A, TYROBP, FCER1G, TRAC, TRBC1, TRBC2, NKG7, GNLY
- GZMB, GZMH, PRF1, CTSW, CCL5, XCL1, XCL2, KLRC1, KLRC2, HCST, SH2D1B1, S1PR5
- TBX21

### Vδ1 γδ T cells

Description: Tissue-surveying γδ T cells enriched for TRDV1 and diverse Vγ chains, with frequent NK-like receptor expression and cytotoxic effector features.

Genes:
- TRDV1, TRGV2, TRGV3, TRGV4, TRGV5, TRGV8, TRDC, TRGC1, TRGC2, CD3D, CD3E, CD3G
- CD247, KLRD1, KLRC1, FCER1G, TYROBP, CCL5, NKG7, GZMK, GZMH, CTSW, ITGA1, CD69

### Vδ2 γδ T cells

Description: Circulating phosphoantigen-responsive γδ T cells dominated by the TRGV9-TRDV2 receptor pair and commonly showing cytotoxic and innate-like activation.

Genes:
- TRGV9, TRDV2, TRDC, TRGC1, TRGC2, CD3D, CD3E, CD3G, CD247, LCK, MAL, LTB
- IL32, CCL5, NKG7, GZMK, GZMH, KLRD1, KLRB1, SLC4A10, BTN3A1, BTN3A2, BTN3A3, HLA-B

## hspc

### CD14_Monocyte

Description: Classical CD14-positive monocytes are a common HSPC misannotation when immature myeloid progenitor cells lose clear CD34 expression and acquire inflammatory myeloid genes.

Genes:
- LYZ, S100A8, S100A9, CTSD, FCN1, CTSS, TYMP, CTSL, LGALS3, LILRB1, IFITM3, FCER1G
- TYROBP, AIF1, SAT1, CFD, SERPINA1, VCAN, MNDA, LGALS9

### GMP

Description: Granulocyte-monocyte progenitors showing immature myeloid commitment with neutrophil granule, innate signaling, and myelopoietic transcriptional programs.

Genes:
- CD34, CSF3R, MPO, ELANE, PRTN3, CTSG, AZU1, BPI, CEBPA, CEBPB, SPI1, FCER1G
- CYBB, CTSS, S100A8, S100A9, MNDA, LILRB1, TYMP, NCF2

### HSC_MPP

Description: Primitive hematopoietic stem and multipotent progenitor cells with strong self-renewal, stemness, and immature CD34-positive programs.

Genes:
- CD34, PROM1, THY1, HLF, MECOM, MLLT3, GATA2, MEIS1, ERG, HOPX, SPINK2, FLI1
- MSI2, AVP, SOCS2, KIT, SELL, G0S2, CYTL1, MPL

### LMPP

Description: Lymphoid-primed multipotent progenitors expressing CD34 and FLT3 together with early lymphoid specification and antigen-receptor assembly programs.

Genes:
- CD34, FLT3, IL7R, LTB, MAL, SATB1, BCL11A, SOX4, TCF4, GATA3, IGLL1, EBF1
- VPREB3, DNTT, RAG1, RAG2, PTCRA, CD7, CCR7, HLA-DRA

### Megakaryocyte_Erythroid_Progenitor

Description: Megakaryocyte-erythroid progenitors combine CD34-positive immaturity with platelet-biased and early erythroid differentiation programs.

Genes:
- CD34, MPL, GATA1, KLF1, TAL1, FLI1, NFE2, ITGA2B, GP9, GP1BA, TUBB1, PF4
- PPBP, RGS18, NRGN, ALAS2, FECH, CA1, HBB, HBA1

## ilc

### CD4 T cell

Description: Conventional CD4 T lymphocytes are a frequent ILC misannotation because they share IL7R, KLRB1, and helper-cytokine programs but retain strong CD3 and T-cell receptor expression.

Genes:
- IL7R, LTB, MAL, CCR7, LTB, MALAT1, TRBC2, TRAC, CD3D, CD3E, CD3G, LST1
- IL32, LTB, MHC2TA, ICOS, CXCR4, MIR155HG, MAL, NOSIP, TCF7, LEF1, CCR6, KLRB1

### ILC1

Description: T-bet-driven innate lymphoid cells producing IFN-gamma and TNF, with an NK-like cytotoxic receptor profile but generally less abundant granzymes than conventional NK cells.

Genes:
- TBX21, IFNG, TNF, XCL1, XCL2, NCR1, KLRD1, FCER1G, TYROBP, TRAC, IL7R, CD69
- CCL5, NKG7, GZMK, RUNX3, ZBTB16, EOMES, HOPX, CXCR6, S1PR5, CD160

### ILC2

Description: Type 2 innate lymphoid cells characterized by GATA3 and RORA expression and production of IL-5, IL-13, and amphiregulin.

Genes:
- GATA3, RORA, IL7R, KLRB1, IL1RL1, PTGDR2, IL17RB, HPGDS, CLC, IL5, IL13, AREG
- KIT, LTC4S, CCR4, GPR183, RGS1, MTRNR2L8, TNFRSF18, ICOS, KLRG1, CCL22

### ILC3

Description: RORC- and AHR-dependent innate lymphoid cells that produce IL-17A and IL-22 and commonly express CCR6, IL23R, and NCR2.

Genes:
- RORC, AHR, KLRB1, IL7R, NCR2, IL23R, IL1R1, CCR6, KIT, IL17A, IL22, CCL20
- TNFSF15, CSF2, L17RA, RORA, TRDC, CD7, LTB, S100A4, MHC2TA, HLA-DPA1

### NK cell

Description: Cytotoxic innate lymphocytes that are commonly confused with ILC1 but show strong perforin, granzyme, NKG7, and NK-receptor programs.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMH, GZMA, CTSW, KLRD1, FCGR3A, TYROBP, TRAC, XCL1
- XCL2, CCL5, KLRF1, KLRC1, KLRC2, NCR1, S1PR5, EOMES, TBX21, CD160, HCST, TRBC1

## mait

### Conventional_CD8_Cytotoxic_T

Description: Conventional cytotoxic CD8 T cells resemble MAIT cells through CD8 and granule programs but generally lack the defining TRAV1-2/SLC4A10 MAIT signature.

Genes:
- CD8A, CD8B, CD3D, CD3E, TRAC, TRBC1, TRBC2, CCL5, NKG7, GZMK, GZMH, CTSW
- PRF1, GZMB, FGFBP2, CX3CR1, CD27, CD28, LAG3, CD96, ITGA1, MAL, LTB, IL32

### Cytotoxic_MAIT

Description: An activated MAIT state with strong cytotoxic effector expression while retaining TRAV1-2, SLC4A10, KLRD1, and NCR3.

Genes:
- TRAV1-2, SLC4A10, KLRD1, NKG7, CCL5, GZMK, GZMH, GZMB, GNLY, CTSW, PRF1, FGFBP2
- KLRF1, KLRB1, NCR3, ZBTB16, RORA, CD8A, CD8B, TRBC1, TRBC2, CD3D, CD3E, IL32

### Gamma_Delta_T_Cell

Description: Gamma-delta T cells can mimic MAIT cells through cytotoxic and innate-like programs but are identified by TRDC, TRGC1/2, and TRDV2 or TRGV9 expression.

Genes:
- TRDC, TRGC1, TRGC2, TRDV2, TRGV9, CD3D, CD3E, TRAC, TRBC1, TRBC2, KLRD1, KLRB1
- NKG7, CCL5, GZMK, GZMB, CTSW, PRF1, FCGR3A, CD247, HCST, KLRC1, ZBTB16, IL32

### Natural_Killer_Cell

Description: NK cells are highly cytotoxic innate lymphocytes with abundant NKG7, GNLY, FCGR3A, TYROBP, and killer-receptor expression but limited T-cell receptor machinery.

Genes:
- NKG7, GNLY, GZMB, GZMH, PRF1, CTSW, FGFBP2, KLRD1, KLRF1, FCGR3A, TYROBP, TRAC
- TRBC1, XCL1, XCL2, CCL5, HCST, TYROBP, SAMD3, SPON2, KLRC1, KLRB1, CD247, LST1

### Resting_IL7R_plus_MAIT

Description: A less-differentiated MAIT population expressing the canonical TRAV1-2/SLC4A10 program together with KLRB1, CCR6, RORA, and IL7R.

Genes:
- TRAV1-2, SLC4A10, KLRB1, IL7R, CCR6, RORA, KLRD1, ZBTB16, NCR3, CD8A, CD3D, CD3E
- TRAC, LTB, IL32, MALAT1, LTB, MAL, CCR7, LST1, GZMK, CCL5, CTSW

## nk

### Adaptive NKG2C-positive NK

Description: CMV-associated adaptive NK cells marked by KLRC2, FCGR3A, FCRL6, LILRB1, and a mature cytotoxic transcriptional program.

Genes:
- KLRC2, FCGR3A, FGFBP2, FCRL6, LILRB1, GZMH, PRF1, GNLY, NKG7, CCL5, KLRD1, TYROBP
- FCER1G, TRDC, SPON2, S1PR5, KLRF1, CD2, HCST, CD247, EOMES, TBX21, LST1, IFITM3

### CD56bright cytokine-producing NK

Description: Less terminally differentiated NK cells with strong cytokine and chemokine production, relatively lower FGFBP2 and GZMB, and frequent IL7R or KLRB1 expression.

Genes:
- NCAM1, KLRD1, KLRC1, IL7R, IL2RB, XCL1, XCL2, CCL5, CCL4, GZMK, NKG7, CTSW
- KLRB1, SELL, LTB, MALAT1, TRBC2, EOMES, TBX21, HCST, CD247, TYROBP, FCER1G, GZMA

### CD56dim cytotoxic NK

Description: Highly cytotoxic, mature NK cells that typically express FCGR3A, FGFBP2, GNLY, PRF1, and GZMB.

Genes:
- NKG7, GNLY, FGFBP2, FCGR3A, PRF1, GZMB, GZMH, CTSW, KLRD1, TYROBP, FCER1G, TRDC
- XCL2, CCL5, SPON2, FCRL6, LST1, S1PR5, KLRF1, KLRB1, HCST, CD247, EOMES, TBX21

### Cytotoxic CD8 T cell

Description: The principal neighboring population confused with NK cells, consisting of T-cell receptor-positive cytotoxic lymphocytes that retain CD3D, CD3E, TRAC, and TRBC expression.

Genes:
- CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, CD8A, CD8B, CCL5, NKG7, GZMK, GZMH
- PRF1, CTSW, GZMA, CD2, CD247, LCK, MALAT1, LTB, IL7R, MHC1, LEF1, MAL

## nk proliferating

### Cycling T cells

Description: Cycling T cells share the proliferative program of dividing NK cells but show a persistent CD3-T-cell receptor complex and often IL7R or LTB expression.

Genes:
- MKI67, TOP2A, STMN1, TUBA1B, TYMS, PCNA, UBE2C, BIRC5, CENPF, CDK1, CCNB1, CCNB2
- CDC20, NUSAP1, TK1, RRM2, AURKB, KIF11, PCLAF, CD3D, CD3E, CD3G, TRBC1, TRBC2
- IL7R, LTB, MALAT1

### Cytotoxic CD8 T cells

Description: Cytotoxic CD8 T cells can resemble NK cells and proliferating NK cells but are distinguished by CD3 and T-cell receptor transcripts together with CD8 expression.

Genes:
- CD3D, CD3E, CD3G, TRBC1, TRBC2, CD8A, CD8B, NKG7, CCL5, PRF1, GZMK, GZMA
- CTSW, LST1, FGFBP2, GZMH, B2M, LTB, IL32, MALAT1, TRAC, CD247, LCK, MHC1
- CX3CR1, CCL4

### Cytotoxic NK cells

Description: Mature cytotoxic NK cells are characterized by abundant granule-mediated killing genes, NK receptors, and chemokines such as XCL1 and XCL2.

Genes:
- NKG7, GNLY, PRF1, GZMB, GZMH, GZMA, CTSW, KLRD1, FCGR3A, TRAC, KLRB1, KLRF1
- KLRC1, XCL1, XCL2, CCL5, FGFBP2, SPON2, HCST, TYROBP, TRDC, S100A4, B2M, IFITM3
- CST7, LST1

### Proliferating NK cells

Description: Cycling natural killer cells retain NK-lineage cytotoxic programs while strongly expressing genes associated with DNA replication, mitosis, and cell division.

Genes:
- MKI67, TOP2A, STMN1, TUBA1B, TUBB, TYMS, PCNA, UBE2C, BIRC5, CENPF, CENPE, CDK1
- CCNB1, CCNB2, CDC20, CDC25C, NUSAP1, HMGB2, PCLAF, TK1, RRM2, DHFR, AURKB, AURKA
- KIF11, KIF20A, KIF2C, GTSE1, NKG7, GNLY, PRF1, KLRD1, FCGR3A

## nk_cd56bright

### CD8_effector_T

Description: Conventional CD8 T cells that can resemble CD56bright NK cells when they express GZMK, NKG7 and CCL5 but retain a strong CD3/TRAC T-cell receptor program.

Genes:
- CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, CD8A, CD8B, LST1, CCL5, NKG7, GZMK
- GZMA, CST7, LTB, IL7R, MAL, TRAT1, CD247, CD2, LCK, MALAT1

### NKT_like

Description: T-cell receptor-positive lymphocytes with a mixed T-cell and NK-cell program, commonly expressing CD3D/E, TRAC, CD8A/B, NKG7 and KLRD1.

Genes:
- TRAC, CD3D, CD3E, CD3G, TRBC1, TRBC2, CD8A, CD8B, KLRD1, NKG7, CCL5, GZMK
- KLRB1, KLRF1, XCL1, XCL2, CCL4, CST7, FCER1G, TYROBP, CD247, HCST

### NK_CD56bright

Description: Cytokine-responsive NK cells with relatively high CD56, IL7R, CCR7, KLRC1, XCL1/XCL2 and GZMK expression and comparatively lower terminal cytotoxicity.

Genes:
- NCAM1, KLRD1, KLRC1, XCL1, XCL2, GZMK, IL7R, CCR7, KLRB1, IL2RA, IL2RB, CCL4
- CCL5, CCL3, NKG7, LTB, MAL, S1PR1, TRDC, AREG

### NK_CD56dim

Description: Mature cytotoxic NK cells characterized by FCGR3A, FGFBP2, S1PR5, KLRF1, GNLY, GZMB and PRF1 expression.

Genes:
- FCGR3A, KLRF1, KLRC2, GNLY, GZMB, PRF1, CTSW, TYROBP, FCER1G, TRAC, NKG7, CCL5
- CCL4, CCL3, KLRD1, NCAM1, GZMH, GZMA, SPON2, FGFBP2, S1PR5, CD247, HCST, XCL1
- XCL2

### NK_activated

Description: Activated NK cells showing inducible antigen-presentation and cytokine-response programs together with NK cytotoxic effector genes.

Genes:
- CD69, HLA-DRA, HLA-DPA1, HLA-DPB1, IL2RA, TNFRSF9, IFNG, CCL3, CCL4, XCL1, XCL2, NKG7
- CCL5, GZMK, GZMB, PRF1, GNLY, KLRD1, FCER1G, TYROBP

## pdc

### AXL+ SIGLEC6+ dendritic cell

Description: AXL+ SIGLEC6+ dendritic cells are an antigen-presenting transitional dendritic population that can resemble pDC but expresses AXL, SIGLEC6, CD5 and cDC-associated genes.

Genes:
- AXL, SIGLEC6, CD5, CD2, CD1C, FCER1A, CLEC10A, CST3, CD1E, CLEC12A, CSF2RA, HLA-DQA1
- HLA-DQB1, HLA-DPA1, HLA-DPB1, HLA-DRA, HLA-DRB1, LILRA4, LILRB1, CTSS, FCGR2A, MS4A7, CD74, GPR183

### Conventional cDC2

Description: Conventional type 2 dendritic cells are CD1C-positive antigen-presenting cells that specialize in uptake and presentation of extracellular antigens and are commonly confused with pDC.

Genes:
- CD1C, FCER1A, CLEC10A, CD1E, CLEC12A, CST3, CSF2RA, CD74, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1
- HLA-DQA1, HLA-DQB1, CTSS, FCGR2A, CD86, IRF4, COTL1, LILRA4, MS4A7, LST1, FCER1G, TYMP
- SERPINF1

### Conventional pDC

Description: Resting plasmacytoid dendritic cells specialize in rapid type I interferon production and express the canonical CLEC4C, IL3RA, GZMB, TCF4 and GZMB program.

Genes:
- GZMB, JCHAIN, IGJ, TCF4, CLEC4C, IL3RA, SERPINF1, PTCRA, PACSIN1, PLD4, TLR7, TLR9
- IRF8, IRF7, BCL11A, GZMB, LILRB4, AQP3, TPM4, HLA-DRA, GZMB, IRF4, SCT, PTPRS

### IFN-activated pDC

Description: IFN-activated pDC retain pDC identity while displaying a strong interferon-stimulated gene response indicative of recent innate immune activation.

Genes:
- CLEC4C, IL3RA, TCF4, GZMB, IRF7, IFIT1, IFIT2, IFIT3, ISG15, MX1, MX2, OAS1
- OAS2, OASL, IFI6, IFI27, IFITM1, IFITM3, RSAD2, USP18, DDX58, IFIH1, XAF1, PLSCR1
- IRF9

## plasmablast

### Activated memory B cell

Description: An activated antigen-presenting B cell that may be confused with an early plasmablast because of activation and immunoglobulin expression but retains a B-cell receptor and MHC-II program.

Genes:
- MS4A1, CD74, HLA-DRA, HLA-DPA1, HLA-DPB1, CD79A, CD79B, CD37, CD22, CD83, CD69, CD86
- TENT5C, BANK1, PAX5, MEF2C, HLA-DQB1, HLA-DQA1, IGHM, IGHD, CD19, CD40, TNFRSF13B, AIM2
- LTB

### IgA plasmablast

Description: A mucosal-type antibody-secreting plasmablast characterized by IgA production and a prominent secretory-endoplasmic-reticulum program.

Genes:
- IGHA1, IGHA2, JCHAIN, MZB1, XBP1, SEC11C, DERL3, FKBP11, SSR4, TXNDC5, PDIA4, HSPA5
- MANF, EDEM1, DNAJC3, CD38, CD27, SDC1, IGKC, IGLC1, IGLC2, MKI67, STMN1, TUBB
- HMGB2

### IgG plasmablast

Description: An antibody-secreting plasmablast expressing predominantly IgG heavy chains together with a strong unfolded-protein-response and immunoglobulin-secretion program.

Genes:
- IGHG1, IGHG3, IGHG4, JCHAIN, MZB1, XBP1, SEC11C, DERL3, FKBP11, SSR4, TXNDC5, PDIA4
- HSPA5, MANF, EDEM1, DNAJC3, CD38, CD27, SDC1, IGKC, IGLC1, IGLC2, MKI67, STMN1
- TUBB, HMGB2

### IgM plasmablast

Description: An IgM-secreting plasmablast retaining an unswitched immunoglobulin program while displaying strong plasma-cell differentiation and secretory activity.

Genes:
- IGHM, IGHD, JCHAIN, MZB1, XBP1, SEC11C, DERL3, FKBP11, SSR4, TXNDC5, PDIA4, HSPA5
- MANF, EDEM1, DNAJC3, CD38, CD27, SDC1, IGKC, IGLC1, IGLC2, MKI67, STMN1, TUBB
- HMGB2

### Plasma cell

Description: A more terminally differentiated antibody-secreting cell that can resemble plasmablasts but typically shows a stronger mature plasma-cell and protein-folding program.

Genes:
- MZB1, XBP1, SEC11C, DERL3, FKBP11, SSR4, TXNDC5, PDIA4, HSPA5, MANF, EDEM1, DNAJC3
- CD38, SDC1, SLAMF7, JCHAIN, IGKC, IGLC1, IGLC2, IGHG1, IGHA1, IGHM, IRF4, PRDM1
- CD27

## platelet

### Megakaryocyte

Description: A rare platelet-producing megakaryocyte or megakaryocyte-derived cell with platelet genes plus nuclear megakaryocytic lineage regulators.

Genes:
- PPBP, PF4, PF4V1, NRGN, RGS18, GNG11, SDPR, GP9, ITGA2B, GP1BA, TUBB1, TREML1
- SPARC, F13A1, NCOA4, RGS10, CLU, GATA1, FLI1, RUNX1, NFE2, MPL, GP6, ITGB3
- RAB27B

### Platelet

Description: Anucleate circulating platelet characterized by abundant platelet granule, integrin, cytoskeletal, and adhesion transcripts.

Genes:
- PPBP, PF4, PF4V1, NRGN, RGS18, GNG11, SDPR, CLU, RGS10, GP9, ITGA2B, GP1BA
- TUBB1, TREML1, SPARC, F13A1, PEAR1, TNS1, FERMT3, TLN1, MYL9, VCL, ARPC1B, RGS19
- ACTB

### Platelet–T-cell aggregate

Description: A platelet attached to or captured with a T lymphocyte, producing a mixed platelet and T-cell transcriptional signature.

Genes:
- PPBP, PF4, NRGN, RGS18, GNG11, SDPR, GP9, ITGA2B, GP1BA, TUBB1, TREML1, CD3D
- CD3E, TRBC1, TRBC2, IL32, LTB, MAL, IL7R, CCR7, LTB, MALAT1, LST1, IL32
- CD247

### Platelet–monocyte aggregate

Description: A platelet adherent to or co-encapsulated with a monocyte, showing a platelet program together with myeloid phagocytic and inflammatory genes.

Genes:
- PPBP, PF4, NRGN, RGS18, GNG11, SDPR, GP9, ITGA2B, GP1BA, TUBB1, TREML1, LST1
- S100A8, S100A9, CTSS, FCER1G, TYMP, AIF1, LGALS3, CTSD, CTSC, LILRB1, FCN1, IFITM3
- SAT1

## treg

### Activated/effector Treg

Description: An antigen-experienced suppressive Treg state marked by high CTLA4, TNFRSF4, TNFRSF18, TIGIT, ICOS, and activation-associated HLA class II expression.

Genes:
- FOXP3, IL2RA, CTLA4, TNFRSF4, TNFRSF18, TIGIT, ICOS, BATF, LAYN, LRRC32, IL32, HLA-DRA
- HLA-DRB1, TNFRSF9, ENTPD1, CCR8, CCL4, CCL5, GZMK, MIR155HG, FCRL3, RTKN2, IKZF2, LAG3

### Conventional CD4 memory T cell

Description: A non-regulatory CD4 T-cell population with naive or memory lymphoid-trafficking features but lacking the defining FOXP3, IL2RA, and CTLA4 Treg program.

Genes:
- IL7R, LTB, CCR7, TCF7, LEF1, MAL, AQP3, NOSIP, LTBR, KLF2, BACH2, MALAT1
- IL32, TRBC1, TRBC2, CD3D, CD3E, CD3G, LST1, PTPRCAP, LTB, CCR6

### Cycling Treg

Description: A proliferating Treg population retaining core FOXP3 and IL2RA identity while displaying a prominent G1/S and G2/M cell-cycle program.

Genes:
- FOXP3, IL2RA, CTLA4, TIGIT, MKI67, TOP2A, TYMS, STMN1, TUBA1B, TUBB, HMGB2, PCLAF
- UBE2C, CENPF, NUSAP1, BIRC5, CDC20, CDK1, CCNB1, CCNA2, HIST1H4C, HIST1H2AC, H2AFZ, MCM6

### Naive/resting Treg

Description: A quiescent, lymphoid-homing Treg population with sustained FOXP3 and IL2RA expression alongside naive T-cell programs such as CCR7, TCF7, and LEF1.

Genes:
- FOXP3, IL2RA, IKZF2, CTLA4, TCF7, LEF1, CCR7, IL7R, BACH2, KLF2, MAL, NOSIP
- AQP3, LTB, MALAT1, LTBR, SATB1, KLF3, TRBC1, TRBC2, CD3D, CD3E

