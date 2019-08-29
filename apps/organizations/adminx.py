import xadmin

from apps.organizations.models import City, CourseOrg, Teacher


class CityAdmin(object):
    list_display = ['id', 'name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    list_editable = ['name', 'desc']


class CourseOrgAdmin(object):
    list_display = ['id', 'name', 'desc', 'tag', 'category', 'city']
    search_fields = ['name', 'desc', 'tag', 'category', 'fav_nums', 'address', 'students',
                     'course_nums', 'city']
    list_filter = ['name', 'desc', 'tag', 'category', 'fav_nums', 'address', 'students',
                   'course_nums', 'city__name', 'add_time']
    list_editable = ['name', 'desc', 'tag', 'category', 'fav_nums', 'address', 'students',
                     'course_nums', 'city']


class TeacherAdmin(object):
    list_display = ['id', 'name', 'org', 'work_years', 'points', 'click_nums', 'fav_nums']
    search_fields = ['name', 'org', 'work_years', 'points', 'click_nums', 'fav_nums']
    list_filter = ['name', 'org', 'work_years', 'points', 'click_nums', 'fav_nums', 'add_time']
    list_editable = ['name', 'org', 'work_years', 'points', 'click_nums', 'fav_nums',
                     'age', 'image', 'work_company']


xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
