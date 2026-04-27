from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post, Comment, Category, Tag

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class PostForm(forms.ModelForm):
    category_names = forms.CharField(
        max_length=255, 
        required=True, 
        help_text="Enter categories separated by commas (e.g. Technology, Lifestyle)",
        label="Categories"
    )
    tag_names = forms.CharField(
        max_length=255, 
        required=False, 
        help_text="Enter tags separated by commas (e.g. python, django, coding)",
        label="Tags"
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'cover_image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['category_names'].initial = ', '.join([c.name for c in self.instance.categories.all()])
            self.fields['tag_names'].initial = ', '.join([t.name for t in self.instance.tags.all()])

    def save(self, commit=True, user=None):
        post = super().save(commit=False)
        if commit:
            post.save()
            
            # Process Categories — assign creator only when newly created
            category_names = self.cleaned_data.get('category_names', '')
            if category_names:
                category_list = [name.strip() for name in category_names.split(',') if name.strip()]
                categories = []
                for name in category_list:
                    cat, created = Category.objects.get_or_create(name=name)
                    if created and user:
                        cat.creator = user
                        cat.save()
                    categories.append(cat)
                post.categories.set(categories)

            # Process Tags
            tag_names = self.cleaned_data.get('tag_names', '')
            if tag_names:
                tag_list = [name.strip() for name in tag_names.split(',') if name.strip()]
                tags = []
                for name in tag_list:
                    tag, created = Tag.objects.get_or_create(name=name)
                    tags.append(tag)
                post.tags.set(tags)
            else:
                post.tags.clear()

        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        }
