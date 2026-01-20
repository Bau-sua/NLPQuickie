import re
from collections import Counter
from typing import Dict, Any

import spacy

nlp = spacy.load("es_core_news_sm")


def process_text(text: str) -> Dict[str, Any]:
    # Pre-proceso: quitar puntuación
    cleaned = re.sub(r"[^\w\s]", "", text.lower())
    words = cleaned.split()
    word_count = len(words)
    # Palabra más usada
    most_common = Counter(words).most_common(1)[0] if words else ("ninguna", 0)
    # NER con spaCy en texto original
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {
        "word_count": word_count,
        "most_common_word": {"word": most_common[0], "count": most_common[1]},
        "entities": entities,
        "cleaned_sample": cleaned[:200] + "..." if len(cleaned) > 200 else cleaned,
    }
