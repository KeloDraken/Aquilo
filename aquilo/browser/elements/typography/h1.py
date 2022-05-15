from aquilo.browser.elements.typography.text import Text
from aquilo.browser.styles import StyleSheet


class h1(Text):
    def __init__(self, styles: StyleSheet, text: str, classList: list[str] = None, eid: str = None):
        super().__init__(styles, self.__class__.__name__, text, classList, eid)
