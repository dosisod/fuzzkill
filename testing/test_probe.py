from flask_testing import LiveServerTestCase # type: ignore
from flask import Flask, request

from fuzzkill.probe import probe

from typing import Dict, Any, cast

"""
Flask-Testing does what i need, but it is old.
I plan on forking and fixing it, then using it here.
In the meantime, you will need to replace:

from werkzeug import cached_property
# with this:
from werkzeug.utils import cached_property

in file `.venv/lib/python3.X/site-packages/flask_testing/utils.py`
"""

class TestProbe(LiveServerTestCase):
	def create_app(self) -> Flask:
		app=Flask(__name__)

		@app.route("/echo", methods=["POST"])
		def echo() -> Dict[str, Any]:
			return cast(
				Dict[str, Any],
				request.json
			)

		@app.route("/html", methods=["POST"])
		def html() -> str:
			return "<p>this is not json</p>"

		return app

	def test_echoed_json_returns_json(self) -> None:
		resp=probe(
			"http://127.0.0.1:5000/echo",
			{"hello":"world"}
		)

		assert resp.status==200
		assert resp.raw
		assert resp.json

	def test_non_json_response_nulls_json(self) -> None:
		resp=probe(
			"http://127.0.0.1:5000/html",
			{"hello":"world"}
		)

		assert resp.status==200
		assert resp.raw
		assert not resp.json
