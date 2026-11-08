"""CLI for plan-repair-backtracking-engine."""
import sys
import argparse
from .repair import PlanRepairBacktrackingEngine, PlanNode


def main():
    parser = argparse.ArgumentParser(description="Plan Repair Backtracking Engine CLI")
    parser.add_argument("--demo", action="store_true", help="Run plan repair demonstration")
    args = parser.parse_args()

    if args.demo:
        nodes = [
            PlanNode("n1", "download_package"),
            PlanNode("n2", "compile_c_extension", alternatives=["use_precompiled_binary", "run_pure_python_fallback"]),
            PlanNode("n3", "run_integration_tests")
        ]
        engine = PlanRepairBacktrackingEngine(nodes)
        print(f"[*] Initial Plan: {[n.action for n in engine.nodes]}")

        print("[*] Simulating step 'n2' failure...")
        repair = engine.mark_failed("n2")
        print(f"[+] Repaired step 'n2' with alternative action: '{repair}'")
        print(f"[+] Updated Executable Plan: {[n['action'] for n in engine.get_remaining_plan()]}")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
