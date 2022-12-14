from django.urls import path

from . import views


app_name = 'subscriptions'

urlpatterns = [
    path('api/active-products/', views.ProductWithMetadataAPI.as_view(), name='products_api'),
]

team_urlpatterns = ([
    path('', views.team_subscription, name='subscription_details'),
    path('demo/', views.team_subscription_demo, name='subscription_demo'),
    path('subscription-gated-page/', views.team_subscription_gated_page, name='subscription_gated_page'),

    # stripe checkout views
    path('checkout-success/', views.checkout_success, name='checkout_success'),
    path('checkout-canceled/', views.checkout_canceled, name='checkout_canceled'),

    # stripe elements views
    path('api/create_customer/', views.team_create_customer, name='create_customer'),
    path('subscription_success/', views.team_subscription_success, name='subscription_success'),

    # stripe integration views that return redirects to Stripe
    # these are the defaults
    path('stripe/create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('stripe/portal/', views.create_portal_session, name='create_stripe_portal_session'),

    # stripe api views that return Stripe URLs instead of redirects
    # these can be used by JavaScript front-ends to handle the redirect from the response
    path('stripe/api/create-checkout-session/', views.CreateCheckoutSession.as_view(),
         name='api_create_checkout_session'),
    path('stripe/api/create-portal-session/', views.CreatePortalSession.as_view(), name='api_create_portal_session'),
], 'subscriptions_team')
