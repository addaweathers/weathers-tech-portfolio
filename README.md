# Diabetes Prediction Using Hospital Data

A machine learning project analyzing hospital encounter data to predict diabetes diagnoses, demonstrating data cleaning, SQL transformation, and the importance of feature engineering in healthcare prediction models.

## Dataset

**Source:** [Diabetes 130-US Hospitals (1999-2008)](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)

**Key Challenge:** The dataset contains limited variables traditionally associated with diabetes diagnosis (primarily administrative and encounter-based features rather than clinical measurements like glucose levels or BMI).

## Project Overview

This assignment explored the end-to-end process of building a predictive model for diabetes using hospital encounter data. While the final model performed poorly, the project provided valuable learning opportunities in data preprocessing, SQL operations, and understanding data leakage.

## Tools & Technologies

- **Data Cleaning:** SQLite3 (Ubuntu terminal)
- **Modeling:** RapidMiner
- **Languages:** SQL
- **Key Techniques:** Data transformation, missing value imputation, ICD-9 code extraction

## Methodology

### Data Cleaning & Transformation (SQL)

The data cleaning process involved systematic handling of missing values and irrelevant features:

1. **Initial Assessment** (Figure A1-A2)
   - Extracted column names
   - Ran SQL script to identify missing values by column with percentages (Code B1)

2. **Column Removal** (Figure A3)
   - Dropped `weight` column (97%+ missing values)
   - Removed `patient_nbr` and `encounter_id` (patient-specific identifiers that wouldn't generalize)

3. **Missing Value Imputation** (Figure A4-A6)
   - Replaced missing `race` with "Race Unknown"
   - Replaced missing `medical_specialty` with "Specialty Unknown"
   - Replaced missing `payer_code` with "Payer Code Unknown"

4. **Diagnosis Data Processing** (Figure A7-A8)
   - Deleted rows with missing values in diagnosis columns (`diag_1`, `diag_2`, `diag_3`)
   - Extracted 250-series ICD-9 codes to identify diabetes cases (Code B2)
   - Confirmed no ICD-10 codes present (appropriate for dataset timeframe)

5. **Label Creation** (Figure A9-A10)
   - Created `diabetic_binary` column as target variable
   - Exported cleaned dataset as CSV

### Exploratory Data Analysis (RapidMiner)

Visual analysis revealed important patterns in the data:

- **Figure C1:** Confirmed successful removal of missing values
- **Figure C2:** Distribution of time in hospital (histogram)
- **Figure C3:** Distribution of number of medications (boxplot)
- **Figure C4:** Total diagnoses by race (horizontal bar chart)
- **Figure C5:** Race distribution (pie chart showing Caucasian majority)
- **Figure C6:** Time in hospital comparison
  - Key insight: Longest stays typically occurred in non-diabetic patients
  - Diabetic patients showed more frequent short-term stays

### Modeling Attempts

#### Random Forest (Figure C7)
- Initial model performed poorly
- Limited predictive power from available features

#### Logistic Regression (Figure C8)
- **Initial Result:** 99% specificity - appeared highly successful
- **Critical Error Identified:** Data leakage
  - Diagnosis columns (`diag_1`, `diag_2`, `diag_3`) were used as features
  - These columns were the source of the target variable, causing overfitting
  
- **After Correction:** Model performed no better than chance
  - Removing diagnosis columns eliminated the data leakage
  - Remaining features (hospital stay duration, medication count, etc.) insufficient for prediction

## Key Learnings

### Technical Skills
- SQLite3 command-line operations in Ubuntu
- SQL-based missing value analysis and handling
- ICD-9 code extraction and filtering (250-series)
- Data transformation workflows

### Machine Learning Concepts
- **Data Leakage:** Using features derived from the target variable leads to artificially inflated performance
- **Feature Importance:** Administrative/encounter data alone cannot capture the clinical relationship with diabetes
- **Model Limitations:** Sometimes datasets simply lack the necessary information for accurate prediction

### Domain Insights
- Hospital administrative data (length of stay, medication count) are poor proxies for diabetes diagnosis
- Effective diabetes prediction requires clinical measurements (glucose, A1C, BMI) not present in this dataset
- High model performance should always be validated for potential data leakage

## Repository Contents

- **SQL Scripts:** 
  - Code B1: Missing value analysis
  - Code B2: ICD-9 code extraction and diabetes identification
- **Screenshots:** Complete workflow documentation (Figures A1-A10, C1-C8)
- **Cleaned Data:** Processed CSV file

## Conclusion

While the model ultimately failed to predict diabetes better than random chance, this project successfully demonstrated the critical importance of:
1. Systematic data cleaning and preprocessing
2. Identifying and eliminating data leakage
3. Understanding the limitations of available features for the prediction task
4. The necessity of domain-appropriate features (clinical measurements) for medical predictions

**Main Takeaway:** Not all datasets are suitable for all prediction tasks. The absence of clinical biomarkers made diabetes prediction from this administrative data fundamentally challenging, regardless of modeling approach.




