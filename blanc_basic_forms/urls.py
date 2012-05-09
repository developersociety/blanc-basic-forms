from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
    url(r'^$',
        views.BasicFormView.as_view(),
        name='form'),
    url(r'^thanks/$',
        views.BasicFormThanksView.as_view(),
        name='form-thanks'),
)
