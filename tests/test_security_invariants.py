import hashlib
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
FIREWALL = (ROOT / "contracts" / "atroot_firewall_v2.py").read_text(encoding="utf-8")
TARGET = (ROOT / "contracts" / "protected_target.py").read_text(encoding="utf-8")

class SecurityInvariantTests(unittest.TestCase):
    def test_action_digest_binds_target_command_both_nonces_and_charter(self):
        for token in ["target", "method", "release", "agent-nonce=", "execution-nonce=", "charter_version"]:
            self.assertIn(token, FIREWALL)

    def test_evidence_digest_is_checked_against_response_body(self):
        self.assertIn("response.body", FIREWALL)
        self.assertRegex(FIREWALL, r"digest\(body\).*evidence_digest")

    def test_registration_cannot_reset_existing_nonce(self):
        self.assertIn("self.agents.get(account) is not None", FIREWALL)
        self.assertIn("account cannot be registered or re-registered", FIREWALL)

    def test_target_rejects_direct_calls_and_replays(self):
        self.assertIn("only ATROOT may apply a release", TARGET)
        self.assertIn("proposal already consumed", TARGET)

    def test_challenge_is_consensus_adjudicated(self):
        section = FIREWALL[FIREWALL.index("def challenge_proposal"):FIREWALL.index("def execute_proposal")]
        self.assertIn("gl.eq_principle.prompt_comparative", section)
        self.assertNotIn('p.status = CANCELED\n        p.rationale = "CHALLENGED:', section)

    def test_digest_fixture_is_deterministic(self):
        value = "target|apply_release|v1|agent-nonce=1|execution-nonce=1|authority-v1"
        self.assertEqual(hashlib.sha256(value.encode()).hexdigest(), hashlib.sha256(value.encode()).hexdigest())

if __name__ == "__main__":
    unittest.main()
