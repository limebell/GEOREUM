#!/bin/sh

case $1 in
	save)
		if [ "$#" -eq 3 ]
			then
			python -c "from musttest.georeum.georeum import Georeum; georeum = Georeum(\"$2\", \"$3\"); georeum.save();"
		else
			echo "Wrong argument: Requires 3 arguments (action[save/generate], root_path(absolute path), test_path(absolute path))"
		fi
	;;

	generate)
		if [ "$#" -eq 3 ]
			then
			python -c "from musttest.georeum.georeum import Georeum; georeum = Georeum(\"$2\", \"$3\"); georeum.select_test_case();"
		else
			echo "Wrong argument: Requires 3 arguments (action[save/generate], root_path(absolute path), test_path(absolute path))"
		fi
	;;

	execute)
		if [ "$#" -eq 3 ]
			then
			python -c "from musttest.georeum.georeum import Georeum; georeum = Georeum(\"$2\", \"$3\"); georeum.select_test_case();\
			georeum.test_run();"
		else
			echo "Wrong argument: Requires 3 arguments (action[save/generate], root_path(absolute path), test_path(absolute path))"
		fi
	;;
esac

	
