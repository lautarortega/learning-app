from typing import Dict, Any
import ollama
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser

class LLMChallengeOutput(BaseModel):
    title: str
    options: list[str]
    correct_answer_id: int
    explanation: str

def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:
    parser = PydanticOutputParser(pydantic_object=LLMChallengeOutput)
    format_instructions = parser.get_format_instructions()
    system_prompt = f"""You are an expert coding challenge creator. 
        Your task is to generate a coding question with multiple choice answers.
        The question should be appropriate for the specified difficulty level.

        For easy questions: Focus on basic syntax, simple operations, or common programming concepts.
        For medium questions: Cover intermediate concepts like data structures, algorithms, or language features.
        For hard questions: Include advanced topics, design patterns, optimization techniques, or complex algorithms.

        Return the challenge in the following JSON structure:
        {format_instructions}

        Make sure the options are plausible but with only one clearly correct answer.
        """
    try:
        response = ollama.chat(
            model="mistral",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Generate a {difficulty} level coding challenge."}
            ],
            # response_format={"type": "json_object"},
            # temperature=0.7,
        )

        # content = response["choices"][0]["message"]["content"]
        content = response["message"]["content"]
        parsed_content = parser.parse(content)
        challenge_data = parsed_content.dict()

        required_fields = ["title", "options", "correct_answer_id", "explanation"]
        for field in required_fields:
            if field not in challenge_data:
                raise ValueError(f"Missing required field {field}")

        return challenge_data

    except Exception as e:
        print(e)
        return {
            "title": "Basic Python List Operation",
            "options": [
                "my_list.append(5)",
                "my_list.add(5)",
                "my_list.push(5)",
                "my_list.insert(5)",
            ],
            "correct_answer_id": 0,
            "explanation": "In Python, append() is the correct method to add an element to the end of a list."
        }

if __name__ == "__main__":
    print(generate_challenge_with_ai("easy"))