from fuzzkill.fuzzers import fuzzed, fuzz_single

from typing import Iterator

class TestFuzzed:
	def test_fuzzed_returns_iter(self) -> None:
		assert isinstance(
			fuzzed({"hello": "world"}),
			Iterator
		)

	def test_fuzz_single_length_gtr_zero(self) -> None:
		assert len(fuzz_single(("some", "thing"))) > 0

	def test_fuzzed_len_is_correct(self) -> None:
		fuzz_size=len(fuzz_single(("some", "thing")))

		data1={"hello": "world", "testing": 123}
		data2={"hello": "world", "testing": 123, "abc": "def"}

		assert len(list(fuzzed(data1))) == fuzz_size ** 2

		assert len(list(fuzzed(data2))) == fuzz_size ** 3
