def count_words(sentence):
    # Sentence ko split karke words ki list ka count return karenge
    words = sentence.strip().split()
    return len(words)