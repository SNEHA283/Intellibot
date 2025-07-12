from scraper import scrape_topic
from embeddings import build_vector_store
from qa_engine import ask_question

def main():
    topic = input("Enter a topic to scrape from Wikipedia: ")
    file_path = scrape_topic(topic)
    db = build_vector_store(file_path)

    while True:
        query = input("Ask a question (or type 'exit'): ")
        if query.lower() == 'exit':
            break
        print(ask_question(db, query))

if __name__ == "__main__":
    main()
