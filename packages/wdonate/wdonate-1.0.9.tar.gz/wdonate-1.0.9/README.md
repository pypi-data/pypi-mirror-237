# Как пользоваться библиотекой?

Сайт: wdonate.ru
Автор питон библы: vk.com/id486001202

Для установки:
```
pip install wdonate
```

Сначало инициализируем класс:

```py
from wdonate import wdonate
wd = wdonate('токен wdonate', group_id)
```

Методы к котором вы можете далее обратиться:

```py
wd.getBalance() -> float - получение баланса
```

Получение ссылки для оплаты:
```py
wd.getLink(user_id: int, amount: float = 0, payload: int = 0, pay_method: str = 'card') -> dict
```

получение списка последних донатов:
```py
wd.getPayments(count: int = 0) -> dict
```

получение текущей url callback:
```py
wd.getCallback() -> dict
```

установка url callback:
```py
wd.setCallback(url: str) -> dict
```

удаление текущей url callback
```py
wd.delCallback() -> dict
```
