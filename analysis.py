import pandas as pd

#Load Dataset
df = pd.read_csv("Titanic-Dataset.csv")

#Dataset Overview
print(f"Shape:{df.shape}")
print(f"Columns:{df.columns}\n")
print("Dataset Head - This shows the first 5 rows of the dataset")
print(df.head(5), "\n")
print("Dataset Tail - This shows the last 5 rows of the dataset")
print(df.tail(5), "\n")
print("Descriptive Statistics -")
print(df.describe(), "\n")
print("Null value count per column - ")
print(df.isnull().sum(), "\n")

#Data Cleaning
df.dropna(subset=['Age'], inplace=True)
df.drop(columns=["Cabin"], inplace=True)
df["Embarked"] = df["Embarked"].fillna('C')
print("After Cleaning -")
print(df.isnull().sum(), "\n")

#Data Analysis
print("---------Titanic Analysis---------")
print("Average Fare -")
PassengersInFC = df[df["Pclass"] == 1]["Fare"].count()
avgFareFC = df[df["Pclass"] == 1]["Fare"].sum()//PassengersInFC
print(f"First Class: {avgFareFC}")
PassengersInSC = df[df["Pclass"] == 2]["Fare"].count()
avgFareSC = df[df["Pclass"] == 2]["Fare"].sum()//PassengersInSC
print(f"Second Class: {avgFareSC}")
PassengersInTC = df[df["Pclass"] == 3]["Fare"].count()
avgFareTC = df[df["Pclass"] == 3]["Fare"].sum()//PassengersInTC
print(f"Third Class: {avgFareTC}\n")

sTotal = df[df["Survived"] == 1]["Survived"].count()
print(f"Passengers Who Survived - {sTotal}")
sMales = df[df["Survived"] == 1]
sMalesCount = sMales[sMales["Sex"] == "male"]["Sex"].count()
print(f"Male: {sMalesCount} ({sMalesCount/sTotal*100:.2f}%)")
print(f"Female: {sTotal-sMalesCount} ({(sTotal - sMalesCount)/sTotal*100:.2f}%)")
firstClassPassengers = df[(df["Pclass"] == 1) & (df["Survived"] == 1)]["Pclass"].count()
print(f"In first class: {firstClassPassengers}")
secondClassPassengers = df[(df["Pclass"] == 2) & (df["Survived"] == 1)]["Pclass"].count()
print(f"In second class: {secondClassPassengers}")
thirdClassPassengers = sTotal - firstClassPassengers - secondClassPassengers
print(f"In third class: {thirdClassPassengers}")
PoEC = df[(df["Embarked"] == 'C') & (df["Survived"] == 1)]["Embarked"].count()
print(f"Embarked from Cherbourg: {PoEC}")
PoEQ = df[(df["Embarked"] == 'Q') & (df["Survived"] == 1)]["Embarked"].count()
print(f"Embarked from Queenstown: {PoEQ}")
PoES = df[(df["Embarked"] == 'S') & (df["Survived"] == 1)]["Embarked"].count()
print(f"Embarked from Southampton: {PoES}\n")

nsTotal = df[df["Survived"] == 0]["Survived"].count()
print(f"Passengers Who Perished - {nsTotal}")
nsMales = df[df["Survived"] == 0]
nsMalesCount = nsMales[nsMales["Sex"] == "male"]["Sex"].count()
print(f"Male: {nsMalesCount} ({nsMalesCount/nsTotal*100:.2f}%)")
print(f"Female: {nsTotal-nsMalesCount} ({(nsTotal - nsMalesCount)/nsTotal*100:.2f}%)")
nsfirstClassPassengers = df[(df["Pclass"] == 1) & (df["Survived"] == 0)]["Pclass"].count()
print(f"In first class: {nsfirstClassPassengers}")
nsSecondClassPassengers = df[(df["Pclass"] == 2) & (df["Survived"] == 0)]["Pclass"].count()
print(f"In second class: {nsSecondClassPassengers}")
nsThirdClassPassengers = nsTotal - nsfirstClassPassengers - nsSecondClassPassengers
print(f"In third class: {nsThirdClassPassengers}")
nsPoEC = df[(df["Embarked"] == 'C') & (df["Survived"] == 0)]["Embarked"].count()
print(f"Embarked from Cherbourg: {nsPoEC}")
nsPoEQ = df[(df["Embarked"] == 'Q') & (df["Survived"] == 0)]["Embarked"].count()
print(f"Embarked from Queenstown: {nsPoEQ}")
nsPoES = df[(df["Embarked"] == 'S') & (df["Survived"] == 0)]["Embarked"].count()
print(f"Embarked from Southampton: {nsPoES}\n")
