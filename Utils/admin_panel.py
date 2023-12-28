from flask_admin.contrib.sqla import ModelView
from Models import db
from Models.support import Support
from Models.users import User, Role
from Models.videos import Category, Subcategory, Video, Page
from Models.consultation import Consultation
from Models.study import Study
from . import basic_auth
from flask_admin import Admin, expose

admin = Admin(name='Admin', template_mode='bootstrap3', url="/admin")

class UserView(ModelView):
    column_exclude_list = ('password', "token", )
    @expose('/')
    @basic_auth.required
    def index(self):
        return super(UserView, self).index_view()
    
class PageView(ModelView):
    column_list = ('name',)
    form_columns = ('name',)
    # @expose('/')
    # def index(self):
    #     return self.render('admin/index.html')
    # @basic_auth.required
    # def index(self):
    #     return super(PageView, self).index_view()
    
class CategoryView(ModelView):
    column_labels = {
        "page": "Страница",
        "name": "Категория"
    }
    column_list = ('id','name', "page")
    form_columns = ('name', "page")
    # @expose('/')
    # @basic_auth.required
    # def index(self):
    #     return super(CategoryView, self).index_view()

class SubcategoryView(ModelView):
    column_labels = {
        "category.page": "Страница",
        "category": "Категория",
        "name": "Подкатегория"
    }
    column_filters = ('category', "category.page")
    column_list = ("id", "category.id", 'category.page', 'category', 'name',)
    form_columns = ('category', 'name',)
    
class VideoViews(ModelView):
    column_exclude_list = ("id", )
    
class RoleViews(ModelView):
    column_list = ("name",)
    form_columns = ('name',)

class ConsultationView(ModelView):
    column_exclude_list = ('id',)
    form_columns = ('levels', 'title', 'link', 'videolink')

class StudyView(ModelView):
    column_exclude_list = ('id',)
    form_columns = ('levels', 'title', 'link', 'videolink')

admin.add_view(RoleViews(Role, db.session))
admin.add_view(UserView(User, db.session, name="Users profile", url="/admin/users"))
admin.add_view(ModelView(Support, db.session, name="Support", url="/admin/support"))
admin.add_view(PageView(Page, db.session))
admin.add_view(CategoryView(Category, db.session))
admin.add_view(SubcategoryView(Subcategory, db.session))
admin.add_view(VideoViews(Video, db.session))
admin.add_view(ConsultationView(Consultation, db.session))
admin.add_view(StudyView(Study, db.session))
