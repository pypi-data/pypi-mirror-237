from rich.console import Console
from rich.markdown import Markdown

from compaipair.types.compaicompletion import CompaiCompletion
from compaipair.utils import configure_palm_api, get_available_models, close_db

console = Console()


available_models_output_template = """# {model_name}
- name: {model_name}
- description: {model_description}
- generation methods: 
{generation_methods}
---"""


def available_models():
    configure_palm_api()
    for m in get_available_models():
        generation_methods = "\n".join(
            [
                f"\t- {generation_method}"
                for generation_method in m.supported_generation_methods
            ]
        )
        output = available_models_output_template.format(
            model_name=m.name,
            model_description=m.description,
            generation_methods=generation_methods,
        )
        console.print(Markdown(output))


def complete(
    question: str,
    priming: str = "",
    decorator: str = "",
    model_name: str = None,
    temperature: float = 0.7,
    verbose: bool = False,
    plain_text_output: bool = False,
    template: str = None,
    output: str = None,
    input_file: str = None,
):
    if input_file is not None:
        print(f"Using input from file {input_file}")
        with open(input_file, "r") as f:
            question = f"{question}\n{f.read()}"

    completion = CompaiCompletion(
        question=question,
        priming=priming,
        decorator=decorator,
        model=model_name,
        temperature=temperature,
        template=template,
    )
    completion.complete()

    if completion.result.result is not None:
        completion_result = completion.result.result
        if verbose:
            completion_result = (
                f"# Prompt\n{completion.prompt}\n---\n# Result\n{completion_result}"
            )
        if not plain_text_output:
            completion_output = Markdown(completion_result)
        else:
            completion_output = completion_result
        console.print(completion_output)

        if output is not None:
            with open(output, "w") as f:
                f.write(completion_result)
    else:
        raise Exception("No data returned by the model!")

    close_db()
