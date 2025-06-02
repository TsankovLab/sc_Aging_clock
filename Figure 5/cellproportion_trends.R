# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

# * File Name : cellproportion_trends.R

# * Description : Plot cell proportion trend with age for HLCA and Xenium data

# * Creation Date : 04-30-2025

# * Last Modified : Wed 30 Apr 2025 11:38:39 AM EDT

# * Created By : Atharva Bhagwat

# _._._._._._._._._._._._._._._._._._._._._.

library(colorRamp2)
library(ComplexHeatmap)

ifelse(!dir.exists(file.path('figures')),
        dir.create(file.path('figures')),
        "")

cellprop <- readRDS('../Data/Spatial/cellprop.rds')

heatmap_matrix = cellprop[['weights']]
annot_matrix = cellprop[['annotations']]

color_mapping <- colorRamp2(c(-10, 0, 10), c("blue", "white", "red"))

heatmapAnnotation <- function(i, j, x, y, w, h, fill) {
    grid.text(annot_matrix[i, j], x, y, gp = gpar(fontsize = 10), rot=90)
}
p_heatmap <- Heatmap(
    t(as.matrix(heatmap_matrix)), 
    cluster_rows = FALSE, 
    cluster_columns = FALSE, 
    name = "-log10p",
    col = color_mapping,
    
    row_names_gp = grid::gpar(fontsize = 6),
    column_names_gp = grid::gpar(fontsize = 6),
    
    heatmap_legend_param = list(
    title_gp = gpar(fontsize = 6),
    labels_gp = gpar(fontsize = 6)
    ),
    
    rect_gp = grid::gpar(col = "white", lwd = 2),
    
    cell_fun = heatmapAnnotation
)

pdf("figures/cellprop.pdf", width = 4, height = 2)
draw(p_heatmap)
dev.off()
