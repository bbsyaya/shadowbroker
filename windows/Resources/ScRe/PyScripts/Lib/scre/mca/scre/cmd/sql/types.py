# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: types.py
from types import *
SQL_ACCESS_TYPE_READ_ONLY = 0
SQL_ACCESS_TYPE_READ_WRITE = 1
SQL_CONNECT_TYPE_DATA_SOURCE = 0
SQL_CONNECT_TYPE_DRIVER = 1
SQL_CONNECT_TYPE_SQLITE = 2
SQL_DATA_TYPE_UNKNOWN = 0
SQL_DATA_TYPE_CHAR = 1
SQL_DATA_TYPE_NUMERIC = 2
SQL_DATA_TYPE_DECIMAL = 3
SQL_DATA_TYPE_INTEGER = 4
SQL_DATA_TYPE_SMALLINT = 5
SQL_DATA_TYPE_FLOAT = 6
SQL_DATA_TYPE_REAL = 7
SQL_DATA_TYPE_DOUBLE = 8
SQL_DATA_TYPE_DATETIME = 9
SQL_DATA_TYPE_TIME = 10
SQL_DATA_TYPE_TIMESTAMP = 11
SQL_DATA_TYPE_VARCHAR = 12
SQL_DATA_TYPE_LONGVARCHAR = -1
SQL_DATA_TYPE_BINARY = -2
SQL_DATA_TYPE_VARBINARY = -3
SQL_DATA_TYPE_LONGVARBINARY = -4
SQL_DATA_TYPE_BIGINT = -5
SQL_DATA_TYPE_TINYINT = -6
SQL_DATA_TYPE_BIT = -7
SQL_DATA_TYPE_WCHAR = -8
SQL_DATA_TYPE_WVARCHAR = -9
SQL_DATA_TYPE_WLONGVARCHAR = -10
SQL_DATA_TYPE_GUID = -11
MSG_KEY_PARAMS_CONNECT = 65536
MSG_KEY_PARAMS_CONNECT_CONNECTION_STRING = 65537
MSG_KEY_PARAMS_CONNECT_FLAGS = 65538
MSG_KEY_PARAMS_CONNECT_ACCESS_TYPE = 65539
MSG_KEY_PARAMS_CONNECT_TIMEOUT = 65540
MSG_KEY_PARAMS_QUERY_BASE = 131072
MSG_KEY_PARAMS_QUERY_BASE_CONNECTION_INFO = 131073
MSG_KEY_PARAMS_QUERY_BASE_MAX_COLUMN_SIZE = 131074
MSG_KEY_PARAMS_QUERY_BASE_MAX_CHUNK_SIZE = 131075
MSG_KEY_PARAMS_QUERY_COLUMNS = 196608
MSG_KEY_PARAMS_QUERY_COLUMNS_BASE_INFO = 196609
MSG_KEY_PARAMS_QUERY_COLUMNS_TABLE_NAME = 196610
MSG_KEY_PARAMS_QUERY_STATEMENT = 262144
MSG_KEY_PARAMS_QUERY_STATEMENT_BASE_INFO = 262145
MSG_KEY_PARAMS_QUERY_STATEMENT_QUERY_STRING = 262146
MSG_KEY_RESULT_ERROR = 327680
MSG_KEY_RESULT_ERROR_ERROR_CODE = 327681
MSG_KEY_RESULT_ERROR_SQL_STATE = 327682
MSG_KEY_RESULT_ERROR_MSG = 327683
MSG_KEY_RESULT_CONNECTIONS = 393216
MSG_KEY_RESULT_CONNECT = 393217
MSG_KEY_RESULT_DISCONNECT = 393218
MSG_KEY_RESULT_CONNECTION = 393219
MSG_KEY_RESULT_CONNECTION_HANDLE_ID = 393220
MSG_KEY_RESULT_CONNECTION_CONNECTION_STRING = 393221
MSG_KEY_RESULT_CONNECTION_CONNECTION_TYPE = 393222
MSG_KEY_RESULT_CONNECTION_ACCESS_TYPE = 393223
MSG_KEY_RESULT_CONNECTION_AUTO_COMMIT = 393224
MSG_KEY_RESULT_CONNECTION_CREATE_TIME = 393225
MSG_KEY_RESULT_CONNECTION_LAST_USE_TIME = 393226
MSG_KEY_RESULT_CONNECTION_MAX_IDLE_DURATION = 393227
MSG_KEY_RESULT_DATABASES = 458752
MSG_KEY_RESULT_TABLES = 458753
MSG_KEY_RESULT_DRIVERS = 524288
MSG_KEY_RESULT_DRIVERS_DRIVER = 524289
MSG_KEY_RESULT_DRIVERS_ATTRIBUTE = 524290
MSG_KEY_RESULT_SOURCE = 589824
MSG_KEY_RESULT_SOURCE_DATA_SOURCE = 589825
MSG_KEY_RESULT_SOURCE_DESCRIPTION = 589826
MSG_KEY_RESULT_SERVER = 655360
MSG_KEY_RESULT_SERVER_SERVER = 655361
MSG_KEY_RESULT_EXECUTE = 720896
MSG_KEY_RESULT_EXECUTE_TOTAL_COLUMNS = 720897
MSG_KEY_RESULT_EXECUTE_START_ROW = 720898
MSG_KEY_RESULT_EXECUTE_END_ROW = 720899
MSG_KEY_RESULT_EXECUTE_ROWS_MODIFIED = 720900
MSG_KEY_RESULT_EXECUTE_QUERY_STRING = 720901
MSG_KEY_RESULT_EXECUTE_CONNECTION_STRING = 720902
MSG_KEY_RESULT_COLUMNS = 786432
MSG_KEY_RESULT_COLUMN_INFO = 786433
MSG_KEY_RESULT_COLUMN_INFO_WIDTH = 786434
MSG_KEY_RESULT_COLUMN_INFO_DATA_TYPE = 786435
MSG_KEY_RESULT_COLUMN_INFO_IS_NULLABLE = 786436
MSG_KEY_RESULT_COLUMN_INFO_NAME = 786437
MSG_KEY_RESULT_COLUMN_INFO_INDEX = 786438
MSG_KEY_RESULT_ROW = 851968
MSG_KEY_RESULT_CELL = 851969
MSG_KEY_RESULT_CELL_DATA = 851970
MSG_KEY_RESULT_CELL_INFO = 851971
MSG_KEY_RESULT_CELL_INFO_DATA_TYPE = 851972
MSG_KEY_RESULT_CELL_INFO_FLAGS = 851973
MSG_KEY_RESULT_CELL_INFO_COLUMN_INDEX = 851974