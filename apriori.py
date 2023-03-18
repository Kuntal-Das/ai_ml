import itertools
import pandas as pd
import numpy as np
from multiprocessing import Pool


class Apriori:
    def __init__(self) -> None:
        self.i = 1

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
            count = 0
            items_indexs = []
            for combination in combinations:
                support, key = self.get_suport(combination)
                if (support / no_of_transactions >= minSup):
                    L[key] = support
                    if len(combination) >= self.i:
                        items_indexs.extend(combination)
                    count += 1

            if count == 0:
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
        key.extend([self.Items[item_indx] for item_indx in combination])
        return support, ", ".join(key)

    def print(self, L):
        string_out = [
            "Combinations\t:\tSupport",
        ]
        for key, value in L.items():
            string_out.append(f"{key}\t:\t{value}")

        return "\n".join(string_out)


if __name__ == '__main__':
    data = pd.read_csv('datasets/groceries - groceries.csv', dtype=str)

    # D = data.apply(lambda x: [y for y in x.dropna()], axis=0).tolist()
    D = data.values.tolist()
    apr = Apriori()
    F = apr.apriori(np.array(D), minSup=0.15)
    apr.print(F)
