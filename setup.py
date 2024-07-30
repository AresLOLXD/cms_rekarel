from setuptools import setup, find_packages

setup(
    name="karel",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "cms.grading.languages": [
            "KarelJava=karel.language:KarelJava",
            "KarelPascal=karel.language:KarelPascal",
        ],
        "cms.grading.tasktypes": [
            "KarelTask=karel.task:KarelTask",
        ]
    }
)