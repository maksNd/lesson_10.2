import json


def load_candidates(json_file: str = "candidates.json") -> list:
    """Загружает данные из json файла"""

    with open(json_file, encoding="utf-8") as file:
        data_from_json = json.load(file)

    return data_from_json


def get_all(candidates: list) -> list:
    """Возвращает имена всех кандидатов"""

    candidates_list = []
    for candidate in candidates:
        candidates_list.append(candidate["name"])

    return candidates_list


def get_by_pk(candidates: list, pk: int) -> str | None:
    """Возвращает кандидата по pk"""

    for candidate in candidates:
        if candidate["pk"] == pk:
            return candidate["name"]
    return "No candidate with such pk"


def get_by_skill(candidates: list, skill_name: str):
    """Возвращает имя кандидата по навыку"""
    for candidate in candidates:
        if skill_name.strip().lower() in candidate["skills"]:
            return candidate["name"]
    return "No candidate with such skills"
