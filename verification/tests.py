"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [100, 0.25],
            "answer": 75.0
        },
        {
            "input": [50, 0.1],
            "answer": 45.0
        },
        {
            "input": [75.5, 0.5],
            "answer": 37.75
        }
    ],
    "Extra": [
        {
            "input": [80, 0],
            "answer": 80
        },
        {
            "input": [80, 1],
            "answer": 0
        }
    ]
}
