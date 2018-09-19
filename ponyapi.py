import requests

maze_host = 'https://ponychallenge.trustpilot.com/pony-challenge/maze'


def _check_http_ans(ans):
    if not ans.ok:
        raise requests.HTTPError(ans.text)
    return ans


def create_maze(width, height, pony_name, difficulty=0):
    json_body = {
        "maze-width": width,
        "maze-height": height,
        "maze-player-name": pony_name,
        "difficulty": difficulty
    }
    ans = _check_http_ans(requests.post(maze_host, json=json_body))
    return ans.json()['maze_id']


def get_maze(maze_id):
    ans = _check_http_ans(requests.get("{}/{}".format(maze_host, maze_id)))
    return ans.json()


def move(maze_id, direction):
    json_body = {
        "direction": direction
    }
    _check_http_ans(requests.post("{}/{}".format(maze_host, maze_id), json=json_body))


def get_ascii_maze(maze_id):
    ans = _check_http_ans(requests.get("{}/{}/print".format(maze_host, maze_id)))
    return ans.text
