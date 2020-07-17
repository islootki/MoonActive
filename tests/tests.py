
from utils import consts
from utils.sql_conn import select_all
from utils.utils import init_log, get_expected_data

log = init_log()


def test_validate_data_in_db():
    tested_table_name = "test_table"
    # read all data from DB and validate
    raw_data = select_all(tested_table_name)
    actual_data = []
    # convert all data from DB to dict
    for line in raw_data:
        actual_data.append(dict(zip(consts.DB_COLUMNS, line)))
    # get expected data from json
    expected_data = get_expected_data(tested_table_name)
    # validate that the table has expected amount of lines
    assert len(expected_data) == len(actual_data), \
        f"Expected amount of records '{len(expected_data)}', Actual:{len(actual_data)}"
    db_codes = [i[consts.COLUMN_CODE] for i in actual_data]
    # validate that the keys are as expected
    assert all(elem in db_codes for elem in expected_data.keys()), \
        "Not all codes are equal"
    # validate for each key that it has the expected value
    for line in actual_data:
        code_items = expected_data[line[consts.COLUMN_CODE]]
        assert code_items[consts.COLUMN_DESC] == line[consts.COLUMN_DESC], \
            f'The description is wrong,\nExpected:' \
            f'{code_items[consts.COLUMN_DESC]}\nActual: {line[consts.COLUMN_DESC]}'
        assert code_items[consts.COLUMN_LIST] == line[consts.COLUMN_LIST], \
            f'The list is wrong,\nExpected:' \
            f'{code_items[consts.COLUMN_LIST]}\nActual: {line[consts.COLUMN_LIST]}'
        assert code_items[consts.COLUMN_DURATION] == line[consts.COLUMN_DURATION], \
            f'The duration is wrong,\nExpected:' \
            f'{code_items[consts.COLUMN_DURATION]}\nActual: {line[consts.COLUMN_DURATION]}'
