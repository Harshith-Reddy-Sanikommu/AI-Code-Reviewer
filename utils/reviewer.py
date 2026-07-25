from config import model
from utils.prompt import get_prompt


def review_code(language, code):

    try:

        prompt = get_prompt(
            language,
            code
        )


        response = model.generate_content(
            prompt
        )


        return response.text


    except Exception as e:

        return "Error: " + str(e)