class UserVkClass(object):

    def __init__(self, name, url, group_name, group_url, theme):
        self.name = name
        self.url = "https://vk.com/id" + url
        self.group_name = group_name
        self.group_url = "https://vk.com/public" + group_url
        self.group_theme = theme

    def __str__(self):
        return "User{ name " + self.name + " url " + self.url + "} : " \
                                                                "Group{ name" + self.group_name + " url " + self.group_url + " theme " + self.group_theme + "}"
