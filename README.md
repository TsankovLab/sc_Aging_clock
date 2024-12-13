# sc_Aging_clock
This repository contains pipelines for single-cell derived aging clock and aging pipeline analysis and reproduces the main analyses in our manuscript.

System Requirements:

Operating System: Tested on RedHat 7.7 x86_64.
R Version: 4.1.0

Installing the conda environment:
```
conda env create --file=AgingClock.yaml
conda activate AgingClock
```

Please find the required file for installation in the main repository named "AgingClock.yaml".

## Dataset 

### Single cell
Here is the link to download the single-cell dataset:  
[Single_cell data](https://cellxgene.cziscience.com/collections/6f6d381a-7701-4781-935c-db10d30de293)

You can find the code to create the Seurat object in the [data folder](https://github.com/TsankovLab/sc_Aging_clock/tree/main/Data).


### Bulk data      
Here is the link to download the bulk dataset:  
[GTEX data](https://gtexportal.org/home/downloads/adult-gtex/bulk_tissue_expression) 

```

rm(list=ls())
options(stringsAsFactors = F)
# load libraries
library(ggplot2)
library(Seurat)
library(dplyr)
library(Matrix)
library(ggpubr)
library(hash)
library(data.table)
library(hashmap)
library(string)


projDir="data path"
sample.df <- read.delim(paste0(projDir,"/GTEx_normal_bulk_RNA/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt"), as.is=TRUE, header=TRUE, row.names=1)
subject.df <- read.delim(paste0(projDir,'/GTEx_normal_bulk_RNA/GTEx_Analysis_v8_Annotations_SubjectPhenotypesDS.txt'), as.is=TRUE, header=TRUE, row.names=1)


rnaseq.sample.df <- sample.df[sample.df['SMAFRZE']=='RNASEQ', ]

as.matrix(sort(table(rnaseq.sample.df['SMTSD']), decreasing=TRUE))

lung.sample.df = rnaseq.sample.df[rnaseq.sample.df['SMTSD']=='Lung', ]
head(lung.sample.df)

rownames(lung.sample.df)[1:3]
blood.sample.df = rnaseq.sample.df[rnaseq.sample.df['SMTSD']=='Whole Blood', ]
head(blood.sample.df)

rownames(blood.sample.df)[1:3]


str(lung.sample.df)
str(blood.sample.df)

Unpaired.sample.df = rnaseq.sample.df[rnaseq.sample.df['SMTSD']==c('Whole Blood',"Lung"), ]

donor.ids <- unlist(lapply(strsplit(rownames(lung.sample.df), '-'), FUN=function(x){paste(x[1],x[2],sep="-")}))
donor.ids <- unlist(lapply(strsplit(rownames(blood.sample.df), '-'), FUN=function(x){paste(x[1],x[2],sep="-")}))
donor.ids <- unlist(lapply(strsplit(rownames(Unpaired.sample.df), '-'), FUN=function(x){paste(x[1],x[2],sep="-")}))

duplicated(donor.ids)

donor.ids[1:3]

subject.df$Donors=rownames(subject.df)

lung.subject.df=subject.df[grepl(paste(donor.ids, collapse="|"),subject.df$Donors),]

lung.sample.df$Sample=0
lung.sample.df$Sample=row.names(lung.sample.df)
lung.sample.df$Donors=0
lung.sample.df$Donors=donor.ids

lung.metadata=merge(lung.subject.df,lung.sample.df,by="Donors")

rownames(lung.metadata)=lung.metadata$Sample
blood.subject.df=subject.df[grepl(paste(donor.ids, collapse="|"),subject.df$Donors),]

blood.sample.df$Sample=0
blood.sample.df$Sample=row.names(blood.sample.df)
blood.sample.df$Donors=0
blood.sample.df$Donors=donor.ids

blood.metadata=merge(blood.subject.df,blood.sample.df,by="Donors")

rownames(blood.metadata)=blood.metadata$Sample



paired.names=intersect((lung.metadata)$Donors ,(blood.metadata)$Donors)


lung.metadata_paired <- lung.metadata[lung.metadata$Donors %in% paired.names, ]
blood.metadata_paired <- blood.metadata[blood.metadata$Donors %in% paired.names, ]


tpm.lung.df <- read.delim(paste0(projDir,"/GTEx_normal_bulk_RNA/gene_tpm_2017-06-05_v8_lung.gct"),
	as.is=T, row.names=1, check.names=FALSE, skip=2)

gene.names.lung.df <- tpm.lung.df[, 'Description', drop=FALSE]
head(gene.names.lung.df)

ENSG.names.lung.df <- tpm.lung.df[, 'Name', drop=FALSE]
head(ENSG.names.lung.df)
duplicated(gene.names.lung.df) 
duplicated(ENSG.names.lung.df)


rownames(tpm.lung.df)=tpm.lung.df$Name

tpm.lung.df1 <- tpm.lung.df[, !(names(tpm.lung.df) %in% c('Description'))]
tpm.lung.df2 <- tpm.lung.df1[, !(names(tpm.lung.df1) %in% c('Name'))]

cat(paste("Number of genes in table: ", dim(tpm.lung.df1)[1]))

head(tpm.lung.df2)

all(rownames(lung.metadata) == colnames(tpm.lung.df2))

setdiff(colnames(tpm.lung.df2),rownames(lung.metadata))


gtex.normal=CreateSeuratObject(counts=tpm.lung.df2, meta.data=lung.metadata)


save(gtex.normal, file=paste0(projDir,"/GTEx_normal_bulk_RNA/GTex.normal.lung.Rda"))


bulk$agetrio <- NA
bulk$agetrio[bulk$AGE == "20-29"] <- "young"
bulk$agetrio[bulk$AGE == "30-39"] <- "young"
bulk$agetrio[bulk$AGE == "40-49"] <- "young"
bulk$agetrio[bulk$AGE == "50-59"] <- "old"
bulk$agetrio[bulk$AGE == "60-69"] <- "old"
bulk$agetrio[bulk$AGE == "70-79"] <- "old"
bulk$agetrio[is.na(bulk$AGE)] <- NA


library(data.table)

data_to_write_out <- as.data.frame(as.matrix(bulk@meta.data))
fwrite(x = data_to_write_out, file=paste0(proj.dir,"GTex_lung_metadata.csv"))

meta=as.data.frame(as.matrix(bulk@meta.data))
library(data.table)
data_to_write_out <- as.data.frame(as.matrix(bulk@assays$RNA@counts))
fwrite(x = data_to_write_out2, row.names=TRUE, file=paste0(proj.dir,"GTex_lung_expression.csv"))


trimmed_donors <- lung.metadata_paired$Sample

tpm.lung.df2_paired <- tpm.lung.df2[, colnames(tpm.lung.df2) %in% trimmed_donors]

all(rownames(lung.metadata_paired) == colnames(tpm.lung.df2_paired))

setdiff(colnames(tpm.lung.df2_paired),rownames(lung.metadata_paired))

gtex.normal=CreateSeuratObject(counts=tpm.lung.df2_paired, meta.data=lung.metadata_paired)

save(gtex.normal, file=paste0(projDir,"/GTEx_normal_bulk_RNA/GTex.normal.lung.blood_paired.Rda"))

tpm.blood.df <- read.delim(paste0(projDir,"/GTEx_normal_bulk_RNA/gene_tpm_2017-06-05_v8_whole_blood.gct"),
	as.is=T, row.names=1, check.names=FALSE, skip=2)

gene.names.blood.df <- tpm.blood.df[, 'Description', drop=FALSE]
head(gene.names.blood.df)

ENSG.names.blood.df <- tpm.blood.df[, 'Name', drop=FALSE]
head(ENSG.names.blood.df)


duplicated(gene.names.blood.df) # so we dont use the gene names as rownames, could convert from ENSG later in srt
duplicated(ENSG.names.blood.df)# use this as rownaems

rownames(tpm.blood.df)=tpm.blood.df$Name

tpm.blood.df1 <- tpm.blood.df[, !(names(tpm.blood.df) %in% c('Description'))]
tpm.blood.df2 <- tpm.blood.df1[, !(names(tpm.blood.df1) %in% c('Name'))]

cat(paste("Number of genes in table: ", dim(tpm.blood.df1)[1]))

all(rownames(blood.metadata) == colnames(tpm.blood.df2))

setdiff(colnames(tpm.blood.df2),rownames(blood.metadata))

gtex.normal=CreateSeuratObject(counts=tpm.blood.df2, meta.data=blood.metadata)

save(gtex.normal, file=paste0(projDir,"/GTEx_normal_bulk_RNA/GTex.normal.blood.Rda"))

trimmed_donors <- blood.metadata_paired$Sample

tpm.blood.df2_paired <- tpm.blood.df2[, colnames(tpm.blood.df2) %in% trimmed_donors]

all(rownames(blood.metadata_paired) == colnames(tpm.blood.df2_paired))

setdiff(colnames(tpm.blood.df2_paired),rownames(blood.metadata_paired))

gtex.normal=CreateSeuratObject(counts=tpm.blood.df2_paired, meta.data=blood.metadata_paired)


save(gtex.normal, file=paste0(projDir,"/GTEx_normal_bulk_RNA/GTex.normal.blood.lung_paired.Rda"))

bulk$agetrio <- NA
bulk$agetrio[bulk$AGE == "20-29"] <- "young"
bulk$agetrio[bulk$AGE == "30-39"] <- "young"
bulk$agetrio[bulk$AGE == "40-49"] <- "young"
bulk$agetrio[bulk$AGE == "50-59"] <- "old"
bulk$agetrio[bulk$AGE == "60-69"] <- "old"
bulk$agetrio[bulk$AGE == "70-79"] <- "old"
bulk$agetrio[is.na(bulk$AGE)] <- NA


library(data.table)
data_to_write_out <- as.data.frame(as.matrix(bulk@meta.data))
fwrite(x = data_to_write_out, file=paste0(proj.dir,"GTex_lung_metadata.csv"))


meta=as.data.frame(as.matrix(bulk@meta.data))
library(data.table)
data_to_write_out <- as.data.frame(as.matrix(bulk@assays$RNA@counts))
fwrite(x = data_to_write_out2, row.names=TRUE, file=paste0(proj.dir,"GTex_lung_expression.csv"))

```






### PBMCs  

Here is the link to download the PBMC data:  
[PBMC data](https://gtexportal.org/home/downloads/adult-gtex/bulk_tissue_expression)     

```

library(Seurat)
library(scRepertoire)
library(harmony)
library(ggpubr)
library(dplyr)
library(stringr)
library(gridExtra)

options(Seurat.object.assay.version = 'v3')



directory_path <- "./tcrs/"

# csv file with files
csv_files <- list.files(directory_path, pattern="\\.csv$", full.names=TRUE)

csv_data_list <- list()

# modify barcodes
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
#--- apply the names to the list

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
```
