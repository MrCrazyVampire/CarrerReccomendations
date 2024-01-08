from project02 import career
import numpy as np

categories = []

for x in range(0, 729):

    b = int(np.base_repr(x, base=3))
    
    lis = list(map(lambda x: str(x).replace('2', '0.5'), str(b)))
    

    if len(lis) < 6:
        lis = ['0'] * (6 - len(lis)) + lis
    
    lis = [ float(x) for x in lis ]
    x = career(lis) 
    categories.append(x)    

from collections import Counter
category_counts = Counter(categories)
for category, count in category_counts.items():
    print(f"{category}: {count} occurrences")