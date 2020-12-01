from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
path('admin/', admin.site.urls),
path('', TemplateView.as_view(template_name="index.html")),
#path('accounts/', include('django.contrib.auth.urls')),
path('api/', include('backend.api.urls')) 
#path('',TemplateView.as_view(template_name="index.html")),
#url(r'^api/',include('backend.urls', namespace='api'))
#最後一行程式碼我註釋掉，因為執行報錯：Error:No module named 'backend.urls',暫時解決不掉，但是我執行的時候，註釋掉這行程式碼，是能正常執行的。
]


