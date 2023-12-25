from flask_admin.contrib.sqla import ModelView
from Models import db
from Models.support import Support
from Models.users import User, Role
from Models.videos import Category, Subcategory, Video
from . import basic_auth

from flask_admin import Admin, expose
admin = Admin(name='Admin', template_mode='bootstrap3', url="/admin")


class UserView(ModelView):
    column_exclude_list = ('password', "token", )
    @expose('/admin')
    @basic_auth.required
    def index(self):
        return super(UserView, self).index_view()
    
class CategoryView(ModelView):
    column_list = ('name',)
    form_columns = ('name',)
    @expose('/admin')
    @basic_auth.required
    def index(self):
        return super(CategoryView, self).index_view()

class SubcategoryView(ModelView):
    column_filters = ('category',)
    column_list = ('name', 'category',)
    form_columns = ('category', 'name',)
    
class VideoViews(ModelView):
    column_exclude_list = ("id", )
    
class RoleViews(ModelView):
    column_list = ("name",)
    form_columns = ('name',)
    
admin.add_view(RoleViews(Role, db.session))
admin.add_view(UserView(User, db.session, name="Users profile", url="/admin/users"))
admin.add_view(ModelView(Support, db.session, name="Support", url="/admin/support"))
admin.add_view(CategoryView(Category, db.session))
admin.add_view(SubcategoryView(Subcategory, db.session))
admin.add_view(VideoViews(Video, db.session))
