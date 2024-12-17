from itertools import combinations


def load_data() -> list[list[str]]:

    return [["I1", "I2", "I3"], ["I2", "I3", "I4"], ["I4", "I5"], ["I1", "I2", "I4"], ["I1", "I2", "I3", "I5"],["I1", "I2", "I3", "I4"]]


def prune(itemset: list, candidates: list, length: int) -> list:

    pruned = []
    for candidate in candidates:
        is_subsequence = True
        for item in candidate:
            if item not in itemset or itemset.count(item) < length - 1:
                is_subsequence = False
                break
        if is_subsequence:
            pruned.append(candidate)
    return pruned


def apriori(data: list[list[str]], min_support: int) -> list[tuple[list[str], int]]:

    itemset = [list(transaction) for transaction in data]
    frequent_itemsets = []
    length = 1

    while itemset:
        counts = [0] * len(itemset)
        for transaction in data:
            for j, candidate in enumerate(itemset):
                if all(item in transaction for item in candidate):
                    counts[j] += 1

        itemset = [item for i, item in enumerate(itemset) if counts[i] >= min_support]

        for i, item in enumerate(itemset):
            frequent_itemsets.append((sorted(item), counts[i]))

        length += 1
        itemset = prune(itemset, list(combinations(itemset, length)), length)

    return frequent_itemsets


if __name__ == "__main__":

    import doctest

    doctest.testmod()

    frequent_itemsets = apriori(data=load_data(), min_support=3)
    print("\n".join(f"{itemset}: {support}" for itemset, support in frequent_itemsets))