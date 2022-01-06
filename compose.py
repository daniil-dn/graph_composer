import random
import string
import re
import os
from graph import Vertex, Graph


def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()
        text = re.sub(r'\[(.+)\]', ' ', text)
        text = ' '.join(text.split())  # whitespaces to spaces
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words


def make_graph(words):
    previous_word = None
    g = Graph()
    # for each word check that word is in the graph, and if not then add it
    for word in words:
        word_vertex = g.get_vertex(word)
        if previous_word:
            previous_word.increment_edge(word_vertex)
        previous_word = word_vertex

    g.generate_probability_mappings()
    return g

    # if there was a porevious word, then add an edge if it does not already exist
    # in the graph, otherwise increment weight by 1
    # set our word to the previous word and iterate!

    # now remeber that we want to generate the probablility mappings before composing
    # this is a great place to do it before we return the graph object


def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main():
    words = get_words_from_text('texts/hp_sorcerer_stone.txt')
    # for song_file in os.listdir(f'songs/{artist}'):

    g = make_graph(words)
    composition = compose(g, words, 100)
    print(' '.join(composition))


if __name__ == '__main__':
    main()
