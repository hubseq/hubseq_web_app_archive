
from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.subscriptions.helpers import get_stripe_module
from apps.subscriptions.models import SubscriptionModelBase
from apps.teams.models import Team

SYNC_INTERVAL = 12  # in hours, how often to sync each model


class Command(BaseCommand):
    help = 'Syncs Stripe subscriptions for associated data models'

    def handle(self, **options):
        for team in Team.get_items_needing_sync():
            _sync_with_stripe(team)


def _sync_with_stripe(subscription_model: SubscriptionModelBase):
    print(f'syncing {subscription_model} with Stripe. Last synced: {subscription_model.last_synced_with_stripe or "never"}')
    # snapshot the time before the sync happens, in case the model changes while it is being synced
    sync_time = timezone.now()
    stripe = get_stripe_module()
    # retrieve and update the quantity on the subscription
    # modified from https://stripe.com/docs/billing/subscriptions/per-seat#change-price
    current_subscription = stripe.Subscription.retrieve(subscription_model.subscription.id)
    stripe.Subscription.modify(
        subscription_model.subscription.id,
        items=[{
            'id': current_subscription['items']['data'][0].id,
            'quantity': subscription_model.get_quantity(),
        }],
    )
    subscription_model.last_synced_with_stripe = sync_time
    subscription_model.save()
