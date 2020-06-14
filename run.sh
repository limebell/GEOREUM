#!/bin/sh

case $1 in
	save)
		if [ "$#" -eq 2 ]
			then
			python -c "from src.georeum.georeum import Georeum; Georeum.save(\"$2\");"
		elif [ "$#" -eq 3 ]
			then
			python -c "from src.georeum.georeum import Georeum; Georeum.save(\"$2\", \"$3\");"
		else
			echo "Wrong argument"
		fi
	;;

	generate)
		if [ "$#" -eq 3 ]
			then
			python -c "from src.georeum.georeum import Georeum; Georeum.select_test_case(\"$2\", \"$3\");"
		else
			echo "Wrong argument"
		fi
	;;
esac

	
