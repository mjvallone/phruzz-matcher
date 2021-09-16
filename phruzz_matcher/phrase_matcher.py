import re

from spacy.matcher import PhraseMatcher
from spacy.tokens import Span, Doc
from spacy.util import filter_spans
from spacy.language import Language
from rapidfuzz import fuzz

MATCH_PERCENTAGE = 92

def fuzzy_matcher(features, tokens, match=None):
    matches = []
    for feature in features:
        feature_length = len(feature.split(" "))
        for i in range(len(tokens) - feature_length + 1):
            matched_phrase = ""
            j = 0
            for j in range(i, i + feature_length):
                if re.search(r"[,!?{}\[\]]", tokens[j]):
                    break
                matched_phrase = matched_phrase + " " + tokens[j].lower()
            matched_phrase.strip()
            if not matched_phrase == "":

                if fuzz.ratio(matched_phrase, feature.lower()) > match:
                    matches.append([matched_phrase, feature, i, j])

    return matches[0] if len(matches) else matches


class PhruzzMatcher:
    name = "phruzz_matcher"

    def __init__(self, nlp: Language, phrases_list, entity_label, match_percentage=None):
        self.phrases_list = phrases_list
        self.entity_label = entity_label
        self.match_percentage = match_percentage or MATCH_PERCENTAGE
        self.matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
        patterns = list(nlp.tokenizer.pipe(phrases_list))
        self.matcher.add(f"{entity_label.lower().replace(' ', '_')}_list", patterns)

    def __call__(self, doc: Doc) -> Doc:
        matches = self.matcher(doc)

        if matches:
            # using PhraseMatcher from Spacy
            match = matches[0]
            start = match[-2]
            end = match[-1]
        else:
            # using RapidFuzz to find matches when there were NO "perfect matches" due to typos or abreviations
            # consider that MATCH_PERCENTAGE is the percentage from the one you will keep matches between
            # what is written in the text and the list of phrases
            # higher the percentage, lower the differences "tolerated" to find a match
            tokens = [token.text for token in doc]
            match = fuzzy_matcher(self.phrases_list, tokens, self.match_percentage)
            if match:
                start = match[-2]
                end = match[-1] + 1

        if match:
            doc.ents = filter_spans([Span(doc, start, end, label=self.entity_label)] + list(doc.ents))

        return doc