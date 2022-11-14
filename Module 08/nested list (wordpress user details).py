list = [
{
"id": 1,
"name": "Igor",
"url": "",
"description": "",
"link": "https://math.berkeley.edu/wp/blog/author/admin/",
"slug": "admin",
"avatar_urls": {
"24": "https://secure.gravatar.com/avatar/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=24&d=identicon&r=g",
"48": "https://secure.gravatar.com/avatar/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=48&d=identicon&r=g",
"96": "https://secure.gravatar.com/avatar/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=96&d=identicon&r=g"
},
"meta": [],
"_links": {
"self": [
{
"href": "https://math.berkeley.edu/wp/wp-json/wp/v2/users/1"
}
],
"collection": [
{
"href": "https://math.berkeley.edu/wp/wp-json/wp/v2/users"
}
]
}
}
]

print(type(list))

print('lenth : ', len(list))

my_list = (list[0])
print(my_list)
avatar_urls = my_list['avatar_urls']

print('User : ', my_list.get('name'))
print('slug : ', my_list.get('slug'))
print('avatar_urls : ',avatar_urls.get('96'))

