from flask import request, jsonify
from flask_restful import Resource
from app import api, app
from app.rest_api.api_resources.api_decorators import *

@app.route("/api/test")
@api_check_auth
@api_require("test", int)
def test_api():
		return jsonify({"status": True, "msg": "test"})


@app.route("/api/version")
def api_version():
	version_report = {}
	version_report['version'] = "TESTING"
	return jsonify(version_report)




