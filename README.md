# Тестовое задание BlackHub Games
Ссылка на тестовое задание: [задача](https://docs.google.com/document/d/1ZzHhi8-RUvANloYVx6XXqWbwZhkqnvvNRYouyVNFdmc/)

Данный сервис реализует простой прокси веб-сервер, возвращающий HTML контент со страницы ``https://blackrussia.online``

## Используемые технологи
- python
- fastapi
- selenium
- pytest
- docker
- docker-compose

## Как запустить этот проект локально?

- Убедитесь, что у вас установлен docker и docker-compose
- Склонируйте репозиторий и перейдите в директорию

  В терминале ввести команды:
  
  ```
  git clone https://github.com/toir02/test-task-blackhub/
  cd test-task-blackhub/
  ```
- Запустить проект

  В терминале ввести команду:

  ```
  docker-compose up --build
  ```

## API эндпоинты

Для обращения к API реализован один единственный эндпоинт, который принимает GET-запросы.

```
http://0.0.0.0:8080/{path}/
```
Данный эндпоинт возвращает HTML контент, в котором заменены ключевые слова ``Black Russia`` на ``BlackHub Games``

На остальные запросы, отличные от GET(POST, PUT, PATCH, DELETE) эндпоинт возвращает сообщение следующего формата со статус кодом 405:

```
{
    "detail": "method not allowed"
}
```
## Тестирование

Тестирование API реализовано с помощью pytest.

На данный момент общее покрытие кода тестами составляет более 75%.
