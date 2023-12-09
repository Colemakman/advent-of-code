from collections import Counter


lines = []
with open('sample.txt', 'r') as file:
    for f in file:
        lines.append(f.strip())
print(
    sum(
        (rank0 + 1) * bid
        for rank0, (*_, bid) in enumerate(
            sorted(
                (
                    max(map(hand.count, hand)),
                    -len(set(hand)),
                    *map("23456789TJQKA".index, hand),
                    int(str_bid),
                )
                for hand, str_bid in map(str.split, lines)
            )
        )
    )
)
