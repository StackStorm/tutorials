#!/usr/bin/node


// Offsets into the versions array
var major = 0,
    minor = 1,
    micro = 2;
// This is a bit array - if an element is true, it indicates that it should be
// included in the printed result
var versions = [false, false, false];

// Parse all arguments, filling in the appropriate elements of the versions
// array
process.argv.slice(2).forEach(function (val) {
	if (val === "--major") {
		versions[major] = true;
	} else if (val === "--minor") {
		versions[minor] = true;
	} else if (val === "--micro") {
		versions[micro] = true;
	}
});

var any_versions = versions.some(function (el) { return el; })

var result = "";

// Get the version string, strip it, and split it
// Then iterate over each value, appending the version substring to the output
// string.
// If there weren't any version substrings specified, then append every
// version substring.
process.version.replace(/^v/, '').split('.').forEach(function (val, i) {
	if (versions[i] || !any_versions) {
		result+=(' ' + val);
	}
});

// Finally, strip any beginning or ending whitespace, replace all spaces with
// periods, and print the resulting version string
console.log(result.replace(/^\s*/, '').replace(/\s+/g, '.'));
