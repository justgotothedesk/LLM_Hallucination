""" 주장 탐지 및 질문 생성 """

from transformers import pipeline

class ClaimDetector:
    def __init__(self):
        self.classifier = pipeline("text-classification", model="ynie/roberta-large-snli_mnli_fever_anli_R1_R2_R3-nli")

    def extract_claims(self, text):
        sentences = text.split('.')
        claims = [s.strip() for s in sentences if self.classifier(s)[0]['label'] == "ENTAILMENT"]
        return claims

    def generate_questions(self, claim):
        return f"{claim.strip()}가 사실인가?"