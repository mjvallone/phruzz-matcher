# phruzz-matcher
> Combination of the RapidFuzz library with Spacy PhraseMatcher
> The goal of this component is to find matches when there were NO "perfect matches" due to typos or abreviations between a Spacy doc and a list of phrases.
> To see more about Spacy Phrase Matcher go to https://spacy.io/usage/rule-based-matching#phrasematcher

## Installation (dev)

        git clone https://github.com/mjvallone/phruzz_matcher_spacy.git

## Configuration (dev)

1. Create virtualenv using python3 (follow https://virtualenvwrapper.readthedocs.io/en/latest/install.html)

        virtualenv venv

2. Activate the virtualenv

        . venv/bin/activate

3. Install requirements

        pip install -r requirements.txt

## Usage

First you need to install it

`pip install phruzz_matcher`


If you want to add it to your pipeline you could do something like this:

```
from phruzz_matcher.phrase_matcher import PhruzzMatcher

@Language.factory("phrase_matcher")
def phrase_matcher(nlp: Language, name: str):
    return PhruzzMatcher(nlp, list_of_phrases, entity_label, match_percentage)


nlp.add_pipe("phrase_matcher")
```

### Parameters
- `nlp`: the Spacy model you use (it was tested with the different Spanish models from Spacy).
- `list_of_phrases`: the list of phrases you want to find in the Spacy doc.
- `entity_label`: the label from the entity that corresponds to what you are trying to match.
- `match_percentage`: percentage from the one you will keep matches between text from Spacy doc and the list of phrases. Higher the percentage, lower the differences "tolerated" to find a match.

## Example
```
nlp = spacy.load("es_core_news_lg")
famous_people = [
        "Brad Pitt",
        "Demi Moore",
        "Bruce Willis",
        "Jim Carrey",
]

@Language.factory("phrase_matcher")
def phrase_matcher(nlp: Language, name: str):
    return PhruzzMatcher(nlp, famous_people, "FAMOUS_PEOPLE", 92)
```