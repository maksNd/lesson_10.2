import json


def load_candidates(json_file: str = "candidates.json") -> list:
    """Загружает данные из json файла"""

    with open(json_file, encoding="utf-8") as file:
        data_from_json = json.load(file)

    return data_from_json


def get_all(candidates: list) -> str:
    """Возвращает имена всех кандидатов"""
    """
    Имя кандидата -
    Позиция кандидата
    Навыки через запятую
    """
    candidates_list = []
    for candidate in candidates:
        candidates_list.append(f"\tИмя кандидата - {candidate['name']}\n"
                               f"\tПозиция кандидата - {candidate['pk']}\n"
                               f"\tНавыки кандидата: {candidate['skills']}\n")

    return ("<pre>" + "\n" + "\n".join(candidates_list) + "</pre>")


def get_by_pk(candidates: list, pk: int):
    """Возвращает кандидата по pk"""

    for candidate in candidates:
        if candidate["pk"] == pk:
            return f"<pre>\n" \
                   f"\tИмя кандидата - {candidate['name']}\n" \
                   f"\tПозиция кандидата - {candidate['pk']}\n" \
                   f"\tНавыки кандидата: {candidate['skills']}\n" \
                   f"</pre>"
    return "No candidate with such pk"


def get_by_skill(candidates: list, skill_name: str):
    """Возвращает имя кандидата по навыку"""
    candidates_by_skill = []
    for candidate in candidates:
        if skill_name.strip().lower() in candidate["skills"].lower():
            candidates_by_skill.append(f"\tИмя кандидата - {candidate['name']}\n"
                                       f"\tПозиция кандидата - {candidate['pk']}\n"
                                       f"\tНавыки кандидата: {candidate['skills']}\n")
    if len(candidates_by_skill) > 0:
        return "\n".join(candidates_by_skill)
    else:
        return "No candidate with such skills"
