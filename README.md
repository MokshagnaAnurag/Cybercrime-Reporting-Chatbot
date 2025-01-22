# 💻 Cybercrime Reporting Chatbot 🛡️

## 🧐 Overview
The **Cybercrime Reporting Chatbot** is an **AI-powered system** designed to help users **recognize and report various types of cybercrimes**. Using advanced machine learning models for **natural language processing**, the chatbot analyzes user queries, detects intents, performs sentiment analysis, and matches the queries to predefined cybercrime cases.

## 🌟 Features
- 🔍 **Intent Recognition**: Understands the user's request.
- 🧠 **Sentiment Analysis**: Analyzes the emotional tone of the query.
- 🧩 **Case-Based Reasoning (CBR)**: Suggests appropriate actions based on user queries.
- 📄 **Detailed Report Generation**: Generates reports for each query.
- 💬 **Interactive Gradio Interface**: User-friendly and easy-to-use chatbot interface.

## 🛠️ Technologies Used
- **Python**: Programming language for building the chatbot.
- **Gradio**: To create the interactive user interface.
- **Transformers**: For natural language processing (Intent recognition, Sentiment analysis).
- **Sentence-Transformers**: For matching user queries with predefined cybercrime cases.
- **scikit-learn**: To compute cosine similarity for case matching.
- **Logging**: For tracking errors and actions.

## ⚡ Setup Instructions

### 📝 Prerequisites
1. **Python 3.7 or higher**.
2. Install dependencies via `pip`:
    ```bash
    pip install -r requirements.txt
    ```

### 🚀 Running the Application
1. Clone the repository:
    ```bash
    git clone https://github.com/MokshagnaAnurag/Cybercrime-Reporting-Chatbot.git
    cd cybercrime-reporting-chatbot
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv llama_env
    source llama_env/bin/activate  # On Windows: llama_env\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the chatbot application:
    ```bash
    python app.py
    ```

5. The **Gradio** interface will open in your browser, and you can interact with the chatbot.

## 🎯 Example Query
![Screenshot 2025-01-22 211607](https://github.com/user-attachments/assets/426df59d-7330-49a8-b7e0-48dbd3485d0d)

- **User**: "I received an email asking for my bank account details."
- **Bot Response**:
  - **Intent**: Phishing attempt through email
  - **Sentiment**: Negative
  - **Suggested Action**: Report to the Anti-Phishing Working Group.

## 🤝 Contributing
1. Fork this repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a clear description of your changes.

## 📝 License
This project is licensed under the [MIT License](LICENSE).
