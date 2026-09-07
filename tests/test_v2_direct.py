from pathlib import Path
import pytest
from gltest.accounts import create_account

ROOT = Path(__file__).parents[1]
def addr(seed):
    return create_account().address
ZERO = addr("zero")

def test_protected_target_rejects_direct_call(direct_vm, direct_deploy):
    owner = addr("owner")
    target = direct_deploy(ROOT / "contracts" / "protected_target.py", ZERO, "v0.0.0")
    with direct_vm.prank(owner):
        with direct_vm.expect_revert("only ATROOT"):
            target.apply_release("forged", "v9.9.9", 1)

def test_protected_target_rejects_replay(direct_vm, direct_deploy):
    owner = addr("owner")
    firewall = addr("firewall")
    target = direct_deploy(ROOT / "contracts" / "protected_target.py", ZERO, "v0.0.0")
    with direct_vm.prank(owner):
        target.bind_firewall(firewall)
    with direct_vm.prank(firewall):
        target.apply_release("proposal-1", "v1.0.0", 1)
        with direct_vm.expect_revert("proposal already consumed"):
            target.apply_release("proposal-1", "v1.0.0", 1)

def test_target_rejects_stale_execution_sequence(direct_vm, direct_deploy):
    owner = addr("owner")
    firewall = addr("firewall")
    target = direct_deploy(ROOT / "contracts" / "protected_target.py", ZERO, "v0.0.0")
    with direct_vm.prank(owner):
        target.bind_firewall(firewall)
    with direct_vm.prank(firewall):
        with direct_vm.expect_revert("invalid release nonce"):
            target.apply_release("proposal-1", "v1.0.0", 9)
