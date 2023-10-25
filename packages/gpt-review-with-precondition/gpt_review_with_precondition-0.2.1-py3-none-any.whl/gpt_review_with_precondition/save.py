from .args.args import get_save_args
from .args.env import SaveEnv
from .llama_index_wrapper.api import Api
from .llama_index_wrapper.notion import Notion
from .storage.storage import Storage
from .zip.zip import compress


def main() -> None:
    args = get_save_args()
    env = SaveEnv()
    notion = Notion(env)
    api = Api(env)
    storage = Storage(env)

    documents = notion.get_documents(
        args.notion_database_id,
        args.get_notion_query(),
        args.notion_document_ids(),
    )
    print(documents)
    api.save_notion_pages(documents)
    compress(env.storage_context_tmp_dir, env.storage_context_tmp_dir)
    storage.upload_from_local(
        env.storage_context_tmp_zip,
        env.google_index_bucket_name,
        env.google_index_file_name,
    )


if __name__ == "__main__":
    main()
