# Stage-2 Precomputed Programs

- tissue: lung parenchyma
- n_program_genes: 50
- n_cached_cell_types: 48

## acinar cell

### Alveolar Type I (AT1) Cell

Description: Large, ultra-thin squamous epithelial cells covering the vast majority of the alveolar surface area to facilitate gas exchange, which can be confused with other epithelial lineages in low-quality or damaged lung tissue.

Genes:
- AGER, PDPN, CAV1, CLDN18, RTKN2, EMP2, S100A4, HOPX, SPOCK2, Ager, COL4A3, EPB41L4B
- GPR116, PECAM1, KRT8, KRT18, KRT19, C1orf54, FXYD3, HEG1

### Alveolar Type II (AT2) Cell

Description: The dominant secretory epithelial cell of the distal lung parenchyma, responsible for producing pulmonary surfactant and acting as a progenitor for AT1 cells, often misannotated as pancreatic acinar cells due to shared high-volume secretory machinery.

Genes:
- SFTPC, SFTPB, SFTPA1, SFTPA2, SFTPD, ABCA3, LAMP3, PGC, NAPSA, ETV5, CEBPA, SLC34A2
- LPCAT1, CYP2F1, SCGB3A2, MUC1, CXCL15, SCD, FASN, LCN2, PGC, B2M, WFDC2, SLPI
- CLDN18

### Bronchiolar Secretory Cell (Club Cell)

Description: Non-ciliated secretory cells of the bronchioles that protect the bronchiolar epithelium by secreting uteroglobin and other immunomodulatory proteins, sharing a highly active secretory profile with acinar cells.

Genes:
- SCGB1A1, SCGB3A2, BPIFA1, BPIFB1, CYP2F2, ALDH1A1, GSTP1, GPX2, TFF3, MUC5B, WFDC2, SLPI
- LCN2, S100A6, S100A14, KRT8, KRT18, KRT19, CD24, ELF3

### Serous Cell of the Submucosal Gland

Description: Specialized secretory cells located in the submucosal glands of the upper airways that secrete antimicrobial proteins and fluid, sharing extreme morphological and transcriptional similarity with pancreatic and salivary acinar cells.

Genes:
- LTF, LYZ, PRR4, PIP, AZGP1, DMBT1, BPIFA1, BPIFB1, ODAM, CST3, SLPI, WFDC2
- MUC5B, SOX9, CXCL14, PRB1, PRB2, PRB4, SEC11C, PIGR

## alveolar adventitial fibroblast

### Adventitial fibroblast

Description: Located in the adventitial space around large bronchovascular bundles, these fibroblasts express high levels of PI16, DCN, and extracellular matrix proteins to maintain structural integrity.

Genes:
- PI16, DCN, FBLN1, FBLN2, COL1A1, COL1A2, COL3A1, PDGFRB, TCF21, MFAP5, SVEP1, CD34
- CLEC3B, APOD, C3, C7, IGFBP5, IGF1, HAS2, LUM, SLIT2, SERPINF1, FBN1, GSN
- A2M

### Airway smooth muscle cell

Description: Contractile cells surrounding the bronchial airways that express high levels of mature smooth muscle markers like MYH11 and CNN1, occasionally misannotated as myofibroblasts or adventitial fibroblasts.

Genes:
- ACTA2, MYH11, TAGLN, CNN1, MYLK, LMOD1, DES, PLN, SLMAP, CASQ2, ACTG2, TPM1
- TPM2, CALD1, PCP4, CSRP2, FILIP1L, CHRM3, ADRA1A, KCNMB1

### Alveolar fibroblast

Description: Residing in the alveolar septa, these fibroblasts express NPNT and WNT2, playing a critical role in alveolar homeostasis, extracellular matrix deposition, and alveolar epithelial cell support.

Genes:
- NPNT, CES1, LIMCH1, GPLD1, SPINT2, FGF18, WNT2, WNT5A, COL18A1, TNC, PDGFRA, ELN
- ACTA2, SCN7A, ITGA8, ASPN, FBLN5, LOX, LOXL1, LOXL2, CTHRC1, POSTN

### Pericyte

Description: Contractile mural cells wrapping around capillaries and small microvessels, characterized by high expression of RGS5, CSPG4, and PDGFRB, which are often confused with adventitial fibroblasts.

Genes:
- PDGFRB, CSPG4, MCAM, RGS5, KCNJ8, ABCC9, VTN, NDUFA4L2, HEYL, COX4I2, HIGD1B, GJA4
- MUSTN1, ACTA2, MYH11, TAGLN, CNN1, CALD1, TPM2, NOTCH3

## alveolar macrophage

### Alveolar Macrophage (Resident)

Description: Resident alveolar macrophages located in the epithelial lining of the alveoli, characterized by high expression of lipid metabolism genes, surfactant processing machinery, and scavenger receptors.

Genes:
- FABP4, MARCO, MCEMP1, SIGLEC1, PPARG, CD68, MSR1, APOC1, APOE, CHIT1, LPL, C1QA
- C1QB, C1QC, ALDH1A1, PCOLCE2, CES1, SFTPA1, SFTPA2, SFTPB, SFTPC, ABCA3, LAMP3, CTSD
- CTSB

### Classical Dendritic Cell (cDC2)

Description: Antigen-presenting myeloid dendritic cells that can be confused with interstitial macrophages but are distinguished by high MHC class II expression, CD1C, CLEC10A, and lack of macrophage lineage markers.

Genes:
- CLEC10A, FCER1A, CD1C, HLA-DQA1, HLA-DQB1, HLA-DRB1, CD1E, ENPP3, PLD4, GSN, COBLL1, PKIB
- RUNX3, IRF4, CD2, CX3CR1, CD86, CD40, CCR7

### Interstitial Macrophage

Description: Macrophages residing within the lung parenchymal interstitium, characterized by high expression of CD163, MRC1 (CD206), and LYVE1, and involved in tissue remodeling and immune regulation.

Genes:
- CD163, MRC1, MS4A4A, LYVE1, FOLR2, F13A1, SELENOP, APOE, C1QA, C1QB, C1QC, CD14
- FCGR3A, CSF1R, TGFBI, MMP9, MMP19, CCL18, CCL2, IL10, HMOX1

### Monocyte-derived Macrophage

Description: Recently recruited inflammatory macrophages derived from circulating blood monocytes, expressing high levels of S100 alarmins, classical monocyte markers, and pro-inflammatory cytokines.

Genes:
- FCN1, S100A8, S100A9, S100A12, VCAN, CD14, LYZ, CD300E, FCGR3A, LST1, AIF1, IL1B
- TNF, CXCL8, CCL3, CCL4, CLEC12A, CD16, SELL, CCR2

## alveolar type 1 fibroblast cell

### Adventitial Fibroblasts

Description: Mesenchymal cells located in the adventitial space surrounding large bronchovascular bundles, characterized by high expression of PI16 and DPP4.

Genes:
- PI16, DPP4, COL14A1, CLEC3B, F3, SEMA3C, CD34, MFAP5, IGFBP5, IGF1, HAS1, ALDH1A3
- APOE, C3, C7, CLU, FBLN5, GLI1, PDGFRA, LAMA2

### Alveolar Fibroblasts

Description: Resident interstitial mesenchymal cells located in the alveolar septa that produce extracellular matrix components like collagen and elastin to maintain lung structural integrity.

Genes:
- COL1A1, COL1A2, COL3A1, DCN, LUM, PDGFRB, PDGFRA, FBLN1, FBLN2, TCF21, NPNT, ACTA2
- TAGLN, MYLK, ELN, MFAP4, FBN1, G0S2, APOD, C1R

### Alveolar Type 1 (AT1) Epithelial Cells

Description: Extremely thin, flat epithelial cells covering the majority of the alveolar surface area, specialized for gas exchange and characterized by AGER and HOPX expression.

Genes:
- AGER, CLDN18, HOPX, PDPN, CAV1, EMP2, SFTPA1, SFTPB, RTKN2, S100A6, GPR116, AQP5
- EPB41L4A, SPOCK2, FXYD3, C3, LMO7, COL14A1, PECAM1, CDH1

### Alveolar Type 2 (AT2) Epithelial Cells

Description: Cuboidal epithelial cells that act as progenitors for AT1 cells and produce pulmonary surfactant to reduce surface tension in the alveoli.

Genes:
- SFTPC, SFTPB, SFTPA1, SFTPA2, ABCA3, LAMP3, PGC, NAPSA, ETV5, CXCL15, SLC34A2, CEACAM6
- MUC1, LPCAT1, MBIP, CYP2F1, SCGB1A1, NKX2-1, I聯合, Sod1

## b cell

### Memory B cell

Description: Antigen-experienced B cells residing in lung mucosal surfaces or lymphoid aggregates, showing class-switch recombination and high expression of CD27.

Genes:
- MS4A1, CD19, CD79A, CD79B, CD27, IGHG1, IGHG3, IGHA1, IGHA2, AIM2, COBLL1, CLECL1
- TNFRSF13B, TXNIP, CD83, EBI3, FCRL5, AHNAK, GPR183, CD86

### Naive B cell

Description: Circulating or tissue-resident naive B cells characterized by the co-expression of IGHD and IGHM alongside classical B-cell lineage markers.

Genes:
- MS4A1, CD19, CD79A, CD79B, IGHD, IGHM, TCL1A, IL4R, FCER2, CD22, CD24, CXCR5
- CCR7, SELL, BACH2, BTG1, YBX3, CXCR4, TXNIP, ZFP36, GIMAP5, LINC00926

### Plasma cell

Description: Terminally differentiated antibody-secreting cells characterized by massive expansion of the endoplasmic reticulum and high expression of JCHAIN and immunoglobulins.

Genes:
- MZB1, PRDM1, XBP1, IRF4, CD38, SDC1, SLAMF7, FKBP11, SEC61A1, SSR4, DERL3, HERPUD1
- TXNDC5, IGHG1, IGHG2, IGHG3, IGHG4, IGHA1, IGHA2, IGKC, IGLC2, IGLC3, JCHAIN, CREB3L2

### Plasmacytoid Dendritic Cell

Description: A major immune cell type frequently confused with B/plasma cells due to shared expression of JCHAIN and certain immunoglobulin-like receptors, specialized in rapid type I interferon production.

Genes:
- LILRA4, CLEC4C, PTGDS, GZMB, TCF4, IRF7, IRF8, IL3RA, NRP1, SCT, PLD4, PACSIN1
- MAP1A, APP, SOX4, SPIB, RUNX2, CCDC50, TXNIP, JCHAIN

## bronchial goblet cell

### Alveolar Type II (AT2) cells

Description: Parenchymal epithelial cells that synthesize and secrete pulmonary surfactant, act as progenitors for AT1 cells, and are frequently confused with bronchial secretory cells in low-quality or damaged lung samples.

Genes:
- SFTPC, SFTPA1, SFTPA2, SFTPB, SFTPD, ABCA3, LAMP3, PGC, NAPSA, ETV5, CEACAM6, SLC34A2
- LPCAT1, MBIP, NKX2-1, HCFC1, CXCL15, S100A2, FASN, SCD, CYP2B6

### Club cells (SCGB1A1+)

Description: Non-ciliated bronchiolar secretory cells that produce uteroglobin (SCGB1A1) and host defense proteins, serving as progenitor cells for the bronchiolar epithelium.

Genes:
- SCGB1A1, SCGB3A2, CYP2F1, BPIFA1, ALDH1A1, SERPINB1, GSTP1, CCSP, SFTPA1, SFTPB, LYZ, HP
- CPB2, CXCL17, SLPI, WFDC2, KRT18, MGP, RARRES2, C3, FGB, FGG

### Goblet cells (MUC5AC+)

Description: Classic secretory cells of the bronchial epithelium characterized by high expression of gel-forming mucins like MUC5AC and regulated by the master transcription factor SPDEF.

Genes:
- MUC5AC, SPDEF, TFF1, TFF3, AGR2, GPX2, BPIFB1, S100A14, CEACAM5, KRT7, KRT8, KRT19
- LCN2, SLPI, WFDC2, MUC5B, PLA2G10, GALNT2, SPINK5, TFF2, S100A6, S100A11, CAPN1, CD24
- ELF3

### Mucous cells of submucosal glands

Description: Specialized secretory cells residing within the submucosal glands of the upper airways, primarily producing MUC5B and antimicrobial proteins like lactoferrin.

Genes:
- MUC5B, BPIFB2, LTF, LALBA, ODAM, PRR4, PIP, AZGP1, ZG16B, TFF3, AGR3, MUC7
- SOX2, KRT5, KRT14, ACTA2, CNN1, TP63, S100A2, DST

## bronchus fibroblast of lung

### Adventitial fibroblast

Description: Located in the adventitial space around large bronchovascular bundles, these fibroblasts express high levels of PI16, extracellular matrix proteins, and universal fibroblast markers.

Genes:
- PI16, DCN, FBLN1, MFAP5, COL1A1, COL1A2, COL3A1, LUM, PDGFRB, PDGFRA, CD34, SVEP1
- C3, C7, IGFBP5, APOD, FBN1, CLEC3B, SLIT2, HAS2, BMP4, GSN, MFAP4, COL6A1
- COL6A2

