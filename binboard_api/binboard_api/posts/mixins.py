import datetime
from django.template.defaultfilters import pluralize


class CreatedAgoMixin:
    def timestamp(self) -> str:
        delta_t = datetime.datetime.now() - self.created_at

        if delta_t.seconds < 60:
            return 'just now'

        elif 60 <= delta_t.seconds < 3600:
            minutes = delta_t.seconds // 60
            return f'{minutes} minute{pluralize(minutes)} ago'

        elif 3600 <= delta_t.seconds < 86400:
            hours = delta_t.seconds // 3600
            return f'{hours} hour{pluralize(hours)} ago'

        elif delta_t.days == 1:
            return 'yesterday'

        elif 1 < delta_t.days < 7:
            days = delta_t.days
            return f'{days} days ago'

        elif 7 <= delta_t.days < 365:
            weeks = delta_t.days // 7
            return f'{weeks} week{pluralize(weeks)} ago'

        else:
            years = delta_t.days // 365
            return f'{years} year{pluralize(years)} ago'
