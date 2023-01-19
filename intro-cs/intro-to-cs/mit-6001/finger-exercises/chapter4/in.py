def isin(first, second):
    return (first in second) or (second in first)

print(isin("hello", "hello world"))