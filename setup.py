import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="phruzz_matcher",
    version="0.0.3",
    author="Martin Vallone",
    author_email="mjvallone@gmail.com",
    description="Combination of the RapidFuzz library with Spacy PhraseMatcher ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mjvallone/phruzz-matcher",
    project_urls={
        "Phruzz Matcher": "https://github.com/mjvallone/phruzz-matcher",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
         "Intended Audience :: Developers",
         "Intended Audience :: Science/Research",
         "Topic :: Scientific/Engineering"        
    ],
    packages=["phruzz_matcher"],
    python_requires=">=3.7",
    install_requires=["setuptools>=54", "wheel", "rapidfuzz"],
)