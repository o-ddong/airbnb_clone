from django.utils import timezone
from rest_framework import serializers

from .models import Booking


class CreateRoomBookingSerializer(serializers.ModelSerializer):

    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate(self, data):
        """
        11.22 - 11.26 / 11.27 - 11.29 있는 경우
        11.26 - 11.27 예약 가능해야 하는데 현재는 불가 이거 처리 해야됨
        """
        if data["check_out"] <= data["check_in"]:
            raise serializers.ValidationError("Check in should be smaller than check out")
        if Booking.objects.filter(
            check_in__lte=data["check_out"],
            check_out__gte=data["check_in"],
        ).exists():
            raise serializers.ValidationError(
                "Those (or some) of those dates are already taken"
            )
        return data




class PublicBookingSerializer(serializers.Serializer):
    """
    Serializer은 따로 정의 필요 O
    ModelSerializer 사용시 따로 정의 필요 X
    """
    pk = serializers.IntegerField()
    check_in = serializers.DateField()
    check_out = serializers.DateField()
    experience_time = serializers.DateTimeField()
    guests = serializers.IntegerField()

    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )
