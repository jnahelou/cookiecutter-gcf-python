"""
Test {{cookiecutter.project_name}}
"""

import main

def test_main():
    """
    Test main function
    """

    assert main.main(None) == "{{cookiecutter.project_name|lower}}"

def test_do_some_stuff():
    """
    Test do_some_stuff function
    """

    tests = [
        {
            "p": "HeLlo",
            "want": "hello",
        }, {
            "p": "HoLa",
            "want": "hola",
        }, {
            "p": "Hi",
            "want": "hi",
        }
    ]

    # Generic tests
    for test in tests:
        assert main.do_some_stuff(test["p"]) == test["want"]

def test_do_some_stuff_with_mock(monkeypatch):
    """
    Test do_some_stuff function but replace lower to upper action
    """

    # Dummy mock
    def mock(*args, **kwargs):
        #pylint: disable=unused-argument

        return args[0].upper()

    monkeypatch.setattr(main, "lower", mock)

    tests = [
        {
            "p": "Hello",
            "want": "HELLO",
        }
    ]

    # Generic tests
    for test in tests:
        assert main.do_some_stuff(test["p"]) == test["want"]
