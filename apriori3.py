import pandas as pd
from itertools import combinations

# Load the dataset
df = pd.read_csv('datasets/groceries - groceries.csv', sep=',', header=None)

# Convert the dataset to a list of lists
records = []
for i in range(0, len(df)):
    records.append([str(df.values[i, j]) for j in range(0, len(df.columns))])

# Define a function to generate candidate itemsets of size k+1 from frequent itemsets of size k


def generate_candidates(frequent_itemsets_k, k):
    candidates = []
    for i in range(len(frequent_itemsets_k)):
        for j in range(i+1, len(frequent_itemsets_k)):
            items1 = frequent_itemsets_k[i][0:k]
            items2 = frequent_itemsets_k[j][0:k]
            if items1 == items2:
                candidate = sorted(list(set(items1) | set(
                    [frequent_itemsets_k[i][k], frequent_itemsets_k[j][k]])))
                if all([sorted(list(x)) in frequent_itemsets_k for x in combinations(candidate, k)]):
                    candidates.append(candidate)
    return candidates

# Define a function to find frequent itemsets with a minimum support


def find_frequent_itemsets(records, min_support):
    # Find all unique items and their counts
    item_counts = {}
    for record in records:
        for item in record:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1

    # Find frequent 1-itemsets
    frequent_itemsets = []
    for item in item_counts:
        if item_counts[item] >= len(records) * min_support:
            frequent_itemsets.append([item])

    # Find frequent itemsets of size k > 1
    k = 2
    while len(frequent_itemsets) > 0:
        # Generate candidate itemsets of size k+1 from frequent itemsets of size k
        candidates = generate_candidates(frequent_itemsets, k-1)
        # Count the support of each candidate itemset
        itemset_counts = {}
        for record in records:
            for candidate in candidates:
                if set(candidate).issubset(set(record)):
                    if tuple(candidate) in itemset_counts:
                        itemset_counts[tuple(candidate)] += 1
                    else:
                        itemset_counts[tuple(candidate)] = 1
        # Find frequent itemsets of size k
        frequent_itemsets = []
        for itemset in itemset_counts:
            support = itemset_counts[itemset] / len(records)
            if support >= min_support:
                frequent_itemsets.append(list(itemset))
        k += 1

    return frequent_itemsets

# Define a function to generate association rules from frequent itemsets


def generate_association_rules(frequent_itemsets, min_confidence):
    rules = []
    for itemset in frequent_itemsets:
        if len(itemset) > 1:
            for i in range(1, len(itemset)):
                for antecedent in combinations(itemset, i):
                    antecedent = sorted(list(antecedent))
                    consequent = sorted(list(set(itemset) - set(antecedent)))
                    support_antecedent = 0
                    support_itemset = 0
                    for record in records:
                        if set(antecedent).issubset(set(record)):
                            support_antecedent += 1
                        if set(itemset).issubset(set(record)):
                            support_itemset += 1
                        confidence = support_itemset / support_antecedent
                        lift = confidence / (support_itemset / len(records))
                        if confidence >= min_confidence:
                            rules.append(
                                (antecedent, consequent, confidence, lift))
    return rules

# Find frequent itemsets with a minimum support of 0.01
frequent_itemsets = find_frequent_itemsets(records, min_support=0.01)

# Generate association rules from frequent itemsets with a minimum confidence of 0.5
rules = generate_association_rules(frequent_itemsets, min_confidence=0.5)

# Print the top 10 rules sorted by lift
rules_sorted = sorted(rules, key=lambda x: x[3], reverse=True)
for antecedent, consequent, confidence, lift in rules_sorted[:10]:
print("{} => {} (Confidence: {:.3f}, Lift: {:.3f})".format(
", ".join(antecedent), ", ".join(consequent), confidence, lift))



