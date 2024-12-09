# Normal-Lung-Aging
This repository contains pipelines for single-cell derived aging clock and aging pipeline analysis and reproduces the main analyses in our manuscript.

System Requirements:

Operating System: Tested on RedHat 7.7 x86_64.
R Version: 4.1.0

Installing the conda environment:
'''
conda env create --file=AgingClock.yml
conda activate AgingClock
'''

Please find the required file for installation in the main repository named "AgingClock.yml".


### PBMCs

'''

library(Seurat)
library(scRepertoire)
library(harmony)
library(ggpubr)
library(dplyr)
library(stringr)
library(gridExtra)

options(Seurat.object.assay.version = 'v3')



directory_path <- "./tcrs/"

csv_files <- list.files(directory_path, pattern="\\.csv$", full.names=TRUE)

csv_data_list <- list()

for(file_path in csv_files) {
      file_name <- basename(file_path)
      parts <- strsplit(file_name, "AS")[[1]]
      if(length(parts) > 1) {
        # extract the part after "AS" and before "-TCR"
        after_AS <- sub("-TCR.*$", "", parts[2])
        first_5_after_AS <- substr(after_AS, 1, 5)
        # construct sample_id by appending 'ALAW-AS' and the first 5 characters after "AS"
        sample_id <- paste0("ALAW-AS", first_5_after_AS)
        print(sample_id)
      } else {
        next
      }
      #sample_id <- strsplit(file_name, "_")[[1]][1] # Extract the sample ID

    df <- read.csv(file_path)
    if("barcode" %in% colnames(df)) {
    df$barcode <- paste(sample_id, df$barcode, sep="_")
  }
    csv_data_list[[file_name]] <- df
}

contig_list <- lapply(csv_data_list, function(df) loadContigs(df, format = "10X"))
combined3 <- combineTCR(removeMulti = TRUE, removeNA = TRUE, contig_list)
tcrL_tumor = lapply (csv_files, function(x) read.csv(x))
names (combined2) = c(sorted_identifiers)

sce <- combineExpression(combined3, 
                  data, 
                  cloneCall="gene",
                  proportion = FALSE, 
                  #cloneSize=c(Single=1, Small=5, Medium=20, Large=100, Hyperexpanded=500
                  cloneSize=c(Single=1, Small=5, Large=500))

sce@meta.data$Age_group3 <- cut(
  sce@meta.data$Age,
  breaks = c(-Inf, 40, 60, Inf),
  labels = c("Young", "Intermediate", "Old"),
  right = FALSE # intervals are of the form [a, b), which includes a but not b
)
'''
