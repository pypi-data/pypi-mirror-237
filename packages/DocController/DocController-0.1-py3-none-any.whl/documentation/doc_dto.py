from documentation.doc_dao import DocumentationService
from tutorial.step_dto import Step
from tutorial.tut_dto import Tutorial


class Documentaion:
    __module_name: str = ""
    __module_desc: str = ""
    __module_src: str = ""
    __list_of_tutorials: list[str] = []
    __tutorials: list[Tutorial] = []

    # Constructor Call
    def __init__(self, module_src: str, **kwargs: dict) -> None:
        self.__module_name = kwargs.get("module_name")  # type: ignore
        self.__module_desc = kwargs.get("module_desc")  # type: ignore
        self.__module_src = module_src
        self.__tutorials = kwargs.get("tutorials")  # type: ignore

        if any(
            [
                self.__module_name is None,
                self.__module_desc is None,
                self.__tutorials is None,
                self.__module_name == "",
                self.__module_desc == "",
                self.__tutorials == "",
            ]
        ):
            if DocumentationService.init_module(self):
                return
            else:
                raise FileNotFoundError()

    # Getters and Setters
    def get_module_name(self) -> str:
        return self.__module_name

    def _set_module_name(self, module_name: str) -> None:
        self.__module_name = module_name
        return

    def get_module_desc(self) -> str:
        return self.__module_desc

    def _set_module_desc(self, module_desc: str) -> None:
        self.__module_desc = module_desc
        return

    def get_module_src(self) -> str:
        return self.__module_src

    def _set_module_src(self, module_src: str) -> None:
        self.__module_src = module_src
        return

    def get_list_of_tutorials(self) -> list[str]:
        return self.__list_of_tutorials

    def _set_list_of_tutorials(self, list_of_tutorials: list[str]) -> None:
        self.__list_of_tutorials = list_of_tutorials
        return

    def _add_list_of_tutorials(self, tutorial_name: str) -> None:
        self.__list_of_tutorials.append(tutorial_name.lower())
        return

    def get_tutorials(self) -> list[Tutorial]:
        return self.__tutorials

    def _set_tutorials(self, tutorials: list[Tutorial]) -> None:
        self.__tutorials = tutorials
        return

    def _add_tutorial(self, title: str, steps: list[Step]) -> None:
        self.__tutorials.append(Tutorial(title=title, steps=steps))  # type: ignore
        return
