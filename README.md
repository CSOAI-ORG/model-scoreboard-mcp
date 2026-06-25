# model-scoreboard-mcp

mcp-name: io.github.CSOAI-ORG/model-scoreboard-mcp

The **track-record hive** — constantly ranks models/agents so the OS routes to the bleeding edge.

**Tools:** register_model · record_result · leaderboard · best_for · bft_vote · ingest_public

Fed by the live telemetry loop + ingested public benchmarks (LMArena/OpenRouter/Artificial Analysis/HELM/SWE-bench). The BFT vote is the "ralph" improve loop; best_for is the router.

```bash
pip install -e .
python server.py
```
