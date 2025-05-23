
class ChangeHistoryViewSetMixin:
    CHANGE_HISTORY_FIELDS_MAPPING = {
        'create': ['created_by', 'updated_by'],
        'update': ['updated_by']
    }

    def _get_model_field_names(self):
        return list(map(lambda field: field.name, self.get_queryset().model._meta.get_fields()))

    def _get_change_history_kwargs(self, action):
        model_field_names = self._get_model_field_names()

        kwargs = {}

        for field in self.CHANGE_HISTORY_FIELDS_MAPPING[action]:
            if field in model_field_names:
                kwargs[field] = self.request.user

        return kwargs

    def get_extra_create_kwargs(self, **kwargs):
        kwargs.update(self._get_change_history_kwargs('create'))
        return super(ChangeHistoryViewSetMixin, self).get_extra_create_kwargs(**kwargs)

    def get_extra_update_kwargs(self, **kwargs):
        kwargs.update(self._get_change_history_kwargs('update'))
        return super(ChangeHistoryViewSetMixin, self).get_extra_update_kwargs(**kwargs)
