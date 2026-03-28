# 🛸 Tic-Tac-Toe: iOS 26 Ultra Edition

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0-green.svg)
![Architecture](https://img.shields.io/badge/architecture-Clean%20Architecture-orange.svg)
![UI](https://img.shields.io/badge/UI-iOS%2026%20Glassmorphism-lightgrey.svg)

Современная реализация "Крестиков-ноликов", построенная на принципах **Clean Architecture**. Проект сочетает в себе строгую серверную логику на Python и футуристичный интерфейс, вдохновленный концептами Apple Intelligence 2026 года.


## 🏗 Архитектура (Clean Architecture)
Проект разделен на независимые слои, что обеспечивает легкость тестирования и масштабирования:

1. **Domain Layer**: Чистые бизнес-модели (`Board`, `Game`) и логика игры (`GameService`). Не имеет внешних зависимостей.
2. **Application Layer**: Координирует выполнение задач через `GameApplicationService`.
3. **Infrastructure/Datasource**: Реализация хранения данных (`InMemoryRepository`) и маппинг сущностей.
4. **Web Layer**: Flask-контроллеры, REST API эндпоинты и DTO-модели (`WebMapper`).


## 🧠 Особенности ИИ и UX
* **Minimax Algorithm**: Бот просчитывает все исходы и гарантирует ничью при идеальной игре человека.
* **Multi-session**: Поддержка нескольких одновременных игр через уникальные `UUID`.
* **iOS 26 UI**: Эффект Glassmorphism (`backdrop-filter`).
* **Optimistic UI**: Мгновенный отклик на действия пользователя.


## 🚀 Запуск приложения

```bash
make all
```
### Адрес локального сервера
```
http://127.0.0.1:5000
```

---
## 🧪 Тестирование


Проект полностью покрыт автоматическими тестами с использованием pytest.
Bash

### Запуск всех тестов проекта
```
make test
```
## 🛠 Технологический стек

* **Backend**: Python 3.10+, Flask

* **Frontend**: Vanilla JavaScript (ES6+), Modern CSS3 (CSS Variables, Grid, Animations)

* **Testing**: Pytest

* **Patterns**: DTO (Data Transfer Object), Mapper, Repository, Dependency Injection

* **Note**: Проект выполнен с соблюдением принципов SOLID и DRY. Каждый компонент системы (модели, интерфейсы, реализации) находится в отдельном файле согласно ТЗ.