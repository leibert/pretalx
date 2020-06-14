from django.db import models
from django.utils.translation import gettext_lazy as _
from django_scopes import ScopedManager

from pretalx.common.mixins import LogMixin


class Resource(LogMixin, models.Model):
    """Resources are file uploads belonging to a.

    :class:`~pretalx.submission.models.submission.Submission`.
    """

    submission = models.ForeignKey(
        to="submission.Submission", related_name="resources", on_delete=models.PROTECT
    )
    description = models.CharField(
        null=True, blank=True, max_length=1000, verbose_name=_("description")
    )
    resource = models.CharField(
        verbose_name=_("file link"), null=True, blank=True, max_length=1000,
        help_text=_("Link to video file or other resource for editing."),
    )

    objects = ScopedManager(event="submission__event")

    def __str__(self):
        """Help when debugging."""
        return f"Resource(event={self.submission.event.slug}, submission={self.submission.title})"
