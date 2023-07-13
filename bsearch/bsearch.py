
from datetime import datetime
from typing import Tuple, List

def nsearch(data:List[Tuple[int, float]], key: int)-> Tuple[int, float]:
    return next((item for item in data if item[0] == key), [])

def bsearch(data:List[Tuple[int, float]], key: int)-> Tuple[int, float]:
    if len(data) == 1:
        return data[0]
    
    attempt = int(len(data) / 2)

    if data[attempt][0] == key:
        return data[attempt]
    
    if data[attempt][0] < key:
        return bsearch(data[attempt:], key)
    else:
        return bsearch(data[:attempt + 1], key)

def bisearch(data:List[Tuple[int, float]], key: int)-> List:
    low = 0
    high = len(data) - 1

    while True:
        if high == low and data[low][0]!= key:
            return []
        
        attempt = low + int((high - low) / 2) if high > low else low

        if data[attempt][0] == key:
            return data[attempt]
        
        if data[attempt][0] < key:
            low = attempt + 1
        else:
            high = attempt 
             

if __name__ == '__main__':
    data = list([i + 1000, (i + 1000)*1.0 +0.1] for i in range(10000))



    key = 5007
    print(nsearch(data, key))
    print(bsearch(data, key))
    print(bisearch(data, key))
    print("-")
    print(bisearch([[5007, 5007.1234]], key))
    print(bisearch([[5006, 5006.1234],[5007, 5007.1234]], key))
    print(bisearch([[5007, 5007.1234],[5008, 5008.1234]], key))
    print(bisearch([[0000, 1234]], key))
    print("-")

    NRUN=10000

    t0 = datetime.now()
    
    for _ in range(NRUN):
        nsearch(data, key)
    t1 = datetime.now()

    for _ in range(NRUN):
        bsearch(data, key)
    t2 = datetime.now()

    for _ in range(NRUN):
        bisearch(data, key)
    t3 = datetime.now()

    print(f"naive: {t1 - t0}")
    print(f"bin  : {t2 - t1}")
    print(f"bin i: {t3 - t2}")

    for key in [k[0] for k in data]:
        r = bisearch(data, key)
        assert r[0] == key



 