from __future__ import annotations

import re
from typing import Any

LANGUAGE_MAPS = {
    "spanish": {
        "hello": "hola",
        "hi": "hola",
        "how": "cómo",
        "are": "estás",
        "you": "tú",
        "good": "bien",
        "thanks": "gracias",
        "thank": "gracias",
        "please": "por favor",
        "yes": "sí",
        "no": "no",
        "what": "qué",
        "is": "es",
        "your": "tu",
        "name": "nombre",
        "i": "yo",
        "love": "amo",
        "language": "idioma",
        "translate": "traducir",
        "this": "esto",
        "sentence": "oración",
        "goodbye": "adiós",
        "thanks": "gracias",
        "today": "hoy",
        "tomorrow": "mañana",
    },
    "french": {
        "hello": "bonjour",
        "hi": "salut",
        "how": "comment",
        "are": "êtes",
        "you": "vous",
        "good": "bien",
        "thanks": "merci",
        "thank": "merci",
        "please": "s'il vous plaît",
        "yes": "oui",
        "no": "non",
        "what": "quoi",
        "is": "est",
        "your": "votre",
        "name": "nom",
        "i": "je",
        "love": "aime",
        "language": "langue",
        "translate": "traduire",
        "this": "ceci",
        "sentence": "phrase",
        "goodbye": "au revoir",
        "today": "aujourd'hui",
        "tomorrow": "demain",
    },
    "german": {
        "hello": "hallo",
        "hi": "hallo",
        "how": "wie",
        "are": "bist",
        "you": "du",
        "good": "gut",
        "thanks": "danke",
        "thank": "danke",
        "please": "bitte",
        "yes": "ja",
        "no": "nein",
        "what": "was",
        "is": "ist",
        "your": "dein",
        "name": "Name",
        "i": "ich",
        "love": "liebe",
        "language": "Sprache",
        "translate": "übersetzen",
        "this": "dies",
        "sentence": "Satz",
        "goodbye": "auf Wiedersehen",
        "today": "heute",
        "tomorrow": "morgen",
    },
    "italian": {
        "hello": "ciao",
        "hi": "ciao",
        "how": "come",
        "are": "sei",
        "you": "tu",
        "good": "bene",
        "thanks": "grazie",
        "thank": "grazie",
        "please": "per favore",
        "yes": "sì",
        "no": "no",
        "what": "cosa",
        "is": "è",
        "your": "tuo",
        "name": "nome",
        "i": "io",
        "love": "amo",
        "language": "lingua",
        "translate": "tradurre",
        "this": "questo",
        "sentence": "frase",
        "goodbye": "arrivederci",
        "today": "oggi",
        "tomorrow": "domani",
    },
    "portuguese": {
        "hello": "olá",
        "hi": "oi",
        "how": "como",
        "are": "está",
        "you": "você",
        "good": "bom",
        "thanks": "obrigado",
        "thank": "obrigado",
        "please": "por favor",
        "yes": "sim",
        "no": "não",
        "what": "o quê",
        "is": "é",
        "your": "seu",
        "name": "nome",
        "i": "eu",
        "love": "amo",
        "language": "idioma",
        "translate": "traduzir",
        "this": "isto",
        "sentence": "frase",
        "goodbye": "adeus",
        "today": "hoje",
        "tomorrow": "amanhã",
    },
}

SUPPORTED_LANGUAGES = sorted(LANGUAGE_MAPS.keys())


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[A-Za-zÀ-ÿ]+|[^A-Za-zÀ-ÿ\s]+|\s+", text)


def _translate_word(word: str, target_language: str) -> str:
    mapping = LANGUAGE_MAPS.get(target_language.lower(), {})
    lower_word = word.lower()

    if lower_word in mapping:
        translated = mapping[lower_word]
        if word[0].isupper():
            translated = translated.capitalize()
        return translated

    return word


def translate_text(text: str, target_language: str) -> str:
    if not text or not text.strip():
        raise ValueError("Missing text to translate.")

    target_language = target_language.strip().lower()
    if target_language not in LANGUAGE_MAPS:
        raise ValueError(
            f"Unsupported target language: {target_language}. Supported languages: {', '.join(SUPPORTED_LANGUAGES)}"
        )

    tokens = _tokenize(text)
    translated_tokens = [
        _translate_word(token, target_language) if token.strip() and token.isalpha() else token
        for token in tokens
    ]
    return "".join(translated_tokens)


def execute(arguments: dict[str, Any]) -> str:
    text = (arguments.get("text") or "").strip()
    target_language = (arguments.get("target_language") or "").strip()

    if not text:
        raise ValueError("Missing text to translate.")

    if not target_language:
        raise ValueError("Missing target language.")

    translation = translate_text(text, target_language)
    return f"Translated to {target_language.title()}:\n{translation}"
