class Step:
    __content: str = ""
    __attachments: dict[str, str] = {}

    # Constructor Call
    def __init__(
        self, content: str, attachments: dict[str, str], **kwargs: dict
    ) -> None:
        self.__content = content
        self.__attachments = attachments
        return

    # Getters and Setters
    def get_content(self) -> str:
        return self.__content

    def _set_content(self, content: str) -> None:
        self.__content = content
        return

    def get_attachments(self) -> dict[str, str]:
        return self.__attachments

    def _set_attachments(self, attachments: dict[str, str]) -> None:
        self.__attachments = attachments
        return

    def _add_attachment(self, alt_text: str, src: str) -> None:
        self.__attachments.update({alt_text: src})
        return
