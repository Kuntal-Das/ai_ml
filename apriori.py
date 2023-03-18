import itertools
import pandas as pd
import numpy as np
from multiprocessing import Pool


class Apriori:
    def __init__(self, pool_nos=8) -> None:
        self.i = 1
        self.pool_nos = pool_nos

    def apriori(self, D, minSup):
        Transactions = {}
        Items = set()
        no_of_transactions, no_of_items = 0, 0
        for T in D:
            no_of_transactions += 1
            for i, I in enumerate(T):
                if I is None or I == 'nan' or i == 0:
                    continue
                if I in Items:
                    Transactions[I] += 1
                else:
                    Items.add(I)
                    no_of_items += 1
                    Transactions[I] = 1

        self.Items = np.array(list(Items))
        items_indexs = list(range(0, no_of_items))

        new_data_list = []
        for r in D:
            new_data_list.append([1 if k in r else 0 for k in self.Items])
        self.new_data_list = np.array(new_data_list)

        C = {}
        L = {}

        c1_len = 0
        while True:
            combinations_set = set()
            for j in itertools.combinations(items_indexs, self.i):
                cmb = frozenset(j)
                if cmb not in combinations_set:
                    combinations_set.add(cmb)

            combinations = np.array(list(combinations_set))
            item_set_found = 0
            items_indexs = []
            with Pool(processes=self.pool_nos) as pool:
                combination_occurance_pairs = pool.map(
                    self.get_suport, combinations)

            for (cmb, occurance) in combination_occurance_pairs:
                key_list = []
                support = occurance / no_of_transactions
                if (support >= minSup):
                    key_list.extend([self.Items[item_indx]
                                    for item_indx in cmb])
                    L[", ".join(key_list)] = support
                    if len(cmb) >= self.i:
                        items_indexs.extend(cmb)
                    item_set_found += 1
            if item_set_found == 0:
                break
            self.i += 1
        return L

    def get_suport(self, combination):
        support = 0
        key = []
        for row in self.new_data_list:
            count = 0
            for item_index, p in enumerate(row):
                if p == 1 and item_index in combination:
                    count += 1
            if count == self.i:
                support += 1
        return combination, support

    def print(self, L):
        print("{:<30} {:<10}".format('Combinations', 'Support'))
        for key, value in L.items():
            print("{:<30} {:<10}".format(key, value))


if __name__ == '__main__':
    data = pd.read_csv('datasets/groceries - groceries.csv', dtype=str)

    # D = data.apply(lambda x: [y for y in x.dropna()], axis=0).tolist()
    D = data.values.tolist()
    apr = Apriori(16)
    F = apr.apriori(np.array(D), minSup=0.03)
    apr.print(F)
