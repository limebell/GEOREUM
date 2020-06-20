from src.cover.cover import Cover
from src.diff.hashcash import hexdigest, hashcash
from src.diff.diff import Diff, DiffFormat, DiffReport, DiffError
from src.util.format import print_formatter
import os
from shutil import copyfile
from pathlib import Path
import pickle

class CoverObject:
	#TODO delete this class and change src.cover.cover
	def __init__(self, file_path: str, covered: list):
		self.file_path = file_path
		self.covered = covered
		
class Module:
	def __init__(self, file_path: str):
		self.file_path = file_path
		# read file & save hashed string
		with open(file_path) as ff:
			text = ff.read()

		# TODO hashcash return exception for empty string, but it needed
		if text is None or text=="":
			self.hashed = ""
		else:
			self.hashed = hashcash(text.splitlines(1))

class Georeum:

	@staticmethod
	def search_py_file(target_directory: str):
		# find all of py file in target_directory
		target_file_list = []
		try:
			filenames = os.listdir(target_directory)
			for filename in filenames:
				full_filename = os.path.join(target_directory, filename)
				if os.path.isdir(full_filename):
					target_file_list.extend(Georeum.search_py_file(full_filename))
				else:
					ext = os.path.splitext(full_filename)[-1]
					if ext == '.py':
						target_file_list.append(full_filename)
		except PermissionError:
			pass

		return target_file_list

	@staticmethod
	def save(target_directory: str, coverage_result_file: str = "", source_save_file: str = ""):
		root_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../")
		# TODO should manage dir_path for real tool release

		# 1. searh py file at target_directory & select target test file
		target_file_list = Georeum.search_py_file(target_directory)
		covered_list = []
		for target_file in target_file_list:
			# 2. get coverage for each file
			file_path = os.path.join(root_directory, target_file)
			covered = Cover.get_coverage(args=['pytest', file_path], root_path = root_directory, module_use =True)
			covered_list.append(CoverObject(file_path, covered))

		# 3. save coverage object list to data
		if coverage_result_file=="":
			pickle.dump(covered_list, open('georeum_coverage.bin', 'wb'))
		else:
			pickle.dump(covered_list, open(coverage_result_file, 'wb'))

		#4. find all of source file and hash
		source_file_name_list = Georeum.search_py_file(root_directory)
		source_file_list = []
		for source_file_name in source_file_name_list:
			source_file_list.append(Module(source_file_name))

		# 5. save all of hashed source file
		if source_save_file=="":
			pickle.dump(source_file_list, open('georeum_source.bin', 'wb'))
		else:
			pickle.dump(source_file_list, open(source_save_file, 'wb'))

	@staticmethod
	def select_test_case(coverage_data: str, source_data: str):
		root_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../")
		# TODO should manage dir_path for real tool release

		# get latest code coverage
		coverObject_list = pickle.load(open(coverage_data, 'rb'))
		# get latest source code
		latest_source_file_list = pickle.load(open(source_data, 'rb'))

		# get current source code
		source_file_name_list = Georeum.search_py_file(root_directory)
		current_source_file_list=[]
		for source_file_name in source_file_name_list:
			current_source_file_list.append(Module(source_file_name))
		
		# find diff of all source code & generate test cases
		Path('georeum_test_case').mkdir(parents=True, exist_ok=True)
		for current_source_file in current_source_file_list:
			exist = False
			df = DiffFormat("tmp")
			for latest_source_file in latest_source_file_list:
				if current_source_file.file_path==latest_source_file.file_path:
					exist = True
					Diff.analyze(df, current_source_file.hashed, latest_source_file.hashed)
					break

			print(f"[DF Test] : {current_source_file.file_path} : {df.modified()}")
			if not exist:
				continue
			if not df.modified():
				continue
			else:
				added = False
				target_line_list = []
				target_line_list.extend(df.added)
				target_line_list.extend(df.removed)
				for line in target_line_list:
					if added:
						break
					for coverObject in coverObject_list:
						if added:
							break
						for covered in coverObject.covered.values():
							if added:
								break
							if os.path.normpath(covered.file_path)==os.path.normpath(current_source_file.file_path):
								if covered.line_no==line:
									added = True
									copyfile(coverObject.file_path, 'georeum_test_case/' + os.path.basename(coverObject.file_path))
									break

		return

	@staticmethod
	def run_test_cases(georeum_test_case_script_path : str) -> None:
		# 1. select_test_case should done before calling this function.
		# 2. run just selected_test_cases
		@print_formatter
		def run(formatting: list, test_cases : list, tester : str = 'pytest') -> None:
			if tester == 'pytest':
				import pytest
				pytest.main(['-x', *test_cases])
			elif tester == 'unittest':
				from unittest import TestLoader, TestCase, TestResult
				runner = TestLoader()
				test_suite = runner.loadTestsFromTestCase(*test_cases)
				test_result = TestResult()
				test_suite.run(test_result)

		with open(georeum_test_case_script_path, 'rb') as tcsp:
			loaded = pickle.load(tcsp)
			test_cases = loaded[:-1]
			tester = loaded[-1]
			run(test_cases, test_cases, tester = tester)
		pass

	@staticmethod
	def run_test_cases_with_coverage_update(target_directory: str, generate_test_case : str, coverage_data: str, source_data: str) -> None:
		# 1. select_test_case should done before calling this function.
		# 2. run selected_test_cases by Georeum.save
		Georeum.save(target_directory, coverage_data, source_data)
		pass

	

			
