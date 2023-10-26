import os
from tutorial.step_dto import Step


class Tutorial:
    __tutorial_title: str = ""
    __steps: list[Step] = []

    # Constructor Call
    def __init__(self, title: str, steps: list[Step], **kwargs: dict) -> None:
        self.__tutorial_title = title
        self.__steps = steps
        return

    # Getters and Setters
    def get_tutorial_title(self) -> str:
        return self.__tutorial_title

    def _set_tutorial_title(self, title: str) -> None:
        self.__tutorial_title = title
        return

    def get_steps(self) -> list[Step]:
        return self.__steps

    def _set_steps(self, steps: list[Step]) -> None:
        self.__steps = steps
        return

    def _add_step(self, step: Step) -> None:
        self.__steps.append(step)
        return
