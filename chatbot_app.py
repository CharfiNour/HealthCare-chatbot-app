import streamlit as st

def load_paragraphs(file_path="health_care.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    paragraphs = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 0]
    return paragraphs

def find_best_paragraph(query, paragraphs):
    query_words = set(query.lower().split())
    best_score = 0
    best_para = "Sorry, I don't know how to answer that yet."
    for para in paragraphs:
        para_words = set(para.lower().split())
        score = len(query_words & para_words)
        if score > best_score:
            best_score = score
            best_para = para
    return best_para

def main():
    st.title("Health Care - Chatbot")
    st.write("Ask me anything.")

    paragraphs = load_paragraphs("health_care.txt")

    user_input = st.text_input("You:")

    if st.button("Submit"):
        if user_input.strip() == "":
            st.write("Chatbot: Please enter a question.")
        else:
            response = find_best_paragraph(user_input, paragraphs)
            st.write("Chatbot: " + response)

if __name__ == "__main__":
    main()