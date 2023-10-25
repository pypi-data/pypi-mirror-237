from .args.args import get_review_args
from .args.env import ReviewEnv
from .llama_index_wrapper.api import Api
from .storage.storage import Storage
from .zip.zip import decompress


def main() -> None:
    args = get_review_args()
    env = ReviewEnv()
    storage = Storage(env)
    storage.download_to_local(
        env.storage_context_tmp_zip,
        env.google_index_bucket_name,
        env.google_index_file_name,
    )
    decompress(env.storage_context_tmp_zip, env.storage_context_tmp_dir)
    api = Api(env)
    api.ask(args.get_prompt())


if __name__ == "__main__":
    main()
