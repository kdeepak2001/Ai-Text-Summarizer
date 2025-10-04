# 🗓️ Development Journey

This document logs the step-by-step process of building the Text Summarizer CLI, including decisions, challenges, and learnings.

---

## Day 1 - October 4, 2025

### ✅ What I Did
- Created project folder structure with app.py, README.md, JOURNEY.md, requirements.txt
- Set up Python virtual environment using `python -m venv .venv`
- Installed dependencies: requests==2.32.3 and beautifulsoup4==4.14.2
- Researched extractive summarization algorithms (word frequency scoring)
- Implemented core functions: fetch_url_text(), read_file_text(), read_stdin_text()
- Built extractive_summarize() function with sentence scoring logic
- Tested successfully on sample.txt file with 10 sentences about AI

### 🔧 Key Decisions
- **Why extractive summarization?** Abstractive requires LLMs/APIs which can fail or cost money. Extractive works offline and is more reliable for a baseline.
- **Why word frequency scoring?** Simple to implement, no external libraries needed, works well for factual text.
- **Why position bonus?** First few sentences often contain main ideas (inverted pyramid in journalism).
- **Why argparse?** Professional CLI framework that handles flags, help text, and error messages automatically.

### 🐛 Challenges & Fixes
- **Challenge:** Wikipedia returned 403 Forbidden error when testing URL mode
  - **Root cause:** Websites block simple requests without user-agent headers to prevent bots
  - **Status:** File input works perfectly, URL feature can be enhanced later with headers
  - **Learning:** Web scraping requires understanding of HTTP headers and bot detection
  
- **Challenge:** Initial indentation error in app.py around line 148
  - **Root cause:** Mixed spaces/tabs or incorrect indentation depth in else block
  - **Fix:** Rewrote the section with consistent 4-space indentation
  - **Learning:** Python is strict about indentation - use consistent spacing

### 📊 Testing Results
- ✅ File input: Successfully extracted 3 sentences from sample.txt
- ✅ Custom sentence count: Works with --sentences flag
- ⚠️ URL input: Blocked by Wikipedia (403 error) - needs user-agent header
- ✅ Stdin input: Ready to test (not tested yet)
- ✅ Edge case: Text with < 3 sentences returns all sentences (expected behavior)

### 📚 What I Learned
- **Extractive summarization** is fundamentally a sentence ranking problem
- **Word frequency (TF)** is surprisingly effective for simple summaries without complex NLP
- **Virtual environments** prevent dependency conflicts and make projects reproducible
- **Git workflow:** Create local commits first, then push to GitHub later
- **Windows CMD** uses backslash (\) for paths, not forward slash (/)
- **argparse** makes CLI apps professional with automatic help text generation

### 🎯 Technical Implementation Details
- Used Counter from collections for efficient word frequency calculation
- Regex pattern `r'(?<=[.!?])\s+(?=[A-Z])'` splits sentences at punctuation
- Normalized frequencies by dividing by max_freq to get scores between 0-1
- Position bonus: 1.0 for first 3 sentences, 0.5 for rest
- Maintained original sentence order in summary for readability

### 🔜 Next Steps for Day 2
- Initialize Git repository with proper .gitignore
- Make first commit with descriptive message
- Create GitHub repository online
- Push local commits to remote repository
- Start planning Streamlit UI design
- Research Hugging Face Inference API for optional AI mode

---

## Future Plans

### Stretch Goals
- [ ] Build Streamlit web UI for non-technical users
- [ ] Add --mode flag to switch between baseline and API summarization
- [ ] Deploy to Hugging Face Spaces (free hosting)
- [ ] Fix URL fetching with proper user-agent headers
- [ ] Add support for PDF and DOCX file inputs
- [ ] Implement ROUGE metrics for summary quality evaluation

### Technical Improvements
- [ ] Add unit tests with pytest
- [ ] Improve sentence splitting (handle abbreviations like "Dr." better)
- [ ] Add stop word removal for better word frequency
- [ ] Implement TF-IDF instead of just TF for scoring
- [ ] Add error handling for empty files
- [ ] Create requirements-dev.txt for development dependencies

---

## Reflections & Key Takeaways

### What Went Well
- **Systematic approach:** Setup → code → test → document kept progress smooth
- **Incremental testing:** Testing each function individually made debugging easier
- **Documentation first:** Writing README and JOURNEY helped clarify thinking
- **Beginner-friendly:** Following step-by-step commands made everything reproducible

### What Could Improve
- **Sentence splitting:** Too simplistic - breaks on "Dr." or "U.S." 
- **No input validation:** Should check for empty files or invalid URLs earlier
- **No tests:** Should add unit tests for core functions (future improvement)
- **URL handling:** Need to add user-agent and handle various website structures

### Skills Developed
- Python CLI development with argparse
- Text processing with regex and string manipulation
- Understanding of extractive summarization algorithms
- Git version control fundamentals
- Windows command line proficiency
- Virtual environment management
- Professional README documentation

### Time Spent
- Project setup and environment: 15 minutes
- Coding and debugging: 30 minutes  
- Testing and fixing errors: 15 minutes
- Documentation (README + JOURNEY): 20 minutes
- **Total:** ~1.5 hours

---

**Assignment Goal:** Build a tiny AI-powered app demonstrating effort, resourcefulness, and learning - ✅ ACHIEVED