### Airway smooth muscle cell

Description: Contractile cells surrounding the bronchial airways that share many structural gene expression profiles with myofibroblasts but are distinguished by mature smooth muscle markers like MYH11 and CNN1.

Genes:
- ACTA2, TAGLN, MYH11, CNN1, MYLK, LMOD1, DES, PLN, SLMAP, CASQ2, CHRM3, ADRA1A
- TPM1, TPM2, CALD1, PCP4, FILIP1L, SORBS2, FRZB, C7, ACTG2

### Alveolar fibroblast

Description: Also known as lipofibrolasts or interstitial fibroblasts, these cells reside in the alveolar septa, expressing NPNT and PDGFRA, and are critical for alveolar structural maintenance.

Genes:
- NPNT, CES1, LIMCH1, GPLD1, SPINT2, PDGFRA, COL14A1, FBLN2, ELN, TNC, ACTA2, WIF1
- FGFR4, SCN7A, ASPN, POSTN, COL1A1, COL1A2, FGF10, LAMA2, ITGA8, DKK2, HHIP

### Pericyte

Description: A common neighboring mural cell type wrapping capillaries and small vessels, often confused with fibroblasts but distinguished by high expression of RGS5, CSPG4, and KCNJ8.

Genes:
- PDGFRB, CSPG4, MCAM, RGS5, KCNJ8, ABCC9, VTN, NDUFA4L2, HEYL, COX4I2, HIGD1B, GJA4
- ACTA2, TAGLN, MYLK, MYH11, CALD1, TPM2, NOTCH3, EBF1, MUSTN1

## brush cell of tracheobronchial tree

### Basal cell

Description: The resident progenitor cells of the airway epithelium, located along the basement membrane, capable of self-renewal and differentiation into ciliated and secretory lineages.

Genes:
- TP63, KRT5, KRT14, KRT15, DST, BCAM, COL17A1, NGFR, S100A2, DLX5, SOX2, ITGA6
- ITGB4, KRT17, ANXA1, ALDH3A1, BNC1, LAMB3, LAMC2, CD44

### Ionocyte

Description: A rare, specialized airway epithelial cell type characterized by high expression of CFTR and FOXI1, playing a critical role in ion transport and fluid regulation.

Genes:
- FOXI1, CFTR, ASGR1, ATP6V1B1, ATP6V0A4, BSND, CLCNKB, S100A14, KRT19, TMEM229B, IGFBP2, FXYD1
- LCN2, SCNN1G, SCNN1B, CA2, CA12, SLC26A9, SPINK5, GSTA1

### Neuroendocrine cell (PNEC)

Description: Rare, specialized airway epithelial cells that integrate environmental signals and secrete neuropeptides and biogenic amines to regulate vascular and bronchial tone.

Genes:
- CHGA, CHGB, ASCL1, CALCA, GRP, SCG2, SYP, INSM1, NCAM1, UCHL1, PCSK1, BEX1
- CPLX2, SCGN, FEV, NEUROD1, NKX2-1, VMAT1, SLC18A1, SST, PYY, GHRL

### Tuft cell (Brush cell)

Description: Chemosensory epithelial cells of the airway (also known as brush cells) that express taste transduction machinery and act as key initiators of type 2 immune responses.

Genes:
- POU2F3, TRPM5, IL25, ALOX5AP, HPGDS, GNG13, PLCG2, AVIL, LRMP, CHAT, SOX9, BMX
- SH2D6, PTGS1, ASCL2, KRT18, KRT8, GFI1B, SPIB, DCLK1, IL17RB, LTC4S, ADCYAP1, PTPRC
- FYN

## capillary endothelial cell

### Aerocyte (aCap)

Description: Specialized alveolar capillary endothelial cells, also known as aCap, that are primarily responsible for gas exchange and regulation of vasomotor tone in the lung parenchyma.

Genes:
- EDNRB, TBX2, GALNT15, APLNR, HPGD, PRX, S100A4, FCN3, COL15A1, EMP2, CA4, CD36
- VIPR1, KDR, FLT1, PECAM1, ICAM1, S100A10, GJA4, GJA5, CLDN5, RAMP2, RAMP3, EMCN
- CD34

### Alveolar Type I (ATI) Epithelial Cell

Description: Flat, thin epithelial cells covering the majority of the alveolar surface area, which share a basement membrane with capillary endothelial cells and are frequently co-isolated or transcriptionally confused with them.

Genes:
- AGER, PDPN, CAV1, CLDN18, RTKN2, EMP2, SFTPA1, SFTPB, HOPX, COL4A3, COL4A4, P2RX4
- EPB41L4A, SPOCK2, Ager, CEMP1, AQP5, FXYD3, GPR116, PHGRP

### General Capillary (gCap)

Description: General capillary endothelial cells, also known as gCap, involved in capillary maintenance, leukocyte trafficking, and serving as progenitor cells for aerocytes during injury repair.

Genes:
- GPIHBP1, PLVAP, SEMA3C, BTNL9, CD36, FBLN5, VWF, PECAM1, CD34, KDR, FLT1, RAMP1
- GNG11, CLDN5, CXCL12, IL7R, ACKR1, SELE, SELPLG, ICAM2, ENG, CDH5, SOX17, LTC4S

### Lymphatic Endothelial Cell

Description: Endothelial cells lining the lymphatic vessels of the lung parenchyma, responsible for fluid drainage and immune cell trafficking, often confused with blood capillaries.

Genes:
- PROX1, PDPN, LYVE1, FLT4, CCL21, TFPI, MMRN1, FABP4, BBOX1, C1QTNF1, CALCRL, NRP2
- ANXA2, S100A13, PTPRB, ESAM, TIE1, TEK, SOX18, ELENE, FGL2, CLDN11

## cd1c-positive myeloid dendritic cell

### Alveolar Macrophages

Description: Tissue-resident macrophages of the alveolar space expressing high levels of lipid metabolism genes and scavenger receptors, which can be confused with dendritic cells due to high autofluorescence and MHC-II expression.

Genes:
- FABP4, MARCO, MCEMP1, SIGLEC1, APOC1, APOE, PPARG, CD68, MSR1, MRC1, CCL18, C1QA
- C1QB, C1QC, FTL, FTH1, LPL, CD11c, ITGAX, CES1

### Classical Monocytes

Description: Circulating myeloid cells that extravasate into lung parenchyma during homeostasis and inflammation, expressing high levels of CD14 and S100 alarmins, often confused with cDC2s due to shared myeloid lineage markers.

Genes:
- CD14, FCN1, S100A9, S100A8, S100A12, VCAN, LYZ, MNDA, FPR1, FPR2, CSF3R, CD300E
- GRN, IL1B, CXCL8, NAMPT, IFITM3, CD44, SELL, CD68

### Monocyte-derived dendritic cells (moDCs)

Description: Inflammatory antigen-presenting cells that differentiate from monocytes in tissue, sharing markers with both classical dendritic cells (CD1c) and monocytes/macrophages (CD14, CD163).

Genes:
- CD14, FCGR3A, S100A12, FCN1, VCAN, LYZ, CD163, MAFB, MNDA, CSF1R, ITGAM, CD68
- IL1RN, CD1C, FCER1A, CLEC10A, S100A8, S100A9, FPR1, FPR2, TREM1, CD300E

### cDC2 (classical dendritic cells type 2)

Description: Classical type 2 dendritic cells characterized by high expression of CD1c and MHC class II molecules, specialized in presenting extracellular antigens to CD4+ T cells.

Genes:
- CD1C, FCER1A, CLEC10A, HLA-DQA1, HLA-DQB1, HLA-DRB1, CD1E, ENHO, PKIB, CXCL8, IL1B, S100A9
- S100A8, FCCN, CD2, CD1A, GSN, COBLL1, RUNX3, PLD4, CCR7, CD80, CD86, LAMP3

## cd4-positive, alpha-beta t cell

### Alveolar Macrophage

Description: The resident myeloid population of the alveolar space, which can be a source of ambient RNA contamination or doublet formation with CD4+ T cells in lung single-cell suspensions.

Genes:
- FABP4, MARCO, MCEMP1, APOC1, APOE, CD68, CD163, SIGLEC1, MSR1, C1QA, C1QB, C1QC
- FTL, FTH1, PPARG, LPL, SFTPA1, SFTPB, SFTPD, PMP22

### CD4+ naive/central memory T cell

Description: Recirculating CD4+ T cells that patrol secondary lymphoid organs and lung-associated lymph nodes, characterized by high expression of CCR7, SELL (L-selectin), and TCF7.

Genes:
- CCR7, SELL, TCF7, LEF1, IL7R, CD27, NOSIP, MAL, CD4, TXNIP, BTG1, EEF1A1
- RPS3, RPL13, RPL21, RPS18, LTB, LDHB, MYC, KLF2

### CD4+ tissue-resident memory T cell (Trm)

Description: Non-recirculating CD4+ T cells residing in the lung parenchyma that provide rapid local memory responses, marked by CD69 and ITGA1 (VLA-1) expression.

Genes:
- CD69, ITGA1, CXCR6, IL7R, DUSP6, CRTAM, IFNG, TNF, FOS, JUN, JUNB, FOSB
- EGR1, EGR2, NR4A1, NR4A2, NR4A3, CD4, GADD45B, ZFP36

### Natural Killer T (NKT) cell

Description: A specialized lineage of T cells sharing properties of both T cells and Natural Killer cells, often confused with CD4+ T cells due to shared CD3 expression and overlapping cytotoxic profiles.

Genes:
- KLRB1, NKG7, GNLY, PRF1, GZMB, GZMA, CD3D, CD3E, CD3G, ZBTB16, SLC4A10, NCR3
- FCGR3A, FGFBP2, CX3CR1, HOPX, S1PR5, KLRD1, KLRG1, CD8A

### T regulatory cell (Treg)

Description: Immunosuppressive CD4+ T cells characterized by high expression of FOXP3 and IL2RA (CD25), crucial for maintaining immunological tolerance in the lung parenchyma.

Genes:
- FOXP3, IL2RA, IKZF2, CTLA4, TNFRSF18, TNFRSF4, TIGIT, BATF, PRDM1, IL10, LRRC32, LAIR2
- CD4, IL7R, CD27, ICOS, FGL2, ANXA1, S100A4, S100A6, CAPG, GATA3

## cd8-positive, alpha-beta t cell

### CD8+ Effector Memory T cells (Tem)

Description: Circulating effector memory CD8+ T cells that patrol the lung vasculature and parenchyma, exhibiting high cytolytic potential and rapid migration capabilities.

Genes:
- GZMH, GZMB, PRF1, GNLY, FGFBP2, CX3CR1, TBX21, T-BET, ZEB2, S1PR1, S1PR5, KLRG1
- KLRD1, KLRF1, NKG7, CCL5, CCL4, CCL3, ADGRG1, G3BP1, HCST, S100A4, S100A6, ANXA1
- CD44

### CD8+ Resident Memory T cells (Trm)

Description: Tissue-resident memory CD8+ T cells localized within the lung parenchyma and mucosal epithelium, characterized by expression of retention integrins and rapid effector cytokine production.

Genes:
- ITGAE, CD103, ITGA1, CD49a, CXCR6, CRTAM, ZNF683, HOBIT, RUNX3, CD69, DUSP6, IFNG
- TNF, CCL20, XCL1, XCL2, GZMB, GZMA, PRF1, FASLG, TNFSF14, RGS1, RGS16, KLRG1
- CAPG

### Gamma-Delta (γδ) T cells

Description: Unconventional T cells expressing the gamma-delta TCR chains that reside at mucosal barriers in the lung, bridging innate and adaptive immune responses.

Genes:
- TRDC, TRGC1, TRGC2, TARPP, CD160, KLRB1, CD161, KLRC1, KLRC2, KLRC3, ZBTB16, PLZF
- RORC, IL23R, CCR6, SOX13, GZMA, GZMK, NKG7, SST, CD27, LEF1, TCF7, BLK
- LAT

### Mucosal-Associated Invariant T (MAIT) cells

Description: Innate-like alpha-beta T cells restricted by the non-polymorphic MHC class I-related molecule MR1, highly abundant in human lung tissue and responsive to bacterial metabolites.

Genes:
- SLC4A10, TRAV1-2, KLRB1, CD161, ZBTB16, PLZF, RORC, IL18RAP, IL18R1, IL23R, CCR6, CXCR6
- GZMK, GZMA, FASLG, TNF, IFNG, CSF2, DUSP1, JUNB, FOS, CD2, CD160, IKZF2
- HEBP2

### Natural Killer (NK) cells

Description: Innate lymphoid cells that share morphological and cytotoxic profiles with CD8+ T cells but lack the T-cell receptor complex, frequently misclassified in high-throughput single-cell pipelines.

Genes:
- NCAM1, CD56, NCR1, NKP46, NCR3, FCGR3A, CD16, KLRF1, KLRD1, KLRG1, KLRC1, KLRC2
- NKG7, GNLY, GZMB, GZMA, PRF1, EOMES, TBX21, HOPX, SPON2, FGFBP2, S1PR5, CST7
- CLIC3

## classical monocyte

### Alveolar Macrophage (AM)

