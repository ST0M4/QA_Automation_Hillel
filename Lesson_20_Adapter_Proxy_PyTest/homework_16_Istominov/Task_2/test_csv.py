from Lesson_20_Adapter_Proxy_PyTest.homework_16_Istominov.Task_2.code_for_testing_1 import add_row, delete_row


file_name = 'example_csv.csv'


def lines_counter():
    with open('example_csv.csv', 'r') as file:
        lines = file.readlines()
        total_lines = sum(1 for line in lines)
    return total_lines


class TestCSVUpdate:

    def test_add_line(self):
        lines_counter_start = lines_counter()
        add_row(file_name, ['Ben', 'Brown', 45, 'Male', 100000])
        lines_counter_end = lines_counter()
        assert lines_counter_start + 1 == lines_counter_end

    def test_delete_line(self):
        lines_counter_start = lines_counter()
        delete_row(file_name)
        lines_counter_end = lines_counter()
        assert lines_counter_start - 1 == lines_counter_end


