import gradio as gr
import logging
import json
import numpy as np
from transformers import pipeline
from datetime import datetime
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


class CyberCrimeChatbot:
    """A chatbot to help users recognize and report cybercrimes."""

    def __init__(self):
        self.setup_logging()
        self.session_history = []
        self.load_templates()
        self.intent_recognizer = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.cases_database = self.load_case_database()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("cyber_crime_chatbot.log"),
                logging.StreamHandler(),
            ],
        )
        self.logger = logging.getLogger(__name__)

    def load_templates(self):
        self.templates = {
            "success": "Your query has been processed successfully!",
            "failure": "There was an issue processing your query. Please try again.",
        }

    def load_case_database(self):
        """Loads predefined cases for CBR analysis."""
        return [
            {"case_id": 1, "description": "Phishing attempt through email", "action": "Report to the Anti-Phishing Working Group."},
            {"case_id": 2, "description": "Online identity theft", "action": "Contact your local cybercrime division."},
            {"case_id": 3, "description": "Cyberstalking", "action": "File a complaint with law enforcement and secure evidence."}
        ]

    def process_user_query(self, query: str) -> dict:
        """Processes the user's query and determines the appropriate action."""
        try:
            # Intent recognition
            intent = self.intent_recognizer(query)
            self.logger.info(f"Intent detected: {intent[0]['label']}")

            # Sentiment analysis
            sentiment = self.sentiment_analyzer(query)
            self.logger.info(f"Sentiment detected: {sentiment[0]['label']}")

            # CBR matching
            embedding_query = self.embedding_model.encode([query])
            embeddings_db = self.embedding_model.encode([case["description"] for case in self.cases_database])
            similarities = cosine_similarity(embedding_query, embeddings_db)[0]
            best_match_index = similarities.argmax()
            matched_case = self.cases_database[best_match_index]
            self.logger.info(f"Best matched case: {matched_case}")

            return {
                "intent": intent[0],
                "sentiment": sentiment[0],
                "matched_case": matched_case,
                "similarity_score": float(similarities[best_match_index])  # Ensure compatibility with JSON serialization
            }
        except Exception as e:
            self.logger.error(f"Error processing user query: {e}")
            raise

    def generate_report(self, query, results, output_path="cyber_crime_report.json") -> str:
        """Generates a report summarizing the query and analysis results."""
        try:
            # Sanitize results for JSON serialization
            sanitized_results = {
                key: float(value) if isinstance(value, (np.float32, np.float64)) else value
                for key, value in results.items()
            }

            report = {
                "timestamp": str(datetime.now()),
                "query": query,
                "results": sanitized_results,
            }
            with open(output_path, "w") as report_file:
                json.dump(report, report_file, indent=2)
            self.logger.info(f"Report saved to {output_path}")
            return output_path
        except Exception as e:
            self.logger.error(f"Error generating report: {e}")
            raise


def create_interface():
    chatbot = CyberCrimeChatbot()

    with gr.Blocks() as interface:
        gr.Markdown("# Cybercrime Reporting Chatbot")
        with gr.Row():
            user_input = gr.Textbox(label="Enter your query", placeholder="Describe your cybercrime issue...")
        with gr.Row():
            analyze_button = gr.Button("Analyze Query")
        with gr.Row():
            output_text = gr.Textbox(label="Analysis Results", interactive=False, lines=6)
        with gr.Row():
            output_file = gr.File(label="Download Report")

        def process_query(query):
            try:
                results = chatbot.process_user_query(query)
                report_path = chatbot.generate_report(query, results)
                response = (
                    f"**Intent:** {results['intent']['label']}\n"
                    f"**Sentiment:** {results['sentiment']['label']}\n"
                    f"**Suggested Action:** {results['matched_case']['action']}\n"
                    f"**Similarity Score:** {results['similarity_score']:.2f}"
                )
                return response, report_path
            except Exception as e:
                return f"Error: {e}", None

        analyze_button.click(
            process_query,
            inputs=[user_input],
            outputs=[output_text, output_file],
        )

    return interface


if __name__ == "__main__":
    interface = create_interface()
    interface.launch(share=True)
