""" RAG + NLI 기반 검증 """

from transformers import pipeline

class FactVerifier:
    def __init__(self):
        self.nli_model = pipeline("text-classification", model="ynie/roberta-large-snli_mnli_fever_anli_R1_R2_R3-nli")

    def verify_with_source(self, claim, evidence_text):
        result = self.nli_model(f"{claim} [SEP] {evidence_text}")
        label = result[0]['label']
        if label == "ENTAILMENT":
            return 1.0
        elif label == "CONTRADICTION":
            return 0.3
        else:
            return 0.6