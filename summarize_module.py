import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation

# 🔧 Ensure required NLTK resources are available
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

def summarize_text(text, max_sentences=3):
    """Generate a simple frequency-based summary of the input text."""
    # Tokenize sentences
    sentences = sent_tokenize(text)

    # Handle empty or short text
    if len(sentences) == 0:
        return "No valid text to summarize."

    # Tokenize words and remove stopwords/punctuation
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english') + list(punctuation))

    # Word frequency table
    word_freq = {}
    for word in words:
        if word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1

    # Sentence scores
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]

    # Pick top N sentences
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:max_sentences]

    # Keep original order
    summary = " ".join([s for s in sentences if s in top_sentences])
    return summary
