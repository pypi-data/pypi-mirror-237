try:
    # For python >= 3.8
    from typing import TypedDict
except ImportError:
    # For python 3.7
    from typing_extensions import TypedDict


class Operator(TypedDict):
    index: int
    active: bool
    name: str
    rewardAddress: str
    stakingLimit: int
    stoppedValidators: int
    totalSigningKeys: int
    usedSigningKeys: int


class OperatorKey(TypedDict):
    index: int
    operator_index: int
    key: bytes
    depositSignature: bytes
    used: bool
