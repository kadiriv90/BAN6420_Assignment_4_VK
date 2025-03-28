# README

# Project Title: Netflix Data Analysis and Visualization using Python and R

# Created by:  Victor Kadiri

# Date Created: 28th March 2025

# Purpose: 
# The objective of the series of python and R scripts below is to perform a detailed analysis and visualisation of Netflix movies data. The procedures performed are as follows:
# - Data preparation and cleaning
# - Exploratory data analysis
# - Interactive visualizations
# - Report generation/saving outputs.

# Key Features:
# Data Preparation: Load and validate Netflix data
# Data Cleaning: Handle missing values and inconsistencies
# Exploratory Analysis: Generate insights about content types, ratings, genres, and more
# Visualizations: Interactive menu-driven visualizations with multiple plot types
# Report Generation/ Saving Outputs: Create detailed analysis reports in text format and Saving output files.

# Desired Output: 
# The outputs of the python model will be:
# 1. Renamed file: "Netflix_shows_movies.csv"
# 2. Clean version: "Netflix_shows_movies_CLEANED.csv"
# 3. Data exploration report: "Netflix_exploration_report.txt"
# 4. Visualization files in the visualizations subfolder
#         a. Python generated - Genre distribution plots (3 versions)
#         b. Python generated - Content ratings plots (3 versions)
# The outputs of the R model will be:
#         c. R generated - top_netflix_genres.png" (R version)

# Prerequisites
# i. Datasets Required
# Download the netflix data required for this analysis from: https://nexford.instructure.com/courses/6205/files/1267279?wrap=1
# ii. Scripts Required: 
# a. Netflix_show_visualization.py
# b. Netflix_show_visualization.r
# iii. Tools and Installations Required 
# - For python analysis and visualization:
# 1. Download and Install VS Code 
# 2. Download and Install Python 3.12.9 or higher
# 3. Additional libraries: pandas, matplotlib, seaborn
# - For R analysis and visualization:
# 1. VS Code with R extension
# 2. R 4.0 or higher
# 3. Libraries: ggplot2, scales

# Procedures Performed:
# - For python visualization:
# 1: Launch the VS Code application
# 2: Create a main folder: "Netflix_Analysis" containing three sub folders( i. "input" ii. "output" and  iii. "scripts") in your desired location. Refer to "vs_code_folder_structure.png" for the folder structure used in VS code for this analysis.
# 3: Download all files from the GIT repos into the relevant sub folders above.
# 4: Locate and the main folder: "Netflix_Analysis" using VS code
# 5: Locate and open the script file (a.Netflix_show_visualization.py) within VS code environment
# 6: Once opened, locate and Run the script using Ctrl+A and then Shift+Enter or click Run within the VS code environment
# 7: Update the input and output paths when prompted
# 8: View the outputs on the terminal panes and saved results in the output folder.
# - For R visualization:
# 1. Launch VS Code with R extension installed
# 2. Create project folder structure:
#   - Main folder: "Netflix_Analysis"
#   - Subfolders: "input", "output/visualizations", "scripts"
# 3. Place "netflix_data.csv" in input folder
# 4. Place R script in scripts folder
# 5. Open the R script in VS Code
# 6. Run the script (Shift+Enter or click Run)
# 7. Type paths when prompted and click enter
# 8. View intermediate output in terminal 
# 9. Find results in output folder:
#   - "top_netflix_genres_r.png" output/visualization folder


# Troubleshooting
# 1. Common Issues
#  a. File Not Found Error: 
#        Ensure netflix_data.csv exists in the input folder
#        Verify the path you provide is correct
#  b. Missing Packages:
#   Run  pip install --upgrade pandas matplotlib seaborn
# 2. Visualization Display Issues:
#  a. If plots don't appear, try running in VS Code with the Python extension
#  b. Alternatively, save plots to files and view them directly
#  3. PowerShell Ampersand Error:
#  a. Change VS Code's default terminal to Command Prompt:
#     - Open Settings (Ctrl+,)
#     - Search for "terminal integrated shell windows"
#     - Set to "Command Prompt"
#  4. Error Messages
#     The tool provides detailed error messages with troubleshooting tips for each phase:
#     a. Data preparation errors
#     b. Data cleaning issues
#     c. Exploration problems
#     d. Visualization failures

# Common R tips:
# 1. If ggplot2 not found:
#      - Run: install.packages("ggplot2")
# 2. For path issues:
#      - Use forward slashes (/) or double backslashes (\\)
#      - Example: "C:/Users/Name/folder" or "C:\\Users\\Name\\folder"
# 3. For blank plots:
#      - Ensure output folder exists
#      - Check for file or folder permission issues


# Example Workflow:
# A. Python
# 1. Run the script
# 2. Enter input path: e.g C:/projects/netflix-analysis/input
# 3. Enter output path: e.g C:/projects/netflix-analysis/output
# 4. Choose to save prepared data (yes)
# 5. Choose to save cleaned data (yes)
# 6. Explore the data through the interactive menus
# 7. Generate visualizations
# 8. Save the analysis report
# 9. Check the output folder for results
# 10. Check Terminal for analysis breakdown and summary

# B. R Script
# 1. Run the R script
# 2. When prompted to type the paths, enter:
#     - Input path: C:/projects/netflix-analysis/input
#     - Output path: C:/projects/netflix-analysis/output/visualizations
# 3. Script will:
#   - Validate paths
#   - Clean data
#   - Analyze genres
#   - Create visualization
#   - Save visualization as "top_netflix_genres_r.png"
# 4. Check output folder for:
#   - top_netflix_genres_r.png for the visualization
#   - Terminal for analysis summary


# Customization
# You can modify:
# - Python options
#   a. Visualization styles by editing the plt.style.use() and sns.set_palette() settings
#   b. Analysis parameters by changing the value counts (e.g., .head(10) to .head(15))
#   c. Report content by editing the data_exploration() function
# - R options
# 1. Change visualization colors:
#      - Edit fill = "#E50914" (Netflix red) to any hex color
# 2. Adjust top genres shown:
#      - Change head(..., 10) to head(..., 15) for top 15
# 3. Modify plot dimensions:
#      - Edit ggsave(width=10, height=6) parameters

# Support:
#   For questions or issues, please open an issue on the GitHub repository.


# Note:
# Refer to the individual scripts for the step by step understanding of the models.
# Refer to "vs_code_folder_structure.png" for the folder structure used in VS code for this analysis.
