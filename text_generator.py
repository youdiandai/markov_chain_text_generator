# Write your code here
import random
from collections import Counter

sentence_ending_punctuation_mark = ('.', '!', '?')


class GenerateRandomText:
    corpus = ""
    trigrams = []
    token = []
    markov_chain = {}
    starts = []
    starts_trigram = []

    def __init__(self, corpus):
        self.corpus = corpus
        self.token = corpus.split()
        self.create_trigrams()
        self.create_markov_chain()
        self.random_starts()

    def create_trigrams(self):
        for x in range(len(self.token) - 2):
            self.trigrams.append([self.token[x] + " " + self.token[x + 1], self.token[x + 2]])

    def create_markov_chain(self):
        default = {}
        for x in self.trigrams:
            default.setdefault(x[0], [])
            default[x[0]].append(x[1])
        for x in default.keys():
            default[x] = Counter(default[x])
        self.markov_chain = default

    def print_head(self, head):
        for x in self.markov_chain[head].keys():
            print(f"Tail: {x}    Count: {self.markov_chain[head][x]}")

    def get_head_counter(self, head):
        return self.markov_chain[head]

    def get_next(self, head):
        counter = self.get_head_counter(head)
        return random.choices(population=list(counter.keys()), weights=list(counter.values()))[0]

    def random_starts(self):
        self.starts = [x for x in self.markov_chain.keys() if
                       x[0].isupper() and x.split()[0][-1] not in sentence_ending_punctuation_mark]

    def get_start(self):
        return random.choice(self.starts)

    def gennerate_random_text(self):
        str_chain = []
        random_start = self.get_start()
        str_chain.append(random_start)
        start = random_start
        while start[-1] not in sentence_ending_punctuation_mark or len(str_chain) < 4:
            new_str = self.get_next(start)
            str_chain.append(new_str)
            start = start.split()[1] + " " + new_str
        print(" ".join(str_chain))


if __name__ == "__main__":
    filename = input()
    with open(filename, "r", encoding="UTF-8") as f:
        corpus = f.read()

    g = GenerateRandomText(corpus)
    for _ in range(10):
        g.gennerate_random_text()
