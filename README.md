---
title: AI Text Summarizer
emoji: 📝
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.50.0
app_file: streamlit_app.py
pinned: false
---

# 📝 Text Summarizer CLI

A lightweight Python command-line tool that extracts the most important sentences from text using extractive summarization. Works offline with no API required.

## ✨ Features

- **Multiple input sources:** URL, file, or stdin
- **Extractive summarization:** Frequency-based sentence scoring algorithm
- **Configurable output:** Choose number of summary sentences (default: 3)
- **Offline-first:** No API keys or internet required for file/stdin mode
- **Cross-platform:** Works on Windows, macOS, and Linux

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone the repository:**

git clone https://github.com/kdeepak2001/Ai-Text-Summarizer.git
cd Ai-Text-Summarizer


2. **Create virtual environment:**

python -m venv .venv
.venv\Scripts\activate

3. **Install dependencies:**

pip install -r requirements.txt


## 📖 Usage

### Summarize a file

python app.py --file examples\sample.txt

### Summarize a URL

python app.py --url https://example.com/article


### Summarize from stdin

echo Your long text here | python app.py

### Custom sentence count

python app.py --file article.txt --sentences 5

### Help

python app.py --help


## 🔧 How It Works

The summarizer uses **extractive summarization** with these steps:

1. **Text cleaning:** Removes HTML tags, normalizes whitespace
2. **Sentence splitting:** Breaks text into individual sentences
3. **Word frequency:** Calculates normalized frequency of content words
4. **Sentence scoring:** Ranks sentences by sum of word frequencies + position bonus
5. **Selection:** Picks top N sentences, maintains original order

## 🗂️ Project Structure

Ai-Text-Summarizer/
├── app.py # Main CLI application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── JOURNEY.md # Development log
├── examples/
│ └── sample.txt # Test data
└── .venv/ # Virtual environment (not in Git)


## 🛣️ Roadmap

### ✅ Completed (Baseline)
- CLI with argparse for URL/file/stdin input
- Extractive summarization with word frequency scoring
- Windows-compatible commands and testing
- Git version control

### 🔜 Next Steps
- [ ] Add Streamlit web UI for interactive use
- [ ] Optional API mode using Hugging Face Inference API
- [ ] Deploy to Hugging Face Spaces (free hosting)
- [ ] Add support for PDF and DOCX files

## 📄 License

MIT License - feel free to use for learning and personal projects.

## 🔗 Links

- **GitHub:** https://github.com/kdeepak2001/Ai-Text-Summarizer
- **Author:** K Deepak

---

