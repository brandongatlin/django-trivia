from django.contrib import admin
from .models import Question, Category, Score, Feedback


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'answer', 'is_true_false', 'options', 'category', 'image']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'player_name', 'score', 'created_at']


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'feedback_text', 'is_positive']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Feedback, FeedbackAdmin)