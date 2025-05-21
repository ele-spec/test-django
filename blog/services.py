from blog.services import get_post
from unittest.mock import MagicMock

def test_mock_post():
    mock_post = MagicMock()
    mock_post.title = "Mocked Post"

    get_post = MagicMock(return_value=mock_post)
    post = get_post()
    
    assert post.title == "Mocked Post"