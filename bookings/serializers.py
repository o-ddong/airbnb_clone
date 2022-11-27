from rest_framework import serializers

from .models import Booking


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
