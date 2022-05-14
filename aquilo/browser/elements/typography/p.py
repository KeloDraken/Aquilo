from aquilo import Element


class p(Element):
    def __init__(self, text: str, classList: list[str] = None, eid: str = None):
        super().__init__(self.__class__.__name__, text, classList, eid)
