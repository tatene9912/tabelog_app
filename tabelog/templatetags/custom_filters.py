from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """辞書からキーに対応する値を取得するカスタムフィルタ"""
    return dictionary.get(key)