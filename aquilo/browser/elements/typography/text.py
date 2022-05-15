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
