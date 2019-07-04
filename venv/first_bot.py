import vk_api
from config import *

vkUser = vk_api.VkApi(token = USER_TOKEN)

USER_ID = 136586
result = vkUser.method('users.get',
                       {'user_ids': '1, 333325'})
print(result[0]['first_name'])