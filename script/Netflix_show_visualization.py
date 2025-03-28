# ----Project Title: Netflix Data Analysis and Visualization using Python----------
# -------------------------------------------------------------------------------------------------------
# Created by: Victor Kadiri
# Date Created: 28th March 2025
# The Actual Analysis Starts from line 23
# The objective of the series of python script below is to perform a detailed analysis and visualisation of Netflix movies data. The procedures performed are as follows:
# - Data preparation and cleaning
# - Exploratory data analysis
# - Interactive visualizations
# - Report generation/saving outputs.

# Desired Output: 
# The outputs of the python model will be:
# 1. Renamed file: "Netflix_shows_movies.csv"
# 2. Clean version: "Netflix_shows_movies_CLEANED.csv"
# 3. Data exploration report: "Netflix_exploration_report.txt"
# 4. Visualization files in the visualizations subfolder
#         a. Python generated - Genre distribution plots (3 versions)
#         b. Python generated - Content ratings plots (3 versions)

## ------ The Actual Analysis Starts here ---------------
# Import required libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# ------------------------ 1. Data Preparation ----------------------------------------
#  This part of the code handles data loading and initial preparation.
def data_preparation():
    try:
        print("\n" + "="*50)
        print("DATA PREPARATION PHASE".center(50))
        print("="*50)
        
        # Get input and output paths from user
        print("\nPlease provide the following paths:")
        input_folder = input(r"Enter path to input folder (e.g., C:\Users\User\Downloads\BAN6420\Assignment_4\input): ").strip()
        output_folder = input(r"Enter path for output folder (e.g., C:\Users\User\Downloads\BAN6420\Assignment_4\output): ").strip()
        
        # Validate the input paths and return error if it does not exist
        if not os.path.exists(input_folder):
            raise FileNotFoundError("The specified input folder does not exist")
        # Validates and create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print("\n✓ Created output folder at:", output_folder)
        
        # Load Netflix data and assign a new name(rename) for the imported data
        input_path = os.path.join(input_folder, "netflix_data.csv")
        output_path = os.path.join(output_folder, "Netflix_shows_movies.csv")
        
        print("\n⏳ Loading Netflix data from:", input_path)
        df = pd.read_csv(input_path)
        
        # Offer option to save the renamed data
        save_choice = input("\nWould you like to save the renamed version of the data? (yes/no): ").lower()
        if save_choice == 'yes':
            df.to_csv(output_path, index=False)
            print(f"\n✓ Successfully saved renamed data to:\n  {output_path}")
        
        # Show the first 3 rows of the renamed data 
        print("\nSample of the loaded data (first 3 rows):")
        print(df.head(3))
        
        return df, output_folder
        # Handle errors during processing
    except Exception as e:
        print("\n" + "="*50)
        print("DATA PREPARATION ERROR".center(50))
        print("="*50)
        print(f"\n× Error occurred: {str(e)}")
        print("\nTroubleshooting tips:")
        print("- Check that the input folder path is correct")
        print("- Ensure netflix_data.csv exists in the input folder")
        print("- Verify you have read/write permissions")
        return None, None

# ------------------------ 2. Data Cleaning -----------------------------------------
#  This part of the code checks for data quality issues and handles data cleaning procedures such missing values.
def data_cleaning(df, output_folder):
    try:
        if df is None:
            raise ValueError("No data provided for cleaning")
            
        print("\n" + "="*50)
        print("DATA CLEANING PHASE".center(50))
        print("="*50)
        
        # Show initial data quality
        print("\nAssessing data quality before cleaning:")
        missing_data = df.isnull().sum()
        print("\nMissing values per column:")
        print(missing_data[missing_data > 0])
        
        # Clean data with clear explanations
        print("\n⏳ Cleaning data...")
        
        # Handle missing values
        df['director'].fillna('Unknown', inplace=True)
        df['cast'].fillna('Unknown', inplace=True)
        df['country'].fillna('Unknown', inplace=True)
        df['date_added'].fillna('Not Available', inplace=True)
        df['rating'].fillna('Not Rated', inplace=True)
        
        print("\n✓ Completed cleaning operations:")
        print("- Filled missing directors/cast/country with 'Unknown'")
        print("- Marked missing dates as 'Not Available'")
        print("- Marked missing ratings as 'Not Rated'")
        
        # Show cleaning results
        print("\nMissing values after cleaning:")
        print(df.isnull().sum())
        
        # Offer option to save cleaned data
        save_choice = input("\nWould you like to save the cleaned data? (yes/no): ").lower()
        if save_choice == 'yes':
            cleaned_path = os.path.join(output_folder, "Netflix_shows_movies_CLEANED.csv")
            df.to_csv(cleaned_path, index=False)
            print(f"\n✓ Successfully saved cleaned data to:\n  {cleaned_path}")
        
        # Show cleaned sample
        print("\nSample of cleaned data (first 3 rows):")
        print(df.head(3))
        
        return df
        #The code handles errors during processing
    except Exception as e:
        print("\n" + "="*50)
        print("DATA CLEANING ERROR".center(50))
        print("="*50)
        print(f"\n× Error occurred: {str(e)}")
        print("\nTroubleshooting tips:")
        print("- Verify the input data structure hasn't changed")
        print("- Check for unexpected null values")
        return None

