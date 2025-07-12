# 🤖 Intellibot – Wikipedia-Based NLP Chatbot

An intelligent chatbot that uses web scraping, vector embeddings, and generative AI (Gemini Pro) to answer user questions from Wikipedia.

---

## 👥 Team

- Sneha Chakraborty (21BAI10204)
- Simran Namdev
- Shambhavi Pandey
- Divya Agarwal
- Aaron Antony Noronha
- Mohini Gupta

---

## 🚀 Features

- Web scraping of Wikipedia articles
- FAISS-based vector store
- Embedding with HuggingFace models
- Natural language Q&A using Google’s Gemini Pro (via LangChain)
- Interactive text interface (can be deployed in Streamlit)

---

## 🧠 How It Works

1. Scrapes the Wikipedia article based on user topic
2. Splits and embeds content using HuggingFace (e.g., `all-MiniLM-L6-v2`)
3. Stores embeddings in FAISS
4. Accepts natural language questions
5. Uses similarity search + Google Generative AI to generate answers

---

## 📦 Requirements

```bash
pip install -r requirements.txt

▶️ Run the Program
python app.py
You’ll be prompted to enter a topic and then ask questions from it.

🛠 Technologies Used
Python
BeautifulSoup
requests
HuggingFace Transformers
FAISS (via LangChain)
Google Generative AI (gemini-pro)

LangChain

📌 Sample Query
Topic: Artificial Intelligence
Question: What is the Turing Test?

Response:
The Turing Test, proposed by Alan Turing, evaluates a machine’s ability to exhibit intelligent behavior indistinguishable from a human...

🔮 Future Enhancements
Streamlit-based GUI
Multi-topic history tracking
Multilingual input/output
Contextual memory and feedback

