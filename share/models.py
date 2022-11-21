from django.db import models
from django.contrib.auth.models import User

# 카테고리
class Category(models.Model):
    sort = models.CharField(max_length = 255)
    def __str__(self):
        return self.sort
    
# 상품 모델
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    Modify_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    price = models.IntegerField()
    dicount_price = models.IntegerField()
    image = models.ImageField(upload_to = 'images', default='default.png', blank=True)
    recruit_num = models.IntegerField()
    participants = models.IntegerField()
    joined_users = models.ManyToManyField(User, related_name='joined_users', blank = True)
    like = models.ManyToManyField(User,related_name = 'liked_users')
    like_num = models.IntegerField(default = 0)



