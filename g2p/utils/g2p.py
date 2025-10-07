# Copyright (c) 2024 Amphion.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from phonemizer.backend import EspeakBackend
from phonemizer.separator import Separator
from phonemizer.utils import list2str, str2list
from typing import List, Union
import os
import json
import sys
import warnings

# separator=Separator(phone=' ', word=' _ ', syllable='|'),
separator = Separator(word=" _ ", syllable="|", phone=" ")

# Initialize language backends with graceful fallback
phonemizer_zh = None
phonemizer_en = None
phonemizer_ko = None
phonemizer_fr = None
phonemizer_de = None

# Try to load Chinese backend (optional)
try:
    phonemizer_zh = EspeakBackend(
        "cmn", preserve_punctuation=False, with_stress=False, language_switch="remove-flags"
    )
except RuntimeError:
    warnings.warn("Chinese (cmn) language not supported by espeak - Chinese features will be disabled")

# Load English backend (required for Hinglish)
try:
    phonemizer_en = EspeakBackend(
        "en-us",
        preserve_punctuation=False,
        with_stress=False,
        language_switch="remove-flags",
    )
except RuntimeError:
    warnings.warn("English (en-us) language not supported by espeak")

# Try to load Korean backend (optional)
try:
    phonemizer_ko = EspeakBackend(
        "ko", preserve_punctuation=False, with_stress=False, language_switch="remove-flags"
    )
except RuntimeError:
    warnings.warn("Korean language not supported by espeak - Korean features will be disabled")

# Try to load French backend (optional)
try:
    phonemizer_fr = EspeakBackend(
        "fr-fr",
        preserve_punctuation=False,
        with_stress=False,
        language_switch="remove-flags",
    )
except RuntimeError:
    warnings.warn("French language not supported by espeak - French features will be disabled")

# Try to load German backend (optional)
try:
    phonemizer_de = EspeakBackend(
        "de", preserve_punctuation=False, with_stress=False, language_switch="remove-flags"
    )
except RuntimeError:
    warnings.warn("German language not supported by espeak - German features will be disabled")


lang2backend = {
    "zh": phonemizer_zh,
    "en": phonemizer_en,
    "fr": phonemizer_fr,
    "ko": phonemizer_ko,
    "de": phonemizer_de,
}

with open("./g2p/utils/mls_en.json", "r", encoding='utf-8') as f:
    json_data = f.read()
token = json.loads(json_data)


def phonemizer_g2p(text, language):
    langbackend = lang2backend.get(language)
    
    # Check if backend is available
    if langbackend is None:
        raise RuntimeError(
            f"Language '{language}' is not supported. "
            f"Please install the required espeak-ng language pack or use a supported language (English for Hinglish)."
        )
    
    phonemes = _phonemize(
        langbackend,
        text,
        separator,
        strip=True,
        njobs=1,
        prepend_text=False,
        preserve_empty_lines=False,
    )
    token_id = []
    if isinstance(phonemes, list):
        for phone in phonemes:
            phonemes_split = phone.split(" ")
            token_id.append([token[p] for p in phonemes_split if p in token])
    else:
        phonemes_split = phonemes.split(" ")
        token_id = [token[p] for p in phonemes_split if p in token]
    return phonemes, token_id


def _phonemize(  # pylint: disable=too-many-arguments
    backend,
    text: Union[str, List[str]],
    separator: Separator,
    strip: bool,
    njobs: int,
    prepend_text: bool,
    preserve_empty_lines: bool,
):
    """Auxiliary function to phonemize()

    Does the phonemization and returns the phonemized text. Raises a
    RuntimeError on error.

    """
    # remember the text type for output (either list or string)
    text_type = type(text)

    # force the text as a list
    text = [line.strip(os.linesep) for line in str2list(text)]

    # if preserving empty lines, note the index of each empty line
    if preserve_empty_lines:
        empty_lines = [n for n, line in enumerate(text) if not line.strip()]

    # ignore empty lines
    text = [line for line in text if line.strip()]

    if text:
        # phonemize the text
        phonemized = backend.phonemize(
            text, separator=separator, strip=strip, njobs=njobs
        )
    else:
        phonemized = []

    # if preserving empty lines, reinsert them into text and phonemized lists
    if preserve_empty_lines:
        for i in empty_lines:  # noqa
            if prepend_text:
                text.insert(i, "")
            phonemized.insert(i, "")

    # at that point, the phonemized text is a list of str. Format it as
    # expected by the parameters
    if prepend_text:
        return list(zip(text, phonemized))
    if text_type == str:
        return list2str(phonemized)
    return phonemized
