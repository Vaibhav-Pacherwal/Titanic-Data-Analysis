# Titanic Data Analysis

## 🚢 Project Overview
This project demonstrates **data analysis using Pandas** on the famous **Titanic dataset**.  
The goal is to explore, clean, and analyze the dataset to uncover **insights about passenger demographics, fares, survival rates, and embarkation points**.

This project is entirely implemented using **Python and Pandas**, without any visualization libraries.

---

## 📁 Dataset
- Source: Kaggle ([Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data))  
- Files used:
  - `titanic.csv` (raw dataset)

- Dataset contains **891 passengers** with the following columns:
  - `PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `Age`, `SibSp`, `Parch`, `Ticket`, `Fare`, `Cabin`, `Embarked`

---

## 🧰 Tools Used
- Python 3.x  
- Pandas  
- NumPy (optional, for numerical operations)

---

## 📝 Project Workflow

### 1️⃣ Data Loading
- Loaded the CSV dataset into a Pandas DataFrame.
- Checked the **shape**, **columns**, and **data types**.

### 2️⃣ Data Exploration
- Examined **head** and **tail** of the dataset.
- Generated **descriptive statistics** using `describe()`.
- Counted **null values** per column.

### 3️⃣ Data Cleaning
- Handled missing values:
  - `Age` → filled with mean
  - `Embarked` → filled with mode
  - `Cabin` → dropped (too many missing values)
- Removed duplicates if any.
- Converted datatypes as needed.

### 4️⃣ Data Analysis
- Average fare per class:
  - First Class: 87.0  
  - Second Class: 21.0  
  - Third Class: 13.0  
- Survival Analysis:
  - **Passengers Who Survived**: 290
    - Male: 93 (32.07%)  
    - Female: 197 (67.93%)  
    - First Class: 122  
    - Second Class: 83  
    - Third Class: 85  
    - Embarked from Cherbourg: 81, Queenstown: 8, Southampton: 201
  - **Passengers Who Perished**: 424
    - Male: 360 (84.91%)  
    - Female: 64 (15.09%)  
    - First Class: 64  
    - Second Class: 90  
    - Third Class: 270  
    - Embarked from Cherbourg: 51, Queenstown: 20, Southampton: 353

---

## 📌 Key Insights
- Survival rate for females is significantly higher than males.  
- Passengers in **first class** had the highest survival rate.  
- Most passengers embarked from **Southampton**.  
- Fare distribution varies widely across classes, with first class paying the most.

---

## 🛠 How to Run
1. Clone this repository:
   ```bash
   git clone <https://github.com/Vaibhav-Pacherwal/Titanic-Data-Analysis>
