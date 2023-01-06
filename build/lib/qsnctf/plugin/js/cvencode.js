function assert(){
	for (var _len = arguments.length, express = Array(_len), _key = 0; _key < _len; _key++) {
		express[_key] = arguments[_key];
	}

	var l = express.length;
	var msg = typeof express[l - 1] === "string" ? express[l - 1] : "Assert Error";
	var _iteratorNormalCompletion = true;
	var _didIteratorError = false;
	var _iteratorError = undefined;

	try {
		for (var _iterator = express[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
			var b = _step.value;
			if (!b) {
				throw new Error(msg);
			}
		}
	} catch (err) {
		_didIteratorError = true;
		_iteratorError = err;
	} finally {
		try {
			if (!_iteratorNormalCompletion && _iterator.
			return) {
				_iterator.
				return ();
			}
		} finally {
			if (_didIteratorError) {
				throw _iteratorError;
			}
		}
	}
}

function randBin(){
	return Math.random() >= 0.5;
}

var values = "富强民主文明和谐自由平等公正法治爱国敬业诚信友善";

function str2utf8(str){
	var notEncoded = /[A-Za-z0-9\-\_\.\!\~\*\'\(\)]/g;
	var str1 = str.replace(notEncoded, function(c) {
		return c.codePointAt(0).toString(16);
	});
	var str2 = encodeURIComponent(str1);
	var concated = str2.replace(/%/g, "").toUpperCase();
	return concated;
}

function utf82str(utfs) {
	assert(typeof utfs === "string", "utfs Error");
	var l = utfs.length;

	assert((l & 1) === 0);

	var splited = [];

	for (var i = 0; i < l; i++) {
		if ((i & 1) === 0) {
			splited.push("%");
		}
		splited.push(utfs[i]);
	}

	return decodeURIComponent(splited.join(""));
}

function hex2duo(hexs){
	assert(typeof hexs === "string");

	var duo = [];

	var _iteratorNormalCompletion2 = true;
	var _didIteratorError2 = false;
	var _iteratorError2 = undefined;

	try {
		for (var _iterator2 = hexs[Symbol.iterator](), _step2; !(_iteratorNormalCompletion2 = (_step2 = _iterator2.next()).done); _iteratorNormalCompletion2 = true) {
			var c = _step2.value;

			var n = Number.parseInt(c, 16);
			if (n < 10) {
				duo.push(n);
			} else {
				if (randBin()) {
					duo.push(10);
					duo.push(n - 10);
				} else {
					duo.push(11);
					duo.push(n - 6);
				}
			}
		}
	} catch (err) {
		_didIteratorError2 = true;
		_iteratorError2 = err;
	} finally {
		try {
			if (!_iteratorNormalCompletion2 && _iterator2.
			return) {
				_iterator2.
				return ();
			}
		} finally {
			if (_didIteratorError2) {
				throw _iteratorError2;
			}
		}
	}
	return duo;
}

function duo2hex(duo){
	assert(duo instanceof Array);

	var hex = [];

	var l = duo.length;

	var i = 0;

	while (i < l) {
		if (duo[i] < 10) {
			hex.push(duo[i]);
		} else {
			if (duo[i] === 10) {
				i++;
				hex.push(duo[i] + 10);
			} else {
				i++;
				hex.push(duo[i] + 6);
			}
		}
		i++;
	}
	return hex.map(function(v) {
		return v.toString(16).toUpperCase();
	}).join("");
}

function duo2values(duo){
	return duo.map(function(d) {
		return values[2 * d] + values[2 * d + 1];
	}).join("");
}

function encode(params){
	return duo2values(hex2duo(str2utf8(params)));
};

function decode(encoded){
	var duo = [];

	var _iteratorNormalCompletion3 = true;
	var _didIteratorError3 = false;
	var _iteratorError3 = undefined;

	try {
		for (var _iterator3 = encoded[Symbol.iterator](), _step3; !(_iteratorNormalCompletion3 = (_step3 = _iterator3.next()).done); _iteratorNormalCompletion3 = true) {
			var c = _step3.value;

			var i = values.indexOf(c);
			if (i === -1) {
				continue;
			} else if (i & 1) {
				continue;
			} else {
				duo.push(i >> 1);
			}
		}
	} catch (err) {
		_didIteratorError3 = true;
		_iteratorError3 = err;
	} finally {
		try {
			if (!_iteratorNormalCompletion3 && _iterator3.
			return) {
				_iterator3.
				return ();
			}
		} finally {
			if (_didIteratorError3) {
				throw _iteratorError3;
			}
		}
	}

	var hexs = duo2hex(duo);

	assert((hexs.length & 1) === 0);

	var str = void 0;
	try {
		str = utf82str(hexs);
	} catch (e) {
		throw e;
	}
	return str;
};