Description: Tissue-resident macrophages residing in the alveolar space, critical for surfactant catabolism and lipid metabolism, characterized by high expression of FABP4, MARCO, and PPARG.

Genes:
- FABP4, MARCO, MCEMP1, SIGLEC1, PPARG, CD68, MSR1, CHIT1, CHI3L1, FTL, FTH1, SFTPA1
- SFTPB, SFTPC, SFTPD, PCOLCE2, LPL, CES1, C1QA, C1QB

### Classical Monocyte (CD14+ Monocyte)

Description: Circulating inflammatory myeloid cells that extravasate into the lung parenchyma during injury or inflammation, characterized by high expression of CD14, S100 alarmin proteins, and classical chemotactic receptors.

Genes:
- CD14, FCN1, S100A8, S100A9, S100A12, VCAN, LYZ, CD300E, CD300LF, FPR1, FPR2, CSF3R
- CLEC4D, CLEC4E, NAMPT, IFITM3, GRN, IL1B, CXCL8, NFKBIA, IER3, EREG, AQP9, SELL
- CD44

### Interstitial Macrophage (IM)

Description: Resident myeloid cells located within the lung parenchymal interstitium, often confused with classical monocytes but distinguished by high expression of antigen presentation machinery, complement components, and scavenger receptors like CD163 and MRC1.

Genes:
- APOE, C1QA, C1QB, C1QC, CD163, MRC1, MS4A4A, LYVE1, FOLR2, SEPP1, F13A1, CD209
- MERTK, CSF1R, MAF, C5AR1, CD68, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1

### Non-classical Monocyte (CD16+ Monocyte)

Description: Patrolling monocytes that maintain vascular integrity and are distinguished by high expression of FCGR3A (CD16), CX3CR1, and genes involved in cytoskeletal remodeling.

Genes:
- FCGR3A, CX3CR1, LST1, AIF1, MS4A7, HES4, RHOC, IFITM1, IFITM2, TCF7L2, C1QA, C1QB
- C1QC, LILRB1, LILRB2, SIGLEC10, CD300A, SMIM25, SPON2, COTL1

## club cell

### Alveolar Type II (AT2) cell

Description: Alveolar epithelial cells responsible for producing pulmonary surfactant and serving as progenitors for Alveolar Type I cells during injury repair.

Genes:
- SFTPC, SFTPB, SFTPA1, SFTPA2, SFTPD, ABCA3, LAMP3, PGC, NAPSA, ETV5, CEACAM6, CYP2B6
- LPCAT1, SLC34A2, MBTPS2, SCD, FASN, CXCL15, S100A2, NKX2-1

### Ciliated cell

Description: Terminally differentiated airway epithelial cells covered in motile cilia that facilitate mucociliary clearance.

Genes:
- CAPS, FOXJ1, TP73, SNTN, CCDC39, CCDC40, DNAH1, DNAH5, DNAH9, DNAI1, DNAI2, DNALI1
- TEKT1, TEKT2, TEKT4, RSPH1, RSPH4A, RSPH9, SPAG6, PIFO, C21orf59, FAM183B, TUBB4B, TUBA1A

### Club cell (canonical)

Description: Canonical secretory cells of the bronchiolar epithelium that produce secretoglobulins, surfactant proteins, and xenobiotic-metabolizing enzymes to protect the airway.

Genes:
- SCGB1A1, SCGB3A2, CYP2F1, BPIFA1, BPIFB1, ALDH1A1, SFTPA1, SFTPA2, SFTPB, WFDC2, SLPI, MUC5B
- GPX2, GSTP1, MGST1, HP, TFF3, CEACAM6, PIGR, LCN2, CXCL17, SERPINB1, KRT8, KRT18
- KRT19

### Goblet cell

Description: Airway secretory cells specialized for mucus production and secretion, characterized by high expression of mucins and anterior gradient 2.

Genes:
- MUC5AC, MUC5B, SPDEF, AGR2, TFF1, TFF3, FCGBP, B3GNT6, GALNT2, CLCA1, SST, REG4
- CEACAM5, S100A14, GPX2, ELF3, MUC16, PI3, SLPI, WFDC2

## conventional dendritic cell

### Alveolar Macrophages

Description: Tissue-resident macrophages of the alveolar space that can be confused with cDCs due to shared expression of MHC-II and antigen-presentation machinery, but distinguished by high FABP4 and MARCO.

Genes:
- FABP4, MARCO, MCEMP1, SIGLEC1, PPARG, MSR1, CD68, APOC1, APOE, CHIT1, LPL, C1QA
- C1QB, C1QC, CCL18, GPNMB, FTL, FTH1, CTSD, CTSB, LGALS3

### Monocyte-derived Dendritic Cells (moDCs)

Description: Inflammatory antigen-presenting cells that differentiate from circulating monocytes in the lung parenchyma, sharing markers with both cDC2s and classical monocytes.

Genes:
- CD14, FCGR3A, S100A8, S100A9, FCN1, VCAN, LYZ, CD300E, ITGAM, CSF1R, MAFB, MNDA
- S100A12, FPR1, FPR2, CD68, HLA-DRA, HLA-DRB1, CD1C, FCER1A

### Plasmacytoid Dendritic Cells (pDCs)

Description: A distinct dendritic cell lineage specialized in rapid, massive production of type I interferons in response to viral pathogens, characterized by LILRA4 and CLEC4C.

Genes:
- LILRA4, CLEC4C, TCF4, IL3RA, NRP1, IRF7, PACSIN1, PLD4, GZMB, SERPINF1, ITM2C, MAP1A
- SCT, SPIB, APP, RUNX2, CCDC50, BCL11A, JCHAIN

### cDC1 (Type 1 Conventional Dendritic Cell)

Description: A specialized dendritic cell lineage highly efficient at cross-presenting intracellular antigens to CD8+ T cells, characterized by the expression of CLEC9A and XCR1.

Genes:
- CLEC9A, XCR1, WDFY4, CADM1, BATF3, IRF8, FLT3, BTLA, CLNK, CPVL, DPP4, S100A4
- ANPEP, C1orf54, APP, GPR141, HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, HLA-DRA, HLA-DRB1

### cDC2 (Type 2 Conventional Dendritic Cell)

Description: The major population of conventional dendritic cells in the lung, specialized in presenting extracellular antigens to CD4+ T cells and promoting helper T cell differentiation.

Genes:
- CD1C, FCER1A, CLEC10A, SIRPA, IRF4, COBLL1, ZEB2, CX3CR1, CD1E, CD2, PLD4, ENPP1
- HLA-DPA1, HLA-DPB1, HLA-DQA1, HLA-DQB1, HLA-DRA, HLA-DRB1, CD1A, S100A9, S100A8

## dendritic cell

### Alveolar Macrophage

Description: Tissue-resident macrophages of the lung alveoli that clear surfactant and pathogens, frequently confused with dendritic cells due to shared myeloid and antigen-presentation machinery.

Genes:
- FABP4, MARCO, MCEMP1, SIGLEC1, PPARG, MSR1, CD68, APOC1, APOE, C1QA, C1QB, C1QC
- CCL18, CHIT1, LPL, CES1, FTL, FTH1, GPNMB, SPP1

### Monocyte-derived Dendritic Cell (moDC)

Description: Inflammatory myeloid cells that differentiate from monocytes in the lung parenchyma during inflammation, sharing phenotypic markers with both classical dendritic cells and macrophages.

Genes:
- CD14, FCGR3A, S100A12, FCN1, VCAN, CD300E, MAFB, MNDA, CSF1R, ITGAX, CD163, MRC1
- LYZ, CD83, CCR2, CX3CR1, LILRB2, LILRB1, GRN, TYROBP

### cDC1 (Classical Dendritic Cell Type 1)

Description: A specialized dendritic cell lineage highly efficient at cross-presenting intracellular antigens to CD8+ T cells, characterized by the expression of CLEC9A and XCR1.

Genes:
- CLEC9A, XCR1, WDFY4, CADM1, BATF3, FLT3, IRF8, IDO1, CLNK, C12orf75, CPVL, S100A4
- DPP4, ANPEP, BTLA, CXCR3, LY75, GPR141, PTPRK, TACSTD2

### cDC2 (Classical Dendritic Cell Type 2)

Description: The major population of conventional dendritic cells in the lung, specialized in presenting MHC-II-restricted antigens to CD4+ T cells and promoting helper T cell responses.

Genes:
- CD1C, FCER1A, CLEC10A, SIRPA, COBLL1, PKIB, CX3CR1, CD2, CD1E, IL1B, NLRP3, S100A9
- S100A8, FCCN, CSF2RA, RUNX3, ZEB2, KLF4, CD86, HLA-DQB1

### pDC (Plasmacytoid Dendritic Cell)

Description: A specialized dendritic cell subset resembling plasma cells that produces massive amounts of type I interferons in response to viral nucleic acids.

Genes:
- LILRA4, CLEC4C, TCF4, IL3RA, NRP1, PLD4, GZMB, SCT, PACSIN1, MAP1A, IRF7, SPIB
- BCL11A, RUNX2, APP, PTGDS, SOX4, SERPINF1, ITM2C, DERL3

## elicited macrophage

### Alveolar Macrophage

Description: Resident macrophages of the alveolar space characterized by high expression of lipid metabolism genes, scavenger receptors, and surfactant-binding proteins.

Genes:
- FABP4, MARCO, MCEMP1, APOC1, APOE, PPARG, SIGLEC1, CD68, MSR1, CHIT1, LPL, C1QA
- C1QB, C1QC, CCL18, SFTPA1, SFTPB, SFTPC, PCOLCE2, CES1, ALDH1A1, TFRC, CD14, FCGR3A

### Classical Monocyte

Description: Circulating myeloid cells that patrol the vasculature and rapidly extravasate into the lung parenchyma during injury or inflammation.

Genes:
- FCN1, VCAN, S100A8, S100A9, S100A12, CD14, SELL, GRN, CD300C, CSF3R, CCR2, CLEC12A
- FPR1, FPR2, NAMPT, MNDA, LYZ, CD4, FCER1G, TYROBP

### Conventional Dendritic Cell Type 2

Description: Professional antigen-presenting cells in the lung parenchyma that can be confused with interstitial macrophages but are distinguished by CD1C, CLEC10A, and high MHC class II expression.

Genes:
- CLEC10A, FCER1A, CD1C, HLA-DQA1, HLA-DQB1, HLA-DRB1, CD1E, ENPP3, PKIB, GSN, COBLL1, CXCL16
- CST3, ANXA1, CD2, IL1R2, PLD4, RUNX3, IRF4, ZBTB46

### Interstitial Macrophage

Description: Tissue-resident macrophages located within the lung parenchyma interstitium, displaying high expression of CD163, LYVE1, and antigen-presentation machinery.

Genes:
- CX3CR1, CD163, MRC1, LYVE1, FOLR2, MS4A4A, SELENOP, C5AR1, F13A1, CD14, FCGR1A, CSF1R
- MAF, MMP9, MMP19, IL10, TGFB1, HLA-DRA, HLA-DPB1, HLA-DPA1

### Monocyte-derived Macrophage

Description: Recently recruited inflammatory macrophages derived from circulating classical monocytes, characterized by high expression of S100 alarmins and pro-inflammatory cytokines.

Genes:
- S100A8, S100A9, S100A12, FCN1, VCAN, CD14, FCGR3A, LST1, AIF1, LYZ, CD300E, CLEC12A
- IL1B, TNF, CXCL8, CCL3, CCL4, IER3, NFKBIA, JUNB

## endothelial cell of lymphatic vessel

### Alveolar capillary endothelial cells (aCap)

Description: Specialized capillary endothelial cells in the alveolar septum optimized for gas exchange and leukocyte trafficking.

Genes:
- PRX, EDN1, TBX2, S100A13, SGK1, FCN3, CA4, APLN, GPIHBP1, PECAM1, CD36, KDR
- VWF, CLDN5, EMCN, PTPRB, ICAM1, SELE, VCAM1, IL6

### Arterial endothelial cells

Description: Endothelial cells lining the high-pressure arterial system of the lung, characterized by shear-stress responsive gene expression.

Genes:
- DKK2, BMX, EFNB2, SOX17, GJA4, GJA5, HEY1, SEMA3G, FBLN5, VWF, PECAM1, CD36
- KDR, CLDN5, EMCN, PTPRB, EDN1, TBX2, SGK1, FCN3

### General capillary endothelial cells (gCap)

Description: General capillary endothelial cells involved in vasomotor tone regulation and nutrient transport in the alveolar wall.

Genes:
- GPIHBP1, PLVAP, CA4, APLNR, PRX, S100A13, PECAM1, CD36, KDR, VWF, CLDN5, EMCN
- PTPRB, COL15A1, FBLN5, VWA1, EDN1, TBX2, SGK1, FCN3

### Lymphatic endothelial cells (LECs)

Description: Specialized endothelial cells lining lymphatic vessels that regulate fluid homeostasis and immune cell trafficking in the lung parenchyma.

Genes:
- PROX1, LYVE1, PDPN, FLT4, CCL21, TFPI, MMRN1, FABP4, IL7R, CALCRL, SST, FCN3
- CLDN5, EMCN, PTPRB, GPR182, BBOX1, CD36, PECAM1, KDR, VWF, ENG

