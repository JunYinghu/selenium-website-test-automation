from airbook.utils.writer import CSVWriter


class SearchResultWriter(CSVWriter):
    def __init__(self, filename):
        CSVWriter.__init__(self, filename, (
            'selected depature_id', 'selected returning_id', 'depature_date', 'returing_date', "promcode", 'diff_day',
            'actual_result_screen', 'expected_result', "status"))

