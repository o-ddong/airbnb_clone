from rest_framework import ModelSerializer

from wishlists.models import Wishlist


class WishlistSerializer(ModelSerializer):

    class Meta:
        model = Wishlist
        fields = "__all__"