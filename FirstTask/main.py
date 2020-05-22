import vk_api

from FirstTask.UserVk import UserVkClass
from FirstTask.contstants import login, password, vk_user_id

vk_session = vk_api.VkApi(login, password)
vk_session.auth()
api = vk_session.get_api()
users = []
tematic = str(input())
# tematic = "юмор"


def friends_get():
    friends = api.friends.get(user_id=vk_user_id)
    return friends


def groups_per_friend(id_group):
    try:
        groups = api.groups.get(user_id=id_group, extended=True, fields='activity')
        for i in groups['items']:
            if tematic.lower() in i['activity'].lower():
                create_friend(id_group, i['name'], i['id'], i['activity'])
                break
    except:
        pass


def create_friend(id_user, group_name, group_id, theme):
    user_vk = api.users.get(user_ids=id_user)[0]
    temp_user = UserVkClass(
        str(user_vk['first_name'] + " " + user_vk['last_name']), str(id_user), str(group_name), str(group_id),
        str(theme))
    users.append(temp_user)


def handle():
    friends = friends_get()['items']
    for id_friend in friends:
        groups_per_friend(int(id_friend))


handle()
if len(users) == 0:
    print("Таких друзей нет")
for u in users:
    print(u)