### Venous endothelial cells

Description: Endothelial cells lining the pulmonary veins, expressing adhesion molecules involved in leukocyte trafficking and inflammatory responses.

Genes:
- ACKR1, VWF, SELE, VCAM1, ICAM1, IL6, PECAM1, CD36, KDR, CLDN5, EMCN, PTPRB
- EDN1, TBX2, SGK1, FCN3, FBLN5, VWA1, COL15A1

## epithelial cell of lower respiratory tract

### Alveolar Type 1 (AT1) Epithelial Cell

Description: Flat, squamous cells covering the majority of the alveolar surface area, specialized for gas exchange and barrier function.

Genes:
- AGER, PDPN, CAV1, CLDN18, RTKN2, EMP2, HOPX, SFTPA1, SFTPA2, AJP, COL4A3, EPB41L4B
- GPR116, SPOCK2, PECAM1, KRT8, KRT18, FXYD3, C3, EDN1, ABCA3, LAMP3, SFTPB, SFTPC

### Alveolar Type 2 (AT2) Epithelial Cell

Description: Cuboidal cells that produce pulmonary surfactant to reduce surface tension and act as progenitors for AT1 cells during injury repair.

Genes:
- SFTPC, SFTPB, SFTPA1, SFTPA2, ABCA3, LAMP3, PGC, NAPSA, ETV5, CEACAM6, LPCAT1, SLC34A2
- CYB5A, SCGB1A1, MUC1, CXCL15, NKX2-1, BPIFB1, FASN, SCD

### Basal Epithelial Cell

Description: Resident progenitor cells of the airway epithelium located along the basement membrane that regenerate ciliated and secretory lineages.

Genes:
- TP63, KRT5, KRT14, KRT15, S100A2, DST, COL17A1, ITGA6, NGFR, SOX2, BCAM, LAMB3
- LAMC2, KRT17, ALDH1A3, EGFR, AREG, CXCL14, GABRP, CD44

### Ciliated Epithelial Cell

Description: Terminally differentiated airway epithelial cells equipped with coordinated beating cilia responsible for mucociliary clearance.

Genes:
- FOXJ1, CAPS, TPPP3, SNTN, CCDC153, CCDC39, CCDC40, DNAH5, DNAH11, DNAI1, DNAI2, RSPH4A
- RSPH9, PIFO, TEKT2, C21orf59, TUBB4B, TUBA1A, AK7, ERICH3, FAM183B, OMP

### Club Cell

Description: Non-ciliated secretory cells of the bronchioles that secrete protective proteins and metabolize xenobiotics.

Genes:
- SCGB1A1, SCGB3A2, BPIFB1, CYP2F1, ALDH1A1, GSTP1, GPX2, MUC5B, SERPINB1, SLPI, WFDC2, LCN2
- TFF3, HP, SFTPA1, SFTPB, KRT8, KRT18, KRT19, CD24

## fibroblast

### Adventitial fibroblast

Description: Located in the adventitial space around large vessels and airways, these fibroblasts express high levels of extracellular matrix proteins, PI16, and universal progenitor markers.

Genes:
- PI16, DCN, FBLN1, FBLN2, COL1A1, COL1A2, COL3A1, PDGFRB, PDGFRA, TCF21, MFAP5, SVEP1
- CD34, APOD, C3, C7, IGFBP5, IGFBP6, LUM, MGP, HAS1, HAS2, FBN1, FBN2
- SERPINF1, CLEC14A, GSN, AOC3, BMP4, WNT2

### Airway smooth muscle cell

Description: Contractile mesenchymal cells surrounding the bronchial tree that are often confused with myofibroblasts or activated fibroblasts due to high expression of ACTA2 and other smooth muscle contractile machinery.

Genes:
- ACTA2, TAGLN, MYH11, CNN1, MYLK, CALD1, DES, PLN, SLMAP, CHRM3, ADR_B2, LMOD1
- PCP4, TPM1, TPM2, ACTG2, CASQ2, C11orf96, SORBS2, FRMD6

### Alveolar fibroblast

Description: Also known as lipofibroblasts or interstitial fibroblasts, these cells reside in the alveolar septa, express NPNT and TCF21, and are critical for alveolar structural maintenance and surfactant synthesis support.

Genes:
- NPNT, CES1, LIMCH1, INMT, GPLD1, FGF18, WNT2B, WNT5A, PDGFRA, TCF21, COL14A1, COL6A3
- ELN, FBLN5, SCARA5, ASPN, SPON1, LAMA2, ITGA8, ACTA2, MYLK, TAGLN, TNS1, VIPR2
- ADRA2A, PTGIR

### Mesothelial cell

Description: Cells forming the protective monolayer of the visceral pleura that share mesenchymal and extracellular matrix genes with fibroblasts but are distinguished by epithelial keratins, MSLN, and WT1.

Genes:
- MSLN, WT1, CALB2, KRT8, KRT18, KRT19, UPK3B, BNC1, HAS3, ALDH1A2, LRRN4, HP
- SLPI, PRG4, CLDN15, VTN, ICAM1, SOD3, CFB, C3

### Pericyte

Description: A common neighboring cell type wrapping around capillaries that is frequently confused with fibroblasts due to shared mesenchymal markers like PDGFRB, but distinguished by RGS5 and CSPG4 expression.

Genes:
- PDGFRB, CSPG4, MCAM, RGS5, KCNJ8, ABCC9, VTN, NDUFA4L2, HEG1, COX4I2, HIGD1B, GJA4
- GJA5, NOTCH3, ANGPT1, MUSTN1, CALD1, MYO1B, ACTA2, TAGLN, MYH11, CNN1

## hematopoietic stem cell

### Alveolar Macrophage

Description: Resident myeloid cells of the alveolar space that express high levels of lipid metabolism genes and scavenger receptors, often misidentified as stem cells due to high autofluorescence and broad myeloid marker expression.

Genes:
- FABP4, MARCO, MCEMP1, APOC1, APOE, PPARG, SIGLEC1, CD68, MSR1, CHIT1, C1QA, C1QB
- C1QC, CCL18, IL1RN, LPL, CD14, FCGR3A, TREM2, GPNMB, SPP1, CTSD, LGALS3, SFTPA1
- SFTPB

### Classical Monocyte

Description: Circulating inflammatory myeloid cells that rapidly traffic into the lung parenchyma and express high levels of S100 alarmins and canonical monocyte markers.

Genes:
- FCN1, S100A8, S100A9, S100A12, VCAN, CD14, LYZ, CD300E, MAFB, CSF3R, FPR1, FCGR1A
- CLEC12A, CD44, SELL, GRN, NAMPT, S100A4, S100A6, IFITM3, CD52

### Interstitial Macrophage

Description: Myeloid cells localized within the lung parenchymal interstitium, characterized by high expression of antigen presentation machinery, CD163, and LYVE1.

Genes:
- SELENOP, LYVE1, FOLR2, CD163, MRC1, MS4A4A, C1QA, C1QB, C1QC, APOE, F13A1, CD14
- CSF1R, HLA-DRA, HLA-DPB1, HLA-DPA1, CD74, CTSB, CTSD, AIF1, TYROBP

### Megakaryocyte

Description: Platelet-producing cells residing in the pulmonary vasculature that share progenitor markers with hematopoietic stem cells, leading to frequent annotation confusion.

Genes:
- PPBP, PF4, GNG11, TUBB1, ITGA2B, GP9, GP1BA, MPL, CLU, SPARC, MYL9, ACTB
- SDPR, TREML1, F13A1, HIST1H2AC, PLEK, PCTAIRE2BP, CD244, PRKAR2B

## ionocyte

### Basal Cell

Description: The resident stem cell population of the pseudostratified airway epithelium, capable of self-renewal and differentiation into ciliated, secretory, and ionocyte lineages.

Genes:
- TP63, KRT5, KRT14, KRT15, S100A2, DST, COL17A1, BCAM, NGFR, ITGA6, SOX2, LAMB3
- LAMC2, CXCL14, BNC1, DSP, KRT17, AREG, EGFR, FGF2

### Neuroendocrine Cell (PNEC)

Description: A specialized airway epithelial cell with neuroendocrine properties that senses hypoxia and mechanical stretch, secreting neuropeptides like calcitonin gene-related peptide (CGRP).

Genes:
- ASCL1, CHGA, CHGB, SYP, CALCA, GRP, SCG2, SCG3, PCSK1, INSM1, TTR, BEX1
- CPLX2, UCHL1, SST, GHRL, NKX2-1, VAMP2, SNAP25, SRRM4, FEV, NEUROD1

### Pulmonary Ionocyte

Description: A rare, specialized airway epithelial cell type that expresses the highest levels of CFTR and FOXI1, playing a critical role in regulating pH and fluid composition of the airway surface liquid.

Genes:
- FOXI1, CFTR, ASGR1, BSND, CLCNKB, ATP6V1G3, ATP6V0D2, SGK1, SCNN1G, SCNN1B, KRT19, SPINK6
- TMEM229B, ALOX5AP, C1orf116, LINC00982, HCN4, GPR153, FXYD1, S100A14, S100A16, GPX2, IL1RAPL2, STAP1
- SLC12A2

### Tuft Cell (Brush Cell)

Description: A chemosensory epithelial cell type in the airway that expresses taste transduction machinery and initiates type 2 immune responses via IL25 secretion.

Genes:
- POU2F3, TRPM5, IL25, CHAT, ALOX5, ALOX5AP, PTGS1, PTGDS, BMX, AVIL, GNAT3, PLCG2
- SH2D6, LRMP, SPIB, SOX9, KRT18, GNG13, TAS2R38, HPGDS, IL17RB, GFI1B

## lung macrophage

### Alveolar Macrophages

Description: Resident macrophages of the alveolar space characterized by high expression of lipid metabolism genes, scavenger receptors, and surfactant-processing machinery.

Genes:
- FABP4, MARCO, MCEMP1, APOC1, APOE, PPARG, SIGLEC1, CD68, MSR1, CHIT1, CCL18, C1QA
- C1QB, C1QC, LPL, SFTPA1, SFTPB, SFTPC, PCOLCE2, CES1, ALDH1A1, TFRC, CD14, FCGR3A
- CTSD

### Classical Monocytes

Description: Circulating or marginated myeloid cells in the lung vasculature that act as precursors to macrophages during inflammation, expressing high levels of S100 alarmins.

Genes:
- FCN1, S100A8, S100A9, S100A12, VCAN, CD14, LYZ, CD300E, FPR1, FPR2, CSF3R, SELL
- CLEC12A, IL1B, CXCL8, NAMPT, IFITM3, GRN, CD44, FCER1G

### Conventional Dendritic Cells (cDC2)

Description: Antigen-presenting cells in the lung parenchyma that can be confused with interstitial macrophages but are distinguished by high MHC class II expression and specific dendritic cell markers.

Genes:
- FCER1A, CLEC10A, CD1C, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1, HLA-DRB1, HLA-DRA, CD1E, ENHO, PKIB
- GSN, COBLL1, CX3CR1, CD2, IL12B, CCR7, IRF4, ZBTB46

### Interstitial Macrophages

Description: Macrophages residing within the lung parenchymal interstitium, often displaying immunomodulatory, tissue-remodeling, or pro-fibrotic profiles.

Genes:
- SPP1, FCN1, CD163, MRC1, LYVE1, FOLR2, SELENOP, APOE, C1QA, C1QB, C1QC, MS4A4A
- CD14, HLA-DRA, HLA-DRB1, IL10, TGFB1, MMP9, MMP12, CCL18, CCL2, CSF1R, MAFB, ZEB2

## lung pericyte

### Adventitial Fibroblast

Description: Stromal fibroblasts located in the adventitial space of large bronchovascular bundles, expressing high levels of extracellular matrix proteins, PDGFRA, and PI16.

Genes:
- PDGFRA, COL1A1, COL1A2, COL3A1, DCN, LUM, FBLN1, FBLN2, MFAP5, FBN1, PI16, DPP4
- CD34, SULF1, APOD, CLEC14A, C3, CFD, IGFBP6, COL6A1, COL6A2, COL6A3

### Alveolar Fibroblast (Myofibroblast/Lipofibroblast-like)

Description: Specialized interstitial fibroblasts of the alveolar septum that support alveolar structure and surfactant production, often sharing overlapping markers with pericytes and myofibroblasts.

Genes:
- PDGFRA, TCF21, NPNT, FGF10, LIMCH1, ASPN, WIF1, APOE, LPL, ADIRF, COL14A1, ACTA2
- POSTN, SPARC, CTGF, CYR61, ELN, FBLN5, SCARA5, G0S2

### Lung Pericyte (Mural Cell)

Description: Perivascular mural cells wrapping around capillaries and post-capillary venules, characterized by high expression of RGS5, PDGFRB, and KCNJ8, crucial for blood-brain and blood-gas barrier regulation.

Genes:
- PDGFRB, CSPG4, MCAM, RGS5, ABCC9, KCNJ8, VTN, NDUFA4L2, HIGD1B, COX4I2, HEYL, GJA4
- MUSTN1, ACTA2, TAGLN, MYLK, CALD1, TPM2, NOTCH3, EBF1, PDLIM3, RBP7, STEAP4, FRZB

