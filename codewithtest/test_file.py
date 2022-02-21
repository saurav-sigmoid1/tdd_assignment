import pytest


from codewithtest.code_part import oddTimeNumberOccurance


class Test_class:

    @pytest.fixture()
    def numberOccurance(self):
        numberoccurance = oddTimeNumberOccurance()
        return numberoccurance

    def test_callfunction(self,numberOccurance):
        assert numberOccurance.getOddOccurrence([1,2,3,4],4)

    def test_number_occur_odd_number_of_time(self,numberOccurance):
        arr =[1,1,2,2,3,3,3]
        val = numberOccurance.getOddOccurrence(arr,7)
        assert  val == 3

    def test_no_number_occur_odd_times(self,numberOccurance):
        arr = [1,1,2,2,3,3]
        val = numberOccurance.getOddOccurrence(arr,6)
        assert val == -1

    def test_array_is_empty(self,numberOccurance):
        arr = []
        val= numberOccurance.getOddOccurrence(arr,0)
        assert val == -1












    def test_readFromFile(self,monkeypatch,numberOccurance):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value = "Hello saurav")
        mock_open = MagicMock(return_value = mock_file)
        monkeypatch.setattr("builtins.open",mock_open)
        result = numberOccurance.readFromfile("test.txt")
        print(result)
        assert result == "Hello saurav"





# if __name__=="__main__":
#     unittest.main()


