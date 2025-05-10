# /// script
# dependencies = [
#   "pygithub>=2.6.1"
# ]
# ///

import csv
import os
from mcp.server.fastmcp import FastMCP
from github import Github

# MCPサーバーインスタンスを作成
mcp = FastMCP("MyMCPServer")  # サーバー名は任意

# GitHubファイル内容取得ツール
@mcp.tool()
def get_file_content(repo: str, filepath: str) -> str:
    """GitHubリポジトリから特定ファイルの内容を取得する"""
    gh_token = os.environ.get("GITHUB_TOKEN")
    # GitHub API呼び出し
    g = Github(gh_token)
    repo_obj = g.get_repo(repo)
    content = repo_obj.get_contents(filepath).decoded_content.decode('utf-8')
    
    return content

# @mcp.resource("csv://sample")
@mcp.tool()
def get_sample_csv() -> list[list[str]]:
    """sample.csvファイルの中身を取得する"""
    
    # CSVファイルのパスを指定
    csv_file_path = os.path.join(os.path.dirname(__file__), "sample.csv")
    
    # CSVファイルを読み込む
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    
    return data

# 必要に応じてSlackメッセージ取得やコード検索のツールも同様に定義可能

if __name__ == "__main__":
    # ローカルでFastAPIサーバーを起動（デフォルトポート8000）
    mcp.run()
