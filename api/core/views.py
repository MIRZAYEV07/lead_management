

class BaseViewSet:
    def get_extra_create_kwargs(self, **kwargs):
        return kwargs

    def get_extra_update_kwargs(self, **kwargs):
        return kwargs

    def perform_create(self, serializer):
        serializer.save(**self.get_extra_create_kwargs())

    def perform_update(self, serializer):
        serializer.save(**self.get_extra_update_kwargs())
