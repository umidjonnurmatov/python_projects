Data Processing Pipeline


1. Data Cleaning Steps
Country Filtering: Standardized to 65 countries across all datasets

Missing Values: Replaced ".." and other placeholders with NaN

Year Range: Filtered to 2010-2024 period

Format Standardization: Converted all datasets to consistent wide format

2. Key Transformations
MultiIndex Resolution: Flattened complex column structures

Agriculture Employment Share: Calculated from total and agriculture employment data

Country Name Cleaning: Removed bracket-enclosed codes (e.g., "Albania [008]" → "Albania")

3. Data Quality Checks
Missing value analysis by variable and country

Consistency checks across merged datasets

Validation of calculated metrics (e.g., agriculture share between 0-100%)