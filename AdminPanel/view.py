from flask_admin.contrib.sqla import ModelView
from Models import db
from Models.support import Support
from Models.users import User, Role
from Models.videos import Category, Subcategory, PageVideo, Page, PageStars, PageBook
from Models.consultation import Consultation
from Models.study import Study
from Models.babyNames import BabyNames
from Models.babyLastnames import BabyLastnames
from AdminPanel import basic_auth
from flask_admin import Admin, expose
# from Admin_panel.video_view import VideoCategoryView, SubcategoryView


admin = Admin(name='Admin', template_mode='bootstrap3', url="/admin")

class UserView(ModelView):
    column_exclude_list = ('password', "token",)
    form_columns = ("email", 'user_name', "family_name", "last_name", "birthday", "role", )
    @expose('/')
    @basic_auth.required
    def index(self):
        return super(UserView, self).index_view()
    
class PageView(ModelView):
    column_list = ('name',)
    form_columns = ('name',)
    # @basic_auth.required
    # def index(self):
    #     return super(PageView, self).index_view()
    
class CategoryView(ModelView):
    column_labels = {
        "page": "Страница",
        "name": "Категория"
    }
    column_list = ('id','name', "page")
    form_columns = ('name', 'page', )
    column_filters = ['page']
    # column_editable_list = ['page']
    
    # form = CustomCategoryForm
    
    # def get_query(self):
    #     page = Page.query.filter_by(name = "video").first()
    #     return super(CategoryView, self).get_query().filter(Category.page == page)
    
    # # Для редактирования
    # def on_form_prefill(self, form, id):
    #     # Установите значение по умолчанию для категории (замените 'your_category_name' на фактическое имя категории)
    #     page = Page.query.filter_by(name='video').first()
    #     if page:
    #         form.page.data = page
            
    # def on_model_change(self, form, model, is_created):
    #     # Установите значение по умолчанию для категории только при создании записи
    #     if is_created:
    #         page = Page.query.filter_by(name='video').first()
    #         if page:
    #             model.page = page
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
    column_list = ('category.page', 'category', 'name',)
    form_columns = ('category', 'name',)
    
class VideoViews(ModelView):
    column_exclude_list = ("id", )
    
class StarsViews(ModelView):
    column_exclude_list = ("id", )
    
class BooksViews(ModelView):
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
    
class BabyNamesView(ModelView):
    column_exclude_list = ('id',)
    column_filters = ("gender", 'name', )
    
class BabyLastnamesView(ModelView):
    column_exclude_list = ('id',)
    column_filters = ("gender", 'name', )

admin.add_view(BabyNamesView(BabyNames, db.session, name="Child's name"))
admin.add_view(BabyLastnamesView(BabyLastnames, db.session, name="Child's lastname"))
# admin.add_view(RoleViews(Role, db.session))
admin.add_view(UserView(User, db.session, name="Users profile", url="/admin/users"))
admin.add_view(ModelView(Support, db.session, name="Support", url="/admin/support"))
admin.add_view(PageView(Page, db.session, category="Video"))
admin.add_view(CategoryView(Category, db.session, category="Video"))
admin.add_view(SubcategoryView(Subcategory, db.session, category="Video"))
admin.add_view(VideoViews(PageVideo, db.session, name="Page Video", category="Video"))
admin.add_view(StarsViews(PageStars, db.session, name="Page Stars", category="Video"))
admin.add_view(BooksViews(PageBook, db.session, name="Page Book", category="Video"))
admin.add_view(ConsultationView(Consultation, db.session))
admin.add_view(StudyView(Study, db.session))
