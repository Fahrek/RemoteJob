from django.contrib import admin
from .models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    list_display       = ["id", "address", "dni", "telephone", "mobile"]
    list_editable      = ["address", "telephone", "mobile"]
    list_display_links = None
    search_fields      = ["dni"]
    list_filter        = ["dni"]
    list_per_page      = 1


admin.site.register(Candidate, CandidateAdmin)
