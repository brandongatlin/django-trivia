from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import game.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', game.views.index, name='home'),
    path('game/', include('game.urls'))] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)