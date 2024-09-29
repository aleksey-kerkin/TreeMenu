from django import template

from tree_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("tree_menu/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context["request"]
    menu_items = MenuItem.objects.filter(menu__slug=menu_name).select_related(
        "menu", "parent"
    )
    current_url = request.path

    def build_menu_tree(items, current_url):
        tree = []
        for item in items:
            active = current_url == item.get_absolute_url()
            children = build_menu_tree(items.filter(parent=item), current_url)
            tree.append(
                {
                    "item": item,
                    "active": active,
                    "children": children,
                }
            )
        return tree

    menu_tree = build_menu_tree(menu_items, current_url)
    return {"menu_tree": menu_tree}
