from collections import Counter

"""
    Q: How to know the most time of an element in a item?
    A: collections.Counter class is specially to do this thing as most-common.
"""


def most_times_in_series():

    pets = [
        'Simba', 'loves', 'cat', 'so', 'much',
        'cat', 'loves', 'rabbit', 'duck', 'say', 'no',
        'Kitty', 'Cat', 'Simba', 'Cat', 'cat', 'duck'
    ]

    pet_counts = Counter(pets)

    top_3_pets = pet_counts.most_common(3)
    print(top_3_pets)
    # [('cat', 3), ('Simba', 2), ('loves', 2)]

    more_pets = [
        'Cat', 'rabbit', 'duck', 'say', 'no'
    ]

    for pet in more_pets:
        pet_counts[pet] += 1

    print(pet_counts['Cat'])  # 3

    pet_counts.update(more_pets)   # same function as above  each word plus 1 here
    print(pet_counts)
    # Counter({'duck': 4, 'Cat': 4, 'cat': 3, 'rabbit': 3, 'say': 3, 'no': 3, 'Simba': 2, 'loves': 2, 'so': 1, 'much': 1, 'Kitty': 1})


if __name__ == '__main__':
    most_times_in_series()