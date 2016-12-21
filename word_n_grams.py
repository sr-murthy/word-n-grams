#!/usr/bin/env python3

import codecs
import os
import string
import sys

from collections import Counter

def get_word_n_grams(input_file_name=None, input_text='', n=1):
    """
    Returns a dict of n-word grams and their frequencies from an
    input source which can be either an existing (UTF-8 encoded) text
    file or a block of text in a string (with newlines separating lines).
    These arguments must be named, and the final argument 'n', the length
    of word n-grams, must also be named - by default it is set to 1. In
    any of the following cases - the input file name is null, the input
    text is an empty string, the integer n exceeds the number of tokens
    in the input source - an error can be expected.

    In stripping special characters from tokens double "" and single ''
    quotation marks are ignored.
    """

    lines = (
        [line for line in codecs.open(input_file_name, 'r', 'utf-8').readlines() if line] if input_file_name
        else [line for line in input_text.split('\n') if line]
    )
    non_alphabetics = string.punctuation + string.whitespace
    word_n_grams = Counter()

    for line in lines:                                
        token_seq = [token.lower().strip(non_alphabetics) for token in line.split(' ')]
        if len(token_seq) >= n:
            word_n_gram_seqs_li = [token_seq[d:d + n] for d in range(len(token_seq) - n + 1)]            
            for seq in word_n_gram_seqs_li:
                word_n_grams[' '.join(seq)] += 1

    total_n_grams = sum(word_n_grams[n_gram] for n_gram in word_n_grams)

    return word_n_grams, total_n_grams

def get_top_k_word_n_grams(word_n_grams, k=10):
    """
    Given a dictionary of word n-grams and their frequencies (such as that returned
    by get_word_n_grams) this method returns the top k word n-grams in descending
    order of frequency, where k is a non-negative integer. The return element is a list
    of tuples

        (seq #1, seq_count #1), (seq #2, seq_count #2), .... ,(seq #k, seq_count #k)

    where <seq #i> is the i-th most frequent word n-gram and <seq_count #i> is the
    frequency. By default k is 10, and an error can be expected if the input dictionary
    does not contain enough word grams.

    """
    return word_n_grams.most_common(k)

def display_top_k_word_n_grams(n, k, top_k_word_n_grams, total_n_grams):
    """
    Given n, k as above, the list of top k word n-gram tuples, as returned
    by get_top_k_word_n_grams, and an output file name, this method writes these
    tuples to a CSV file of the given name. In the process it also prints this
    information to screen.
    """
    print('\nThe top {} word {}-grams and their frequencies (absolute and relative) are as follows.\n'.format(k, n))
    for seq, seq_count in top_k_word_n_grams:
        print('\t{} {} ({})'.format(seq, seq_count, round(float(seq_count) / total_n_grams, 3)))
    print('\n')

# The script main method: the default is to call it with three arguments in the following order:
#
#     <input file name> <n> <k>
#
# <input file name> is the name of a text file in the same directory, <n> is the word gram
# length and <k> the number of most frequent word n-grams.
if __name__ == '__main__':
    if len(sys.argv) == 4:
        if os.path.exists('output.csv'):
            os.remove('output.csv')
        input_source = sys.argv[1]
        input_file_name = input_text = None
        if os.path.exists(input_source):
            input_file_name = input_source
        else:
            input_text = input_source
        n = int(sys.argv[2])
        k = int(sys.argv[3])
        word_n_grams, total_n_grams = get_word_n_grams(input_file_name=input_file_name, input_text=input_text, n=n)
        top_k_word_n_grams = get_top_k_word_n_grams(word_n_grams, k)
        display_top_k_word_n_grams(n, k, top_k_word_n_grams, total_n_grams)
    else:
        raise Exception('Error: Call the script with three arguments in order: <text input file name>, <word sequence length>, <top k (k most frequent) word sequences)>')
