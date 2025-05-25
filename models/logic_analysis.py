""" 논리 구조 분석 """

import spacy
from nltk.parse import DependencyGraph

class LogicAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def evaluate_logic(self, response):
        doc = self.nlp(response)
        premises, conclusions = 0, 0
        for sent in doc.sents:
            if "because" in sent.text or "due to" in sent.text:
                premises += 1
            if "therefore" in sent.text or "thus" in sent.text:
                conclusions += 1
        logic_score = min(premises, conclusions) / max(1, len(list(doc.sents)))
        return round(logic_score, 3)
