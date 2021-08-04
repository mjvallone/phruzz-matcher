# phruzz-matcher
> Combination of the RapidFuzz library with Spacy PhraseMatcher 

## Installation

        git clone https://github.com/mjvallone/phruzz_matcher_spacy.git

## Configuration

1. Create virtualenv using python3 (follow https://virtualenvwrapper.readthedocs.io/en/latest/install.html)

        virtualenv venv

2. Activate the virtualenv

        . venv/bin/activate

3. Install requirements

        pip install -r requirements.txt

4. Download a spanish base model (we recommend the large one)

        python -m spacy download es_core_news_lg

## Using it!

        Open a console and run the command
                `python [function you want to use] [parameters for that function]`
