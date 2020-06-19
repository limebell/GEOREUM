from typing import List, Dict
from coverage.control import Coverage
from coverage.execfile import PyRunner
from coverage.report import get_analysis_to_report
from src.diff.hashcash import hexdigest
from collections import defaultdict
from coverage.misc import NoSource
import os

class Function:
    def __init__(self, file_path:str, name:str, start: int, end: int):
        self.file_path = file_path
        self.name = name
        self.start = start
        self.end = end # line number of the last line that belongs to the function
    
    def __str__(self):
        return f"Function '{self.name}' at file {self.file_path}: {self.start} - {self.end}"
    
    def getHash(self):
        return hexdigest(f"{self.file_path}{self.name}{self.start}{self.end}")

def get_indent(line:str)->int:
    indent = 0
    space_counter = 0
    for char in line:
        if char == "\t":
            indent+=1
        elif char==" ":
            space_counter +=1
        else:
            break
    assert not (indent and space_counter), "inconsistent use of tab and spaces for indentation"
    return max(indent, space_counter//4)

def get_functions(root_path:str)->List[Function]:
        assert root_path.split(".")[-1] =="py", "file is not python file"
        f = open(root_path,"r")

        # initialize
        s = -1
        e = -1
        indent = -1
        name = ""
        functions = []

        lines = f.readlines()
        for l in range(len(lines)):
            line = lines[l]
            if line.lstrip().startswith("def"):
                s = l
                name = line.strip().split()[1].split("(")[0]
                indent = get_indent(line)
            elif s!=-1 and not line.lstrip().startswith("#") and line.strip() != "":
                # condition for the function to end
                if get_indent(line)<=indent:
                    assert e!=-1 and e>s, "function declared, but contains nothing"
                    function = Function(root_path,name,s+1,e+1)
                    functions.append(function)
                    s = -1
                    e = -1
                    name =""
                    indent = -1
                # meaningful line inside the function
                else:
                    e=l
        # function ends at the end of file.
        if s!=-1:
            function = Function(root_path,name, s+1,e+1)
            functions.append(function)
        return functions

class Line:
    def __init__(self, file_path: str, line_no: int, text: str):
        self.file_path = file_path
        self.line_no = line_no
        self.text = text.rstrip()

    def getHash(self):
        return hexdigest(f"{self.file_path}{self.line_no}{self.text}")

    def __str__(self):
        return self.text

    def __int__(self):
        return self.line_no

    def get_file_path(self):
        return self.file_path

class Cover:
    @staticmethod
    def get_coverage(args: list, root_path: str, module_use=False) -> Dict[str, Line]:
        """
        Returns Dict of covered line's Line object.
         :param args: list of module name and target testcase want to get coverage
         :param root_path: target src root want to get coverage
         :return: {
             Line1_hash: {file_path, line_no, line_text},
             Line2_hash: {file_path, line_no, line_text}
         }
        1. cover 한 라인 (file path, line no, line text)
        2. file path 가 root 에 포함되는가.
        2. Line(line text, line no, file path)
        3. res_dict[Line.getHash()] = Line
        4. return res_dict
        """

        regular_path = os.path.abspath(root_path)
        covered = defaultdict(Line)
        
        # path 에 해당하는 .py file run.
        # report 에 covered line 정보 담겨있음.
        cov = Coverage()
        runner = PyRunner(args, as_module=module_use)
        runner.prepare()

        cov.start()
        code_ran = True
        try:
            runner.run()
        except NoSource:
            code_ran = False
            raise
        finally:
            cov.stop()
            if code_ran:
                cov.save()


            # testcase.py args 없다고 가정.
            report = get_analysis_to_report(cov, [])

            for fr, analysis in report:
                # report : [(file1, [line1, line2, ...]), (), ...]
                fn = fr.filename
                if regular_path not in fn:
                    continue

                with open(fn, 'r') as f:
                    lines = f.readlines()
                    for line_no in analysis.executed:
                        lo = Line(fr.filename, line_no, lines[line_no-1])
                        covered[lo.getHash()] = lo
                    f.close()

            return covered

    def get_function_coverage(root_path:str, covered_lines:Dict[str,Line])->Dict[Function,List[Line]]:
        """
        Returns Dict of covered lines organised by the function they belong to.
         :param root_path: target src root want to get coverage
         :return: {
             Function1_Hash: [{file_path,line_no,line_text}, {file_path, line_no, line_text}],
             Function2_Hash: [{file_path,line_no,line_text}, {file_path, line_no, line_text}]
         }
        1. Functions containing at least one covered line will be a key of this dictionary (precisely, its hash will be the key)
        2. All lines in a function that are covered can be found as a list of Line objects, under the key being the hash of the function
        3. Line(line text, line no, file path)
        4. res_dict[Function.getHash()] = List[Line]
        5. return res_dict
        """
        functions = get_functions(root_path)
        covered_function_info = dict()
        lines = list(covered_lines.values())
        for function in functions:
            #file_path, line_no, text
            covered_lines_in_function = []
            for line in lines:
                if line.file_path == function.file_path and line.line_no >= function.start and line.line_no <= function.end:
                    covered_lines_in_function.append(line)
            if len(covered_lines_in_function) > 0:
                covered_function_info[function.getHash()] = covered_lines_in_function

        return covered_function_info
            
            
