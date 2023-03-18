def apriori(transactions, min_support):
    """
    Implementation of Apriori algorithm to find frequent itemsets.

    Parameters:
    transactions (list of lists): A list of transactions. Each transaction is a list of items.
    min_support (float): The minimum support threshold.

    Returns:
    list of sets: A list of frequent itemsets.
    """
    # Get all unique items in transactions
    unique_items = set(
        item for transaction in transactions for item in transaction)

    # Initialize the frequent itemsets
    frequent_itemsets = []
    one_itemsets = get_one_itemsets(transactions, unique_items, min_support)
    frequent_itemsets.extend(one_itemsets)

    k = 2
    while True:
        # Generate candidate itemsets of size k
        candidate_itemsets = generate_candidate_itemsets(
            frequent_itemsets[-1], k)

        # Count the support of each candidate itemset
        itemset_counts = count_itemsets(
            transactions, candidate_itemsets, min_support)

        # Prune the itemsets that don't meet the support threshold
        frequent_itemsets_k = set(
            itemset for itemset, count in itemset_counts.items() if count >= min_support)

        # Stop if no frequent itemsets of size k were found
        if not frequent_itemsets_k:
            break

        frequent_itemsets.append(frequent_itemsets_k)
        k += 1

    return frequent_itemsets


def get_one_itemsets(transactions, unique_items, min_support):
    """
    Get the frequent itemsets of size one.

    Parameters:
    transactions (list of lists): A list of transactions. Each transaction is a list of items.
    unique_items (set): A set of unique items.
    min_support (float): The minimum support threshold.

    Returns:
    list of sets: A list of frequent itemsets of size one.
    """
    itemset_counts = count_itemsets(transactions, unique_items, min_support)
    frequent_itemsets = [set([itemset]) for itemset,
                             count in itemset_counts.items() if count >= min_support]
    return frequent_itemsets


def generate_candidate_itemsets(itemsets, k):
    """
    Generate candidate itemsets of size k.

    Parameters:
    itemsets (list of sets): A list of frequent itemsets of size k-1.
    k (int): The size of the candidate itemsets to generate.

    Returns:
    set: A set of candidate itemsets of size k.
    """
    candidate_itemsets = set()
    for itemset1 in itemsets:
        for itemset2 in itemsets:
            union = itemset1.union(itemset2)
            if len(union) == k:
                candidate_itemsets.add(union)
    return candidate_itemsets


def count_itemsets(transactions, itemsets, min_support):
    """
    Count the support of each itemset in itemsets.

    Parameters:
    transactions (list of lists): A list of transactions. Each transaction is a list of items.
    itemsets (set): A set of itemsets to count the support of.
    min_support (float): The minimum support threshold.

    Returns:
    dict: A dictionary mapping each frequent itemset to its support count.
    """
    itemset_counts = {}
    for transaction in transactions:
        for itemset in itemsets:
            if itemset.issubset(transaction):
                itemset_counts[itemset] = itemset_counts.get(itemset, 0) + 1

    itemset_counts = {itemset: count for itemset, count in itemset_counts.items() if count >= min_support}



# We can test the `apriori` function with the following example:
transactions = [
    ["bread", "milk", "eggs"],
    ["bread", "milk", "eggs", "cheese"],
    ["bread", "eggs"],
    ["milk", "cheese"],
    ["bread", "milk", "cheese"]
]

min_support = 0.4

frequent_itemsets = apriori(transactions, min_support)

for itemset in frequent_itemsets:
    print(itemset)
