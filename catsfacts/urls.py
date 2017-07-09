from django.conf.urls import include, url
from django.contrib import admin
from facts import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'catsfacts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', views.view_list),
    url(r'^$', views.view_list, name='home'),

]
