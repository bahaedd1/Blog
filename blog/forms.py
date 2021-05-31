from django.forms import ModelForm
from .models import Article,Details
class ArticleForm(ModelForm): 
	class Meta : 
		model = Article 
		#fields = "__all__"  #pour tous les champs de la table
		fields=['title','content','img']   #pour quelques champs
class UserForm(ModelForm):
    model= Details()
    fields = "__all__"