from aquilo.browser.elements import Element
from aquilo.browser.styles import StyleSheet


class Text(Element):
    def __init__(
            self,
            styles: StyleSheet,
            etype: str,
            text: str,
            classList: list[str] = None,
            eid: str = None
    ):
        super().__init__(etype, text, classList, eid)


class h1(Text):
    def __init__(self, styles: StyleSheet, text: str, classList: list[str] = None, eid: str = None):
        super().__init__(styles, self.__class__.__name__, text, classList, eid)


class h2(Text):
    def __init__(self, styles: StyleSheet, text: str, classList: list[str] = None, eid: str = None):
        super().__init__(styles, self.__class__.__name__, text, classList, eid)


class p(Text):
    def __init__(self, styles: StyleSheet, text: str, classList: list[str] = None, eid: str = None):
        super().__init__(styles, self.__class__.__name__, text, classList, eid)