# ------------------------ 3. Data Exploration -----------------------------------------
# The part of code performs data exploration analysis on the netflix data
def data_exploration(df, output_folder):
    try:
        if df is None:
            raise ValueError("No data provided for exploration")
            
        print("\n" + "="*50)
        print("DATA EXPLORATION PHASE".center(50))
        print("="*50)
        
        # The code initializes a report content to allow the appending of the exploration results.
        report_content = []
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_content.append(f"Netflix Content Analysis Report ({current_time})")
        report_content.append("="*50 + "\n")
        
        # 1. The code provides on overview of the dataset including basic Information
        report_content.append("1. DATASET OVERVIEW")
        report_content.append("-"*50)
        report_content.append(f"Total titles analyzed: {len(df):,}")
        report_content.append(f"Data columns available: {list(df.columns)}")
        report_content.append("\nThis dataset contains information about Netflix movies and TV shows, including:")
        report_content.append("- Title, director, and cast members")
        report_content.append("- Country of origin and content categories")
        report_content.append("- Release year and when added to Netflix")
        report_content.append("- Duration and age rating\n")
        
        # 2. This provides an analysis of Netflix Content Types
        report_content.append("2. CONTENT TYPE BREAKDOWN")
        report_content.append("-"*50)
        type_dist = df['type'].value_counts()
        report_content.append(f"Movies: {type_dist['Movie']:,} ({type_dist['Movie']/len(df)*100:.1f}%)")
        report_content.append(f"TV Shows: {type_dist['TV Show']:,} ({type_dist['TV Show']/len(df)*100:.1f}%)")
        report_content.append(f"\nFor every TV show, there are {type_dist['Movie']/type_dist['TV Show']:.1f} movies")
        report_content.append("\nThis shows Netflix's catalog leans more heavily toward movies than TV shows.\n")
        
        # 3. This provides an analysis of Netflix Yearly Releases
        report_content.append("3. RELEASE YEAR TRENDS")
        report_content.append("-"*50)
        recent_content = df[df['release_year'] >= 2010]
        old_content = df[df['release_year'] < 2010]
        report_content.append(f"Content released in 2010s/20s: {len(recent_content):,} ({len(recent_content)/len(df)*100:.1f}%)")
        report_content.append(f"Content released before 2010: {len(old_content):,} ({len(old_content)/len(df)*100:.1f}%)")
        report_content.append(f"\nNewest content: {df['release_year'].max()}")
        report_content.append(f"Oldest content: {df['release_year'].min()}")
        report_content.append("\nThis indicates Netflix offers a mix of recent and classic content.\n")
        
        # 4. This provides a detailed analysis of Netflix Content Ratings
        report_content.append("4. AGE RATINGS ANALYSIS")
        report_content.append("-"*50)
        ratings = df['rating'].value_counts().head(10)
        report_content.append("Most common content ratings:")
        report_content.append(str(ratings))
        
        # This provides a further analysis of Netflix Rating categories
        mature_ratings = ['TV-MA','R','NC-17','NR','UR']
        family_ratings = ['G', 'PG', 'TV-Y', 'TV-Y7', 'TV-G', 'TV-PG']
        general_ratings = ['PG-13', 'TV-14']
        
        mature_content = df[df['rating'].isin(mature_ratings)]
        family_content = df[df['rating'].isin(family_ratings)]
        general_content = df[df['rating'].isin(general_ratings)]
        
        report_content.append("\nContent Categories:")
        report_content.append(f"- Adult-oriented: {len(mature_content):,} titles ({len(mature_content)/len(df)*100:.1f}%)")
        report_content.append(f"- Family-friendly: {len(family_content):,} titles ({len(family_content)/len(df)*100:.1f}%)")
        report_content.append(f"- General audience: {len(general_content):,} titles ({len(general_content)/len(df)*100:.1f}%)")
        report_content.append("\nThis breakdown helps understand the target audience for Netflix's content.\n")
        
        # 5. This provides an analysis of Netflix geographic distribution
        report_content.append("5. GEOGRAPHIC DISTRIBUTION")
        report_content.append("-"*50)
        countries = df['country'].str.split(', ').explode().value_counts().head(10)
        report_content.append("Top 10 countries producing content:")
        report_content.append(str(countries))
        report_content.append("\nThis shows where Netflix sources most of its content from.\n")
        
        # 6. This provides an analysis of Netflix genre distribution
        report_content.append("6. GENRE DISTRIBUTION")
        report_content.append("-"*50)
        genres = df['listed_in'].str.split(', ').explode().value_counts().head(10)
        report_content.append("Top 10 most common genres/categories:")
        report_content.append(str(genres))
        report_content.append("\nThis reveals the most popular types of content on Netflix.\n")
        
        # This prints the report to console terminal area
        print("\n" + "\n".join(report_content[:50])) 
        print("\n... (additional report content available in saved file) ...")
        
        # This Saves the full report to the output folder 
        save_choice = input("\nWould you like to save the full analysis report? (yes/no): ").lower()
        if save_choice == 'yes':
            report_path = os.path.join(output_folder, "Netflix_exploration_report.txt")
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write("\n".join(report_content))
            print(f"\n✓ Successfully saved analysis report to:\n  {report_path}")
            print("\nThe report contains:")
            print("- Comprehensive analysis of Netflix's content catalog")
            print("- Key statistics and insights")
        
        return True
        # This helps to handle errors during processing
    except Exception as e:
        print("\n" + "="*50)
        print("DATA EXPLORATION ERROR".center(50))
        print("="*50)
        print(f"\n× Error occurred: {str(e)}")
        print("\nTroubleshooting tips:")
        print("- Verify the cleaned data structure")
        print("- Check for unexpected values in key columns")
        return False

