from typing import List
from sacremoses import MosesDetokenizer

emoji = {
    '😀': ':D',
    '😃': ':)',
    '😄': ':)',
    '😁': ':)',
    '😆': 'xD',
    '😅': ':)',
    '🤣': 'xD',
    '😂': 'xD',
    '🙂': ':)',
    '🙃': ':)',
    '😉': ';)',
    '😊': ':)',
    '😇': ':)',
    '🥰': ':*',
    '😍': ':*',
    '🤩': ':*',
    '😘': ':*',
    '😗': ':*',
    '☺': ':)',
    '😚': ':*',
    '😋': ':P',
    '😛': ':P',
    '😜': ':P',
    '😝': ':P',
    '🤑': ':P',
    '🤪': ':P',
    '🤗': ':P',
    '🤭': ':P',
    '🤫': ':|',
    '🤔': ':|',
    '🤨': ':|',
    '😐': ':|',
    '😑': ':|',
    '😶': ':|',
    '😏': ':)',
    '😒': ':(',
    '🙄': ':|',
    '🤐': ':|',
    '😬': ':$',
    '😌': 'zzz',
    '😔': ':(',
    '😪': 'zzz',
    '🤤': ':(',
    '🤒': ':(',
    '🤕': ':(',
    '🤢': ':(',
    '🤮': ':(',
    '🤧': ':(',
    '🥵': ':(',
    '🥶': ':(',
    '🥴': ':(',
    '😵': ':(',
    '🤯': ':(',
    '🤠': ':)',
    '🥳': ':)',
    '😎': ':)',
    '🤓': ':)',
    '🧐': ':)',
    '😕': ':(',
    '😟': ':(',
    '🙁': ':(',
    '☹': ':(',
    '😮': ':O',
    '😯': ':O',
    '😲': ':O',
    '😳': ':(',
    '🥺': ':(',
    '😦': ':(',
    '😧': ':(',
    '😨': ':(',
    '😰': ':(',
    '😥': ':(',
    '😢': ':(',
    '😭': ':(',
    '😱': ':(',
    '😖': ':(',
    '😣': ':(',
    '😞': ':(',
    '😓': ':(',
    '😩': ':(',
    '😫': ':(',
    '🥱': 'zzz',
    '😤': ':(',
    '😡': ':(',
    '😠': ':(',
    '🤬': ':(',
    '😈': ']:->',
    '👿': ']:->',
    '💀': ':(',
    '☠': ':(',
    '💋': ':*',
    '💔': ':(',
    '💤': 'zzz'
}

class TextNormalizer(object):

    def __init__(self, detokenize: bool=True, replace_emoji: bool=True, lang: str="pl"):
        self._moses = MosesDetokenizer(lang=lang)
        self._detokenize = detokenize
        self._replace_emoji = replace_emoji

    def process(self, text: str) -> str:
        if self._replace_emoji:
            text = "".join((emoji.get(c, c) for c in text))
        if self._detokenize:
            text = text.replace(" em ", "em ").replace(" śmy ", "śmy ").replace(" m ", "m ")
            tokens: List[str] = text.split()
            text = self._moses.detokenize(tokens)
        return text