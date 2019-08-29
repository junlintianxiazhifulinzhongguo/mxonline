import xadmin

from apps.operations.models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ['id', 'name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']
    list_editable = ['name', 'mobile', 'course_name']


class CourseCommentsAdmin(object):
    list_display = ['id', 'user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']
    list_editable = ['user', 'course', 'comments']


class UserFavoriteAdmin(object):
    list_display = ['id', 'user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']
    list_editable = ['user', 'fav_id', 'fav_type']


class UserMessageAdmin(object):
    list_display = ['id', 'user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    list_editable = ['user', 'message', 'has_read']


class UserCourseAdmin(object):
    list_display = ['id', 'user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']
    list_editable = ['user', 'course']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
