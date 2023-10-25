# gpt-review-with-precondition

## summery

notion 上にある技術文書を前提とした PR レビューを行います

## for user

### Envioronment Variables

### install

```shell
pip install gpt-review-with-precondition
```

### save-precondition コマンド

```shell
save-precondition ${NOTION_DATABASE_ID}
```

notion document を取得して前提条件のためのデータを保存します。

- NOTION_DATABASE_ID
  指定した id の Notion Database から ドキュメントを取得します。`inputs/notion_database_query.json` で取得条件を指定できます。`inputs/notion_document_ids.json` に指定された id のドキュメントも併せて取得します。

```json
// example notion_database_query
{
  "filter": {
    "or": [
      {"property": "status", "select": {"equals": "approved"}},
      {"property": "status", "select": {"equals": "posted"}},
    ]
  }
}
```

```json
// example notion_document_ids
["id1","id2"]
```

### gpt-review-with-precondition コマンド

```shell
gpt-review-with-precondition
```

前提条件付きで `inputs/prompt.md` に記載されたプロンプトを実行します。

## for developer setup

```shell
pip install poetry
make install
```