### Vascular Smooth Muscle Cell (vSMC)

Description: Contractile mural cells surrounding larger pulmonary arteries and veins, distinguished from pericytes by high expression of mature contractile proteins like MYH11 and CNN1.

Genes:
- ACTA2, TAGLN, MYH11, CNN1, MYLK, LMOD1, TPM2, CALD1, ACTG2, PLN, SLMAP, NOTCH3
- PDGFRB, FLNA, CSRP1, AOC3, DES, SYNPO2, CHRM3, VIPR2

## mast cell

### Alveolar Macrophages

Description: Resident myeloid cells of the alveolar space that can be confused with mast cells due to high autofluorescence, myeloid marker expression, and phagocytic uptake of surfactant proteins.

Genes:
- FABP4, MARCO, MCEMP1, APOC1, APOE, CHIT1, MSR1, CD68, SIGLEC1, PPARG, LPL, C1QA
- C1QB, C1QC, CD14, FCGR3A, CSF1R, CTSD, LGALS3, SFTPA1, SFTPB, SFTPC, SFTPA2, PCOLCE2
- CES1

### Basophils

Description: Circulating granulocytes closely related to mast cells that share the high-affinity IgE receptor and key histamine synthesis machinery, leading to frequent annotation confusion.

Genes:
- CLC, MS4A2, FCER1A, GATA2, HPGDS, ALOX5, IL4, IL13, CD123, IL3RA, LRMP, SMPD3
- RUNX3, LTC4S, CPA3, TPSB2, TPSAB1, HDC, PLD4, CD9

### Connective Tissue Mast Cells

Description: A mature mast cell subtype localized to the lung pleura and perivascular connective tissue, characterized by high expression of both tryptase and chymase.

Genes:
- TPSAB1, TPSB2, CPA3, HPGDS, MS4A2, FCER1A, CMA1, CTSG, GATA2, KIT, HDC, ALOX5AP
- LTC4S, PTGS2, CD63, CD9, VAMP8, RGS13, SLC18A2, SCG2, ANXA1, TPSD1, MLPH, P2RY14

### Mucosal Mast Cells

Description: A mast cell subtype predominantly found in the bronchial mucosa and alveolar septa of the lung, expressing high levels of tryptase but lacking chymase.

Genes:
- TPSAB1, TPSB2, CPA3, HPGDS, MS4A2, FCER1A, GATA2, KIT, HDC, LTC4S, IL4, IL13
- CCL1, CCL2, CXCL8, AREG, CSF2, TNFSF14, IL5, RGS1

## mesothelial cell

### Alveolar macrophages

Description: Resident myeloid cells of the alveolar space that can be confused with mesothelial cells in low-quality or doublet-prone single-cell suspensions due to high autofluorescence and ambient RNA contamination.

Genes:
- FABP4, MARCO, MCEMP1, APOC1, APOE, CD68, SIGLEC1, MSR1, PPARG, MRC1, CCL18, C1QA
- C1QB, C1QC, CTSD, FTL, FTH1, LIPA, LGALS3, CD14, A2M, SFTPA1, SFTPB

### Fibroblasts

Description: Lung parenchymal interstitial fibroblasts that share mesenchymal gene expression programs with mesothelial cells, such as extracellular matrix deposition genes, leading to frequent misannotation.

Genes:
- COL1A1, COL1A2, COL3A1, DCN, LUM, FBLN1, FBLN2, PDGFRB, PDGFRA, TCF21, ACTA2, TAGLN
- MYLK, POSTN, MFAP4, ELN, FBN1, SPARC, BGN, COL6A1, COL6A2, COL6A3

### Lymphatic endothelial cells

Description: Endothelial cells lining the lymphatic vessels of the lung that share key marker genes with mesothelial cells, such as PDPN (podoplanin), causing potential lineage confusion.

Genes:
- PROX1, PDPN, LYVE1, FLT4, CCL21, TFPI, MMRN1, ANGPT2, CALCRL, RAMP2, RAMP3, VWF
- PECAM1, CDH5, EMCN, ELOF1, PTPRB, KDR, CLDN5, GJA4

### Mesothelial cells

Description: True pleural mesothelial cells forming the monolayer lining the visceral pleura of the lung parenchyma, characterized by expression of mesothelial-specific markers and cell-adhesion molecules.

Genes:
- MSLN, WT1, CALB2, KRT8, KRT18, KRT19, UPK3B, HAS1, BNC1, ALDH1A2, HP, SLPI
- CFB, PRG4, LRRN4, VTN, SOD3, IGFBP2, S100A4, CLDN15, MUC16, GPM6B, HEG1, PDPN

## mucus secreting cell

### Alveolar Type II cells

Description: Cuboidal epithelial cells of the alveolar parenchyma that synthesize and secrete pulmonary surfactant to reduce surface tension, and act as progenitors for Type I cells.

Genes:
- SFTPC, SFTPA1, SFTPA2, SFTPB, SFTPD, ABCA3, LAMP3, PGC, NAPSA, ETV5, CEACAM6, LPCAT1
- SLC34A2, CYB5A, SCD, FASN, NKX2-1, MBTPS2, S100A2, CLDN18

### Ciliated cells

Description: Terminally differentiated airway epithelial cells covered in motile cilia that drive mucociliary clearance, frequently co-isolated or confused with secretory cells in parenchymal preps.

Genes:
- CAPS, FOXJ1, TPPP3, SNTN, CCDC39, CCDC40, DNAH5, DNAH11, DNAI1, DNAI2, TEKT2, TEKT4
- RSPH4A, RSPH9, PIFO, FAM183B, C11orf96, TUBB4B, TUBA1A, EFHC1, AK7, C20orf85

### Club cells

Description: Non-ciliated bronchiolar secretory cells that produce surfactant-associated proteins and uteroglobins, playing a key role in xenobiotic metabolism and airway host defense.

Genes:
- SCGB1A1, SCGB3A2, SFTPB, SFTPA1, SFTPA2, CYP2F1, ALDH1A1, GSTP1, BPIFA1, CCSP, HP, PON1
- SERPINB1, CPB2, CXCL17, SLPI, WFDC2, LCN2, MGP, RARRES2, S100A6, S100A10

### Goblet cells

Description: Classic airway secretory cells specialized in the production and secretion of high-molecular-weight mucins like MUC5AC and MUC5B to form the protective mucus barrier.

Genes:
- MUC5AC, MUC5B, SPDEF, TFF3, AGR2, FCGBP, BPIFB1, GPX2, TFF1, S100A14, CEACAM5, GALNT12
- CREB3L1, SCGB3A1, KRT7, KRT8, KRT18, CLDN4, LCN2, SLPI, WFDC2, PIGR, MUC1, MUC16
- ELF3

## multiciliated columnar cell of tracheobronchial tree

### Club cell

Description: Non-ciliated secretory cells of the bronchioles that protect the bronchiolar epithelium by secreting uteroglobin, surfactant-associated proteins, and xenobiotic-metabolizing enzymes.

Genes:
- SCGB1A1, SCGB3A2, SFTPB, SFTPA1, SFTPA2, CYP2F1, BPIFA1, BPIFB1, ALDH3A1, GSTP1, GPX2, HP
- TFF3, MUC5B, PIGR, LCN2, SLPI, WFDC2, SERPINB1, LYZ

### Deuterosomal cell (precursor)

Description: An active transitional progenitor state undergoing massive centriole amplification via deuterosomes prior to mature ciliated cell differentiation.

Genes:
- CCNO, CDC20B, DEUP1, PLK4, SASS6, CEP152, CENPF, MYB, FOXN4, MCIDAS, E2F5, TP73
- STIL, NEK2, C21orf58, HAUS6, CEP120, LRRC45, SFI1, CETN3

### Goblet cell

Description: Mucus-secreting cells of the bronchial epithelium that play a critical role in mucociliary clearance and innate mucosal defense.

Genes:
- MUC5AC, MUC5B, SPDEF, FOXA3, AGR2, TFF1, TFF3, FCGBP, CLCA1, BPIFB1, GPX2, S100A9
- S100A8, GALNT2, B3GNT6, TXNDC5, CREB3L1, ERN2, PDIA4, SDF2L1

### Multiciliated cell (mature)

Description: Terminally differentiated airway epithelial cells characterized by hundreds of apical motile cilia driven by a highly coordinated axonemal dynein machinery.

Genes:
- CAPS, TPPP3, SNTN, FOXJ1, CCDC39, CCDC40, DNAH5, DNAH11, DNAI1, DNAI2, TEKT2, TEKT4
- RSPH1, RSPH4A, RSPH9, SPAG6, SPAG16, SPEF2, GAS8, C21orf59, PIFO, ODF2, CCDC113, CCDC151
- EFHC1, CIB2, CETN2, C2orf16, FAM183B, LRRC36

## multiciliated epithelial cell

### Club cell

Description: Non-ciliated secretory cells of the bronchioles that protect the bronchiolar epithelium by secreting uteroglobin and other immunomodulatory proteins.

Genes:
- SCGB1A1, SCGB3A2, SFTPB, SFTPA1, SFTPA2, CYP2F1, BPIFA1, BPIFB1, ALDH1A1, ALDH3A1, GSTP1, GPX2
- TFF3, MUC5B, KRT8, KRT18, SLPI, WFDC2, LCN2, PIGR, CXCL17, HP, CEACAM6, LYZ

### Deuterosomal cell

Description: A transient progenitor state undergoing massive centriole amplification via deuterosomes prior to committing to a fully multiciliated epithelial cell fate.

Genes:
- CCNO, CDC20B, MCIDAS, DEUP1, FOXN4, SASS6, CEP152, PLK4, CENPF, STIL, MYB, TP73
- HES6, NEK2, E2F7, E2F8, CDK1, CCNB1, CDC25C, TOP2A, NUSAP1, BIRC5, MKI67, CENPE
- ASPM

### Goblet cell

Description: Mucus-secreting airway epithelial cells that play a critical role in barrier defense and are frequently confused with ciliated cells in inflamed or remodeling lung tissues.

Genes:
- MUC5AC, MUC5B, SPDEF, FOXA3, AGR2, TFF1, TFF3, FCGBP, CLCA1, BPIFB1, GPX2, S100A9
- S100A8, KRT8, KRT19, GALNT2, ST3GAL1, FUT4, TXNDC5, CREB3L1, ERN2, PDIA3

### Mature multiciliated cell

Description: Terminally differentiated airway epithelial cells covered with hundreds of motile cilia responsible for mucociliary clearance in the respiratory tract.

Genes:
- CAPS, FOXJ1, TPPP3, SNTN, RSPH1, RSPH4A, RSPH9, DNAH1, DNAH5, DNAH9, DNAI1, DNAI2
- DNALI1, TEKT1, TEKT2, TEKT4, CCDC39, CCDC40, SPEF2, PIFO, C21orf59, ODF2, CIB2, FAM183B
- AK7, C1orf198, EFHC1, GAS8

## myofibroblast cell

### Adventitial Fibroblast

Description: Fibroblasts located in the adventitial connective tissue sheath surrounding bronchovascular bundles, characterized by high extracellular matrix deposition and immunomodulatory gene expression.

Genes:
- PDGFRA, DCN, LUM, FBLN2, FBN1, MFAP5, COL6A1, COL6A2, COL6A3, SCD, APOD, C3
- C7, CFD, PI16, CD34, DPP4, HAS1, HAS2, IL6, CXCL12, IGFBP5, IGFBP6, ALDH1A3

### Airway Smooth Muscle Cell

Description: Contractile spindle-shaped cells wrapping around the bronchi and bronchioles that regulate airway caliber and bronchoconstriction.

Genes:
- ACTA2, MYH11, CNN1, TAGLN, LMOD1, MYLK, TPM1, TPM2, ACTG2, DES, PLN, SLMAP
- KCNMB1, CHRM3, ADRA1A, VIPR1, PTGIR, CASQ2, PCP4, CALD1, CSRP2, FILIP1L

### Alveolar Myofibroblast

Description: Contractile interstitial cells located in the alveolar septal tips that express elastin and are essential for alveolar formation and structural maintenance.

Genes:
- ACTA2, PDGFRB, NPNT, WIF1, FGF18, ASPN, POSTN, COL3A1, COL1A1, COL1A2, TAGLN, MYLK
- TPM2, PLN, HHIP, PTCH1, GLI1, LGR6, SCN7A, MUSTN1, TNS1, ITGA8, ELN, GJA4

### Pericyte

Description: Perivascular cells closely associated with the abluminal surface of capillaries and microvessels, regulating endothelial cell stability and microvascular blood flow.

Genes:
- PDGFRB, RGS5, CSPG4, KCNJ8, ABCC9, MCAM, VTN, NDUFA4L2, COX4I2, HIGD1B, HEG1, NOTCH3
- GJA4, ANGPT1, COL18A1, PECAM1, CD248, IFITM1, MUSTN1, CALD1

### Vascular Smooth Muscle Cell

Description: Contractile cells surrounding arterial and venous blood vessels in the lung parenchyma that regulate vascular tone and blood pressure.

