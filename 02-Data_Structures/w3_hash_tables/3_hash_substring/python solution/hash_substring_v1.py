# python3

class TextSearch:
    '''Rabin's algorithm for searching a given pattern in a given text.'''

    def __init__(self, pattern, text):
        self._pattern = pattern
        self._text = text
        self._window = len(pattern)
        self._scan_bound = len(text) - len(pattern) + 1
        self._checksums = []

    def checksum(self, string):
        '''Returns hash of the string.'''
        return sum([ord(string[i]) for i in range(len(string))])

    def precompute_hashes(self):
        '''Precomputes hash values for the whole possible pattern items in the text.
        '''
        self._checksums = [self.checksum(self._text[:self._window])]

        for i in range(1, self._scan_bound):
            old_hash = self._checksums[i-1]
            left_l_hash = ord(self._text[i-1])
            right_l_hash = ord(self._text[i + self._window - 1])

            ith_hash = old_hash - left_l_hash + right_l_hash
            self._checksums.append(ith_hash)

    def find(self):
        '''Returns all occurrences of pattern in the text.'''
        pattern_checksum = self.checksum(self._pattern)
        self.precompute_hashes()

        result = []
        for i in range(self._scan_bound):
            if pattern_checksum == self._checksums[i]:
                if self._pattern == self._text[i:i + self._window]:
                    result.append(i)
        return result


if __name__ == '__main__':
    pattern, text = input().rstrip(), input().rstrip()

    text_search = TextSearch(pattern, text)
    result = text_search.find()

    print(" ".join(map(str, result)))
