from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.


class ExamCategory(models.Model):
    """Model definition for ExamCategory."""

    name = models.CharField(_("name"), max_length=128)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )

    class Meta:
        """Meta definition for ExamCategory."""

        verbose_name = 'ExamCategory'
        verbose_name_plural = 'ExamCategorys'

    def __str__(self):
        """Unicode representation of ExamCategory."""
        return self.name


class Exam(models.Model):
    """Model definition for Exam."""

    name = models.CharField(_("name"), max_length=128)
    category = models.ManyToManyField(ExamCategory,
                                      verbose_name=_("categories"),
                                      related_name="%(app_label)s_%(class)s_related",
                                      related_query_name="%(app_label)s_%(class)ss")
    created_at = models.DateField(_("created_at"), auto_now_add=True)

    class Meta:
        """Meta definition for Exam."""

        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'

    def __str__(self):
        """Unicode representation of Exam."""
        return self.name


class MCQExam(Exam):
    """Model definition for MCQExam."""

    class Meta:
        """Meta definition for MCQExam."""

        verbose_name = 'MCQExam'
        verbose_name_plural = 'MCQExams'


class MockExam(models.Model):
    """Model definition for MockExam."""

    timer = models.TimeField(_("timer"))

    class Meta:
        """Meta definition for MockExam."""

        verbose_name = 'MockExam'
        verbose_name_plural = 'MockExams'


class GorkhapatraExam(models.Model):
    """Model definition for GorkhapatraExam."""

    content = models.FileField(
        _("content"), upload_to='exams/files/', blank=True, null=True)

    class Meta:
        """Meta definition for GorkhapatraExam."""

        verbose_name = 'GorkhapatraExam'
        verbose_name_plural = 'GorkhapatraExams'


class Question(models.Model):
    """Model definition for Question."""

    detail = models.TextField(_("detail"))
    img = models.ImageField(
        _("img"), upload_to='questions/', null=True, blank=True)
    exam = models.ForeignKey(Exam, verbose_name=_(
        "exam"), related_name=_("questions"), on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return "{}_{}".format(self.exam, self.id)


class Option(models.Model):
    """Model definition for Option."""
    detail = models.TextField(_("detail"))
    correct = models.BooleanField(_("correct"), default=False)
    question = models.ForeignKey(Question, verbose_name=_(
        "question"), related_name=_("options"), on_delete=models.CASCADE)
    feedback = models.TextField(_("feedback"))
    img = models.ImageField(
        _("img"), upload_to='options/', null=True, blank=True)

    class Meta:
        """Meta definition for Option."""

        verbose_name = 'Option'
        verbose_name_plural = 'Options'

    def __str__(self):
        """Unicode representation of Option."""
        return "{}_{}".format(self.question, self.id)


class QuestionStatus(models.Model):
    """Model definition for QuestionStatus."""

    examinee = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(
        "examinee"), on_delete=models.CASCADE, related_name='question_states')
    question = models.ForeignKey(Question, verbose_name=_(
        'question'), related_name=_("user_states"), on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, verbose_name=_(
        'selected_option'), related_name=_("user_choices"), on_delete=models.CASCADE)
    updated_at = models.DateTimeField(_("upadated_at"), auto_now=True)

    class Meta:
        """Meta definition for QuestionStatus."""

        verbose_name = 'QuestionStatus'
        verbose_name_plural = 'QuestionStatuss'

    def __str__(self):
        """Unicode representation of QuestionStatus."""
        return "option {} by {} for {}".format(
            self.selected_option,
            self.examinee,
            self.selected_option
        )