Genes:
- ACTA2, MYH11, TAGLN, CNN1, MCAM, NOTCH3, HEG1, RGS5, CSPG4, PDGFRB, VTN, KCNJ8
- ABCC9, ACTG2, MYLK, CALD1, TPM2, MUSTN1, GJA4, GJA5, HRG, BGN

## nasal mucosa goblet cell

### Alveolar Type II (AT2) cell

Description: The progenitor cells of the alveolar epithelium that synthesize, secrete, and recycle pulmonary surfactant to prevent alveolar collapse.

Genes:
- SFTPC, SFTPA1, SFTPA2, SFTPB, SFTPD, ABCA3, LAMP3, PGC, NAPSA, ETV5, CEACAM6, LPCAT1
- SLC34A2, CYB5A, SCD, FASN, NKX2-1, MBTPS2, CXCL15, MUC1

### Ciliated cell

Description: Epithelial cells possessing motile cilia that beat metachronally to propel mucus and trapped foreign particles out of the respiratory tract.

Genes:
- FOXJ1, CAPS, TPPP3, SNTN, CCDC39, CCDC40, DNAH5, DNAH11, DNAI1, DNAI2, TEKT2, TEKT4
- RSPH4A, RSPH9, PIFO, TUBB4B, TUBA1A, AK7, C20orf85, EFHC1, FAM183B, C1orf193

### Club cell

Description: Non-ciliated secretory cells of the bronchioles that secrete uteroglobin (SCGB1A1) and surfactant proteins to protect the bronchiolar epithelium.

Genes:
- SCGB1A1, SCGB3A2, SFTPB, SFTPA1, SFTPA2, CYP2F2, ALDH1A1, CCSP, BPIFA1, REG3G, LYZ, SLPI
- WFDC2, GSTA3, HP, CXCL17, MGST1, PEBP1, S100A6, KRT18

### Goblet cell (airway secretory)

Description: Classic airway secretory cells that produce mucins like MUC5AC and MUC5B to trap inhaled particulates in the respiratory tract.

Genes:
- MUC5AC, MUC5B, SPDEF, GPX2, TFF3, AGR2, BPIFB1, S100A9, S100A8, CEACAM5, TFF1, SLPI
- LCN2, WFDC2, MUC16, SCGB3A1, ALDH3A1, CYP2F1, GSTA1, KRT5, KRT15, KRT19, CD24, ELF3
- SPINK5

## natural killer cell

### CD56bright CD16- NK cells

Description: A cytokine-producing, immunomodulatory NK cell subset characterized by high expression of NCAM1 (CD56) and homing receptors, but low cytotoxicity.

Genes:
- NCAM1, SELL, KLRC1, KLRD1, XCL1, XCL2, CSF2, IFNG, TNF, IL2RB, LTB, GZMK
- CAPG, CD44, MYC, TCF7, RUNX2, SOX4, CCR7, CXCR3, TNFRSF18, TNFRSF4, CD2, CD27
- KLRC2

### CD56dim CD16+ NK cells

Description: The dominant, highly cytotoxic NK cell subset in the lung parenchyma, characterized by high expression of CD16 (FCGR3A), perforin, and granzymes.

Genes:
- FCGR3A, FGFBP2, CX3CR1, PRF1, GZMB, GZMA, GNLY, KLRG1, KLRF1, SPON2, S1PR5, ZEB2
- TBX21, ADGRG1, CLIC3, CST7, NKG7, CD244, CD160, LAIR2, PRF1, HCST, S100A4, S100A6

### CD8+ Cytotoxic T cells

Description: An adaptive cytotoxic lymphoid lineage commonly confused with NK cells due to shared expression of cytolytic machinery like perforin, granzymes, and NKG7.

Genes:
- CD8A, CD8B, CD3D, CD3E, CD3G, TRAC, TRBC1, TRBC2, LCK, CD247, GZMK, GZMH
- NKG7, PRF1, CST7, EOMES, RUNX3, CD2, CD5, CD7, LAT, ITAL, ZAP70

### Gamma-delta T cells

Description: An unconventional T cell subset bridging innate and adaptive immunity, frequently sharing NK-like receptors and cytotoxic profiles in the lung.

Genes:
- TRDC, TRGC1, TRGC2, CD3D, CD3E, CD247, KLRB1, KLRC1, KLRC2, KLRD1, ZBTB16, RORC
- IL23R, SST, SOX13, NKG7, GZMA, GZMK, CD160, CD2, LAT, LCK

### Tissue-resident NK cells

Description: A lung-resident NK cell population that expresses tissue-retention markers like CD69 and integrin alpha-1 (ITGA1) and exhibits a transcriptionally primed state.

Genes:
- ITGA1, CD69, CXCR6, ZNF683, EOMES, XCL1, XCL2, GZMK, KLRC1, DUSP1, FOS, JUN
- IER3, ATF3, GADD45B, TNFAIP3, RGS1, CD101, CXCR3, IFNG

## non-classical monocyte

### Alveolar Macrophage (AM)

Description: Highly specialized resident macrophages of the alveolar space characterized by high expression of FABP4, MARCO, and PPARG, critical for surfactant clearance and lipid metabolism.

Genes:
- FABP4, MARCO, MCEMP1, SIGLEC1, PPARG, MSR1, CD68, CD11C, ITGAX, CHIT1, CHI3L1, ALDH1A1
- C1QA, C1QB, C1QC, APOE, LPL, SFTPA1, SFTPB, SFTPC, SFTPD, PCOLCE2, CES1, TFRC

### Classical monocyte (CD14+)

Description: Inflammatory monocytes that express high levels of CD14 and CCR2, which rapidly recruit to sites of pulmonary infection or injury and can differentiate into macrophages.

Genes:
- CD14, S100A12, S100A8, S100A9, FCN1, VCAN, CD300E, CLEC12A, MAFB, CCR2, MNDA, GRN
- LYZ, CTSS, IER3, FPR1, FPR2, NAMPT, IL1B, CXCL8, CD44, CD68, CSF3R, S100A4
- S100A6

### Interstitial Macrophage (IM)

Description: Resident macrophages located within the lung parenchymal interstitium, expressing CD163 and MRC1, which function in tissue remodeling, antigen presentation, and immune regulation.

Genes:
- APOE, C1QA, C1QB, C1QC, CD163, MRC1, MS4A4A, SELENOP, FOLR2, LYVE1, CD209, MERTK
- C5AR1, CD14, FCGR1A, CSF1R, HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, CTSB, CTSD, LGALS3, GPNMB

### Non-classical monocyte (CD16+)

Description: Patrolling intravascular monocytes characterized by high expression of FCGR3A (CD16) and CX3CR1, involved in vascular surveillance and endothelial homeostasis.

Genes:
- FCGR3A, CX3CR1, LST1, AIF1, MS4A7, IFITM3, LYN, HCK, SIGLEC10, C1QA, C1QB, C1QC
- CSF1R, RHOC, TCF7L2, SPN, PECAM1, ITGAL, CD300A, CD300C, TNFSF10, C3AR1, FGR, VNN2
- S100A8, S100A9

## plasma cell

### B cell

Description: A neighboring lineage of mature, non-secreting lymphocytes that express membrane-bound immunoglobulins and B-cell receptor complex components, often confused with plasma cells due to shared lineage markers.

Genes:
- MS4A1, CD19, CD79A, CD79B, BANK1, LINC00926, CD22, CD37, FCRL1, FCRL2, FCRL5, PAX5
- MEF2C, BLNK, HVCN1, RALGPS2, AFF3, COL19A1, CXCR5, CCR7, CD24, CD40, TNFRSF13C, P2RX5
- BACH2, SPIB, BLK, LY9, CD83, HLA-DRA

### IgA plasma cell

Description: A mucosal-associated antibody-secreting cell subtype predominantly producing IgA to protect the mucosal surfaces of the lung parenchyma.

Genes:
- IGHA1, IGHA2, IGHG1, IGHG2, IGHG3, IGHG4, IGKC, IGLC1, IGLC2, IGLC3, JCHAIN, MZB1
- DERL3, PRDM1, IRF4, XBP1, SLAMF7, TNFRSF17, SDC1, FKBP11, SSR4, SEC61A1, SEC11C, HERPUD1
- CREB3L2, TXNDC5, PDIK1L, SPCS1, SEL1L, MANF

### IgG plasma cell

Description: A systemic-associated antibody-secreting cell subtype predominantly producing IgG, often enriched in chronically inflamed or fibrotic lung parenchyma.

Genes:
- IGHG1, IGHG2, IGHG3, IGHG4, IGKC, IGLC1, IGLC2, IGLC3, JCHAIN, MZB1, DERL3, PRDM1
- IRF4, XBP1, SLAMF7, TNFRSF17, SDC1, FKBP11, SSR4, SEC61A1, SEC11C, HERPUD1, TXNDC5, PDIK1L
- SPCS1, SEL1L, MANF, CD38, CD27, TNFRSF13B

### Plasmablast

Description: A proliferating, short-lived precursor to terminally differentiated plasma cells, characterized by the co-expression of cell-cycle genes and immunoglobulin transcripts.

Genes:
- MKI67, TYMS, PCNA, TOP2A, CDK1, UBE2C, BIRC5, CCNB1, HMGB2, STMN1, JCHAIN, MZB1
- PRDM1, IRF4, XBP1, SLAMF7, TNFRSF17, SDC1, FKBP11, SSR4, IGKC, IGLC1, IGHG1, IGHA1
- DUT, RRM2, TK1, CENPF, NUSAP1, DIAPH3

### Plasmacytoid dendritic cell

Description: A specialized dendritic cell subset producing high levels of type I interferons, which shares morphological features and several secretory pathway markers (like MZB1 and DERL3) with plasma cells.

Genes:
- LILRA4, CLEC4C, PTGDS, GZMB, TCF4, IRF7, IRF8, IL3RA, NRP1, PLD4, SCT, PACSIN1
- MAP1A, APP, SOX4, SPIB, RUNX2, BCL11A, TXNIP, CD4, ITM2C, SERPINF1, C1orf186, LAMP5
- SCAMP5, PTPRS, CCDC50, GPM6B, DERL3, MZB1

## plasmacytoid dendritic cell

### Conventional dendritic cell type 1 (cDC1)

Description: A neighboring dendritic cell lineage specialized in cross-presentation of intracellular antigens to CD8+ T cells, sharing some lineage markers like IRF8 with pDCs but distinguished by CLEC9A and XCR1.

Genes:
- CLEC9A, XCR1, CADM1, WDFY4, BATF3, IRF8, FLT3, CPVL, ID2, CLNK, C1orf54, APP
- SNX22, GPR141, S100A3, S100A10, LY75, BTLA, DPP4, ANPEP

### Plasma cell

Description: Terminally differentiated B lineage cells that are frequently confused with pDCs due to shared high expression of secretory pathway machinery, immunoglobulin genes, and markers like MZB1 and JCHAIN.

Genes:
- MZB1, JCHAIN, IGKC, IGHG1, IGHG2, IGHG3, IGHG4, IGHA1, IGHA2, SDC1, PRDM1, XBP1
- FKBP11, HERPUD1, SEC11C, TXNDC5, DERL3, SSR4, CREB3L2, SDF2L1, SEL1L, MANF, CD27, CD38

### Plasmacytoid dendritic cell (pDC)

Description: Bonafide plasmacytoid dendritic cells specialized in rapid, massive secretion of type I interferons in response to viral pathogens, characterized by high expression of LILRA4, CLEC4C, and TCF4.

Genes:
- LILRA4, CLEC4C, PTGDS, GZMB, TCF4, IRF7, IRF8, IL3RA, NRP1, PLD4, SCT, PACSIN1
- MAP1A, APP, DERL3, HERPUD1, MZB1, SEC61A1, TXNDC5, JCHAIN, IGKC, IGHG1, IGHG3, SPIB
- RUNX2, BCL11A, CCDC50, LAMP5, PTPRS, SERPINF1

## pulmonary alveolar epithelial cell

### Alveolar Epithelial Type I (AT1)

Description: Large, extremely thin squamous cells covering over 95% of the alveolar surface area, specialized for gas exchange and barrier function.

Genes:
- AGER, HOPX, CAV1, PDPN, CLDN18, EMP2, RTKN2, SFTPA1, SFTPA2, AJP, SPOCK2, COL4A3
- EPB41L4A, GPR116, C3, FXYD3, P2RY6, ABCC1, S100A13, KRT8, KRT18, PECAM1, ICAM1, AQP5

### Alveolar Epithelial Type II (AT2)

Description: Cuboidal epithelial cells that act as progenitors for AT1 cells and synthesize, secrete, and recycle pulmonary surfactant to reduce surface tension.

Genes:
- SFTPC, SFTPB, SFTPA1, SFTPA2, SFTPD, ABCA3, LAMP3, PGC, NAPSA, ETV5, CEBPB, LPCAT1
- SLC34A2, CYB5A, MUC1, SCGB3A2, CXCL15, FASN, SCD, LCN2, SLPI, BPIFB1, WFDC2, NKX2-1

### Bronchiolar Club Cells

Description: Secretory cells of the bronchioles that can be confused with AT2 cells due to shared secretory machinery and overlapping expression of surfactant proteins.

