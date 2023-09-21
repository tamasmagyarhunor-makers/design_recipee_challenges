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

"""
Given 300 word string
It returns "2 minutes"
"""
def test_given_300_word_string_returns_1_minute():
    string_with_300_words = """
        Python is a versatile, high-level programming language known for its simplicity, readability, and wide range of applications. Developed by Guido van Rossum and first released in 1991, Python has grown to become one of the most popular programming languages globally.

        One of Python's core strengths is its clear and elegant syntax, which emphasizes code readability through the use of indentation rather than braces or semicolons. This simplicity makes Python an ideal choice for beginners and experienced developers alike.

        Python's standard library is extensive, offering modules for everything from file handling and data manipulation to web development and scientific computing. Additionally, Python's package ecosystem, with tools like NumPy, pandas, and TensorFlow, makes it a powerful choice for data analysis, machine learning, and artificial intelligence.

        Dynamic typing in Python allows for flexibility in code writing, making it easy to prototype and develop applications rapidly. However, to enhance code robustness, Python 3 introduced type hints, allowing developers to specify expected types using annotations.

        The Python community is vibrant and supportive, offering a wealth of online resources, forums, and tutorials. This collaborative environment fosters knowledge sharing and problem-solving among developers.

        Prominent organizations such as Google, Facebook, and NASA utilize Python in various capacities. Its versatility and extensive library support have made it a top choice for web development, automation, and scientific research.

        In summary, Python is a powerful, accessible, and widely used programming language known for its simplicity, readability, and versatility. Whether you're a beginner or an experienced programmer, Python can empower you to create a wide range of applications and solve complex problems while being part of a thriving developer community.
        """
    actual = calculate_rpm(string_with_300_words)
    expected = "2 minutes"

    assert actual == expected