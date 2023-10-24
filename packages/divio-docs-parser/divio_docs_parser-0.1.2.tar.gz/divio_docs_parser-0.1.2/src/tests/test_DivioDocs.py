import unittest

from .helpers import test_data_readme_path as readme_path, TEST_README_PARSED, test_data_dir, test_data_tutorials_path

from ..divio_docs_parser.DivioDocs import DivioDocs
from ..divio_docs_parser.constants import ID_TUTORIALS


class TestDivioDocs(unittest.TestCase):
    
    def test_empty_init(self):
        docs = DivioDocs()
        
        self.assertDictEqual(docs.tutorials, {})
        self.assertDictEqual(docs.how_to_guides, {})
        self.assertDictEqual(docs.explanation, {})
        self.assertDictEqual(docs.reference, {})

    def test_init_with_input(self):
        docs = DivioDocs(readme_path)

        self.assertEqual(docs.tutorials["README.md"], TEST_README_PARSED["tutorials"])
        


    def test_get(self):
        docs = DivioDocs()
        docs.tutorials = {"README.md": "Data"}
        self.assertEqual(docs._get(ID_TUTORIALS, "README.md"), "Data")

    def test_set_undefined_key(self):
        docs = DivioDocs()
        docs._set(ID_TUTORIALS, "README.md", "New data")
        
        self.assertEqual(docs.tutorials["README.md"], "New data")

    def test_set_existing_key(self):
        docs = DivioDocs()
        docs.tutorials = {"README.md": "old data"}
        docs._set(ID_TUTORIALS, "README.md", "New data")
        
        self.assertEqual(docs._get(ID_TUTORIALS, "README.md"), "New data")

    def test_append(self):
        docs = DivioDocs()
        docs.tutorials = {"README.md": "123"}
        docs._append(ID_TUTORIALS, "README.md", "456")

        self.assertEqual(docs._get(ID_TUTORIALS, "README.md"), "123456")

    def test_prepend(self):
        docs = DivioDocs()
        docs.tutorials = {"README.md": "456"}
        docs._prepend(ID_TUTORIALS, "README.md", "123")

        self.assertEqual(docs._get(ID_TUTORIALS, "README.md"), "123456")

    def test_joined(self):
        docs = DivioDocs()
        docs.tutorials = {"README.md": "123", "Tutorials.md": "456"}

        joined = docs.section_without_filenames(ID_TUTORIALS)
        self.assertListEqual(joined, ["123", "456"])
    

    def test_import_docs_single(self):
        docs = DivioDocs().import_docs(readme_path)

        self.assertEqual(docs.tutorials["README.md"], TEST_README_PARSED["tutorials"])

        self.assertIsNone(docs.tutorials.get("extra/Tutorials.md")) 
        docs.import_docs(test_data_tutorials_path)
        self.assertEqual(docs.tutorials["extra/Tutorials.md"], """# Extra file
## Extra content
For a different test""")

    
    def test_import_docs_multiple(self):
        docs = DivioDocs().import_docs(test_data_dir)

        self.assertEqual(docs.tutorials["README.md"], TEST_README_PARSED["tutorials"])
        self.assertEqual(docs.tutorials["extra/Tutorials.md"], """# Extra file
## Extra content
For a different test""")
    

    def test_embed_relative_files(self):
        docs = DivioDocs().import_docs(test_data_dir, embed_relative_files=True)

        tutorial_content = docs.tutorials["README.md"]
        for tag in ["<svg", "<img alt=\"A cute picture of a cat\"", "<details><summary>External markdown file</summary>"]:
            self.assertTrue(tag in tutorial_content, f"{tag} not found in tutorial_content")



if __name__ == "__main__":
    unittest.main()