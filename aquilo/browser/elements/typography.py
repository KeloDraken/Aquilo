from aquilo.browser.elements import Element
from aquilo.browser.styles import StyleSheet


class Text(Element):
    def __init__(
            self,
            etype: str,
            text: str,
            styles: StyleSheet = StyleSheet.create({}),
            classList: list[str] = None,
            eid: str = None
    ):
        super().__init__(etype, text, classList, eid)


class h1(Text):
    def __init__(self, text: str, styles: StyleSheet = StyleSheet.create({}), classList: list[str] = None,
                 eid: str = None):
        super().__init__(self.__class__.__name__, text, styles, classList, eid)


class h2(Text):

    def __init__(self, text: str, styles: StyleSheet = StyleSheet.create({}), classList: list[str] = None,
                 eid: str = None):
        super().__init__(self.__class__.__name__, text, styles, classList, eid)


class h3(Text):

    def __init__(self, text: str, styles: StyleSheet = StyleSheet.create({}), classList: list[str] = None,
                 eid: str = None):
        super().__init__(self.__class__.__name__, text, styles, classList, eid)


class h4(Text):

    def __init__(self, text: str, styles: StyleSheet = StyleSheet.create({}), classList: list[str] = None,
                 eid: str = None):
        super().__init__(self.__class__.__name__, text, styles, classList, eid)


class h5(Text):

    def __init__(self, text: str, styles: StyleSheet = StyleSheet.create({}), classList: list[str] = None,
                 eid: str = None):
        super().__init__(self.__class__.__name__, text, styles, classList, eid)


class h6(Text):

    def __init__(self, text: str, styles: StyleSheet = StyleSheet.create({}), classList: list[str] = None,
                 eid: str = None):
        super().__init__(self.__class__.__name__, text, styles, classList, eid)


class p(Text):

    def __init__(self, text: str, styles: StyleSheet = StyleSheet.create({}), classList: list[str] = None,
                 eid: str = None):
        super().__init__(self.__class__.__name__, text, styles, classList, eid)


class strong(Text):

    def __init__(self, text: str, styles: StyleSheet = StyleSheet.create({}), classList: list[str] = None,
                 eid: str = None):
        super().__init__(self.__class__.__name__, text, styles, classList, eid)


class small(Text):

    def __init__(self, text: str, styles: StyleSheet = StyleSheet.create({}), classList: list[str] = None,
                 eid: str = None):
        super().__init__(self.__class__.__name__, text, styles, classList, eid)


class a(Text):
    def __init__(self, text: str, href: str, styles: StyleSheet = StyleSheet.create({}), classList: list[str] = None,
                 eid: str = None):
        super().__init__(self.__class__.__name__, text, styles, classList, eid)
        self.href = href

    def __call__(self, *args, **kwargs):
        if self.classList is None:
            return f'<{self.etype} href={self.href}>{self.innerHTML}</{self.etype}>'
        else:
            self.className = " ".join(self.classList)
            return f'<{self.etype} href={self.href} class="{self.className}">{self.innerHTML}</{self.etype}>'
