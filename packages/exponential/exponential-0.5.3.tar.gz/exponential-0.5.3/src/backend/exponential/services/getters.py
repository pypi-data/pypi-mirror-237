from exponential.services import ServiceType, service_manager
from typing import TYPE_CHECKING, Generator


if TYPE_CHECKING:
    from exponential.services.database.manager import DatabaseService
    from exponential.services.settings.manager import SettingsService
    from exponential.services.cache.manager import BaseCacheService
    from exponential.services.session.manager import SessionService
    from exponential.services.task.manager import TaskService
    from exponential.services.chat.manager import ChatService
    from sqlmodel import Session


def get_settings_service() -> "SettingsService":
    try:
        return service_manager.get(ServiceType.SETTINGS_SERVICE)
    except ValueError:
        # initialize settings service
        from exponential.services.manager import initialize_settings_service

        initialize_settings_service()
        return service_manager.get(ServiceType.SETTINGS_SERVICE)


def get_db_service() -> "DatabaseService":
    return service_manager.get(ServiceType.DATABASE_SERVICE)


def get_session() -> Generator["Session", None, None]:
    db_service = service_manager.get(ServiceType.DATABASE_SERVICE)
    yield from db_service.get_session()


def get_cache_service() -> "BaseCacheService":
    return service_manager.get(ServiceType.CACHE_SERVICE)


def get_session_service() -> "SessionService":
    return service_manager.get(ServiceType.SESSION_SERVICE)


def get_task_service() -> "TaskService":
    return service_manager.get(ServiceType.TASK_SERVICE)


def get_chat_service() -> "ChatService":
    return service_manager.get(ServiceType.CHAT_SERVICE)
