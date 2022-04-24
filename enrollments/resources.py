from import_export import resources
from enrollments.models import Enrollment


class EnrollmentResource(resources.ModelResource):
    enrolled = resources.Field()

    def dehydrate_enrolled(self, obj):
        enrolled = ""
        if obj.parts:
            enrolled += ", ".join([f"{p.name}(part)" for p in obj.parts.all()])
        if obj.exams:
            enrolled += "(exams), ".join(
                [f"{e.name}(exam)" for e in obj.exams.all()])
        if obj.notes:
            enrolled += "(notes), ".join(
                [f"{n.title}(note)" for n in obj.notes.all()])
        return enrolled


    class Meta:
        model = Enrollment
        fields = ("id", "student__phone", "student__email", "status", "enrolled",)
        export_order = ("id", "student__phone", "student__email", "status", "enrolled",)
