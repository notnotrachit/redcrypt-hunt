from django.urls import path
from .views import get_profile, verify_discord_id, leaderboard
from apis.views import stats, ban, unban, easteregg

urlpatterns = [
    path('profile/<int:discord_id>', get_profile),
    path('verify_discord_id/<int:discord_id>', verify_discord_id),
    path('leaderboard', leaderboard),
    path('stats/<int:discord_id>', stats),
    path('ban/<int:discord_id>/<str:reason>', ban),
    path('unban/<int:discord_id>', unban),
    path('easteregg/<int:discord_id>/<str:egg>', easteregg),
]
