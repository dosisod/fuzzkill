from fuzzkill.fuzzkill import Fuzzkill as fk

class TestFuzzkill:
	def test_url_ctor_applied(self) -> None:
		url="api url"
		fuzzer=fk(url)

		assert fuzzer._target_url==url

	def test_adding_objects(self) -> None:
		objs=[
			False,
			1337,
			{"hello": "world"},
			["hello", "world"],
			"hello"
		]

		fuzzer=fk("api url")

		for obj in objs:
			fuzzer.add(obj)

		assert fuzzer._known_objects==objs

	def test_exit_code_is_0(self) -> None:
		fuzzer=fk("api url")

		try:
			fuzzer.run()

		except(SystemExit) as e:
			assert e.code==0
