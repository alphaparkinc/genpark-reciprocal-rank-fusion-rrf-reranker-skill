import sys
import json
from client import ReciprocalRankFusion

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-reciprocal-rank-fusion-rrf-reranker-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "fuse_rankings_rrf",
                        "description": "Fuse multiple ranked lists using Reciprocal Rank Fusion",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "rankings_list": {
                                    "type": "array",
                                    "items": {"type": "array", "items": {"type": "object"}},
                                    "description": "List of ranked search results from different retrievers"
                                },
                                "k_constant": {"type": "integer", "default": 60}
                            },
                            "required": ["rankings_list"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "fuse_rankings_rrf":
            ranks = args.get("rankings_list", [])
            k = args.get("k_constant", 60)
            rrf = ReciprocalRankFusion(k=k)
            fused = rrf.fuse(ranks)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps({"fused_rankings": fused})}]
                }
            }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
