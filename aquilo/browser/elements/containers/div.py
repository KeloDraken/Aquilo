from typing import Union, Iterable, List

from aquilo.browser.elements import Element
from aquilo.html.generators import generate_dom_tree


class div(Element):
    def __init__(
        self, *args: Union[Iterable[Element], Element], class_list: List[str] = None
    ):
        etype = self.__class__.__name__
        super().__init__(etype, class_list=class_list)
        self.elements = args

    def get_elements(self) -> Union[Iterable[Element], Element]:
        return self.elements

    def __call__(self, *args, **kwargs) -> str:
        return generate_dom_tree(self.elements)
