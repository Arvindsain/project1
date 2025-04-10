from django.contrib import admin
from .models import Question, Answer

# Question Admin
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    inlines = [AnswerInline]
    ordering = ('id',)

# Answer Admin
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'user', 'like_count', 'created_at',  'updated_at')
    list_filter = ('created_at',)
    search_fields = ('content',)
    ordering = ('id',)

    def like_count(self, obj):
        return obj.likes.count()
    like_count.short_description = 'Likes'

# Register models with admin site
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)