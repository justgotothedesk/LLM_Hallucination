""" 불확실성 감지 """

import re

class UncertaintyDetector:
    def __init__(self):
        self.uncertain_patterns = ["might", "maybe", "possibly", "uncertain", "not sure", "아마도", "아마", "확실하지 않"]

    def detect(self, text):
        count = sum([1 for word in self.uncertain_patterns if re.search(rf'\b{word}\b', text.lower())])
        return 0.1 * count
