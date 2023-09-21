from lib.calculate_rpm import *

"""
Given 200 word string
It returns "1 minute"
"""
def test_given_200_word_string_returns_1_minute():
    string_with_200_words = """
        Python is a versatile and popular programming language. It is known for its simplicity and readability, making it an excellent choice for both beginners and experienced developers. Python's extensive standard library and a vast ecosystem of third-party packages make it suitable for a wide range of applications, from web development and data analysis to scientific computing and artificial intelligence.

        One of Python's key features is its elegant and straightforward syntax, emphasizing code readability and maintainability. Indentation is used for code blocks, reducing the need for braces or semicolons, which can clutter code in other languages.

        Python's dynamic typing allows developers to write code more quickly and flexibly, but it's essential to use type hints when necessary to enhance code robustness and understandability.

        Python's community is active and supportive, with numerous online resources, forums, and tutorials available to help you learn and solve problems. Many large companies, including Google, Facebook, and NASA, rely on Python for their projects.

        In conclusion, Python is a powerful and accessible language that can empower you to create a wide range of applications and solve complex problems while enjoying a vibrant and welcoming developer community.
        """

    actual = calculate_rpm(string_with_200_words)
    expected = "1 minute"

    assert actual == expected