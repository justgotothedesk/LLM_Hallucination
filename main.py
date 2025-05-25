from models.semantic_similarity import SemanticSimilarityEvaluator
from models.claim_detection import ClaimDetector
from models.fact_verification import FactVerifier
from models.logic_analysis import LogicAnalyzer
from models.source_check import SourceChecker
from models.uncertainty_detector import UncertaintyDetector

class TrustworthinessEvaluator:
    def __init__(self):
        self.sim_eval = SemanticSimilarityEvaluator()
        self.claim_det = ClaimDetector()
        self.fact_ver = FactVerifier()
        self.logic_an = LogicAnalyzer()
        self.source_chk = SourceChecker()
        self.uncertain_det = UncertaintyDetector()

    def evaluate(self, user_input, ai_response):
        score_summary = {}
        # 1. 의미 유사도
        sim_score = self.sim_eval.evaluate(user_input, ai_response)
        score_summary['semantic_similarity'] = sim_score

        # 2. 주장 검출 + 사실성 검증
        claims = self.claim_det.extract_claims(ai_response)
        if claims:
            fact_scores = [self.fact_ver.verify_with_source(c, ai_response) for c in claims]
            fact_score = sum(fact_scores) / len(fact_scores)
        else:
            fact_score = 0.5
        score_summary['fact_verification'] = fact_score

        # 3. 논리성
        logic_score = self.logic_an.evaluate_logic(ai_response)
        score_summary['logic_consistency'] = logic_score

        # 4. 출처 평가
        urls = self.source_chk.extract_sources(ai_response)
        if urls:
            source_scores = [self.source_chk.evaluate_source(u) for u in urls]
            source_score = sum(source_scores) / len(source_scores)
        else:
            source_score = 0.5
        score_summary['source_reliability'] = source_score

        # 5. 불확실성 감지
        uncertainty_penalty = self.uncertain_det.detect(ai_response)
        score_summary['uncertainty_penalty'] = uncertainty_penalty

        # 6. 통합 점수 산출
        total = (
            sim_score * 0.3 +
            fact_score * 0.4 +
            logic_score * 0.15 +
            source_score * 0.1 -
            uncertainty_penalty
        ) * 100
        score_summary['total_score'] = round(total, 2)

        # 등급화
        if total >= 80:
            level = "높은 신뢰"
        elif total >= 60:
            level = "중간 신뢰"
        else:
            level = "낮은 신뢰"
        score_summary['level'] = level
        return score_summary

if __name__ == "__main__":
    evaluator = TrustworthinessEvaluator()
    user_q = "2023년 미국 연준 금리 인상은 경제에 어떤 영향을 미쳤는가?"
    ai_a = "2023년 연준은 금리를 5%로 인상하여 주택 시장이 위축되고 소비가 감소했다."
    result = evaluator.evaluate(user_q, ai_a)
    print(result)

