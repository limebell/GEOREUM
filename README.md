# GEOREUM
GEREUM is colandering in Korean (거름, /kʌ̹ɾɯm/)

Automated selection of test cases with emphasis on amended fragments.


# How to run
- save coverage & source file
	- ./run.sh save {test case directory} : generates "georeum_coverage.bin", "georeum_source.bin"
	- ./run.sh save {test case directory} {result coverage file name} {result source file name}

	- example) ./run.sh save tests/georeum/pytest01

- select test case
	- ./run.sh generate {coverage file} {source file}

	- example) ./run.sh generate georeum_coverage.bin georeum_source.bin
		- it generates "georeum_test_case"

