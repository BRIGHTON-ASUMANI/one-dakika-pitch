from app.models import Technology,User
from app import db

def setUp(self):
        self.user_brighton = User(username = 'brighton',password = 'password', email = 'brighton@gmail.com', bio = 'i am tall', profile_pic_path ='./static/photos/image.png' )
        self.new_technology = Technology(technology_id=12345,technologyname='technology',information = 'enter anything',user = self.user_brighton )

def tearDown(self):
        Technology.query.delete()
        User.query.delete

def test_check_instance_variables(self):
        self.assertEquals(self.new_technology.technology_id,12345)
        self.assertEquals(self.new_technology.technologyname,'enter anything')
        self.assertEquals(self.new_technology.information,"./static/photos/image.png")

def test_save_technology(self):
        self.new_technology.save_technology()
        self.assertTrue(len(Technology.query.all())>0)

def test_get_technology_by_id(self):

        self.new_technology.save_technology()
        get_technology = Technology.get_technology(12345)
        self.assertTrue(len(got_categories) == 1)
