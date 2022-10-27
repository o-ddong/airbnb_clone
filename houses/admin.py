from django.contrib import admin

from houses.models import House

# Register your models here.

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    field = ("name", "address", "price")

    # Admin columns에 보여지는 항목들
    list_display = ["name", "price_per_night", "address", "pets_allowed"]
    
    # filter
    list_filter = ["price_per_night", "pets_allowed"]

    # search filter
    search_fields = ["address"]

    # link 연결
    list_display_links = ["name", "address"]

    # 화면에서 수정 가능
    list_editable = ["pets_allowed"]