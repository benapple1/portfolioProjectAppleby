from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("automation", "Automation"),
        ("agent", "Agent"),
        ("media", "Media"),
        ("machine-learning", "Machine Learning"),
        ("web-app", "Web App"),
    ]

    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    summary = models.TextField()
    business_problem = models.TextField()
    tools_used = models.CharField(max_length=255)
    key_features = models.TextField()
    role_contribution = models.TextField()
    biggest_challenge = models.TextField()
    lessons_learned = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True)
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})
