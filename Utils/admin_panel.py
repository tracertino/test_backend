from flask_admin.contrib.sqla import ModelView
from Models import db
from Models.support import Support
from Models.users import User, Role
from Models.videos import Category, Subcategory, Video
from flask_jwt_extended import jwt_required

from flask_admin import Admin
admin = Admin()

class UserView(ModelView):
    column_exclude_list = ('password', "token", )
    
class CategoryView(ModelView):
    
    # @jwt_required()
    # def is_accessible(self):
    #     # Ваша логика проверки доступа (например, на основе ролей пользователя)
    #     return True
    
    column_list = ('name',)
    form_columns = ('name',)

class SubcategoryView(ModelView):
    column_filters = ('category',)
    column_list = ('name', 'category',)
    form_columns = ('category', 'name',)
    
class VideoViews(ModelView):
    column_exlude_list = ("id", )
    
class RoleViews(ModelView):
    column_list = ("name",)
    form_columns = ('name',)
   
admin.add_view(RoleViews(Role, db.session))
admin.add_view(UserView(User, db.session, name="Users profile", url="/admin/users"))
admin.add_view(ModelView(Support, db.session, name="Support", url="/admin/support"))
admin.add_view(CategoryView(Category, db.session))
admin.add_view(SubcategoryView(Subcategory, db.session))
admin.add_view(VideoViews(Video, db.session))
