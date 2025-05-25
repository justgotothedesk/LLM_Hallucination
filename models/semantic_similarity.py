""" 의미 유사도 평가 """

from sentence_transformers import SentenceTransformer, util

class SemanticSimilarityEvaluator:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def evaluate(self, user_input, ai_response):
        embeddings = self.model.encode([user_input, ai_response], convert_to_tensor=True)
        score = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
        return round(score, 3)