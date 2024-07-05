from django.test import TestCase
from django.contrib.auth import get_user_model
from catalog.models import Comment, Blog, Author

User = get_user_model()
class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Blog.objects.create(title = 'A blog')
        test_user = User.objects.create_user(username = 'test_user')
        comment = Comment.objects.create(blog = Blog.objects.get(id=1), user = test_user)
        comment.save()
        test_user.save()

    def test_string_rep(self):
        comment = Comment.objects.get(id=1)
        expected_name = f'Comment Id - {comment.id}, User - {comment.user.username}'
        self.assertEqual(str(comment), expected_name)