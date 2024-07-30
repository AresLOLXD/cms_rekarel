from setuptools import setup, find_packages

setup(
    name="karel",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "cms.grading.languages": [
            "KarelJava=karel:KarelJava",
            "KarelPascal=karel:KarelPascal",
        ]
    }
)