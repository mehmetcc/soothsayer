from soothsayer.utils import FileUtils


def test_get_parent_valid_filename_given_should_return_parent():
    filename = __file__
    parent = FileUtils.get_parent(filename)
    assert parent.split("/")[-2] == "soothsayer"


def test_get_caller_parent_valid_filename_given_should_return_parent():
    parent = FileUtils.get_caller_parent()
    assert parent.split("/")[-1] == "soothsayer"
