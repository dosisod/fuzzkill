from simplejson.errors import JSONDecodeError # type: ignore
from collections import namedtuple
from contextlib import suppress
import requests

from typing import Any, Dict

APIResponse=namedtuple("APIResponse", "raw json status")

def probe(url: str, json: Dict[str, Any]) -> APIResponse:
	resp=requests.post(url, json=json)

	resp_json=None
	with suppress(JSONDecodeError):
		resp_json=resp.json()

	return APIResponse(
		status=resp.status_code,
		raw=resp.text,
		json=resp_json
	)
