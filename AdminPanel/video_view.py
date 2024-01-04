# from wtforms import StringField
# from wtforms.validators import DataRequired
# from flask_admin import form  
# from Models.videos import Page, Category, Subcategory
# from flask_admin.contrib.sqla import ModelView
# from Admin_panel import basic_auth
# from flask_admin import expose
  
# class VideoCustomCategoryForm(form.BaseForm):
#     page = StringField('Page', validators=[DataRequired()], render_kw={'readonly': 'readonly'})
#     name = StringField('Name', validators=[DataRequired()])
    
#     def __init__(self, *args, **kwargs):
#         super(VideoCustomCategoryForm, self).__init__(*args, **kwargs)
#         self.page.data = Page.query.filter_by(name = "video").first()
 
# class VideoCategoryView(ModelView):
#     column_labels = {
#         "page": "Страница",
#         "name": "Категория"
#     }
#     column_list = ('id','name', "page")
#     form_columns = ('name', 'page', )
#     column_filters = ['page']
#     form = VideoCustomCategoryForm
    
#     def get_query(self):
#         page = Page.query.filter_by(name = "video").first()
#         return super(VideoCategoryView, self).get_query().filter(Category.page == page)
    
#     def on_form_prefill(self, form, id):
#         page = Page.query.filter_by(name='video').first()
#         if page:
#             form.page.data = page
            
#     def on_model_change(self, form, model, is_created):
#         if is_created:
#             page = Page.query.filter_by(name='video').first()
#             if page:
#                 model.page = page
#     # @expose('/')
#     # @basic_auth.required
#     # def index(self):
#     #     return super(CategoryView, self).index_view()
    
    
# class SubcategoryView(ModelView):
#     column_labels = {
#         "category.page": "Страница",
#         "category": "Категория",
#         "name": "Подкатегория"
#     }
#     column_filters = ('category', "category.page")
#     column_list = ('category.page', 'category', 'name',)
#     form_columns = ('category.page', 'category', 'name',)
    
#     # def get_query(self):
#     #     page = Page.query.filter_by(name = "video").first()
#     #     return super(SubcategoryView, self).get_query().filter(Category.page == page)
    
#     # def on_form_prefill(self, form, id):
#     #     page = Page.query.filter_by(name='video').first()
#     #     if page:
#     #         form.page.data = page
            
#     # def on_model_change(self, form, model, is_created):
#     #     if is_created:
#     #         page = Page.query.filter_by(name='video').first()
#     #         if page:
#     #             model.page = page
    
 