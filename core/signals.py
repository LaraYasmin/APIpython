from django.db.models import Avg, Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from .models import Review, Product


@receiver(post_save, sender=Review)
def review_created(sender, instance, created, **kwargs):
    if created:
        product = get_object_or_404(Product, id=instance.product_id)
        reviews = Review.objects.all()
        count = 0
        avg = 0.0
        for r in reviews:
            avg += r.score
            count += 1
        avg = avg / count
        product.review_score = round(avg, 1)
        product.save()
        print(product.review_score)