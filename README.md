
# Obesity Level Analysis

This repository contains the analysis of obesity levels in individuals from Mexico, Peru, and Colombia, based on their eating habits and physical conditions. The analysis is performed on a dataset containing 17 attributes and 2111 records.

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset Description](#dataset-description)
3. [Data Preprocessing](#data-preprocessing)
4. [Feature Engineering](#feature-engineering)
5. [Exploratory Data Analysis](#exploratory-data-analysis)
6. [Conclusions](#conclusions)
7. [Usage](#usage)

## Introduction
The objective of this analysis is to explore the relationship between eating habits, physical conditions, and obesity levels.

## Dataset Description
The dataset includes the following attributes:
- Gender
- Age
- Height
- Weight
- Family history with overweight
- Frequent consumption of high caloric food (FAVC)
- Frequency of consumption of vegetables (FCVC)
- Number of main meals (NCP)
- Consumption of food between meals (CAEC)
- Consumption of water daily (CH2O)
- Consumption of alcohol (CALC)
- Calories consumption monitoring (SCC)
- Physical activity frequency (FAF)
- Time using technology devices (TUE)
- Transportation used (MTRANS)
- Obesity level (NObesity)

## Data Preprocessing
The data preprocessing steps include:
1. Loading the data
2. Cleaning the data
3. Handling duplicates
4. Handling missing values

## Feature Engineering
A new feature 'Weight_Category' is created based on BMI calculations to categorize weight into classes like Underweight, Normal, Overweight, and various levels of Obesity.

## Exploratory Data Analysis
Exploratory Data Analysis (EDA) includes:
- Distribution plots for Age, Height, and Weight
- Count plots for categorical variables
- Correlation matrix

## Conclusions
The analysis highlights the strong influence of both genetic factors and lifestyle choices on obesity levels. Public health interventions focusing on improving dietary habits and increasing physical activity are recommended.

## Usage
To run the analysis, clone the repository and follow these steps:

1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the Jupyter notebook:
    ```bash
    jupyter notebook notebooks/analysis.ipynb
    ```
