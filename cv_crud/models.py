from django.db import models
from django.contrib.auth.models import User
from candidate_crud.models import Candidate


class CV(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    candidate     = models.ForeignKey(Candidate, on_delete=models.CASCADE, default='', blank=True, null=True)
    cv_txt        = models.TextField(default=None, verbose_name="CV en texto")
    created_at    = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.candidate.id

    class Meta:
        db_table: 'cv'
        verbose_name: 'Curriculum'
        verbose_name_plural: 'Curriculums'
        ordering: [id]
