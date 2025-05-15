from smolagents import Tool

class HFModelDownloadsTool(Tool):
    name = "model_download_counter"
    description = """
    指定したタスクカテゴリでHugging Face Hub上から最もダウンロード数が多いモデル（チェックポイント名）を返すツール。
    """
    inputs = {
        "task": {
            "type": "string",
            "description": "タスクカテゴリ（例: text-classification, depth-estimation など）",
        }
    }
    output_type = "string"

    def forward(self, task: str):
        from huggingface_hub import list_models

        model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
        return model.id

model_downloads_tool = HFModelDownloadsTool()