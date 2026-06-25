import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import server

def test_rank_and_route():
    server.record_result("opus-4.8", "t", 0.9); server.record_result("opus-4.8", "t", 0.94)
    server.record_result("deepseek-v4", "t", 0.8)
    lb = server.leaderboard("t")
    assert lb.ranked[0].model == "opus-4.8"
    assert server.best_for("t")["best"] == "opus-4.8"

def test_bft_vote():
    v = server.bft_vote("t", [{"model": "opus-4.8", "output": "A"}, {"model": "deepseek-v4", "output": "B"}])
    assert v.winner in ("opus-4.8", "deepseek-v4")
    assert v.method.startswith("score")

def test_ingest():
    assert "lmarena" in server.ingest_public("all")["sources"]
