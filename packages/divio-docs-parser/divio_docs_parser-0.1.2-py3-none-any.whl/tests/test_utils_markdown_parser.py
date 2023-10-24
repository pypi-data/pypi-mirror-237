import unittest

from .helpers import TEST_README_PARSED as expected_output, test_data_readme_path
from ..divio_docs_parser.utils.markdown_parser import parse_sections_from_markdown, _parse_sections_from_markdown_file, _parse_sections_from_markdown_string
from ..divio_docs_parser.DivioDocs import DivioDocs
from ..divio_docs_parser.constants import *


class TestUtilsMarkdownParser(unittest.TestCase):
    def setUp(self) -> None:
        self.sections = DivioDocs()._sectionObjects
    
    def tearDown(self) -> None:
        self.sections = None
        
    
    def test_parse_all_sections_from_markdown_file(self):
        data = _parse_sections_from_markdown_file(self.sections, test_data_readme_path)
        self.assertDictEqual(data, expected_output)
        
       
    def test_parse_all_sections_from_markdown_string(self):
        with open(test_data_readme_path, "r", encoding="utf-8") as file:
            input = file.read()

        data = _parse_sections_from_markdown_string(self.sections, input)
        self.assertDictEqual(data, expected_output)

    
    def test_parse_all_sections_from_either(self):
        with open(test_data_readme_path, "r", encoding="utf-8") as file:
            test_data_string = file.read()

        inputs = [test_data_readme_path, test_data_string]
        for input in inputs:
            data = parse_sections_from_markdown(self.sections, input)
            self.assertDictEqual(data, expected_output)



if __name__ == "__main__":
    unittest.main()