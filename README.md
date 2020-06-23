# GEOREUM
GEREUM is colandering in Korean (거름, /kʌ̹ɾɯm/)

Automated selection of test cases with emphasis on amended fragments.


# How to run
- save coverage & source file
	- ./run.sh save {project_root_path} {test_path} : generates ".cache/coverage.bin", ".cache/cache.pkl"

- select test case
	- ./run.sh generate {project_root_path} {test_path} : returns test cases to be executed

- select test case and run
	- ./run.sh execute {project_root_path} {test_path} : run test cases which is get from "generate" command

- example
	- copy 'source.py_before' to 'source.py' in 'GEOREUM/tests/georeum/source/'
	- ./run.sh save tests/georeum/pytest01
		- "georeum_coverage.bin", "georeum_source.bin" generated		
	- copy 'source.py_after' to 'source.py' in 'GEOREUM/tests/georeum/source/'
	- ./run.sh generate georeum_coverage.bin georeum_source.bin
		- "georeum_test_case" directory generated
