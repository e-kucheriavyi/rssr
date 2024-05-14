from pages.index import INDEX_PAGE
from pages.todo import TODO_PAGE

from ui.shared import validate_root

PAGES = {
    '/': INDEX_PAGE,
    '/todo': TODO_PAGE,
}

for key in PAGES:
    validate_root(PAGES[key]['root'], state=None)
