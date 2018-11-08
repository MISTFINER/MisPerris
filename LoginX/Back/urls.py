from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

#, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
urlpatterns=[
    url(r'^GestionUsuario/$',views.gestionarUsuario,name="gestionUsuario"),
    url(r'^login/$',views.ingresar,name="login"),
    url(r'^$',views.index,name="inicio"),
    url(r'^logout/$',views.salir,name="logout"),
    url(r'^listing/$',views.listing,name="listing"),
    url(r'^index/$', views.index,name="index"),
    url(r'^user_logged/$',views.user_logged,name="user_logged"),
    url(r'^password_restaurar/$',auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_email.html',
            ),name='password_reset',),
    url(r'^password_restaurar/done/$',auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html',
            ),name='password_reset_done',
            ),
    url(r'^password_restaurar/done/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                #[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}
        auth_views.PasswordResetConfirmView.as_view(
                success_url=reverse_lazy('password_reset_complete'),
                post_reset_login=True,
                template_name='password_reset_confirm.html',
                post_reset_login_backend=('django,contrib.auth.backend.AllowAllUsersModelBackend'),
                ),name='password_reset_confirm',
        ),
    url(r'^password_restaurar_complete', auth_views.PasswordResetCompleteView.as_view(
           template_name='password_reset_complete.html',
           ),name='password_reset_complete',
           ),
]

    #url(r'^reset/password_reset',password_reset,{'template_name':'templates/password_reset.html','email_template_name':'templates/password_email.html'},name="password_reset"),
    #url(r'^password_reset_done',password_reset_done,{'template_name':'templates/password_reset_done.html'},name="password_reset_done"),
    #url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',password_reset_confirm,{'template_name':'templates/password_reset_confirm.html'},name="password_reset_confirm"),
    #url(r'^reset/done',password_reset_complete,{'template_name':'templates/password_reset_complete.html'},name="password_reset_complete"),﻿
#     'django.contrib.auth.views.password_reset'
#    (r'^password/reset/done/$','django.contrib.auth.views.password_reset_done'),
#    (r'^password/reset/confirm/$','django.contrib.auth.views.password_reset_confirm'),
#    (r'^password/reset/complete/$','django.contrib.auth.views.password_reset_confirm'),
#    (r'^password/change/$','django.contrib.auth.views.password_change'),
#    (r'^password/change/done/$','django.contrib.auth.views.password_change_done'),
#    url(r'^password_reset/$',views.email,name="enviar_email"),
