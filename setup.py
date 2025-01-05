from setuptools import setup, find_packages

setup(
    name="karel",
    version="1.4",
    packages=find_packages(),
    entry_points={
        "cms.grading.languages": [
            "KarelLanguage=karel.language:KarelLanguage",
            "OldKarelLanguage=karel.language:OldKarelLanguage"
        ],
        "cms.grading.tasktypes": [
            "KarelTask=karel.task:KarelTask",
        ]
    }
)