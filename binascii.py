import binascii
from hypothesis import assume
from hypothesis import given
from hypothesis import settings
from hypothesis import strategies as st


@given(st.binary(), st.booleans(), st.integers(), st.integers(), st.booleans())
@settings(print_blob=True)
def binascii_b2a_ascii85(data: bytes, foldspaces: bool, wrapcol: int, pad: int, adobe: bool) -> None:
    assume(len(data) <= wrapcol)
    binascii.b2a_ascii85(data, foldspaces=foldspaces, wrapcol=wrapcol, pad=pad, adobe=adobe)


# Exposes the Hypothesis fuzz target for integrating with OSS-Fuzz.
FuzzerRunOne = binascii_b2a_ascii85.hypothesis.fuzz_one_input