# ------------------------ 4. Data Visualization -----------------------------------------
# This part of code creates visualizations for the Netflix data using a menu-driven interface. 
def create_visualizations(df, output_folder):
    try:
        # This code prepares netflix visualization data
        genres = df['listed_in'].str.split(', ').explode().value_counts().head(10)
        ratings = df['rating'].value_counts().head(8)
        
        # This code creates the visualization folder if it does not exist
        viz_folder = os.path.join(output_folder, "visualizations")
        os.makedirs(viz_folder, exist_ok=True)
        
        # This code helps to Configure the visualization style
        plt.style.use('seaborn')
        sns.set_palette("husl")
        plt.ion()  # Enable interactive mode
        
        # =======================================================================
        # 1. GENRE VISUALIZATION MENU
        # =======================================================================
        # This code displays all genre visualisation types and assign them separate figures for easy interaction
        def show_genre_plots():
            plt.close('all')
            
            # This code uses the Seaborn library to generate the visual
            plt.figure(1, figsize=(12,6))
            sns.barplot(x=genres.values, y=genres.index, palette="rocket")
            plt.title("Top 10 Genres on Netflix (Seaborn)", pad=20)
            plt.xlabel("Number of Titles", labelpad=10)
            plt.ylabel("Genre", labelpad=10)
            plt.tight_layout()
            plt.show()
            
            #  This code uses the Pyplot library to generate the visual
            plt.figure(2, figsize=(12,6))
            plt.barh(genres.index, genres.values, color='dodgerblue')
            plt.title("Top 10 Genres on Netflix (Pyplot)", pad=20)
            plt.xlabel("Number of Titles", labelpad=10)
            plt.ylabel("Genre", labelpad=10)
            plt.tight_layout()
            plt.show()
            
            #  This code uses the Matplotlib library to generate the visual.
            plt.figure(3, figsize=(12,6))
            bars = plt.barh(genres.index, genres.values, 
                          color='mediumseagreen', edgecolor='black')
            plt.bar_label(bars, padding=3)
            plt.title("Top 10 Genres on Netflix (Matplotlib)", pad=20)
            plt.xlabel("Number of Titles", labelpad=10)
            plt.ylabel("Genre", labelpad=10)
            plt.grid(axis='x', alpha=0.3)
            plt.tight_layout()
            plt.show()
        
        # This code saves all genre related visuals as PNG files"
        def save_genre_plots():
            # This uses the Seaborn library version
            plt.figure(figsize=(12,6))
            sns.barplot(x=genres.values, y=genres.index, palette="rocket")
            plt.title("Top 10 Genres on Netflix (Seaborn)", pad=20)
            plt.savefig(os.path.join(viz_folder, "genres_seaborn.png"), 
                      dpi=300, bbox_inches='tight')
            plt.close()
            
            # # This uses the Pyplot library version 
            plt.figure(figsize=(12,6))
            plt.barh(genres.index, genres.values, color='dodgerblue')
            plt.title("Top 10 Genres on Netflix (Pyplot)", pad=20)
            plt.savefig(os.path.join(viz_folder, "genres_pyplot.png"), 
                      dpi=300, bbox_inches='tight')
            plt.close()
            
            # This uses the Matplotlib library version
            plt.figure(figsize=(12,6))
            bars = plt.barh(genres.index, genres.values, 
                          color='mediumseagreen', edgecolor='black')
            plt.bar_label(bars, padding=3)
            plt.title("Top 10 Genres on Netflix (Matplotlib)", pad=20)
            plt.grid(axis='x', alpha=0.3)
            plt.savefig(os.path.join(viz_folder, "genres_matplotlib.png"), 
                      dpi=300, bbox_inches='tight')
            plt.close()
            
            print(f"\n✓ Saved genre plots to: {viz_folder}")
            print("   - genres_seaborn.png (Stylized bar plot)")
            print("   - genres_pyplot.png (Basic bar plot)")
            print("   - genres_matplotlib.png (Enhanced bar plot)")
        
        # This shows the Genre menu list for easy interaction
        while True:
            print("\n" + "="*50)
            print("GENRE DISTRIBUTION VISUALIZATIONS".center(50))
            print("="*50)
            print("\nSelect visualization option:")
            print("1. View Seaborn Version (Stylized Bar Plot)")
            print("2. View Pyplot Version (Basic Bar Plot)")
            print("3. View Matplotlib Version (Enhanced Bar Plot)")
            print("4. View All Versions")
            print("5. Save All Versions")
            print("6. Continue to Ratings Visualizations")
            print("="*50)
            #The user can select any of the 6 options above
            choice = input("\nEnter choice (1-6): ").strip()
            
            if choice == '1':
                plt.close('all')
                plt.figure(figsize=(12,6))
                sns.barplot(x=genres.values, y=genres.index, palette="rocket")
                plt.title("Top 10 Genres (Seaborn)", pad=20)
                plt.tight_layout()
                plt.show()
                input("\nPress Enter to return to menu...")
            elif choice == '2':
                plt.close('all')
                plt.figure(figsize=(12,6))
                plt.barh(genres.index, genres.values, color='dodgerblue')
                plt.title("Top 10 Genres (Pyplot)", pad=20)
                plt.tight_layout()
                plt.show()
                input("\nPress Enter to return to menu...")
            elif choice == '3':
                plt.close('all')
                plt.figure(figsize=(12,6))
                bars = plt.barh(genres.index, genres.values, 
                              color='mediumseagreen', edgecolor='black')
                plt.bar_label(bars, padding=3)
                plt.title("Top 10 Genres (Matplotlib)", pad=20)
                plt.grid(axis='x', alpha=0.3)
                plt.tight_layout()
                plt.show()
                input("\nPress Enter to return to menu...")
            elif choice == '4':
                show_genre_plots()
                input("\nPress Enter to return to menu...")
            elif choice == '5':
                save_genre_plots()
            elif choice == '6':
                plt.close('all')
                break
            else:
                print("\n⚠️ Invalid input. Please enter 1-6")
        
        # =======================================================================
        # 2. RATINGS VISUALIZATION MENU (UPDATED)
        # =======================================================================
        #This part of the code displays all ratings related visualizations as a bar chart"""
        def show_rating_plots():
            plt.close('all')
            
            # # This uses the Seaborn library version- Bar Chart
            plt.figure(1, figsize=(10,6))
            sns.countplot(y='rating', data=df, order=ratings.index,
                         palette="viridis")
            plt.title("Content Ratings Distribution (Seaborn)", pad=20)
            plt.xlabel("Number of Titles", labelpad=10)
            plt.ylabel("Rating", labelpad=10)
            plt.tight_layout()
            plt.show()
            
            # This uses the Pyplot library version- Bar Chart
            plt.figure(2, figsize=(10,6))
            plt.bar(ratings.index, ratings.values, color='skyblue', edgecolor='black')
            plt.title("Content Ratings Distribution (Pyplot)", pad=20)
            plt.xlabel("Rating", labelpad=10)
            plt.ylabel("Number of Titles", labelpad=10)
            plt.xticks(rotation=45)
            plt.grid(axis='y', alpha=0.3)
            plt.tight_layout()
            plt.show()
            
            # This uses the Matplotlib library version
            plt.figure(3, figsize=(10,6))
            bars = plt.bar(ratings.index, ratings.values,
                         color='tomato', width=0.7, edgecolor='black')
            plt.bar_label(bars, padding=3)
            plt.title("Content Ratings Distribution (Matplotlib)", pad=20)
            plt.xlabel("Rating", labelpad=10)
            plt.ylabel("Number of Titles", labelpad=10)
            plt.grid(axis='y', alpha=0.3)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        
        def save_rating_plots():
            # This Saves all ratings related visuals to the output location
            # This uses the Seaborn library version
            plt.figure(figsize=(10,6))
            sns.countplot(y='rating', data=df, order=ratings.index,
                         palette="viridis")
            plt.title("Content Ratings Distribution (Seaborn)", pad=20)
            plt.savefig(os.path.join(viz_folder, "ratings_seaborn.png"), 
                       dpi=300, bbox_inches='tight')
            plt.close()
            
            # # This uses the Pyplot library version - Bar Chart
            plt.figure(figsize=(10,6))
            plt.bar(ratings.index, ratings.values, color='skyblue', edgecolor='black')
            plt.title("Content Ratings Distribution (Pyplot)", pad=20)
            plt.xlabel("Rating", labelpad=10)
            plt.ylabel("Number of Titles", labelpad=10)
            plt.xticks(rotation=45)
            plt.grid(axis='y', alpha=0.3)
            plt.savefig(os.path.join(viz_folder, "ratings_pyplot.png"), 
                       dpi=300, bbox_inches='tight')
            plt.close()
            
            #  This uses the Matplotlib library version - Bar Chart
            plt.figure(figsize=(10,6))
            bars = plt.bar(ratings.index, ratings.values,
                         color='tomato', width=0.7, edgecolor='black')
            plt.bar_label(bars, padding=3)
            plt.title("Content Ratings Distribution (Matplotlib)", pad=20)
            plt.grid(axis='y', alpha=0.3)
            plt.xticks(rotation=45)
            plt.savefig(os.path.join(viz_folder, "ratings_matplotlib.png"), 
                       dpi=300, bbox_inches='tight')
            plt.close()
            
            print(f"\n✓ Saved ratings plots to: {viz_folder}")
            print("   - ratings_seaborn.png (Count plot)")
            print("   - ratings_pyplot.png (Bar chart)")
            print("   - ratings_matplotlib.png (Enhanced bar chart)")
        
        # This helps the user to navigate and interact with the Ratings visualization menu
        while True:
            print("\n" + "="*50)
            print("CONTENT RATINGS VISUALIZATIONS".center(50))
            print("="*50)
            print("\nSelect visualization option:")
            print("1. View Seaborn Version (Count Plot)")
            print("2. View Pyplot Version (Bar Chart)")
            print("3. View Matplotlib Version (Enhanced Bar Chart)")
            print("4. View All Versions")
            print("5. Save All Versions")
            print("6. Finish Visualizations")
            print("="*50)
            # Allow users to select the desired task option
            choice = input("\nEnter choice (1-6): ").strip()
            
            if choice == '1':
                plt.close('all')
                plt.figure(figsize=(10,6))
                sns.countplot(y='rating', data=df, order=ratings.index,
                             palette="viridis")
                plt.title("Ratings Distribution (Seaborn)", pad=20)
                plt.tight_layout()
                plt.show()
                input("\nPress Enter to return to menu...")
            elif choice == '2':
                plt.close('all')
                plt.figure(figsize=(10,6))
                plt.bar(ratings.index, ratings.values, color='skyblue', edgecolor='black')
                plt.title("Ratings Distribution (Pyplot)", pad=20)
                plt.xlabel("Rating", labelpad=10)
                plt.ylabel("Number of Titles", labelpad=10)
                plt.xticks(rotation=45)
                plt.grid(axis='y', alpha=0.3)
                plt.tight_layout()
                plt.show()
                input("\nPress Enter to return to menu...")
            elif choice == '3':
                plt.close('all')
                plt.figure(figsize=(10,6))
                bars = plt.bar(ratings.index, ratings.values,
                             color='tomato', width=0.7, edgecolor='black')
                plt.bar_label(bars, padding=3)
                plt.title("Ratings Distribution (Matplotlib)", pad=20)
                plt.grid(axis='y', alpha=0.3)
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
                input("\nPress Enter to return to menu...")
            elif choice == '4':
                show_rating_plots()
                input("\nPress Enter to return to menu...")
            elif choice == '5':
                save_rating_plots()
            elif choice == '6':
                plt.close('all')
                print("\n" + "="*50)
                print("VISUALIZATION COMPLETE".center(50))
                print("="*50)
                print("\n✓ All visualizations generated successfully")
                print(f"✓ Files saved to: {viz_folder}")
                break
            else:
                print("\n⚠️ Invalid input. Please enter 1-6")
                
        return True
        #This handles error during processing
    except Exception as e:
        print("\n" + "="*50)
        print("VISUALIZATION ERROR".center(50))
        print("="*50)
        print(f"\n× Error occurred: {str(e)}")
        print("\nTroubleshooting tips:")
        print("- Check matplotlib/seaborn are properly installed")
        print("- Verify the data contains expected columns")
        print("- Try reducing the figure sizes if memory issues occur")
        return False

