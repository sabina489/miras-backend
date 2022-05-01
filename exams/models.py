from django.db import models
from decimal import Decimal
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from courses.validators import validate_positive
# Create your models here.


class ExamType:
    MOCK = "mock"
    MCQ = "mcq"
    GORKHA = "gorkha"
    CHOICES = [
        (MOCK, "mock"),
        (MCQ, "mcq"),
        (GORKHA, "gorkha"),
    ]


class Exam(models.Model):
    """Model definition for Exam."""

    name = models.CharField(_("name"), max_length=128)
    category = models.ManyToManyField("courses.CourseCategory",
                                      verbose_name=_("categories"),
                                      related_name="%(app_label)s_%(class)s_related",
                                      related_query_name="%(app_label)s_%(class)ss")
    created_at = models.DateField(_("created_at"), auto_now_add=True)
    kind = models.CharField(_("kind"), max_length=32,
                            choices=ExamType.CHOICES, default=ExamType.MOCK)
    course = models.ForeignKey("courses.Course",
                               verbose_name=_("course"),
                               related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss",
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)
    price = models.DecimalField(
        _("price"), max_digits=5, decimal_places=2, default=Decimal("0.0"),
        validators=[validate_positive])

    def save(self, *args, **kwargs):
        if isinstance(self, MCQExam):
            self.kind = ExamType.MCQ
        elif isinstance(self, GorkhapatraExam):
            self.kind = ExamType.GORKHA
        super().save(*args, **kwargs)

    class Meta:
        """Meta definition for Exam."""

        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'
        ordering = ['-created_at']

    def __str__(self):
        """Unicode representation of Exam."""
        return self.name


class MCQExam(Exam):
    """Model definition for MCQExam."""

    class Meta:
        """Meta definition for MCQExam."""

        verbose_name = 'MCQExam'
        verbose_name_plural = 'MCQExams'


class MockExam(Exam):
    """Model definition for MockExam."""

    timer = models.TimeField(_("timer"))

    class Meta:
        """Meta definition for MockExam."""

        verbose_name = 'MockExam'
        verbose_name_plural = 'MockExams'


class GorkhapatraExam(Exam):
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
    marks = models.DecimalField(
        _("marks"), max_digits=5, decimal_places=2, default=Decimal("0.0"))
    neg_marks = models.DecimalField(
        _("neg_marks"), max_digits=5, decimal_places=2, default=Decimal("0.0"))

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['exam','id']

    def __str__(self):
        """Unicode representation of Question."""
        return f"{self.exam}_{self.id}"


class Option(models.Model):
    """Model definition for Option."""
    detail = models.TextField(_("detail"))
    correct = models.BooleanField(_("correct"), default=False)
    question = models.ForeignKey(Question, verbose_name=_(
        "question"), related_name=_("options"), on_delete=models.CASCADE)
    feedback = models.TextField(_("feedback"), blank=True, null=True)
    img = models.ImageField(
        _("img"), upload_to='options/', null=True, blank=True)
    marks = models.DecimalField(
        _("marks"), max_digits=5, decimal_places=2, default=Decimal("0.0"))

    class Meta:
        """Meta definition for Option."""

        verbose_name = 'Option'
        verbose_name_plural = 'Options'
        ordering = ['question', 'id']

    def __str__(self):
        """Unicode representation of Option."""
        return f"{self.question}_{self.id}"


class QuestionStatus(models.Model):
    """Model definition for QuestionStatus."""

    # examinee = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(
    #     "examinee"), on_delete=models.CASCADE, related_name='question_states')
    exam_stat = models.ForeignKey("enrollments.ExamStatus", verbose_name=_(
        "exam_stat"), on_delete=models.CASCADE, related_name='question_states')
    question = models.ForeignKey(Question, verbose_name=_(
        "question"), related_name=_("user_states"), on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, verbose_name=_(
        "selected_option"), related_name=_("user_choices"), on_delete=models.CASCADE)
    updated_at = models.DateTimeField(_("upadated_at"), auto_now=True)

    def save(self, *args, **kwargs):
        try:
            question = self.exam_stat.exam.questions.get(pk=self.question.id)
            option = self.question.options.get(pk=self.selected_option.id)
            super().save(*args, **kwargs)
        except Exception as error:
            raise error

    class Meta:
        """Meta definition for QuestionStatus."""

        verbose_name = 'QuestionStatus'
        verbose_name_plural = 'QuestionStatuss'
        ordering = ['-updated_at']

    def __str__(self):
        """Unicode representation of QuestionStatus."""
        return f"option {self.exam_stat} by {self.question} for {self.selected_option}"
