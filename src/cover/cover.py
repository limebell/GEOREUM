from typing import List, Dict
from coverage.control import Coverage
from coverage.execfile import PyRunner
from coverage.report import get_analysis_to_report
from src.diff.hashcash import hexdigest
from collections import defaultdict
import os

class Line:
    def __init__(self, file_path: str, line_no: int, text: str):
        self.file_path = file_path
        self.line_no = line_no
        self.text = text[:-1]
    def getHash(self):
        return hexdigest(f"{self.file_path}{self.line_no}{self.text}")

    def __str__(self):
        return self.text

    def __int__(self):
        return self.line_no

class Cover:
    
    @staticmethod
    def get_coverage(testcase_path: str, root_path: str) -> Dict[str, Line]:
        """
        Returns Dict of covered line's Line object.
         :param testcase_path: target testcase want to get coverage
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

        
        path = os.path.abspath(testcase_path)
        regular_path = os.path.abspath(root_path)
        covered = defaultdict(Line)

        # path 에 해당하는 .py file run.
        # report 에 covered line 정보 담겨있음.
        cov = Coverage()
        runner = PyRunner([path], as_module=False)
        runner.prepare()
        cov.start()
        runner.run()
        cov.stop()
        cov.save()
        report = get_analysis_to_report(cov,[]) # testcase.py args 없다고 가정.
        
        for fr,analysis in report:
            # report : [(file1, [line1, line2, ...]), (), ...]
            fn = fr.filename
            if regular_path not in fn: continue
            lines = open(fn, 'r').readlines()
            
            for line_no in analysis.statements:

                lo = Line(fr.filename, line_no, lines[line_no-1])
                covered[lo.getHash()] = lo
        return covered


    

    





