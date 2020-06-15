# GEOREUM
GEREUM is colandering in Korean (거름, /kʌ̹ɾɯm/)

Automated selection of test cases with emphasis on amended fragments.


# How to run
- save coverage & source file
	- ./run.sh save {test case directory} : generates "georeum_coverage.bin", "georeum_source.bin"
	- ./run.sh save {test case directory} {result coverage file name} {result source file name}

- select test case
	- ./run.sh generate {coverage file} {source file}

- example
	- copy 'source.py_before' to 'source.py' in 'GEOREUM/tests/georeum/source/'
	- ./run.sh save tests/georeum/pytest01
		- "georeum_coverage.bin", "georeum_source.bin" generated		
	- copy 'source.py_after' to 'source.py' in 'GEOREUM/tests/georeum/source/'
	- ./run.sh generate georeum_coverage.bin georeum_source.bin
		- "georeum_test_case" directory generated
