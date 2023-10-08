from django.forms import Form, CharField, Textarea, FloatField, FileField, ModelForm

from work_01_app.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "prod_name",
            "description",
            "price",
            "prod_count",
            "photo",
        ]

