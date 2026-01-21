import unittest
from gen_content import extract_title

class TestUtils(unittest.TestCase):
    def test_extract_title(self):
        md = """
            # this is an h1

            this is paragraph text

            ## this is an h2
            """
        title = extract_title(md)
        self.assertEqual(
            title,
            "this is an h1"
        )
    
    def test_extract_title_in_middle(self):
        md = """
            this is paragraph text
            
             # this is an h1

            ## this is an h2
            """
        title = extract_title(md)
        self.assertEqual(
            title,
            "this is an h1"
        )
    def test_eq_double(self):
        actual = extract_title(
            """
            # This is a title

            # This is a second title that should be ignored
            """
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = extract_title(
            """
            # title

            this is a bunch

            of text

            - and
            - a
            - list
            """
                    )
        self.assertEqual(actual, "title")

    def test_none(self):
        try:
            extract_title(
                """
                no title
                """
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass


if __name__ == "__main__":
    unittest.main()