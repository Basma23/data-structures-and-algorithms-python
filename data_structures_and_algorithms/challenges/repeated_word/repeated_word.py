import re

def repeated_word(sentence):
    words = set()
    sentences = re.findall(r'[A-Za-z]+', sentence.lower())

    for word in sentences:
        if word in words:
            return word
        words.add(word)
    return None

if __name__ == "__main__":
    sentence = "Once upon a time, there was a brave princess who..."
    sentence1 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    sentence2 = "it was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    sentence3 = "Realy nice"
    print(repeated_word(sentence))
    print(repeated_word(sentence1))
    print(repeated_word(sentence2))
    print(repeated_word(sentence3))