#! /bin/bash

echo "Getting database name"
rm db.* store/migrations/0*

python manage.py makemigrations
python manage.py migrate


imports="
from django.contrib.auth import get_user_model;
from store.models import Dish;
User = get_user_model();
"

admin=adm
password=adm
shell_comd="
$imports
User.objects.create_superuser(email='admin@admin.com', username='$admin', password='$password');

data = {'name': 'Chicken Soup', 'price': 20000, 'weight': 100, 'rations': 2, 'price_per_weight': 20000/100};
Dish.objects.create(**data);
data = {'name': 'Vietnamese rolls', 'price': 50000, 'weight': 300, 'rations': 1, 'price_per_weight': 50000/300};
Dish.objects.create(**data);
data = {'name': 'Rice with pork and vegetables', 'price': 40000, 'weight': 180, 'rations': 3, 'price_per_weight': 40000/180};
Dish.objects.create(**data);
"

echo $shell_comd | python manage.py shell

python manage.py runserver
