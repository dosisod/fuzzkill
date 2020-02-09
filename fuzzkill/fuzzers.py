from collections import ChainMap
import itertools

from typing import Iterable, Dict, Any, List, Tuple, Union

def fuzzed(json: Dict[str, Any]) -> Iterable[Dict[str, Any]]:
	fuzzy_lists=[]

	for item in json.items():
		fuzzy_lists.append(
			fuzz_single(item)
		)

	for fuzzy_list in itertools.product(*fuzzy_lists):
		yield dict(ChainMap(*fuzzy_list))

def fuzz_single(obj: Tuple[str, Any]) -> List[Dict[str, Any]]:
	return [
		{ obj[0]: obj[1] },
		{ obj[0]: "" },
		{ obj[0]: 0 },
		{ obj[0]: False },
		{ obj[0]: [] },
		{ obj[0]: {"":""} },
		{ obj[0]: None }
	]
