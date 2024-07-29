# epm.api.tests


## Зависимости

Перед началом запуска необходимо открыть в терминале корень репозитория с тестами и установить зависимости.
```
cd path_to_repo
pip install git+https://polygit.polymatica.ru/tests/infrastructure/data.types.db.git
pip install -r requirements.txt
```

## Запуск

**Запускать тесты нужно всегда только из корня репозитория!**

Для запуска прогона есть множество опций, с которыми можно ознакомится запустив команду pytest --help. Ниже представлен список основных опций запуска.
- host=HOST                                       Адрес стенда на котором будет выполнен прогон 
- admin_login=ADMIN_LOGIN                         Логин администратора стенда epm
- admin_password=ADMIN_PASSWORD                   Пароль администратора стенда epm
- platform_host=PLATFORM_HOST                     Адрес стенда платформы
- platform_admin_login=PLATFORM_ADMIN_LOGIN       Логин администратора стенда платформы  
- platform_admin_password=PLATFORM_ADMIN_PASSWORD Пароль администратора стенда платформы
- n=NUMBER OF THREADS                             Количество потоков.  
!! Важно подметить, что переданный администратор не должен использоваться другими пользователями, чтобы не ломать стабильность тестового прогона.   
!! В связи с отсутствием возможности создавать полноценных новых юзеров, временно поддерживается только один поток
!! admin_login и platform_admin_login должны быть разными учетными записями
  
Пример команды запуска:
```
pytest --host=https://dev.epm.polymatica.ru/ --admin_login=admin_user --admin_password=password --platform_host=http://192.168.10.204:11180/ --platform_admin_login=platform_admin_user --platform_admin_password=password -n=1
```

Отчеты о регулярных прогонах автотестов https://tests.pages.polymatica.ru/epm/epm.api.tests/