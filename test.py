import requests


TOKEN = 'wyxsqUlhpuCY2OgHCpeNtdVAsUSIHIOtBtoflmZzSMQ'
# APIのURL
api_url = 'https://notify-api.line.me/api/notify'
# 送りたい内容
send_contents = 'キノコード'

# 情報を辞書型にする
TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
send_dic = {'message': send_contents}

requests.post(api_url, headers=TOKEN_dic, data=send_dic)