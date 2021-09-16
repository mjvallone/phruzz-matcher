import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span, Doc
from spacy.util import filter_spans
from spacy.language import Language
import fuzzy_matcher from utils
MATCH_PERCENTAGE = 92 #TODO deberia recibir match_percentage


nlp = spacy.blank('es') #FIXME eliminar una vez probado que recibe un modelo

class PhruzzMatcher:
    name = "phruzz_matcher"

    def __init__(self, nlp: Language, phrases_list, entity_label):
        self.phrases_list = phrases_list
        self.entity_label = entity_label
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
            match = fuzzy_matcher(self.phrases_list, tokens, MATCH_PERCENTAGE)
            if match:
                start = match[-2]
                end = match[-1] + 1

        if match:
            doc.ents = filter_spans([Span(doc, start, end, label=self.entity_label)] + list(doc.ents))

        return doc