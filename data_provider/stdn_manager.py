import sql_provider.db_manager_sql as sql
import data_provider.user_input as us_in


def add_stdn():
    stdn = us_in.input_data()
    sql.add_stdn_sql(stdn)
