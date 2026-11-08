"""Core Plan Repair Backtracking Engine implementation."""
from typing import List, Dict, Optional, Any


class PlanNode:
    def __init__(self, node_id: str, action: str, alternatives: Optional[List[str]] = None):
        self.node_id = node_id
        self.action = action
        self.alternatives = alternatives or []
        self.executed = False
        self.failed = False


class PlanRepairBacktrackingEngine:
    def __init__(self, plan_nodes: List[PlanNode]):
        self.nodes = list(plan_nodes)

    def mark_failed(self, node_id: str) -> Optional[str]:
        target = next((n for n in self.nodes if n.node_id == node_id), None)
        if not target:
            return None
        target.failed = True

        # Check if alternative exists for this node
        if target.alternatives:
            replacement_action = target.alternatives.pop(0)
            target.action = replacement_action
            target.failed = False
            return replacement_action
        return None

    def get_remaining_plan(self) -> List[Dict[str, Any]]:
        return [
            {"id": n.node_id, "action": n.action, "executed": n.executed, "failed": n.failed}
            for n in self.nodes if not n.executed
        ]
