from mygrades.models import Student, Curriculum, Assignment, Standard, GradeBook, StudentAssignment, Teacher, Enrollment
import django_filters


GRADELEVEL = [
        ("P", "Pre-K"),
        ("K", "Kindergarten"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
    ]

class TeacherFilter(django_filters.FilterSet):
    
    first_name = django_filters.CharFilter(
        lookup_expr="icontains", label="First Name Contains(Complete Name Not Required)"
    )
    last_name = django_filters.CharFilter(
        lookup_expr="icontains", label="Last Name Contains(Complete Name Not Required)"
    )
   
    class Meta:
        model = Teacher
        fields = {}

class StudentFilter(django_filters.FilterSet):
    epicenter_id = django_filters.CharFilter(
        lookup_expr="icontains", label="Epicenter ID"
    )
    first_name = django_filters.CharFilter(
        lookup_expr="icontains", label="First Name Contains(Complete Name Not Required)"
    )
    last_name = django_filters.CharFilter(
        lookup_expr="icontains", label="Last Name Contains(Complete Name Not Required)"
    )
    grade = django_filters.CharFilter(
        lookup_expr="icontains", label="Grade Level"
    )

    class Meta:
        model = Student
        fields = {}

class EnrollmentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains", label="Title",
        field_name="curriculum__name",
    )
    subject = django_filters.CharFilter(
        lookup_expr="icontains", label="Subject",
        field_name="curriculum__subject",
    )
    #grade_level = django_filters.CharFilter(
    #    lookup_expr="icontains", label="Grade Level"
    #)
    recorded_from = django_filters.CharFilter(
        lookup_expr="icontains", label="Manual or Automatic?"
    )

    class Meta:
        model = Enrollment
        fields = {}

class CurriculumFilter(django_filters.FilterSet):

    SUBJECT = [
        ("Math", "Math"),
        ("ELA", "ELA"),
        ("Science", "Science"),
        ("History", "History"),
        ("Other", "Other"),
    ]
    CURRICULUMGRADE = [
        ("P", "Pre-K"),
        ("K", "Kinder"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
        ("All", "All"),
    ] 
    SEMESTER = [("1", "1"), ("2", "2"), ("Full Year", "Full Year"),]
    name = django_filters.CharFilter(
        lookup_expr="icontains", label="Title"
    )
    subject = django_filters.CharFilter(
        lookup_expr="icontains", label="Subject"
    )
    grade_level = django_filters.CharFilter(
        lookup_expr="icontains", label="Grade Level"
    )
    recorded_from = django_filters.CharFilter(
        lookup_expr="icontains", label="Manual or Automatic?"
    )

    class Meta:
        model = Curriculum
        fields = {}


class StandardFilter(django_filters.FilterSet):
    GRADELEVEL = [
        ("P", "Pre-K"),
        ("K", "Kinder"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
    ]
    SUBJECT = [
        ("Math", "Math"),
        ("ELA", "ELA"),
        ("Science", "Science"),
        ("History", "History"),
        ("Other", "Other"),
    ]

    subject = django_filters.CharFilter(
        lookup_expr="icontains", label="Subject")
    grade_level = django_filters.CharFilter(
        lookup_expr="icontains", label="Grade Level" )
    standard_code = django_filters.CharFilter(
        lookup_expr="icontains", label="Name Contains")
    objective_description = django_filters.CharFilter(
        lookup_expr="icontains", label="Objective Description Contains The Words")

    class Meta:
        model = Standard
        fields = {}


class AssignmentFilter(django_filters.FilterSet):
   
    standard = django_filters.CharFilter(
        lookup_expr="icontains", field_name="standard__standard_code",label="Standard Code")
    grade_level = django_filters.CharFilter(
        lookup_expr="exact", field_name="standard__grade_level", label="Standard Grade Level")
    curriculum = django_filters.CharFilter(
        lookup_expr="icontains", field_name="curriculum__name", label="Curriculum Title")
    name = django_filters.CharFilter(
        lookup_expr="icontains", label="Assignment Title")
    # tracking = django_filters.CharFilter(
        # lookup_expr="icontains", label="Grading Method")

    class Meta:
        model = Assignment
        fields = {}


class StudentAssignmentFilter(django_filters.FilterSet):
    
    assignment = django_filters.CharFilter(
        lookup_expr="icontains", label="Assignment Name")
    status = django_filters.CharFilter(
        lookup_expr="icontains", label="Assignment Status")
    
    class Meta:
        model = StudentAssignment
        fields = {}


class GradeBookFilter(django_filters.FilterSet):
    WEEK = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
        ("13", "13"),
        ("14", "14"),
        ("15", "15"),
        ("16", "16"),
        ("17", "17"),
        ("18", "18"),
    ]

    QUARTER = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ]
    student__name = django_filters.CharFilter(
        lookup_expr="icontains", label="Student")
    # curriculum = django_filters.CharFilter(
    #     lookup_expr="icontains", label="Curriculum")
    quarter = django_filters.CharFilter(
        lookup_expr="exact", label="Quarter")
    semester = django_filters.CharFilter(
        lookup_expr="exact", label="Semester")
    week = django_filters.CharFilter(
        lookup_expr="exact", label="Week")
    grade = django_filters.CharFilter(
        lookup_expr="icontains", label="Grade")

    class Meta:
        model = GradeBook
        fields = {}
