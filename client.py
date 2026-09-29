"""Reciprocal Rank Fusion (RRF) Multi-Retriever Rank Aggregator.
100% Python Standard Library.
"""

import collections

class ReciprocalRankFusion:
    """Reciprocal Rank Fusion (RRF) rank aggregator."""
    def __init__(self, k=60):
        self.k = k

    def fuse(self, rankings_list):
        scores = collections.defaultdict(float)
        item_details = {}
        for ranking in rankings_list:
            for rank, item in enumerate(ranking, 1):
                item_id = item["id"] if isinstance(item, dict) else item
                scores[item_id] += 1.0 / (self.k + rank)
                if isinstance(item, dict):
                    item_details[item_id] = item
        sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [{"id": item_id, "rrf_score": score, "data": item_details.get(item_id)} for item_id, score in sorted_items]
