import re

text = "Random string 1232 321, my email: piOOter125@gmail.com, and its good, MyLor3d@word.gov, MyLor3d@word.gov, Mhehszki23@wordki.gov, pieter.sobieszczyk@gmail.pl"

pattern = re.compile("[a-zA-Z0-9.-_]+@+[a-zA-Z]+\.[a-z]+")

result = pattern.findall(text)
print(list(set(result)))