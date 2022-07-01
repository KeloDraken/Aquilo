from setuptools import setup, find_packages

setup(
    name="aquilo",
    version="0.0.1",
    description="The uncompromising code formatter.",
    author="Łukasz Langa",
    author_email="lukasz@langa.pl",
    url="https://github.com/psf/black",
    packages=find_packages(),
    python_requires=">=3.10.1",
    entry_points={
        "console_scripts": [
            "aquilo-admin=aquilo:main",
        ]
    },
)
