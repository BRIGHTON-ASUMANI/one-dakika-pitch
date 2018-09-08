from app.models import Category,User
from app import db

def setUp(self):
        self.user_brighton = User(username = 'brighton',password = 'password', email = 'brighton@gmail.com', bio = 'i am tall', profile_pic_path ='./static/photos/image.png' )
        self.new_category = Category(category_id=12345,categoryname='technology',information = 'enter anything',user = self.user_brighton )

def tearDown(self):
        Category.query.delete()
        User.query.delete

def test_check_instance_variables(self):
        self.assertEquals(self.new_category.category_id,12345)
        self.assertEquals(self.new_category.categoryname,'enter anything')
        self.assertEquals(self.new_category.information,"./static/photos/image.png")

def test_save_category(self):
        self.new_category.save_category()
        self.assertTrue(len(Category.query.all())>0)

def test_get_category_by_id(self):

        self.new_category.save_category()
        got_categories = Review.get_categories(12345)
        self.assertTrue(len(got_categories) == 1)
