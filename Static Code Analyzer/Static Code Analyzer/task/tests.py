from hstest.stage_test import *
from hstest.test_case import TestCase


class AnalyzerTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase(stdin="test/single_line_valid_example.py", attach=1),
                TestCase(stdin="test/single_long_line_example.py", attach=2),
                TestCase(stdin="test/multiple_long_lines.py", attach=3)]

    def test_1(self, output):
        if output != "":
            return CheckResult.wrong("Your program warned a style error in the correct file."
                                     "There was no any rows with string length more than 79 symbols.")
        return CheckResult.correct()

    def test_2(self, output: str):
        output = output.strip().lower().splitlines()
        if not len(output) == 1:
            return CheckResult.wrong("A wrong number of warning messages. "
                                     "Your program should warn only about one mistake")
        if not output[0].startswith("line 1: s001"):
            return CheckResult.wrong("Incorrect format of the warning message.")
        return CheckResult.correct()

    def test_3(self, output: str):
        output = output.strip().lower().splitlines()
        if not len(output) == 2:
            return CheckResult.wrong("A wrong number of warning messages. "
                                     "Your program should warn about two mistakes in this test case")
        if not output[0].startswith("line 3: s001"):
            return CheckResult.wrong("Incorrect format of the warning message.")
        if not output[1].startswith("line 5: s001"):
            return CheckResult.wrong("Incorrect format of the warning message.")
        return CheckResult.correct()

    def check(self, reply: str, attach) -> CheckResult:
        if attach == 1:
            output = self.test_1(reply)
        elif attach == 2:
            output = self.test_2(reply)
        elif attach == 3:
            output = self.test_3(reply)
        else:
            return CheckResult.wrong("Unknown error")

        return output


if __name__ == '__main__':
    AnalyzerTest("analyzer.code_analyzer").run_tests()
