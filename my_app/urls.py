from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AboutViewSet, ContactViewSet, NewsViewSet,
    PartnerViewSet, PublicationViewSet, ReviewViewSet,
    ServiceViewSet, TeamMemberViewSet
)

# Инициализация маршрутизатора
router = DefaultRouter()

# Регистрация ViewSet-ов для каждого ресурса
router.register(r'about', AboutViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'news', NewsViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'publications', PublicationViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'team-members', TeamMemberViewSet)

# Подключение маршрутизатора к URL-ам приложения
urlpatterns = [
    path('', include(router.urls)),
]
