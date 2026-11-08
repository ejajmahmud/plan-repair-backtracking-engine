"""Unit tests for plan-repair-backtracking-engine."""
import unittest
from plan_repair_backtracking_engine.repair import PlanRepairBacktrackingEngine, PlanNode


class TestPlanRepairBacktrackingEngine(unittest.TestCase):
    def test_repair_with_alternative(self):
        nodes = [PlanNode("1", "act_a", alternatives=["fallback_a"])]
        engine = PlanRepairBacktrackingEngine(nodes)
        rep = engine.mark_failed("1")
        self.assertEqual(rep, "fallback_a")
        self.assertEqual(engine.nodes[0].action, "fallback_a")

    def test_repair_exhausted(self):
        nodes = [PlanNode("1", "act_a", alternatives=[])]
        engine = PlanRepairBacktrackingEngine(nodes)
        rep = engine.mark_failed("1")
        self.assertIsNone(rep)
        self.assertTrue(engine.nodes[0].failed)