# ------------------------ Main Function -----------------------------------------
# This is the main function that runs the entire Nexflix data analysis workflow.
def main():
    try:
        print("\n" + "="*50)
        print("NETFLIX DATA ANALYSIS TOOL".center(50))
        print("="*50)
        print("\nThis tool will guide you through:")
        print("- Data preparation and cleaning")
        print("- Exploratory analysis")
        print("- Interactive visualizations")
        print("="*50)
        
        # Step 1: Data Preparation
        print("\nSTEP 1: DATA PREPARATION")
        netflix_data, output_folder = data_preparation()
        if netflix_data is None:
            raise RuntimeError("Cannot proceed without data")
        
        # Step 2: Data Cleaning
        print("\nSTEP 2: DATA CLEANING")
        cleaned_data = data_cleaning(netflix_data, output_folder)
        if cleaned_data is None:
            raise RuntimeError("Cannot proceed with dirty data")
        
        # Step 3: Data Exploration
        print("\nSTEP 3: DATA EXPLORATION")
        if not data_exploration(cleaned_data, output_folder):
            raise RuntimeError("Exploration phase encountered issues")
        
        # Step 4: Data Visualization
        viz_choice = input("\nWould you like to create visualizations? (yes/no): ").lower()
        if viz_choice == 'yes':
            print("\nSTEP 4: DATA VISUALIZATION")
            if not create_visualizations(cleaned_data, output_folder):
                raise RuntimeError("Visualization phase encountered issues")
        
        # Completion message
        print("\n" + "="*50)
        print("ANALYSIS COMPLETE".center(50))
        print("="*50)
        print("\n✓ Successfully completed all analysis steps!")
        print(f"\nOutput files saved to: {output_folder}")
        print("\nThank you for using the Netflix Data Analysis Tool!")
        # Helps to handle error during processing
    except Exception as e:
        print("\n" + "="*50)
        print("ANALYSIS ERROR".center(50))
        print("="*50)
        print(f"\n× Critical error occurred: {str(e)}")
        print("\nPlease check:")
        print("- Your input data format")
        print("- System resources")
        print("- Error messages above")
        print("\nYou may need to restart the analysis.")

if __name__ == "__main__":
    main()