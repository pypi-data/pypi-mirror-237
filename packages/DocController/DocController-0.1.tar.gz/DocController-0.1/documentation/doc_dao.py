import json
import traceback

# from Util.documentation.doc_dto import Documentaion
from tutorial.step_dto import Step
from tutorial.tut_dto import Tutorial


class DocumentationService:
    @staticmethod
    def init_module(doc) -> bool:
        key = ""
        temp_attach = {}

        try:
            with open(doc.get_module_src(), "r") as module:
                data = json.load(module)

            key = "module_name"
            doc._set_module_name(module_name=data[key])

            key = "module_description"
            doc._set_module_desc(module_desc=data[key])

            key = "tutorials"
            tutorials = data[key]

            ret_val = []

            for tutorial in tutorials:
                temp_tut = Tutorial(title="", steps=[])
                key = "tutorial_title"
                temp_tut._set_tutorial_title(tutorial[key])
                doc._add_list_of_tutorials(tutorial[key])

                key = "steps"
                steps = tutorial[key]

                for step in steps:
                    temp_step = Step(content="", attachments={})
                    key = "content"
                    temp_step._set_content(content=step[key])

                    key = "attachments"
                    attachments = step[key]

                    for attachment in attachments:
                        key = "alt_text"
                        alt_text = attachment[key]

                        key = "src"
                        src = attachment[key]

                        temp_attach.update({alt_text: src})

                    temp_step._set_attachments(temp_attach)
                    temp_tut._add_step(temp_step)

                ret_val.append(temp_tut)

            doc._set_tutorials(ret_val)

            return True

        except KeyError as KE:
            print(
                f"An exception occurred: {KE}\nThe key '{key}' does not exist in the JSON file."
            )
            traceback.print_exc()
            return False

        except FileNotFoundError as FNFE:
            print(f"An exception occurred: {FNFE}")
            traceback.print_exc()
            return False

        except Exception as e:
            print(f"An exception occurred: {e}")
            traceback.print_exc()
            return False