Genes:
- SCGB1A1, SCGB3A2, CYP2F1, BPIFB1, SLPI, ALDH1A1, WFDC2, KRT19, GPX2, GSTP1, MUC5B, SFTPA1
- SFTPD, TFF3, LYZ, CXCL17, HP, CP, SERPINB1, S100A14, S100A6, KRT8

### Transitional/Pre-TB Epithelial Cells (PATS/ADI/DATS)

Description: A transient, injury-induced state of alveolar differentiation (also known as PATS, ADI, or DATS) expressing both epithelial and mesenchymal markers, often confused with AT1 or AT2 cells during fibrosis.

Genes:
- KRT8, CLDN4, S100A9, S100A8, LGALS3, FN1, VIM, CD44, SOX4, TP63, KRT17, KRT19
- MMP7, CTNNB1, TGFB1, COL1A1, COL1A2, LCN2, TIMP1, SPP1

## pulmonary alveolar type 1 cell

### Alveolar capillary endothelial cell

Description: Capillary endothelial cells (specifically aerocytes and general capillaries) that form an extremely tight physical barrier and basement membrane interface with AT1 cells.

Genes:
- PECAM1, CD34, KDR, VWF, CLDN5, EMCN, PLVAP, GPIHBP1, CA4, PRX, SGIP1, FCN3
- CLEC14A, SOX17, ELENE, APLN, VIPR1, ADGRL4, RAMP2, RAMP3

### Pulmonary alveolar type 1 cell

Description: True alveolar type 1 (AT1) epithelial cells, which are extremely thin, flat cells covering over 95% of the alveolar surface area to facilitate gas exchange.

Genes:
- AGER, PDPN, CAV1, CLDN18, RTKN2, EMP2, SFTPA1, SFTPA2, HOPX, Ager, AQP5, COL4A3
- COL4A4, PECAM1, GPR116, SPOCK2, EPB41L4A, FXYD3, S100A13, PHLDA2, C3, LMO7, Sema3c, KRT8
- KRT18

### Pulmonary alveolar type 2 cell

Description: Alveolar type 2 (AT2) cells, which act as progenitor cells for AT1 cells and secrete pulmonary surfactant to prevent alveolar collapse.

Genes:
- SFTPC, SFTPB, SFTPA1, SFTPA2, SFTPD, ABCA3, LAMP3, PGC, NAPSA, ETV5, CEBPB, LPCAT1
- SLC34A2, CYB5A, MUC1, CXCL15, SCD1, FASN, I聯合, LCN2, SLPI, BPIFB1

### Transitional alveolar epithelial cell

Description: An intermediate, state-transitioning alveolar epithelial cell state (also known as PATS, ADI, or DATPs) observed during injury, fibrosis, or active regeneration of AT1 cells from AT2 progenitors.

Genes:
- KRT8, KRT19, CLDN4, S100A4, SOX4, TP63, LCN2, MMP7, ITGB6, FN1, COL1A1, CTNNB1
- TGFB1, YAP1, HBEGF, AREG, SERPINB1, SPRRI, GDF15, S100A9

## pulmonary alveolar type 2 cell

### Alveolar Type 1 (AT1) Cell

Description: A highly flattened, thin epithelial cell type covering the majority of the alveolar surface area, specialized for gas exchange and frequently confused with AT2 cells in damaged lungs.

Genes:
- AGER, PDPN, CAV1, CLDN18, RTN4, EMP2, HOPX, S100A6, Ager, AQP5, SPOCK2, EPB41L4A
- GPRC5A, COL4A3, COL4A4, PECAM1, KRT8, KRT18, FXYD3, C1orf116, S100A10, S100A11, HEBP2, ANXA2

### Alveolar Type 2 (AT2) Cell

Description: The canonical alveolar epithelial type 2 cell responsible for surfactant production, maintenance of the alveolar niche, and acting as a progenitor for type 1 cells.

Genes:
- SFTPC, SFTPA1, SFTPA2, SFTPB, SFTPD, ABCA3, LAMP3, PGC, NAPSA, SLC34A2, ETV5, CEBPA
- LPCAT1, SCGB3A2, CYP2F1, MUC1, FASN, SCD, CXCL15, PGC, LCN2, BPIFB1, NKX2-1, HCFC1R1
- SFTPA1B

### Club Cell

Description: A secretory bronchiolar epithelial cell type that can be confused with AT2 cells due to shared expression of certain secretoglobins and surfactant-associated proteins.

Genes:
- SCGB1A1, SCGB3A2, CYP2F1, BPIFB1, CCSP, ALDH1A1, MUC5B, KRT15, SFTPA1, SFTPB, GPX2, GSTP1
- TFF3, WFDC2, SLPI, LYZ, CXCL17, MSMB, HP, CP

### Transitional Alveolar Epithelial Cell (DATS/ADI/PATS)

Description: An intermediate, pre-alveolar type 1 transitional state (also known as ADI, PATS, or DATS) that emerges during alveolar injury and regeneration, expressing both epithelial and mesenchymal markers.

Genes:
- KRT8, CLDN4, S100A9, S100A8, SOX4, TP63, KRT19, KRT17, LCN2, MMP7, FN1, VIM
- CDKN1A, GDF15, CTNNB1, TGFB1, ITGB6, COL1A1, COL1A2, SERPINB1, B2M, CD24

## pulmonary artery endothelial cell

### Lymphatic Endothelial Cells

Description: Endothelial cells forming the lymphatic vessels of the lung, responsible for fluid drainage and immune cell trafficking, often confused with blood vascular endothelial cells.

Genes:
- PROX1, PDPN, LYVE1, FLT4, CCL21, TFPI, MMRN1, CALCRL, ANXA2, FABP4, CDH5, PECAM1
- CLDN5, S100A13, PTPRB, ELN, B2M, TMSB4X, FTL, FTH1

### Pulmonary Artery Endothelial Cells

Description: Macrovascular arterial endothelial cells lining the pulmonary artery, characterized by high expression of arterial specification markers and shear-stress responsive genes.

Genes:
- DKK2, FBLN5, GJA5, BMX, SEMA3G, EFNB2, SOX17, HEY1, VWF, CDH5, PECAM1, CLEC14A
- MECOM, PRSS23, S100A10, CXCL12, SFTPA1, SFTPA2, CLDN5, EMCN, KDR, FLT1, NRP1, RAMP2

### Pulmonary Capillary Aerocytes (aCap)

Description: Specialized alveolar capillary endothelial cells (also known as aCap or CAP2) dedicated to gas exchange and leukocyte trafficking within the lung parenchyma.

Genes:
- EDNRA, TBX2, GALNT15, APLNR, HPGD, PRX, FIBIN, S100A4, VIPR1, EMP2, PECAM1, CDH5
- KDR, CA4, COL15A1, ADGRF5, GNG11, CLDN5, ICAM1, CD36

### Pulmonary Capillary General Endothelial Cells (gCap)

Description: General capillary endothelial cells (also known as gCap or CAP1) involved in capillary homeostasis, lipid metabolism, and serving as progenitor cells for aerocytes.

Genes:
- GPIHBP1, PLVAP, SEMA3C, BTNL9, FCN3, CD36, PECAM1, CDH5, KDR, CLDN5, EMCN, RAMP3
- AQP1, SGK1, LPL, FABP4, CAV1, CAV2, IL7R, C7

### Pulmonary Vein Endothelial Cells

Description: Venous endothelial cells draining the lung parenchyma, characterized by the expression of specific venous markers and cell adhesion molecules.

Genes:
- VWF, VCAM1, SELPLG, SELE, POSTN, COL15A1, NPR3, LDLRAD3, WNT2, MMRN1, PECAM1, CDH5
- CLDN5, EMCN, KDR, FLT1, NRP1, RAMP2, BBOX1, C3

## pulmonary neuroendocrine cell

### Basal Cell

Description: Multipotent progenitor cells of the airway epithelium located along the basement membrane, characterized by the expression of TP63 and high-molecular-weight cytokeratins.

Genes:
- TP63, KRT5, KRT14, KRT15, S100A2, DST, COL17A1, BCAM, NGFR, ITGA6, SOX2, ALDH1A3
- CXCL14, GPX3, BNC1, LAMB3, LAMC2, KRT17, AREG, EGFR

### Club Cell

Description: Secretory epithelial cells of the bronchioles that protect the bronchiolar epithelium by secreting uteroglobin (SCGB1A1), surfactant proteins, and xenobiotic-metabolizing enzymes.

Genes:
- SCGB1A1, SCGB3A2, SFTPB, SFTPA1, SFTPA2, CYP2F1, ALDH1A1, BPIFA1, BPIFB1, WFDC2, MUC5B, GPX2
- GSTP1, HP, PIGR, SLPI, SERPINB1, LYZ, CXCL17, TFF3

### Pulmonary Neuroendocrine Cell (PNEC)

Description: Rare, specialized airway epithelial cells that act as sensory receptors, secreting neuropeptides like calcitonin gene-related peptide (CGRP) and gastrin-releasing peptide (GRP) in response to hypoxia or injury.

Genes:
- CHGA, CHGB, ASCL1, CALCA, GRP, SCG2, SCG3, PCSK1, INSM1, SYP, UCHL1, BEX1
- SST, CPLX2, SNAP25, VAMP2, NCAM1, TPH1, NEUROD1, DLK1, SCGN, S100A6, CD24, TMSB4X

### Tuft Cell (Brush Cell)

Description: Chemosensory epithelial cells of the airways that express taste transduction machinery and produce IL-25 to initiate type 2 immune responses.

Genes:
- POU2F3, TRPM5, IL25, ALOX5AP, CHAT, GNG13, PLCG2, LRMP, SH2D6, BMX, AVIL, PTGS1
- HPGDS, SOX9, KRT18, KRT8, GFI1B, ASCL2, SPIB, IL17RB, HCK, FGR

## respiratory basal cell

### Club Cell

Description: Non-ciliated secretory cells of the bronchioles that produce surfactant-associated proteins and host defense molecules, often confused with basal cells during transitional differentiation phases.

Genes:
- SCGB1A1, SCGB3A2, BPIFA1, CYP2F1, ALDH3A1, SERPINB1, MUC5B, WFDC2, SLPI, SFTPA1, SFTPB, SFTPA2
- CEACAM6, CD24, GPX2, GSTP1, HP, LYZ, CXCL17, TFF3

### Differentiating Basal Cell

Description: A transitional state of basal cells undergoing early differentiation toward suprabasal or secretory lineages, showing downregulation of TP63 and upregulation of KRT4 and KRT13.

Genes:
- KRT4, KRT13, KRT8, KRT19, SPINK5, CLDN4, S100A9, S100A8, IVL, TGM1, SPRRIB, ALOX12B
- PI3, SLPI, MUC1, ELF3, JAG2, NOTCH3, HES1, KRT23

### Ionocyte

Description: A rare, specialized airway epithelial cell type responsible for regulating pH and water transport via high expression of CFTR and FOXI1, which can be misannotated as basal cells due to shared rare progenitor markers.

Genes:
- FOXI1, CFTR, ASCL3, ATP6V1B1, ATP6V0A4, BSND, CLCNKB, SCNN1G, IGFBP2, S100A14, TMEM229B, L1CAM
- FXYD1, FXYD5, KRT18, KRT19, CA2, CA12, SLC26A9, GSTA1

### Respiratory Basal Cell (True)

Description: Resident progenitor cells of the airway epithelium characterized by the expression of TP63 and high-molecular-weight cytokeratins, which anchor to the basement membrane.

Genes:
- TP63, KRT5, KRT14, KRT15, DST, BCAM, COL17A1, NGFR, S100A2, DLX5, SOX2, ITGA6
- ITGB4, LAMB3, LAMC2, KRT17, CXCL14, BNC1, ALDH1A3, AREG, EGFR, FGF2, GAS6, SERPINB3
- SERPINB4

## respiratory tract hillock cell

### Classical basal cell

Description: The resident progenitor cell of the airway epithelium, anchored to the basement membrane and characterized by high expression of TP63, KRT5, and KRT15.

Genes:
- KRT5, KRT15, TP63, COL17A1, DST, BCAM, NGFR, S100A2, DLX5, SOX2, KRT17, LAMB3
- LAMC2, ITGA6, ITGB4, CXCL14, MEG3, HELLS, BIRC5, TOP2A

### Club cell

Description: Secretory cells of the bronchiolar epithelium that produce surfactant-associated proteins and host defense molecules, often confused with hillock cells due to shared secretory gene expression.

Genes:
- SCGB1A1, SCGB3A2, SFTPB, SFTPA1, SFTPA2, CYP2F1, BPIFA1, BPIFB1, ALDH1A3, MUC5B, TFF3, WFDC2
- SLPI, PIGR, GPX2, GSTP1, HP, CP, LYZ, CXCL17

### Goblet cell

Description: Mucus-producing secretory cells of the respiratory tract that can be confused with hillock cells during transitional or hyperplastic states in the lung parenchyma.

Genes:
- MUC5AC, MUC5B, SPDEF, FOXA3, AGR2, TFF1, TFF3, BPIFB1, GPX2, CLCA1, FCGBP, S100A11
- CEACAM5, GALNT2, SPINK4, REG4, TSPAN8, MIA, JCHAIN, LTF

