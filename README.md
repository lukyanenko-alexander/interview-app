```shell
from services.models import Service
from clients.models import Client

Service(name="Burger", price=100).save()
Client(name="Viktor").save()
```



## 1.
* написать сериалайзер, который будет валидировать следующие поля:
  * client - проверять что переданный клиент существует в бд
  * address
  * services: 
    * проверка наличия в бд переданного товара, 
    * quanyity > 0 и < 99
* дописать метод create для создания заказа

## 2.
1. реализовать фикстуру для фабрики товара
2. отправить запрос на создание (/orders/)
3. проверить, что код ответа = 201

## 3. 
1. переписать фикстуру create_order_data так, чтобы в нее можно было передать произвольный параметр quanyity
2. проверить, что код ответа = 400, если передать кол-во > 100

## 4.
написать запрос, чтобы получить информацию о товаре, через промежуточную таблицу (OrderService)
следующим образом **order.order_services[i].service.name**
использовать методы select_related и prefetch_related, чтобы избежать проблему n + 1
