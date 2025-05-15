from tools import model_download_tool
from utils import create_agent, is_valid_result

def main():
    tools = [model_download_tool]
    additional_authorized_imports = ["requests", "bs4", "pandas"]
    model_id = "mistralai/mistral-medium-3"
    agent = create_agent(tools, additional_authorized_imports, model_id)
    
    max_retry = 5
    for i in range(max_retry):
        result = agent.run(
            """最新のAIエージェント開発フレームワークについて日本語でまとめてください。
            結果はtxtで保存してください。""")
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