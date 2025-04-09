from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Mood(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Mood Name"))
    emoji = models.CharField(max_length=10, blank=True, null=True, verbose_name=_("Emoji"))

    class Meta:
        verbose_name = _("Mood")
        verbose_name_plural = _("Moods")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Mood_detail", kwargs={"pk": self.pk})


class Song(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Song Title"))
    artist = models.CharField(max_length=200, verbose_name=_("Artist"))
    category = models.ForeignKey(Mood, on_delete=models.CASCADE, related_name="songs", verbose_name=_("Mood"))
    review = models.TextField(blank=True, null=True, verbose_name=_("Review"))
    url = models.URLField(verbose_name=_("Song URL"))

    class Meta:
        verbose_name = _("Song")
        verbose_name_plural = _("Songs")

    def __str__(self):
        return f"{self.title} by {self.artist}"


class UserInput(models.Model):
    explanation = models.TextField(blank=True, null=True, verbose_name=_("Explanation"))
    selected_mood = models.ForeignKey(Mood, on_delete=models.CASCADE, related_name="user_inputs", verbose_name=_("Mood"))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("Date"))

    class Meta:
        verbose_name = _("User Input")
        verbose_name_plural = _("User Inputs")

    def __str__(self):
        return f"Input on {self.date.strftime('%Y-%m-%d %H:%M')}"


class Feedback(models.Model):
    user_input = models.ForeignKey(UserInput, on_delete=models.CASCADE, verbose_name=_("User Input"))
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name=_("Song"))
    liked = models.BooleanField(verbose_name=_("Liked"))

    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")

    def __str__(self):
        return f"Feedback: {'👍' if self.liked else '👎'}"
