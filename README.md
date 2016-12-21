# Word n-Grams

A simple script that scans a piece of text (a local file in the same location as the script, or a string literal enclosed in quotes) and displays the top *k* word *n*-grams (word sequences of length *n*) from the text, including their absolute and relative frequencies. For example, in the following sentence

> "It is raining today, and I will need an umbrella."

the word *4*-grams are *"It is raining today"*, *"is raining today and"*, *"raining today and I"*, *"and I will need"*, *"I will need an"*, *"will need an umbrella."* Case and punctuation marks and ignored when comparing word grams, so that the word *4*-grams "It is raining today," and "it is raining today" are considered the same.

An example:

    The top 10 word 5-grams and their frequencies (absolute and relative) are as follows.

        it's important to be confident 4 (0.014)
        a photo is real or 4 (0.014)
        be confident and stand up 4 (0.014)
        photo is real or retouched 4 (0.014)
        important to be confident and 3 (0.01)
        idea of what beauty is 3 (0.01)
        confident and stand up to 3 (0.01)
        think words can never hurt 3 (0.01)
        to be confident and stand 3 (0.01)
        and stand up to bullies 3 (0.01)
