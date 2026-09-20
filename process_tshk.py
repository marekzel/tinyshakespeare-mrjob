from mrjob.job import MRJob
from mrjob.protocol import RawProtocol
import re

# WORD_RE = re.compile(r'[\w]+')

class TSHKJob(MRJob):

    IGNORE_PATTERN = re.compile(r"^[A-Z\u00D3\u0106\u0118\u0141\u0143\u015A\u0179\u017B]+:$")
    OUTPUT_PROTOCOL = RawProtocol

    def mapper(self, _, line):

        clean_line = line.strip()
        if not clean_line:
            return

        if self.IGNORE_PATTERN.match(clean_line):
            return

        for word in clean_line.split():
            cleaned_word = re.sub(r'[^\w\s]', '', word.lower())
            if cleaned_word:
                yield cleaned_word, 1

    def reducer(self, key, values):
        total = sum(values)
        yield f"{key},{total}", None

if __name__ == '__main__':
    TSHKJob.run()

