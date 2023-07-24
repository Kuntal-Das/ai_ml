def load_dataset():
    # Replace this function with loading your own dataset
    dataset = [
        [1, 3, 4],
        [2, 3, 5],
        [1, 2, 3, 5],
        [2, 5]
    ]
    return dataset

def create_candidate_itemsets(itemset, length):
    return set([item1.union(item2) for item1 in itemset for item2 in itemset if len(item1.union(item2)) == length])

def support_count(itemset, dataset):
    count = 0
    for transaction in dataset:
        if itemset.issubset(transaction):
            count += 1
    return count

def frequent_itemsets(dataset, min_support):
    itemset = [frozenset([item]) for item in set(item for transaction in dataset for item in transaction)]
    itemset = sorted(itemset)
    length = 1
    while itemset:
        candidate_itemset = create_candidate_itemsets(itemset, length + 1)
        itemset_to_remove = []
        for item in candidate_itemset:
            support = support_count(item, dataset)
            if support >= min_support:
                print(item, support)
            else:
                itemset_to_remove.append(item)
        itemset = [item for item in itemset if item not in itemset_to_remove]
        length += 1

if __name__ == "__main__":
    dataset = load_dataset()
    min_support = 2
    frequent_itemsets(dataset, min_support)
