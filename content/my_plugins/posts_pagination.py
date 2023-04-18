from pelican import signals
from pelican.generators import Pagination


def set_posts_pagination(sender):
    posts = sender.context["articles"]
    per_page = sender.settings.get("PAGINATED_TEMPLATES", {}).get("posts", 10)

    if per_page:
        sender.context["pagination_page"] = Pagination(sender.settings, 1, posts, per_page)
    else:
        sender.context["pagination_page"] = None


def register():
    signals.page_generator_context.connect(set_posts_pagination)
