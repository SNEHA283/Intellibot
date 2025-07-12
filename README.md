# 🤖 Intellibot – Wikipedia-Based NLP Chatbot

An intelligent chatbot that uses web scraping, vector embeddings, and generative AI (Gemini Pro) to answer user questions from Wikipedia content.

---

## 👥 Team

- Sneha Chakraborty (21BAI10204)
- Simran Namdev
- Shambhavi Pandey
- Divya Agarwal
- Aaron Antony Noronha
- Mohini Gupta

---

## 🧠 What It Does

- Scrapes a Wikipedia article on a user-defined topic
- Splits the text and creates vector embeddings
- Stores them in a FAISS vector database
- Accepts user questions
- Uses Google’s Gemini Pro to answer based on the context

---

## 🛠️ Technologies Used

- Python
- BeautifulSoup (for scraping)
- HuggingFace Embeddings
- LangChain
- FAISS (vector store)
- Google Gemini Pro (Generative AI)

---

## 📦 Installation & Requirements

Install dependencies with:

```bash
pip install -r requirements.txt

▶️ How to Run the Code
Make sure the following files exist in the same folder:

app.py
scraper.py
embeddings.py
qa_engine.py

Then run:
python app.py

You’ll be asked:
Enter a topic to scrape from Wikipedia: Artificial Intelligence
Ask a question (or type 'exit'): What is the Turing Test?

The bot will respond using Gemini Pro based on your question and the topic you scraped.

To end the session, type:
exit


📌 Example Output
Topic: Artificial Intelligence
Question: What is the Turing Test?

Response:
The Turing Test, proposed by Alan Turing, is a measure of a machine's ability to exhibit intelligent behavior indistinguishable from a human...

🔮 Future Improvements
Streamlit UI
Multilingual support
Response confidence display
Support for multiple documents

📄 License
For academic use only.
