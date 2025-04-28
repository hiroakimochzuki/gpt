from openai import AzureOpenAI
import os  
  
# Azure OpenAI の API キーとエンドポイントを環境変数から取得  
azure_endpoint = os.environ["CHATBOT_AZURE_OPENAI_ENDPOINT"] 
api_key = os.environ["CHATBOT_AZURE_OPENAI_API_KEY"] 
deployment_name = "gpt-4o" # 先ほど作成したモデルのデプロイ名に置き換えてください
api_version = "2024-08-01-preview" # 先ほど作成したモデルの API バージョンに置き換えてください

# Azure OpenAI クライアントを作成  
client = AzureOpenAI(  
    azure_endpoint=azure_endpoint,  
    api_key=api_key,  
    api_version=api_version 
)
# チャット履歴を保持するリスト  
chat_history = [  
    {"role": "system", "content": "You are a helpful assistant."}  
]
  
# ユーザーからのメッセージに対して応答を生成する関数  
def get_response(message):  
    # ユーザーのメッセージを履歴に追加  
    chat_history.append({"role": "user", "content": message})  
    # ChatGPT からの応答を取得  
    response = client.chat.completions.create(  
        model=deployment_name, 
        messages=chat_history  
    ) 
    # 応答を履歴に追加  
    assistant_message = response.choices[0].message.content.strip()  
    chat_history.append({"role": "assistant", "content": assistant_message})
    return assistant_message  
  
if __name__ == "__main__":  
    while True:  
        user_input = input("You: ")  
        if user_input.lower() in ["exit", "quit"]:  
            break  
        print("ChatGPT:", get_response(user_input))   