from django.urls import path

from . import views

app_name="trading_dashboard"
urlpatterns = [
        path("",views.index, name="index" ),
        path("<int:asset_id>/", views.asset_details, name="asset_details"),
]
