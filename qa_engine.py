from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

def ask_question(db, question):
    docs = db.similarity_search(question)
    content = "\n".join([doc.page_content for doc in docs])

    prompt = PromptTemplate.from_template(
        "Based on the context:\n{context}\nAnswer the question:\n{question}"
    )
    input_text = prompt.format(context=content, question=question)

    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.5)
    chain = load_qa_chain(llm, chain_type="stuff")
    result = chain.run(input_documents=docs, question=question)
    return result
