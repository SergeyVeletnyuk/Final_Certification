import logging
import requests
import yaml

with open("testdata.yaml", "r") as f:
    data = yaml.safe_load(f)


def user_loging(token):
    resource = requests.get("https://test-stand.gb.ru/api/users/profile/20906",
                            headers={"X-Auth-Token": token})

    return resource.json()


def test_1(test_login):
    logging.info("Test1 API: logging user == user ")
    user = user_loging(test_login)['id']
    assert user == 20906

# def ttest_login():
#     response = requests.post(url="https://test-stand.gb.ru/gateway/login",
#                              data={'username': data['login'], 'password': data['passwd']})
#
#     # if response.status_code == 200:
#     return response.json()['token']
# print()
# print(f"id:{user_data['id']} == 20906,  name:{user_data['username']} == leonid")
# assert user_data['username'] == 'leonid'
# return user_data
