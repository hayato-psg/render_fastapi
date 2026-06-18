from typing import Optional

from fastapi.responses import HTMLResponse

from fastapi import FastAPI

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]


### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <html>
    <head>
        <title>ホームページだよ</title>
    </head>
    <body>
        <h1>私のホームページ</h1>

        <ul>
            <li>名前：島野勇斗</li>
            <li>趣味：スポーツ</li>ß
            <li>好きな食べ物：お肉</li>
        </ul>

        <p>ご覧いただきありがとうございます。</p>
    </body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/food")
async def favorite_food(food: str):
    return {
        "response": f"{food}が好きなんですね！私も食べてみたいです。"
    }