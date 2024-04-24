import nltk
from collections import Counter
from nltk.corpus import stopwords

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Function to remove stop words from text
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text.lower())
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

# Read contents of the file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Count word frequency
def count_frequency(words):
    return Counter(words)

# Main function
def main():
    file_path = 'random_paragraphs.txt'
    text = read_file(file_path)
    words = remove_stopwords(text)
    word_freq = count_frequency(words)
    print("Word Frequency Count:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
