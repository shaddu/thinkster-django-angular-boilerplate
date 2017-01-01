from rest_framework_nested import routers
from authentication.views import AccountViewSet, LoginView
from django.conf.urls import patterns
from django.conf.urls import include, url 
from thinkster_django_angular_boilerplate.views import IndexView



router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
     '',
    # ... URLs
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),    
    url(r'^api/v1/', include(router.urls)),
    url('^.*$', IndexView.as_view(), name='index'),

)