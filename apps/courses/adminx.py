import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource


class GlobalSettings(object):
    site_title = '君临天下之福邻忠帼'
    site_footer = '君临天下之福邻忠帼'
    menu_style = 'accordion'


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class CourseAdmin(object):
    list_display = [
        'id', 'name', 'teacher', 'desc', 'degree',
        'students', 'category', 'add_time'
    ]
    search_fields = [
        'id', 'name', 'teacher', 'desc', 'degree',
        'students', 'category', 'add_time']
    list_filter = [
        'name', 'teacher', 'desc', 'degree',
        'students', 'category', 'add_time'
    ]
    list_editable = [
        'id', 'name', 'teacher', 'desc', 'degree',
        'students', 'category', 'add_time'
    ]


class LessonAdmin(object):
    list_display = ['id', 'name', 'learn_times', 'add_time']
    search_fields =['name', 'learn_times', 'add_time']
    list_filter = ['name', 'learn_times', 'add_time']
    list_editable = ['name', 'learn_times']


class VideoAdmin(object):
    list_display = ['id', 'name', 'url', 'learn_times', 'add_time']
    search_fields = ['name', 'url', 'learn_times']
    list_filter = ['name', 'url', 'learn_times', 'add_time']
    list_editable = ['name', 'url', 'learn_times']


class CourseResourceAdmin(object):
    list_display = ['id', 'name', 'file', 'add_time']
    search_fields = ['name', 'file']
    list_filter = ['name', 'file', 'add_time']
    list_editable = ['name', 'file']











xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)