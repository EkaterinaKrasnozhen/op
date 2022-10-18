import user_view as uv
import menu

res  = int(menu.user_interface_choce())

# запускается программа в зависимости от выбора пользователя
def start(number):
 if number == 1:
  uv.new_pers()
 elif number == 2:
  uv.find_someone()
 elif number == 3:
     return 3
  

