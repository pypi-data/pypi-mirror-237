import json
import sys
import uuid
from typing import Any, Dict, List


class Args:
    def __init__(self) -> None:
        pass


class ReviewArgs(Args):
    def __init__(self) -> None:
        super().__init__()
        self.dummy = ""

    def get_prompt(self) -> str:
        with open("./inputs/prompt.md", encoding="utf-8") as f:
            s = f.read()
            return s


class SaveArgs(Args):
    def __init__(self, args: list[str]) -> None:
        super().__init__()
        self.args = args

        if len(self.args) > 1:
            self.notion_database_id = args[1]
            with open("./inputs/notion_database_query.json", encoding="utf-8") as f:
                self.notion_query_json = f.read()
        else:
            self.notion_database_id = None
        with open("./inputs/notion_document_ids.json", encoding="utf-8") as f:
            self.notion_document_ids_json = f.read()
        assert self.notion_database_id is not None or self.notion_document_ids_json is not None

    def get_notion_query(self) -> Dict[str, Any]:
        if self.notion_query_json is None:
            return {}
        return json.loads(self.notion_query_json)

    def notion_document_ids(self) -> List[str]:
        ids: List[str] = []
        if self.notion_document_ids_json is not None:
            for doc_id in json.loads(self.notion_document_ids_json):
                ids.append(str(uuid.UUID(doc_id)))
        return ids


def get_review_args() -> ReviewArgs:
    a = ReviewArgs()
    return a


def get_save_args() -> SaveArgs:
    a = SaveArgs(sys.argv)
    return a
