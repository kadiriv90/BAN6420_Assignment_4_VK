# ----Project Title: Netflix Data Visualization using R----------
# -------------------------------------------------------------------------------------------------------
# Created by: Victor Kadiri
# Date Created: 28th March 2025

# The Actual Analysis Starts from line 20

# The objective of the series of R script below is to perform a detailed analysis and visualisation of Netflix movies data. The procedures performed are as follows:
# - Data preparation and cleaning
# - R visualization
# - saving outputs.

# Desired Output: 
# The output of the R model will be:
#         c. R generated - top_netflix_genres.png" (R version)

## ------ The Actual Analysis Starts here ---------------
# Import required libraries
# Load the ggplot2 package for creating graphs
library(ggplot2)

# ------------------------ 1. Data Preparation ----------------------------------------

#  This part of the code handles data loading and initial preparation.
#  Get input and output paths from user
cat("\nPlease enter your folder paths (use forward slashes /. e.g C:/Users/User/Downloads/BAN6420/Assignment_4/input)\n")
input_folder <- readline("Enter input folder path: ")
output_folder <- readline("Enter output folder path: ")

# Create output folder if it doesn't exist
if (!dir.exists(output_folder)) {
  dir.create(output_folder, recursive = TRUE)
  message("✓ Created output folder at: ", output_folder)
}

# Create full file paths
input_file <- file.path(input_folder, "netflix_data.csv")
output_file <- file.path(output_folder, "visualizations/top_netflix_genres_r.png")

# Check if input file exists
if (!file.exists(input_file)) {
  stop("❌ Error: Input file not found at: ", input_file)
}

# Read the Netflix data
message("\n⏳ Loading Netflix data...")
netflix <- read.csv(input_file, stringsAsFactors = FALSE)

# ------------------------ 2. Data Cleaning ----------------------------------------
# Fix missing values (replace NA with "Unknown")
message("🔧 Cleaning data...")
netflix$director[is.na(netflix$director)] <- "Unknown"
netflix$cast[is.na(netflix$cast)] <- "Unknown"
netflix$country[is.na(netflix$country)] <- "Unknown"

# Count how many shows/movies are in each genre
message("📊 Analyzing genres...")
genres <- unlist(strsplit(netflix$listed_in, ", "))
genre_counts <- as.data.frame(table(genres))
top_genres <- head(genre_counts[order(-genre_counts$Freq), ], 10)
names(top_genres) <- c("genre", "count")

## ------------------------ 3. Data Visualization ----------------------------------------
# Create a bar chart using ggplot
message("🎨 Creating visualization...")
p <- ggplot(top_genres, aes(x = count, y = reorder(genre, count))) +
  geom_col(fill = "#E50914", alpha = 0.8) + 
  geom_text(aes(label = count), 
            hjust = -0.2, 
            size = 4, 
            color = "black",
            fontface = "bold") +
  labs(title = "Top 10 Most Common Netflix Genres", 
       subtitle = "Based on current Netflix catalog",
       x = "Number of Titles", 
       y = "Genre",
       caption = "Data Source: Netflix") +
  scale_x_continuous(expand = expansion(mult = c(0, 0.1))) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(color = "#E50914", face = "bold", size = 16),
    plot.subtitle = element_text(color = "#555555"),
    panel.grid.major.y = element_blank(),
    axis.text = element_text(color = "#333333")
  )

# Save the visual to the output location
ggsave(output_file, p, width = 10, height = 6, dpi = 300, bg = "white")
message("\n✅ Analysis complete! Visualisation saved to:\n", normalizePath(output_file))