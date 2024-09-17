import random
import pandas as pd

n = int(input("enter number to generate: "))
data = [{
    'PERSON_ID': random.choice([i for i in range(10000, 10010)]),
    'DISTRIC_ID': random.choice([i for i in range(1, 10)]),
    'PERSONAL_INCOME': random.choice([i for i in range(10000, 99999, 1000)])
} for i in range(int(n))]
df = pd.DataFrame(data)
df.to_csv("data.txt", index=False, header=False)
