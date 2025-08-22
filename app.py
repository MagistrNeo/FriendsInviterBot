key1, key2, key3 = "секретные ключи"

#Профиль 4 Название профиля ()
key4 = ''
#Профиль 5 Название профиля ()
key5 = ''

#Профиль 6 Название профиля ()
key6 = ''

#Профиль 7 Название профиля ()
key7 = ''

#Профиль 8 Название профиля ()
key8 = ''

#Профиль 9 Название профиля ()
key9 = ''

#Профиль 10 Название профиля ()
key10 = ''

#Параметры для запроса
action = "отправить заявки"
zapros ="сухоцветы"
number_people = 20
profile = "диана"
#если поменяете название чата в своём сообществе, то здесь необходимо писать название чата
#на которое вы поменяли
#Наши чаты '💟ЛАЙКИ 10|10💟'  ВЗАИМНЫЕ ВСТУПЛЕНИЯ 5|5  КОММЕНТАРИИ 3|3 'ЛАЙКИ 15|15'
chat = 'ЛАЙКИ 15|15'

#Код
!pip install vk_api
import vk_api
profile = profile.lower()
data = {'диана':key1, 'лиза': key2, 'мария': key3}
def perevod(profile):
  return vk_api.VkApi(token=profile).get_api()

def abc(sess):
    sum = 0
    t = sess.groups.search(q = zapros, count = 200)['items']
    for e in t:
        try:
            if sess.groups.getMembers(group_id=e['id'])['count'] <= 2000:
              print(sum)
              if sum > number_people: break
              for j in sess.groups.getById(group_id=e['id'],fields = 'contacts'):
                  for s in j['contacts']:
                      user =  s['user_id']
                      if sess.users.get(user_ids=user,fields = 'sex')[0]['sex'] == 1 and sess.users.get(user_ids=user)[0]['is_closed'] == False:
                          sess.friends.add(user_id = user)
                          sum += 1
                          print('https://vk.com/public' + str(e['id']))
                          print('https://vk.com/id'+str(user))
        except BaseException as o:
            if 'Flood' in str(o):
              print("Vk больше не позволяет.")
              break


abc(perevod(data[profile]))