# sc_Aging_clock
#### This repository contains pipelines for single-cell derived aging clock and aging pipeline analysis and reproduces the main analyses in our manuscript, "Human Cellular Clock of the Aging Lung Parenchyma". 
Scripts are organized by figure in separate folders;
You can find the link to download the dataset in the following and for creating the object you can refer to the scripts in the data dolder.        

     
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

You can find the code to create the single cell object in the [data folder](https://github.com/TsankovLab/sc_Aging_clock/tree/main/Data).

### Bulk data      
Here is the link to download the bulk dataset:  
[GTEx data](https://gtexportal.org/home/downloads/adult-gtex/bulk_tissue_expression) 
  
You can find the code to create the GTEx object in the [data folder](https://github.com/TsankovLab/sc_Aging_clock/tree/main/Data).

### PBMCs  

Here is the link to download the PBMC data:  
[PBMC data](https://www.synapse.org/Synapse:syn49637038/files/)   
   
You can find the code to create the PBMC object in the [data folder](https://github.com/TsankovLab/sc_Aging_clock/tree/main/Data).

### Spatial (10x Xenium)
Here is the link to download files required to reproduce the figures:
[Spatial data](https://drive.google.com/file/d/17qEP3kDs6POwiAmpuCiz_zlYfWXNfiCr/view?usp=sharing)

Download and extract the `Spatial` folder in `Data` folder.
