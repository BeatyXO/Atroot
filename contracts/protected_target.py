# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *

STATUS_IDLE = 0

class ProtectedTarget(gl.Contract):
    owner: Address
    firewall: Address
    release: str
    release_nonce: u256
    consumed: TreeMap[str, bool]

    def __init__(self, firewall: Address, initial_release: str):
        self.owner = gl.message.sender_address
        self.firewall = firewall
        self.release = initial_release
        self.release_nonce = u256(0)

    @gl.public.view
    def get_state(self) -> dict:
        return {"release": self.release, "release_nonce": int(self.release_nonce), "firewall": str(self.firewall)}

    @gl.public.write
    def bind_firewall(self, firewall: Address) -> bool:
        if gl.message.sender_address != self.owner:
            raise gl.vm.UserError("EXPECTED: owner only")
        if self.firewall != Address("0x0000000000000000000000000000000000000000"):
            raise gl.vm.UserError("EXPECTED: firewall already bound")
        self.firewall = firewall
        return True

    @gl.public.write
    def apply_release(self, proposal_key: str, release: str, nonce: u256) -> bool:
        if gl.message.sender_address != self.firewall:
            raise gl.vm.UserError("EXPECTED: only ATROOT may apply a release")
        if self.consumed.get(proposal_key, False):
            raise gl.vm.UserError("EXPECTED: proposal already consumed")
        if int(nonce) != int(self.release_nonce) + 1:
            raise gl.vm.UserError("EXPECTED: invalid release nonce")
        if not release or len(release) > 80:
            raise gl.vm.UserError("EXPECTED: invalid release")
        self.consumed[proposal_key] = True
        self.release = release
        self.release_nonce = nonce
        return True
