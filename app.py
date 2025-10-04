"""
Text Summarizer CLI
Reads text from URL, file, or stdin and outputs exactly N sentences using extractive summarization.
"""

import argparse
import sys
import re
from collections import Counter
import requests
from bs4 import BeautifulSoup


def fetch_url_text(url):
    """Fetch and extract clean text from a URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for script in soup(["script", "style"]):
            script.decompose()
        
        text = soup.get_text(separator=' ', strip=True)
        return text
    except Exception as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        sys.exit(1)


def read_file_text(filepath):
    """Read text from a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)


def read_stdin_text():
    """Read text from standard input."""
    return sys.stdin.read()


def clean_text(text):
    """Clean and normalize text."""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def split_into_sentences(text):
    """Split text into sentences using basic regex."""
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
    return [s.strip() for s in sentences if len(s.strip()) > 10]


def calculate_word_frequencies(sentences):
    """Calculate word frequency scores from all sentences."""
    all_words = []
    for sentence in sentences:
        words = re.findall(r'\b[a-z]{3,}\b', sentence.lower())
        all_words.extend(words)
    
    word_freq = Counter(all_words)
    
    if word_freq:
        max_freq = max(word_freq.values())
        word_freq = {word: freq / max_freq for word, freq in word_freq.items()}
    
    return word_freq


def score_sentences(sentences, word_freq):
    """Score sentences based on word frequency."""
    sentence_scores = {}
    
    for i, sentence in enumerate(sentences):
        words = re.findall(r'\b[a-z]{3,}\b', sentence.lower())
        score = sum(word_freq.get(word, 0) for word in words)
        
        position_bonus = 1.0 if i < 3 else 0.5
        score *= position_bonus
        
        sentence_scores[i] = score
    
    return sentence_scores


def extractive_summarize(text, num_sentences=3):
    """Perform extractive summarization using word frequency scoring."""
    text = clean_text(text)
    sentences = split_into_sentences(text)
    
    if len(sentences) <= num_sentences:
        return sentences
    
    word_freq = calculate_word_frequencies(sentences)
    sentence_scores = score_sentences(sentences, word_freq)
    
    top_indices = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    top_indices.sort()
    
    summary_sentences = [sentences[i] for i in top_indices]
    return summary_sentences


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Text Summarizer - Extract key sentences from text',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python app.py --file examples\\sample.txt
  python app.py --url https://example.com/article
  echo Some long text here | python app.py
  python app.py --file article.txt --sentences 5
        '''
    )
    
    parser.add_argument('--url', type=str, help='URL to fetch and summarize')
    parser.add_argument('--file', type=str, help='File path to summarize')
    parser.add_argument('--sentences', type=int, default=3, 
                        help='Number of sentences in summary (default: 3)')
    
    args = parser.parse_args()
    
    if args.url:
        text = fetch_url_text(args.url)
    elif args.file:
        text = read_file_text(args.file)
    else:
        if sys.stdin.isatty():
            print("Error: No input provided. Use --url, --file, or pipe text via stdin.", 
                  file=sys.stderr)
            sys.exit(1)
        text = read_stdin_text()
    
    summary = extractive_summarize(text, args.sentences)
    
    print(f"\n{'='*60}")
    print(f"SUMMARY ({len(summary)} sentences)")
    print(f"{'='*60}\n")
    
    for i, sentence in enumerate(summary, 1):
        print(f"{i}. {sentence}\n")


if __name__ == '__main__':
    main()
