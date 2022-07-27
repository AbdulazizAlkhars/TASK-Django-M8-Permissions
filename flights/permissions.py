from rest_framework.permissions import BasePermission
from datetime import datetime


class HasAuth(BasePermission):
    message = "You must be Authorized of this booking."

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.is_staff


class IsNotTooSoon(BasePermission):
    message = "You cannot cancel this booking before 3 days."

    def has_object_permission(self, request, view, obj):
        return obj.date >= datetime.date.today() + datetime.timedelta(days=3)


"""
Adjust the permissions of the UpdateBooking and CancelBooking so that the booking cannot be canceled or modified unless it's more than 3 days away.
"""
