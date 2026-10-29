import pandas as pd
import os

# importing data_raw/bird_data_raw/bird_data_raw.csv into a DataFrame
df= pd.read_csv("data_raw/bird_data_raw/bird_data_raw.csv", sep="\t")

print(df[df["taxonRank"]== "FORM"].value_counts())
#print(df.head(5))
#print(df.shape)

#finding missing values
#print(df.isnull().sum().sort_values(ascending=False))

species_records_missing = df[df["species"].isnull()]
#print(species_records_missing[["scientificName", "genus", "family", "taxonRank"]])

#print(species_records_missing["taxonRank"].value_counts())

form_records = species_records_missing[
    species_records_missing["taxonRank"] == "FORM"
]
#print(form_records["scientificName"].value_counts())

birds_clean = df[df["taxonRank"] != "FORM"]
print(birds_clean.shape)

Mystery_bird = df[
    (df["taxonRank"] == "FORM") & (df["species"].notnull())
]
print(Mystery_bird[["scientificName", "species", "taxonRank"]])

print(birds_clean["species"].isnull().sum())

bird_species = birds_clean[birds_clean["species"].notnull()]
print(bird_species.shape)

#checking for duplicates
duplicates = bird_species["gbifID"].duplicated().sum()
print(duplicates)


#Final clean Dataframe
birds_final = bird_species[[
    "gbifID",
    "species",
    "scientificName",
    "family",
    "taxonRank",
    "decimalLatitude",
    "decimalLongitude",
    "coordinateUncertaintyInMeters",
    "eventDate",
    "datasetKey",
    "basisOfRecord"
]]

print(birds_final.shape)

birds_final.to_csv("data_processed/birds_clean.csv", index=False)