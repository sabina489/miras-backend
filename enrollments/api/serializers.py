from rest_framework import serializers

from enrollments.models import Enrollment

from part.models import Part


class EnrollmentCreateSerializer(serializers.ModelSerializer):
    # object_id = serializers.IntegerField()
    # object_type = serializers.ChoiceField(choices=EnrollmentType.CHOICES)

    class Meta:
        model = Enrollment
        fields = (
            'student',
            'parts',
        )
        # extra_kwargs = {
        #     'object_id': {'write_only': True},
        #     'object_type': {'write_only': True}
        # }

    # def create(self, validated_data):
    #     object_type = validated_data['object_type']
    #     type_id = validated_data['object_id']
    #     enrollment = Enrollment.objects.create(student=validated_data['student'])
    #     enrollment.save()
    #     if object_type == EnrollmentType.PART:
    #         print('hurray this is the part I want')
    #         part = Part.objects.get(pk=type_id)
    #         part.enrolls.add(enrollment)
    #     # TODO: Handle the below cases
    #     elif object_type == EnrollmentType.NOTE:
    #         pass
    #     elif object_type == EnrollmentType.TEST:
    #         pass
    #     return validated_data


class EnrollmentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = (
            'id'
        )


class EnrollmentRetrieveSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['parts'] = [{
            'name': part.name,
            'id': part.id
        }
            for part in instance.parts.all()]
        part_0 = instance.parts.first()
        if part_0:
            course = part_0.course
            all_parts = course.parts.all()

            ret['course'] = course.name
            ret['all_parts'] = [{
                'name': part.name,
                'id': part.id
            } for part in all_parts]

        return ret

    class Meta:
        model = Enrollment
        fields = (
            'id',
            'student',
            'status',
            'parts',
            'created_at',
        )
