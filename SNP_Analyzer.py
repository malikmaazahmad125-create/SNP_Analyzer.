import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("." * 30)

print("SNP DETECTION ANALYZER")

print("." * 30)

reference = "ATGCGATCGATCG"

sample = "ATGCAATCGATCG"

print("\n", "." * 10, "SNP DETECTION", "." * 10)

for i in range(len(reference)):

    if reference[i] != sample[i]:

        print("SNP found at point", i)


print("\n", "." * 10, "USING FUNCTIONS", "." * 10)


def find_snp(reference, sample):

    snp = []

    for i in range(len(reference)):

        if reference[i] != sample[i]:

            snp.append(i)

    return snp


result = find_snp(reference, sample)

print("SNP found at point list is:", result)


print("\n", "." * 10, "NUMPY BOOLEAN MASKING", "." * 10)

reference_array = np.array(list(reference))

sample_array = np.array(list(sample))

mask = reference_array != sample_array

print("BOOLEAN MASK:", mask)

print("SNP POSITIONS:", np.where(mask)[0])


print("\n", "." * 10, "CREATING SNP DATAFRAME", "." * 10)

snp_positions = np.where(mask)[0]

snp_data = []

for position in snp_positions:

    snp_data.append({

        "Position": position,

        "Reference": reference[position],

        "Sample": sample[position]

    })


dataframe = pd.DataFrame(snp_data)

print("SNP DATAFRAME IS:\n", dataframe)


filtered_dataframe = dataframe[dataframe["Position"] > 5]

print("FILTERED DATAFRAME IS:\n", filtered_dataframe)


dataframe["Change"] = dataframe["Reference"] + ">" + dataframe["Sample"]

frequency = dataframe["Change"].value_counts()

print("SNP FREQUENCY IS:\n", frequency)


snp_types = dataframe["Sample"].value_counts()

print("SAMPLE NUCLEOTIDES FREQUENCY IS:\n", snp_types)


print("\n" + "." * 10, "SNP SUMMARY", "." * 10)

print("Total SNPs:", len(dataframe))

print("Unique SNP Changes:", dataframe["Change"].nunique())

print("Most Frequent Change:", frequency.idxmax())

print("Most Frequent Change Count:", frequency.max())


# ==========================================
# VISUALIZATION 1
# ==========================================

print("\n" + "." * 10, "SNP CHANGE VISUALIZATION", "." * 10)

plt.figure(figsize=(7, 5))

plt.bar(frequency.index, frequency.values)

plt.title("SNP Change Frequency")

plt.xlabel("SNP Change")

plt.ylabel("Frequency")

plt.tight_layout()

plt.show()


# ==========================================
# VISUALIZATION 2
# ==========================================

print("\n" + "." * 10, "NUCLEOTIDE FREQUENCY VISUALIZATION", "." * 10)

plt.figure(figsize=(7, 5))

plt.bar(snp_types.index, snp_types.values)

plt.title("Sample Nucleotide Frequency")

plt.xlabel("Nucleotide")

plt.ylabel("Frequency")

plt.tight_layout()

plt.show()
