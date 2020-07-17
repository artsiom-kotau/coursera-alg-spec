# python3
from collections import deque

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [deque() for i in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, value):
        hash_value = self._hash_func(value)
        bucket = self.elems[hash_value]
        contains = False
        for item in bucket:
            contains = item == value
            if contains:
                break

        if not contains:
            bucket.appendleft(value)

    def remove(self, value):
        hash_value = self._hash_func(value)
        bucket = self.elems[hash_value]
        try:
            bucket.remove(value)
        except ValueError:
            pass

    def find(self, value):
        hash_value = self._hash_func(value)
        bucket = self.elems[hash_value]
        result = False
        for item in bucket:
            result = item == value
            if result:
                break
        return result

    def check(self, i):
        values = self.elems[i]
        if values is None:
            values = deque()
        return values


    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        array = []
        if chain:
            for item in chain:
                array.append(item)
        print(' '.join(array))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(self.check(query.ind))
        else:
            if query.type == 'find':
                self.write_search_result(self.find(query.s))
            elif query.type == 'add':
                self.add(query.s)
            else:
                self.remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
