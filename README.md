# Normal-Lung-Aging
This repository contains pipeline for single-cell derived aging clock and aging pipeline analysis and to reproduce main analyses in our manuscript.

System Requirements:

Operating System: Tested on RedHat 7.7 x86_64.
R Version: 4.1.0
R Packages:
   Seurat (v4.1.0) (https://satijalab.org/seurat/)
   ComplexHeatmap (v2.10.0) 
(https://bioconductor.org/packages/release/bioc/html/ComplexHeatmap.html)
clusterProfiler (v4.2.2) (https://bioconductor.org/packages/release/bioc/html/clusterProfiler.html)
SCENT (v1.0.3) (https://github.com/aet21/SCENT)
ggpubr (v0.4.0) (https://rdrr.io/cran/ggpubr/)
ggplot2 (v3.3.6) (https://ggplot2.tidyverse.org)
cgdsr (v1.3.0) (https://rdrr.io/cran/cgdsr)
survival (v3.2.11) (https://rdrr.io/cran/survival/)

Installation Guide:
install.packages("Seurat", version = "4.0.4")
install.packages("dplyrr", version = "1.0.6")
install.packages("patchwork", version = "1.1.1")
install.packages("harmony", version = "0.1.0")
install.packages("ggsci", version = "2.9")
install.packages("Rcpp", version = "1.0.10")
install.packages("SeuratObject", version = "4.0.2")
install.packages("sp", version = "1.4.5")
install.packages("remotes", version = "2.4.0")
install.packages("devtools", version = "2.4.1")
install.packages("viridisLite", version = "0.4.0")
install.packages("paleteer", version = "1.5.0")
install.packages("ggpubr", version = "0.4.0")
install.packages("ggplot2", version = "3.4.2")
install.packages("ggExtra", version = "0.10.1")
install.packages("cgdsr", version = "1.3.0")
install.packages("survival", version = "3.2.11")
install.packages("tidyr", version = "1.1.3")
install.packages("circlize", version = "0.4.12")
install.packages("tibble", version = "3.2.1")
install.packages("devtools", version = "2.4.1")
install.packages("cowplot", version = "1.1.1")

install.packages("grid", version = "4.1.1")

install.packages("viridis", version = "0.6.1")
install.packages("ggnewscale", version = "0.4.7")
install.packages("Matrix", version = "1.3.4")
install.packages("hash", version = "2.2.6.1")
install.packages("fitdistrplus", version = "1.1.5")
install.packages("gdata", version = "2.18.0")
install.packages("tidyverse", version = "2.0.0")
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("ComplexHeatmap", version = "2.8.0")
BiocManager::install("clusterProfiler", version = "4.0.0")

if (!requireNamespace("devtools", quietly = TRUE))
    install.packages("devtools")
devtools::install_github("aet21/SCENT@v1.0.3")
