from flask_babel import gettext as _
from searx.plugins import Plugin


class RedditTranslationFilterPlugin(Plugin):
    id = "reddit_translation_filter"

    def __init__(self, plg_cfg):
        super().__init__(plg_cfg)
        self.info = PluginInfo(
            id=self.id,
            name=_("Reddit Translation Filter"),
            description=_("Filters auto-translated posts from results"),
        )

    def reddit_translation_filter(result, field_name, url_src) -> bool | str:
        if "reddit.com" not in url_src:
            return True
        return "?tl=" not in url_src

    def on_result(self, request, search, result) -> bool:
        result.filter_urls(RedditTranslationFilterPlugin.reddit_translation_filter)
        return True
