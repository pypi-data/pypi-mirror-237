import contextlib
import contextvars
import os

namespace_context_var = contextvars.ContextVar('namespace_context_var', default=None)


@contextlib.contextmanager
def namespace_provider(namespace: str):
    # noinspection PyTypeChecker
    token = namespace_context_var.set(namespace)
    yield
    namespace_context_var.reset(token)


@contextlib.contextmanager
def namespace_context():
    # noinspection PyTypeChecker
    namespace = namespace_context_var.get()
    if namespace is None:
        namespace = os.environ.get("EVENTIX_NAMESPACE", "default")
    yield namespace


delay_tasks_context_var = contextvars.ContextVar('delay_tasks_context_var', default=True)


@contextlib.contextmanager
def delay_tasks(delay_tasks: bool = True):
    # noinspection PyTypeChecker
    token = delay_tasks_context_var.set(delay_tasks)
    yield
    delay_tasks_context_var.reset(token)


@contextlib.contextmanager
def delay_tasks_context():
    # noinspection PyTypeChecker
    delay_tasks = delay_tasks_context_var.get()
    yield delay_tasks


worker_id_context_var = contextvars.ContextVar('worker_id_context_var', default=None)


@contextlib.contextmanager
def worker_id_provider(worker_id: str):
    # noinspection PyTypeChecker
    token = worker_id_context_var.set(worker_id)
    yield
    worker_id_context_var.reset(token)


@contextlib.contextmanager
def worker_id_context():
    # noinspection PyTypeChecker
    worker_id = worker_id_context_var.get()
    if worker_id is None:
        worker_id = "default"
    yield worker_id


task_priority_context_var: contextvars.ContextVar[int | None] = contextvars.ContextVar(
    'task_priority_context_var',
    default=0
)


@contextlib.contextmanager
def task_priority_provider(priority: int):
    # noinspection PyTypeChecker
    token = task_priority_context_var.set(priority)
    yield
    task_priority_context_var.reset(token)


@contextlib.contextmanager
def task_priority_context():
    # noinspection PyTypeChecker
    priority = task_priority_context_var.get()
    yield priority


eventix_base_url_context_var: contextvars.ContextVar[str | None] = contextvars.ContextVar(
    'eventix_base_url_context_var',
    default=None
)


@contextlib.contextmanager
def eventix_base_url_provider(base_url: str | None):
    # noinspection PyTypeChecker
    token = eventix_base_url_context_var.set(base_url)
    yield
    eventix_base_url_context_var.reset(token)


@contextlib.contextmanager
def eventix_base_url_context():
    # noinspection PyTypeChecker
    base_url = eventix_base_url_context_var.get()
    yield base_url
