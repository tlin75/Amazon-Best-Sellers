# Amazon Bestselling Books Analysis (2009–2019)

This project analyses the top 50 bestselling books on Amazon each year from 2009 to 2019. The dataset includes information about book titles, authors, ratings, prices, and genres. The goal is to explore trends in book popularity, author success, and genre performance over the decade.

## Dataset

- **Source**: [Kaggle - Amazon Top 50 Bestselling Books 2009–2019](https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019)
- **Rows**: 550 entries (50 books per year × 11 years)
- **Columns**: 
  - `Title`: Name of the book
  - `Author`: Author of the book
  - `Genre`: Fiction or Non-Fiction
  - `Price`: Price of the book in USD
  - `Rating`: User rating (out of 5)
  - `Reviews`: Number of customer reviews
  - `Publication Year`: Year the book was published

## Data Cleaning

- Removed duplicate entries
- Renamed columns for clarity (`Name` → `Title`, `Year` → `Publication Year`, `User Rating` → `Rating`)
- Converted `Price` to float type for numerical analysis

## Analysis

### 1. Author Popularity
Counted how many times each author appeared in the bestsellers list to identify the most popular authors.

### 2. Average Rating by Genre
Calculated the average user rating for books in each genre (Fiction vs. Non-Fiction).

## Results

- **Top Authors** (by number of appearances): Exported to `top_authors.csv`
- **Average Rating by Genre**: Exported to `avg_rating_by_genre.csv`

## Tools Used

- Python (pandas)
- VS Code

## How to Run

1. Install dependencies:
    pip3 install pandas
2. Run main file:
    python best-sellers.py