# PFAS-rBRICS-SME

This repository contains supplementary code and representative example outputs developed for the manuscript:

**Machine Learning Explainability & Interpretability for Accelerating QSPR Modeling in PFAS Molecules**

## Overview

PFAS-rBRICS is a PFAS-specific extension of the rBRICS fragmentation strategy used within the Substructure Mask Explanation (SME) framework for molecular explainability. The method introduces additional SMARTS environments and compatibility rules designed to improve fragmentation of characteristic PFAS structural motifs, including perfluoroalkyl chains, fluorotelomers, perfluoroethers, sulfonamides, PFSA, and PFCA functional groups.

This repository contains:

- **PFAS-specific SMARTS environments and compatibility rules** used to extend the original rBRICS fragmentation strategy.
- **Hyperparameter search space** used for optimization of the RGCN models.
- **Representative molecular prediction outputs** for electron affinity (EA), ionization potential (IP), and HOMO-LUMO gap (HL).
- **Representative SME fragment attribution examples** illustrating fragment-level explanations generated using PFAS-rBRICS.

## Acknowledgements

PFAS-rBRICS extends the Substructure Mask Explanation (SME) framework by introducing PFAS-specific SMARTS environments and compatibility rules for molecular fragmentation. The underlying SME methodology and original implementation were developed by Wu et al.

**Original SME publication**

Wu, Z., et al. *Chemistry-intuitive explanation of graph neural networks for molecular property prediction with substructure masking.* Nature Communications, **14**, 2555 (2023).

https://www.nature.com/articles/s41467-023-38192-3

**Original SME software**

Wu, Z., et al. *Substructure-Mask-Explanation (SME).* Zenodo.

https://doi.org/10.5281/zenodo.7707093
