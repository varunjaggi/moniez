"""moniez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from moniez.apis import InitiateConsent
from moniez.apis import FetchConsent
from moniez.apis import AllStocks
from moniez.apis import (
    CreditDebitRatioMonthly,
    CurrentInvestment,
    CategoryWise,
    RecommendationView,
    InvestmentOptions,
    Profile,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("initiate-consent", InitiateConsent.as_view()),
    path("fetch-consent", FetchConsent.as_view()),
    path("recommendations", RecommendationView.as_view()),
    path("allinvestmentoptions", InvestmentOptions.as_view()),
    path("allstocks", AllStocks.as_view()),
    path("debitavg", CreditDebitRatioMonthly.as_view()),
    path("categorywise", CategoryWise.as_view()),
    path("currentinvestment", CurrentInvestment.as_view()),
    path("profile", Profile.as_view()),
]
