import argparse
import sys
from datetime import datetime
from typing import Any

import requests
from loguru import logger
from pydantic import BaseModel, Field


class Response(BaseModel):
    code: int = Field(..., alias="code", description="返回值")
    msg: str = Field(..., alias="msg", description="提示信息")
    success: bool | None = Field(None, alias="success", description="token有时才有")
    data: Any | None = Field(None, alias="data", description="请求成功才有")


FIND_ROLE_LIST_API_URL = "https://api.kurobbs.com/user/role/findRoleList"
SIGN_URL = "https://api.kurobbs.com/encourage/signIn/v2"


def get_headers(token: str) -> dict:
    return {
        "osversion": "Android",
        "devcode": "2fba3859fe9bfe9099f2696b8648c2c6",
        "countrycode": "CN",
        "ip": "10.0.2.233",
        "model": "2211133C",
        "source": "android",
        "lang": "zh-Hans",
        "version": "1.0.9",
        "versioncode": "1090",
        "token": token,
        "content-type": "application/x-www-form-urlencoded; charset=utf-8",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.10.0",
    }


def make_request(url: str, headers: dict, data: dict) -> Response:
    response = requests.post(url, headers=headers, data=data)
    res = Response.model_validate_json(response.content)
    logger.info(res.model_dump_json(indent=2, exclude={"data"}))
    return res


def get_user_game_list(token: str, game_id: int) -> list[dict]:
    headers = get_headers(token)
    data = {"gameId": game_id}
    res = make_request(FIND_ROLE_LIST_API_URL, headers, data)
    return res.data


def sign(token: str) -> Response:
    user_game_list = get_user_game_list(token, 3)

    date = datetime.now().month
    headers = get_headers(token)
    data = {
        "gameId": user_game_list[0].get("gameId", 2),
        "serverId": user_game_list[0].get("serverId", None),
        "roleId": user_game_list[0].get("roleId", 0),
        "userId": user_game_list[0].get("userId", 0),
        "reqMonth": f"{date:02d}",
    }
    return make_request(SIGN_URL, headers, data)


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Sign in using a token.")
    parser.add_argument("token", type=str, help="The token to use for signing in.")
    args = parser.parse_args()
    try:
        # Call the sign function with the token from command line
        sign(args.token)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)
