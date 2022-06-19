from django.conf.urls import url
from .views import listar_animais, index, listar_campanhas, perfil_animal, campanha_view,apoie,sobre

urlpatterns = [
    url('index/$', index,name='index'),
    url('sobre/$', sobre,name='sobre'),
    url('apoie/$', apoie,name='apoie'),
    url('adocao/$', listar_animais, name='listar_animais'),
    url('campanhas/$', listar_campanhas, name='listar_capanhas'),
    url('animal/perfil/(?P<pk>[0-9]+)', perfil_animal, name='perfil_animal'),
    url('campanha/view/(?P<pk>[0-9]+)', campanha_view, name='campanha_view'),
]