from aquilo.browser.elements import Element
from aquilo.browser.styles.styles import StyleSheet
from aquilo.html.generators import get_element_tree


class div(Element):
    def __init__(self, styles: StyleSheet, *args: Element):
        self.styles = styles
        etype = self.__class__.__name__
        super().__init__(etype)
        self.elements = args

    def get_elements(self):
        return self.elements

    def __call__(self, *args, **kwargs):
        return get_element_tree(self.elements)
