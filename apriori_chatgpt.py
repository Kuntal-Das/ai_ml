import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from collections import defaultdict
from multiprocessing import Pool


class Apriori:
    def __init__(self, min_items=1, pool_nos=8):
        self.min_items = min_items
        self.pool_nos = pool_nos

    def fit(self, D, minSup):
        # Convert the data to a sparse matrix
        sparse_data = csr_matrix((D == '1').astype(int))
        no_of_transactions, no_of_items = sparse_data.shape

        # Find the support count for single items
        item_count = sparse_data.sum(axis=0)
        frequent_items = item_count >= (minSup * no_of_transactions)
        frequent_itemsets = [(str(i), count)
                             for i, count in enumerate(item_count.tolist()[0])
                             if frequent_items[0, i]]

        # Use the Apriori property to find frequent itemsets of length greater than 1
        i = 2
        while len(frequent_itemsets) > 0:
            itemsets = defaultdict(int)
            for transaction in sparse_data:
                # Use the previous frequent itemsets to generate the candidate itemsets
                transaction_itemsets = set()
                for j, freq_set in enumerate(frequent_itemsets):
                    if freq_set[1] >= (minSup * no_of_transactions):
                        for k in range(j+1, len(frequent_itemsets)):
                            if frequent_itemsets[k][1] >= (minSup * no_of_transactions):
                                itemset = freq_set[0] + ',' + frequent_itemsets[k][0]
                                transaction_itemsets.add(itemset)

                # Count the support of candidate itemsets
                for itemset in transaction_itemsets:
                    itemsets[itemset] += 1

            # Filter candidate itemsets based on minimum support
            frequent_itemsets = [(itemset, count)
                                 for itemset, count in itemsets.items()
                                 if count >= (minSup * no_of_transactions)]
            
            # Add frequent itemsets to the result
            frequent_itemsets = sorted(frequent_itemsets, key=lambda x: x[1], reverse=True)
            frequent_itemsets = [(itemset.replace(',', ', '), count) for itemset, count in frequent_itemsets if itemset.count(',') == i-1 and i >= self.min_items]
            i += 1

        return frequent_itemsets

    # print function for printing occurances
    def print(self, L):
        print("{:<55} {:<10}".format('COMBINATIONS', 'SUPPORT'))
        for (items, support) in L:
            print("{:<55} {:<10}".format(items, support))


if __name__ == '__main__':
    data = pd.read_csv('datasets/groceries - groceries.csv', dtype=str)
    D = data.values[:, 1:]
    apr = Apriori(min_items=2, pool_nos=16)
    F = apr.fit(D, minSup=0.01)
    apr.print(F)
