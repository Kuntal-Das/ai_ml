import itertools
import pandas as pd
import numpy as np
from multiprocessing import Pool


class Apriori:
    # min_items to consider, no of process to speed up the processing
    def __init__(self, min_items=1, pool_nos=8):
        self.i = 1
        self.min_items = min_items
        self.pool_nos = pool_nos

    def fit(self, D, minSup):
        # unique items list                                
        Items = set()
        no_of_transactions, no_of_items = 0, 0
        for T in D:
            no_of_transactions += 1
            for i, I in enumerate(T):
                # ignoring the transaction count and NaN values
                if I is None or I == 'nan' or i == 0:
                    continue
                if I not in Items:
                    Items.add(I)
                    no_of_items += 1
                    
        # unique items list                                
        self.Items = np.array(list(Items))
        items_indexs = list(range(0, no_of_items))

        # mapping items with O and 1 based on the presence of the item
        new_data_list = []
        for r in D:
            new_data_list.append([1 if k in r else 0 for k in self.Items])
        self.new_data_list = np.array(new_data_list)

        L = {}

        while True:
            # geting all unique combinations with no of items per set being `i`
            combinations_set = set()
            for j in itertools.combinations(items_indexs, self.i):
                cmb = frozenset(j)
                if cmb not in combinations_set:
                    combinations_set.add(cmb)

            combinations = np.array(list(combinations_set))
            item_set_found = 0
            items_indexs = []
            
            # using pooling to speed up the compute utilizing more than one cpu cores
            with Pool(processes=self.pool_nos) as pool:
                # get no of occurances in the dataset
                combination_occurance_pairs = pool.map(self.get_occurance, combinations)

            for (cmb, occurance) in combination_occurance_pairs:
                key_list = []
                support = occurance / no_of_transactions
                # eleminating combinations based on min support value
                if (support >= minSup):
                    key_list.extend([self.Items[item_indx]
                                    for item_indx in cmb])
                    if len(cmb) >= self.i:
                        items_indexs.extend(cmb)
                    item_set_found += 1
                    # adding to result if it contains more than `min_items` items
                    if self.i >= self.min_items:
                        L[", ".join(key_list)] = support
                        
            # stop searching when no combination is found with min support and `i` items
            if item_set_found == 0:
                break
            self.i += 1
        return L

    def get_occurance(self, combination):
        occurance = 0
        key = []
        for row in self.new_data_list:
            count = 0
            for item_index, p in enumerate(row):
                if p == 1 and item_index in combination:
                    count += 1
            if count == self.i:
                occurance += 1
        return combination, occurance

    # print function for printing occurances 
    def print(self, L):
        print("{:<55} {:<10}".format('COMBINATIONS', 'SUPPORT'))
        for key, value in L.items():
            print("{:<55} {:<10}".format(key, value))


if __name__ == '__main__':
    data = pd.read_csv('datasets/groceries - groceries.csv', dtype=str)
    D = data.values.tolist()
    apr = Apriori(1, 16)
    F = apr.fit(np.array(D), minSup=0.045)
    apr.print(F)
