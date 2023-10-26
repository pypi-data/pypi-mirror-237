# gpt-code-generator

## summery

GPT code generator refer to GitHub repository

## for user

### Environment Variables

### use GitHub Actions

```yml
name: Save precondition indexes from GitHub repositry for generate code
on:
  workflow_dispatch:
  schedule:
    - cron: '0 0 * * *' # every day at midnight

permissions:
  actions: read
  contents: read
  id-token: write
  checks: write
  pull-requests: write

jobs:
  save:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Auto GPT Review With Preconditions
        uses: wakuwaku3/gpt-code-generator@v0.0.0
        with:
          AZURE_OPEN_AI_KEY: "${{ secrets.AZURE_OPEN_AI_KEY }}"
          AZURE_OPEN_AI_ENDPOINT: "${{ secrets.AZURE_OPEN_AI_ENDPOINT }}"
          AZURE_OPEN_AI_VERSION: "2023-05-15"
          AZURE_OPEN_AI_MODEL_NAME: "gpt-35-turbo"
          AZURE_OPEN_AI_MODEL_DEPLOY_NAME: "gpt-35-turbo"
          AZURE_OPEN_AI_EMBEDDING_MODEL_NAME: "text-embedding-ada-002"
          AZURE_OPEN_AI_EMBEDDING_MODEL_DEPLOY_NAME: "text-embedding-ada-002"
          GOOGLE_APPLICATION_CREDENTIALS_JSON: "${{ secrets.GOOGLE_APPLICATION_CREDENTIALS_JSON }}"
          GOOGLE_INDEX_BUCKET_NAME: "${{ secrets.GOOGLE_INDEX_BUCKET_NAME }}"
          GITHUB_OWNER: wakuwaku3 # optional, default: ${GITHUB_REPOSITORY_OWNER}
          GITHUB_REPO: gpt-code-generator # optional, default: ${GITHUB_REPOSITORY#${GITHUB_REPOSITORY_OWNER}/}
          GITHUB_TOKEN:  "${{ secrets.TOKEN }}" # optional, default: ${{ secrets.GITHUB_TOKEN }}
          IGNORE_FILE_EXTENSIONS: "" # optional
          IGNORE_DIRECTORIES: "" # optional
```

### install command

```shell
pip install gpt-code-generator
```

### save-code-generating-precondition command

```shell
save-code-generating-precondition --help
```

### gpt-code-generator command

```shell
gpt-code-generator --help
```

## for developer setup

```shell
pip install poetry
poetry config virtualenvs.in-project true --local
make install
```
