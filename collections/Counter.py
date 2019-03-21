"""
collections.Counter
"""

from collections import Counter
import random

words = (
    'people',
    'history',
    'way',
    'art',
    'world',
    'information',
    'map',
    'two',
    'family',
    'government',
    'health',
    'system',
    'computer',
    'meat',
    'year',
    'thanks',
    'music',
    'person',
    'reading',
    'method',
    'data',
    'food',
    'understanding',
    'theory',
    'law',
    'bird',
    'literature',
    'problem',
    'software',
    'control',
    'knowledge',
    'power',
    'ability',
    'economics',
    'love',
    'internet',
    'television',
    'science',
    'library'
)


def random_choice_list(n, l):
    """Choose a random word 'n' times from list l, generating a new list.
    There likely be duplicates if n > len(words)
    """
    return [random.choice(l) for i in range(n)]

n = 100
counter = Counter(random_choice_list(n, words))

print('*'*30)
print("Counter 1:")
print("The three most common words were {}.".format(counter.most_common(3)))
print("The word {} appeared {} times.".format('data', counter['data']))
print("The sum, {}, should have been {}.".format(n, sum(counter.values())))
print("\n")

n2 = 50
counter2 = Counter(random_choice_list(n2, words))

print('*'*30)
print("Counter 2:")
print("The three most common words were {}.".format(counter2.most_common(3)))
print("The word {} appeared {} times.".format('data', counter2['data']))
print("The sum, {}, should have been {}.".format(n2, sum(counter2.values())))
print("\n")

print('*'*30)
print("Intersection of Counter 1 and Counter 2: \n{}\n".format(counter & counter2))
print('*'*30)
print("Join of Counter 1 and Counter 2: \n{}\n".format(counter + counter2))
print('*'*30)
print("Difference of Counter 1 and Counter 2: \n{}\n".format(counter - counter2))
