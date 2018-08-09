#!/bin/bash

MAJOR=""
MINOR=""
MICRO=""

# Parse arguments
while [[ $# -gt 0 ]]; do
	case "$1" in
		--major)
			MAJOR=$(bash --version \
			  | grep 'GNU bash, version' \
			  | awk '{ print $4 }' \
			  | sed 's/\([[:digit:]]\{1,\}\)\.\([[:digit:]]\{1,\}\)\.\([[:digit:]]\{1,\}\).*/\1/')
			shift
			;;
		--minor)
			MINOR=$(bash --version \
			  | grep 'GNU bash, version' \
			  | awk '{ print $4 }' \
			  | sed 's/\([[:digit:]]\{1,\}\)\.\([[:digit:]]\{1,\}\)\.\([[:digit:]]\{1,\}\).*/\2/')
			shift
			;;
		--micro)
			MICRO=$(bash --version \
			  | grep 'GNU bash, version' \
			  | awk '{ print $4 }' \
			  | sed 's/\([[:digit:]]\{1,\}\)\.\([[:digit:]]\{1,\}\)\.\([[:digit:]]\{1,\}\).*/\3/')
			shift
			;;
		*)
			echo "Unrecognized argument: $1"
			echo "Usage: $0 [flag [flag]]"
			echo ""
			echo "Flags:"
			echo "  --major  - include the major version substring"
			echo "  --minor  - include the minor version substring"
			echo "  --micro  - include the micro/bugfix version substring"
			echo ""
			echo "One or more flags can be passed in, and the same flag passed"
			echo "in more than once has no further effect."
			echo "If no flags are passed in, the entire original version string"
			echo "is printed."
			exit -1
			;;
	esac
done

if [[ -n "$MAJOR" || -n "$MINOR" || -n "$MICRO" ]]; then
	# The *_VERSION variables are either the version substring or are empty,
	# so we join them all together with spaces, then strip off beginning and
	# ending spaces, and finally replace any remaining spaces with periods.
	echo " $MAJOR $MINOR $MICRO " \
	  | sed 's/^ \{0,\}//' \
	  | sed 's/ \{0,\}$//' \
	  | sed 's/ \{1,\}/./g'
else
	# If we weren't passed any flags, just print the entire version string
	bash --version \
	  | grep 'GNU bash, version' \
	  | awk '{ print $4 }'
fi
