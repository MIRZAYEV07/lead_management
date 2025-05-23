from django.utils.translation import gettext as _
from rest_framework.permissions import BasePermission, SAFE_METHODS




class DjangoModelPermissions(BasePermission):
    perms_action_map = {
        'create': ['%(app_label)s.add_%(model_name)s'],
        'retrieve': ['%(app_label)s.view_%(model_name)s'],
        'list': ['%(app_label)s.view_%(model_name)s'],
        'update': ['%(app_label)s.change_%(model_name)s'],
        'partial_update': ['%(app_label)s.change_%(model_name)s'],
        'destroy': ['%(app_label)s.delete_%(model_name)s']
    }

    custom_action_permission_format = '%(app_label)s.%(action)s' # '%(app_label)s.%(action)s_%(model_name)s'

    def get_custom_permission(self, view):
        if hasattr(view, 'action') and not view.action in self.perms_action_map:
            custom_perm = self.custom_action_permission_format % {
                'app_label': view.queryset.model._meta.app_label,
                'action': view.action,
                'model_name': view.queryset.model._meta.model_name
            }
            return custom_perm
        return None

    def has_permission(self, request, view):
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root views when using DefaultRouter.
        if getattr(view, '_ignore_model_permissions', False):
            return True

        if not request.user or not request.user.is_authenticated:
            return False

        queryset = self._queryset(view)

        custom_perm = self.get_custom_permission(view)

        if not hasattr(view, 'action') and custom_perm is None:
            raise NotImplementedError(
                _('ViewSet should be used or custom permission should be set to views')
            )

        perms = self.get_required_action_permissions(view.action, queryset.model)

        return request.user.has_perms(perms)

    def get_required_action_permissions(self, action, model_cls):
        """
        Given a model and an HTTP method, return the list of permission
        codes that the user is required to have.
        """
        kwargs = {
            'app_label': model_cls._meta.app_label,
            'model_name': model_cls._meta.model_name
        }

        if action in self.perms_action_map:
            return [perm % kwargs for perm in self.perms_action_map[action]]

        kwargs['action'] = action

        return [self.custom_action_permission_format % kwargs]

    def _queryset(self, view):
        # assert getattr(views, 'queryset', None) is not None, (
        #     'Cannot apply {} on a views that does not set '
        #     '`.queryset`'
        # ).format(self.__class__.__name__)
        return view.get_queryset()



