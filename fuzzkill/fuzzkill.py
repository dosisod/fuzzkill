from typing import List, NoReturn

class Fuzzkill:
	_target_url: str
	_known_objects: List[object]=[]

	def __init__(self, target_url: str) -> None:
		self._target_url=target_url

	def add(self, data: object) -> None:
		self._known_objects.append(data)

	def run(self) -> NoReturn:
		print("Fuzzing [", self._target_url, "]")

		exit(0)