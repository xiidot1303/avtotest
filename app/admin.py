from django.contrib import admin
from app.models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'photo_display')
    list_filter = ('id',)
    search_fields = ('question_text',)
    ordering = ('id',)
    # fieldsets = (
    #     (None, {
    #         'fields': ('question_text', 'photo')
    #     }),
    #     ('Answer Variants', {
    #         'fields': ('variant_a', 'variant_b', 'variant_c', 'variant_d'),
    #     }),
    # )

    def photo_display(self, obj):
        if obj.photo:
            return f"📷 {obj.photo.url.split('/')[-1]}"
        return "No photo"
    photo_display.short_description = "Photo"