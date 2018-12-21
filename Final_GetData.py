import facebook
import requests

#### change the token here ####
# token = 'EAAa5vIGsXhIBAHWRUZAFEl7xhXbYlP5EbujAeOtZC8fOvjSqUp7lSKHZCUPMawGznX4SJZB4QTUCp1Nv5osbgcB6Axxk0vbjETlA7LMKkK3AADjjibuPZAnZCzeWT3OrhVPayZA5NmXF0ZAvoDLZBzyuy8064tHluvquQ3H49xDF2wUAZBDyuUZCGX4utTw7qADMqEZD'
#### --------------------- ####

with open('parameters.txt') as f:
    read_data = f.readline()
    token = f.readline()
# print(token)

graph = facebook.GraphAPI(access_token = token)
posts_info = graph.get_object('me/posts')

result = []

# get first 25 results
for post in posts_info['data']:
    post_info={}
    post_info['id'] = post['id']
    post_info['created_time']=post['created_time']

    comments_info = graph.get_object(post['id']+'/comments', summary=True)
    #print(comments_info)
    post_info['comments_count']=comments_info['summary']['total_count']
    likes_info = graph.get_object(post['id']+'/likes', summary=True)
    post_info['likes_count']=likes_info['summary']['total_count']
    result.append(post_info)

# get second 25 results
posts_info = requests.get(posts_info["paging"]["next"]).json()
for post in posts_info['data']:
    post_info={}
    post_info['id'] = post['id']
    post_info['created_time']=post['created_time']

    comments_info = graph.get_object(post['id']+'/comments', summary=True)
    #print(comments_info)
    post_info['comments_count']=comments_info['summary']['total_count']
    likes_info = graph.get_object(post['id']+'/likes', summary=True)
    post_info['likes_count']=likes_info['summary']['total_count']
    result.append(post_info)

# get third 25 results
posts_info = requests.get(posts_info["paging"]["next"]).json()
for post in posts_info['data']:
    post_info={}
    post_info['id'] = post['id']
    post_info['created_time']=post['created_time']

    comments_info = graph.get_object(post['id']+'/comments', summary=True)
    #print(comments_info)
    post_info['comments_count']=comments_info['summary']['total_count']
    likes_info = graph.get_object(post['id']+'/likes', summary=True)
    post_info['likes_count']=likes_info['summary']['total_count']
    result.append(post_info)

# write file
outfile = open("Facebook_analysis.txt", "w")
print(result, file=outfile)
