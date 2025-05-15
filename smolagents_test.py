from smolagents import WebSearchTool
from utils import create_agent, is_valid_result

def main():
    tools = [WebSearchTool()]
    additional_authorized_imports = []
    model_id = "o4-mini-2025-04-16"
    agent = create_agent(tools, additional_authorized_imports, model_id)
    
    max_retry = 5
    for i in range(max_retry):
        result = agent.run(
            """
https://github.com/topics/ai?o=desc&s=updated
https://github.com/trending

githubのトレンドを日本語で分かりやすくまとめてください。
リポジトリ名と概要をそれぞれお願いいたします。
出力はテキスト形式で出して。

""")
        if is_valid_result(result):
            with open("result.txt", "w", encoding="utf-8") as f:
                f.write(str(result))
            print(result)
            break
        print(f"retry {i+1}")
        import time; time.sleep(2)
    else:
        print("データ取得に失敗しました")

if __name__ == "__main__":
    main()