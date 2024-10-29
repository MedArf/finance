from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from django.template import loader
from .models import Asset, AssetDetails

#To add user_id and filter
def index(request):
    all_assets=Asset.objects.all()
    context = {"all_assets": all_assets }
    return render(request, "trading_dashboard/index.html", context)

def asset_details(request, asset_id):
    assetdetails = get_object_or_404(AssetDetails, pk=asset_id)
    return render(request, "trading_dashboard/asset_details.html", {"assetdetails": assetdetails})

def portfolio(request) :
    return HttpResponse("You're viewing portfolio")

