from client import ReciprocalRankFusion

rrf = ReciprocalRankFusion(k=60)
bm25_list = [{"id": "docA", "title": "Database Internals"}, {"id": "docB", "title": "Network Protocols"}]
vector_list = [{"id": "docB", "title": "Network Protocols"}, {"id": "docC", "title": "Compiler Design"}]

fused_ranks = rrf.fuse([bm25_list, vector_list])
for item in fused_ranks:
    print(f"Rank Item: {item['id']} | RRF Score: {item['rrf_score']:.6f}")
