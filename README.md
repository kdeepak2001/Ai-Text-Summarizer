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

# 📝 AI Text Summarizer

[![Live Demo](https://img.shields.io/badge/🤗%20Hugging%20Face-Live%20Demo-blue)](https://huggingface.co/spaces/deepak95026/ai-text-summarizer)
[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent text summarization tool that extracts the most important sentences from any text using **extractive summarization** powered by word frequency scoring algorithms.

🔗 **[Try the Live Demo](https://huggingface.co/spaces/deepak95026/ai-text-summarizer)**

---

## ✨ Features

- 📄 **Text Input** - Paste or type any text directly
- 🌐 **URL Support** - Fetch and summarize content from any webpage
- ⚙️ **Customizable** - Adjust the number of sentences (1-10)
- 📊 **Statistics** - View original length, summary length, and reduction percentage
- 🚀 **No API Required** - Works completely offline with no external dependencies
- 💻 **Dual Interface** - Command-line tool and interactive web UI

---

## 🎯 How It Works

The application uses **extractive summarization** with a word frequency scoring algorithm:

1. **Tokenization** - Splits text into sentences and words
2. **Frequency Analysis** - Calculates word occurrence frequencies
3. **Sentence Scoring** - Assigns scores based on word frequencies
4. **Position Bonus** - Prioritizes sentences from the beginning
5. **Top Extraction** - Selects highest-scoring sentences

---

## 🛠️ Tech Stack

- **Python 3.13** - Core programming language
- **Streamlit** - Interactive web interface
- **BeautifulSoup4** - Web scraping and HTML parsing
- **Requests** - HTTP requests for URL fetching
- **Git/GitHub** - Version control
- **Hugging Face Spaces** - Cloud deployment

---

## 🚀 Quick Start

### Installation

1. **Clone the repository:**

git clone https://github.com/kdeepak2001/Ai-Text-Summarizer.git
cd Ai-Text-Summarizer

2. **Create virtual environment:**

python -m venv .venv
.venv\Scripts\activate # Windows
source .venv/bin/activate # Linux/Mac

3. **Install dependencies:**

pip install -r requirements.txt

---

---

## 💡 Usage

### Web Interface (Streamlit)

streamlit run streamlit_app.py


Then open http://localhost:8501 in your browser.

### Command Line

**From text input:**
echo "Your text here..." | python app.py


**From file:**
python app.py --file document.txt --num-sentences 5

**From URL:**
python app.py --url https://example.com/article


---

## 📸 Screenshots

### Web Interface
![Streamlit UI](https://via.placeholder.com/800x400.png?text=Add+Your+Screenshot)

### CLI Usage

$ python app.py --help
usage: app.py [-h] [--file FILE] [--url URL] [--num-sentences N]

AI Text Summarizer - Extract key sentences from any text

optional arguments:
-h, --help show this help message and exit
--file FILE, -f FILE Path to text file
--url URL, -u URL URL to fetch and summarize
--num-sentences N, -n N
Number of sentences (default: 3)


---

## 📂 Project Structure

'''
Ai-Text-Summarizer/
├── app.py # CLI application
├── streamlit_app.py # Web UI application
├── requirements.txt # Python dependencies
├── .streamlit/
│ └── config.toml # Streamlit configuration
├── README.md # Project documentation
├── JOURNEY.md # Development log
└── LICENSE # MIT License

undefined
'''


---

## 🎓 Learning Outcomes

This project demonstrates proficiency in:

- ✅ Natural Language Processing fundamentals
- ✅ Algorithm implementation (word frequency scoring)
- ✅ Web application development with Streamlit
- ✅ Command-line interface design with argparse
- ✅ Web scraping with BeautifulSoup4
- ✅ Git version control and GitHub workflow
- ✅ Cloud deployment on Hugging Face Spaces
- ✅ Professional documentation and code organization

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**K Deepak**  
🔗 [LinkedIn](https://linkedin.com/in/kalava-deepak) | 🐙 [GitHub](https://github.com/kdeepak2001) | Gmail - kalavadeepak2001@gmail.com 

---

## 🙏 Acknowledgments

- Built with ❤️ using Python and Streamlit
- Deployed on Hugging Face Spaces
- Inspired by NLP research in extractive summarization

---

**⭐ If you found this project helpful, please consider giving it a star!**
