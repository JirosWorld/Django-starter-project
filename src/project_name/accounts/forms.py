from django.contrib.auth.forms import UserChangeForm as _UserChangeForm

from .utils import validate_max_permissions, validate_max_user_permissions


class UserChangeForm(_UserChangeForm):
    _current_user = None
    _target_user = None

    def clean(self):
        if self._current_user is None:
            raise RuntimeError("Could not determine current user.")
        if self._target_user is None:
            raise RuntimeError("Could not determine target user.")

        cleaned_data = super().clean()
        user_permissions = cleaned_data.get("user_permissions")
        groups = cleaned_data.get("groups")
        is_superuser = cleaned_data.get("is_superuser")

        # Validate intended permissions
        validate_max_permissions(
            self._current_user, user_permissions, groups, is_superuser
        )

        # Validate current permissions
        validate_max_user_permissions(self._current_user, self._target_user)
