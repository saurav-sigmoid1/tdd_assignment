import pytest
from codewithtest.code_part import oddTimeNumberOccurance


class TestClass:

    @pytest.fixture()
    def numberOccurance(self):
        numberoccurance = oddTimeNumberOccurance()
        return numberoccurance

    def setup_class(self):
        self.testfile = open('test.txt','r')
        self.testdata = self.testfile.readlines()

    def teardown_class(self):
        self.testfile.close()

    def test_callfunction(self,numberOccurance):
        assert numberOccurance.getOddOccurrence([1,2,3,4],4)

    def test_number_occur_odd_number_of_time(self,numberOccurance):
        arr =[1,1,2,2,3,3,3]
        val = numberOccurance.getOddOccurrence(arr,7)
        assert  val == 3

    def test_only_single_elementPresent(self,numberOccurance):
        arr=[1]
        val = numberOccurance.getOddOccurrence(arr,1)
        assert val == 1

    def test_no_number_occur_odd_times(self,numberOccurance):
        arr = [1,1,2,2,3,3]
        val = numberOccurance.getOddOccurrence(arr,6)
        assert val == -1

    def test_number_occur_odd_number_of_time_unsorted_array(self,numberOccurance):
        arr  = [1,2,3,1,2,3,1]
        val = numberOccurance.getOddOccurrence(arr,7)
        assert val==1

    def test_array_is_empty(self,numberOccurance):
        arr = []
        val= numberOccurance.getOddOccurrence(arr,0)
        assert val == -1





