### Hillock-like basal cell

Description: A transitional or stratified squamous-like basal cell state found in the airway epithelium, characterized by high expression of keratins 4 and 13 and genes involved in barrier function and inflammation.

Genes:
- KRT13, KRT4, SPINK5, CLDN4, S100A2, S100A8, S100A9, ALDH3A1, DST, LYPD3, SERPINB3, SERPINB4
- PI3, IVL, SPRRI, SPRR2A, KRT5, TP63, GABRP, AREG, EREG, IL1B, CXCL8, NFKBIA

## smooth muscle cell

### Airway smooth muscle cells

Description: Smooth muscle cells surrounding the bronchi and bronchioles that regulate airway resistance, distinguished by cholinergic receptor expression and extracellular matrix deposition.

Genes:
- ACTA2, MYH11, TAGLN, CNN1, LMOD1, SLMAP, CHRM3, ADR_B2, PTGER3, C3, POSTN, COMP
- SPON1, LTBP2, ELN, BGN, DCN, COL1A1, COL3A1, ASPN, MFAP5, FBLN2

### Alveolar fibroblasts

Description: Resident interstitial mesenchymal cells of the alveolar septum that produce structural extracellular matrix and support alveolar epithelial homeostasis, often confused with smooth muscle due to shared mesenchymal markers.

Genes:
- PDGFRA, TCF21, NPNT, FBLN1, FBLN5, LIMCH1, COL1A1, COL1A2, COL3A1, DCN, LUM, MFAP4
- ELN, G0S2, APOD, C7, FGF10, SVEP1, PI16, CD34

### Pericytes

Description: Mural cells closely associated with the abluminal surface of capillaries, sharing lineage markers with vascular smooth muscle but lacking mature myofibrillar proteins like MYH11.

Genes:
- PDGFRB, RGS5, KCNJ8, ABCC9, NDUFA4L2, VTN, CSPG4, MCAM, COX4I2, HIGD1B, GJA4, HEG1
- ANGPT1, TBX18, ALX4, ZNF385D, STEAP4, CACNA1C, KCNA5, TRPC6

### Vascular smooth muscle cells

Description: Contractile mural cells wrapping arterial and venous vessels in the lung parenchyma, characterized by high expression of mature contractile apparatus genes and Notch3 signaling.

Genes:
- ACTA2, MYH11, TAGLN, CNN1, MYLK, LMOD1, TPM2, NOTCH3, PDGFRB, MCAM, HEG1, VTN
- CSPG4, KCNJ8, ABCC9, RGS5, MUSTN1, CALD1, ACTG2, MYG1, FLNA, AOC3, PLN

## stromal cell

### Adventitial Fibroblast

Description: A specialized stromal fibroblast subtype localized in the adventitia of large bronchovascular bundles, characterized by high expression of extracellular matrix proteins, CD34, and PI16.

Genes:
- PDGFRB, COL1A1, COL1A2, COL3A1, DCN, LUM, FBLN1, FBLN2, MFAP5, SVEP1, PI16, CD34
- DPP4, APOD, C3, C7, IGF1, PDGFRB, TCF21, HAS2, COL6A1, COL6A2, FBN1, SERPINF1
- CLEC3B

### Alveolar Fibroblast

Description: Also known as lipofibroblasts or interstitial fibroblasts, these cells reside in the alveolar septa, express PDGFRA, and are critical for alveolar maintenance and surfactant production support.

Genes:
- PDGFRA, TCF21, NPNT, FGF10, LIMCH1, ASPN, G0S2, ELN, COL14A1, ITGA8, WNT2, WNT5A
- ACTA2, SPON1, FBLN5, SCARA5, ADAMTSL1, TNC, COL18A1, LAMA2

### Mesothelial Cell

Description: Specialized epithelial-like stromal cells forming the protective lining of the visceral pleura, expressing both epithelial keratins and mesenchymal markers like WT1 and MSLN.

Genes:
- MSLN, WT1, CALB2, KRT8, KRT18, KRT19, UPK3B, BNC1, HAS1, ALDH1A2, PRG4, LRRN4
- SLPI, CLDN15, HP, CFB, ICAM1, SOD3, COL1A1, COL3A1

### Pericyte

Description: Contractile mural cells wrapping around capillaries and post-capillary venules, expressing RGS5 and CSPG4, which are frequently confused with general stromal fibroblasts.

Genes:
- PDGFRB, CSPG4, MCAM, RGS5, KCNJ8, ABCC9, VTN, NDUFA4L2, HEYL, COX4I2, HIGD1B, GJA4
- ACTA2, TAGLN, MYLK, CALD1, NOTCH3, EBF1, PECAM1, CD248

### Vascular Smooth Muscle Cell

Description: Contractile cells surrounding larger pulmonary arteries and veins, characterized by high expression of mature contractile apparatus proteins like MYH11 and CNN1, often transcriptionally similar to myofibroblasts.

Genes:
- ACTA2, TAGLN, MYH11, MYLK, CNN1, LMOD1, TPM2, FLNA, CALD1, NOTCH3, PDGFRB, RGS5
- DES, PLN, SLMAP, MUSTN1, CHRM3, CASQ2, PCP4, AOC3

## t cell

### CD4+ T Regulatory Cells (Tregs)

Description: Immunosuppressive CD4+ T cells characterized by FOXP3 expression that maintain immune tolerance and prevent autoimmunity in the lung parenchyma.

Genes:
- FOXP3, IL2RA, IKZF2, CTLA4, TIGIT, TNFRSF18, TNFRSF4, BATF, PRDM1, IL10, LAIR2, CD4
- IL32, CD27, ICOS, FGL2, SST, RTKN2, ANXA1, CD1c

### CD8+ Tissue-Resident Memory T Cells (Trm)

Description: Non-recirculating CD8+ cytotoxic T cells residing in the lung parenchyma that provide rapid localized protection against mucosal pathogens.

Genes:
- CD8A, CD8B, ITGA1, ITGAE, CD69, CXCR6, CRTAM, RUNX3, ZNF683, IFNG, TNF, CCL3
- CCL4, CCL5, GZMB, GZMK, PRF1, NKG7, HOPX, DUSP6, RGS1

### Gamma-Delta (γδ) T Cells

Description: T cells expressing the gamma-delta TCR chains that bridge innate and adaptive immunity, enriched at mucosal barriers like the lung parenchyma.

Genes:
- TRDC, TRGC1, TRGC2, CD3D, CD3E, CD3G, KLRB1, KLRC1, ZBTB16, RORC, IL23R, SOX13
- BLK, GZMA, GZMK, NKG7, CCL5, S100A4, CD2, LAT

### Natural Killer (NK) Cells

Description: Innate lymphoid cells that share morphological and cytotoxic gene expression profiles with CD8+ T cells, often leading to annotation confusion in lung tissue.

Genes:
- NCAM1, NCR1, KLRD1, KLRF1, KLRB1, KLRC1, FCGR3A, PRF1, GZMB, GZMA, NKG7, GNLY
- FGFBP2, SPON2, CST7, CD160, XCL1, XCL2, CLIC3, HOPX

## tracheobronchial goblet cell

### Alveolar Type II (AT2) cell

Description: Cuboidal epithelial cells of the alveolar parenchyma that synthesize and secrete pulmonary surfactant and act as progenitors for AT1 cells.

Genes:
- SFTPC, SFTPA1, SFTPA2, SFTPB, SFTPD, ABCA3, LAMP3, PGC, NAPSA, ETV5, CEACAM6, SLC34A2
- LPCAT1, CYP2B6, MBTPS2, SCD, FASN, CXCL15, MUC1, NKX2-1, PGC, LCN2

### Club cell

Description: Dome-shaped secretory cells of the bronchioles that produce uteroglobin and surfactant proteins to protect the bronchiolar epithelium.

Genes:
- SCGB1A1, SCGB3A2, SFTPB, CYP2F1, BPIFB1, ALDH1A3, WFDC2, SLPI, MGP, HP, SST, RARRES2
- PEBP1, GSTA1, CPB2, LY6D, KRT18, KRT8, FGB, FGG, SEC14L3, CBR1, S100A6, CXCL17

### Goblet cell (nasal/bronchial-like)

Description: Classic secretory goblet cells of the conducting airways characterized by high expression of gel-forming mucins and defense response genes.

Genes:
- MUC5AC, MUC5B, SPDEF, GPX2, TFF3, AGR2, BPIFB1, S100A9, S100A8, CEACAM5, TFF1, SLPI
- ALDH3A1, CYP2F1, GSTP1, KRT5, KRT19, LYPD3, CLDN4, ELF3, CD24, PI3, LCN2, WFDC2
- MUC16

### Mucinous bronchial gland cell

Description: Specialized secretory cells residing in the submucosal glands of the upper airways, producing high levels of MUC5B and antimicrobial proteins.

Genes:
- MUC5B, LTF, LYZ, PRB1, PRB2, PRH1, PRH2, PIP, AZGP1, BPIFA1, BPIFB1, PIGR
- SOX9, DMBT1, TFF3, AGR2, MUC7, CST3, CST1, CST4, S100A1, S100A13

## tracheobronchial smooth muscle cell

### Airway smooth muscle cell

Description: Smooth muscle cells wrapping around the bronchi and bronchioles of the lung, responsible for bronchoconstriction and bronchodilation.

Genes:
- ACTA2, TAGLN, MYH11, CNN1, LMOD1, TPM2, DES, SLMAP, PTGER3, ADRA1B, CHRM3, VIPR1
- BBOX1, C7, COMP, POSTN, COL1A1, COL3A1, SPON1, ELN, LTBP2, HAS2, IL6, CXCL8

### Myofibroblast

Description: Activated contractile interstitial fibroblasts that express alpha-smooth muscle actin and produce high levels of extracellular matrix proteins, often expanded during tissue remodeling and fibrosis.

Genes:
- ACTA2, TAGLN, COL1A1, COL1A2, COL3A1, COL5A1, FN1, POSTN, TNC, SPARC, CTGF, CYR61
- PDGFRB, PDGFRA, FAP, VCAN, ELN, LOX, LOXL1, ACTG1, TPM1, CALD1, COMP

### Pericyte

Description: Perivascular cells closely associated with the abluminal surface of pulmonary capillaries and microvessels, sharing several markers with vascular smooth muscle cells but lacking mature contractile markers like MYH11.

Genes:
- PDGFRB, MCAM, RGS5, KCNJ8, ABCC9, VTN, CSPG4, NDUFA4L2, COX4I2, HIGD1B, GJA4, HEG1
- ANGPT1, TBX18, STEAP4, KCNA5, CACNA1C, TRPC6, EDNRA, AGTR1

### Vascular smooth muscle cell

Description: Contractile mural cells surrounding pulmonary blood vessels, characterized by high expression of classic smooth muscle contractile machinery and distinct from airway smooth muscle.

Genes:
- ACTA2, TAGLN, MYH11, MYLK, CNN1, LMOD1, TPM2, NOTCH3, PDGFRB, MCAM, HEG1, VTN
- CSPG4, KCNJ8, ABCC9, RGS5, CALD1, ACTG2, FLNA, MYG1, AOC3, MUSTN1, PLN, CHRM3

## vein endothelial cell

### Aerocyte (aCap) Endothelial Cells

Description: Specialized alveolar capillary endothelial cells (aerocytes) dedicated to gas exchange, often confused with venous cells due to shared capillary-venous transition markers.

Genes:
- HPGD, EDN1, TBX2, APLNR, PRX, SEMA3C, FCN3, GALNT18, GPR116, ADGRG6, CD300LG, S100A13
- CA4, EMP2, VIPR1, PECAM1, CDH5, KDR, FLT1, CLEC14A

### Lymphatic Endothelial Cells

Description: Endothelial cells lining the lymphatic vessels of the lung parenchyma, frequently confused with venous endothelial cells due to shared expression of genes like MMRN1 and FLT4.

Genes:
- PROX1, PDPN, LYVE1, FLT4, CCL21, TXNIP, TFPI, MMRN1, FABP4, B2M, CALCB, ANXA2
- S100A10, CD36, PTPRB, GNG11, ELN, FXYD6, EFNB2, NRP2

### Pulmonary Vein Endothelial Cells

Description: Endothelial cells of the pulmonary venous system that return oxygenated blood to the heart, expressing distinct extracellular matrix and signaling genes like COL15A1.

Genes:
- VWF, EMCN, WNT2, PRSS23, COL15A1, S100A4, CD9, TSPAN8, FGL2, GNG11, CLDN5, RAMP2
- CALCRL, ESAM, ENG, FLT4, PROX1, MMRN2, CLEC14A, ELENE

### Systemic Vein Endothelial Cells

Description: Endothelial cells lining the systemic venules and veins of the lung, characterized by high expression of leukocyte adhesion molecules and chemokine receptors like ACKR1.

Genes:
- ACKR1, SELE, SELPLG, VWF, ICAM1, VCAM1, CCL2, IL6, CXCL8, POSTN, MMRN1, GJA4
- PLAT, F3, BBLN, LDLR, PLVAP, CD36, PECAM1, CDH5, KDR, FLT1

