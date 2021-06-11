#  Visit http://www.druva.com/ for more information.
# ******************************************************************************
import os
import time
from datetime import date
import logging
import MySQLdb
from pymysql.cursors import DictCursor

# Edit these w.r.t. your environment dev/qa/staging/production
MYSQL_HOST = 'db'
MYSQL_PORT = 3306
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = 'qawzsx1'
MYSQL_DBNAME = 'dcloud'
MYSQL_DRIVER = 'pymysql'
LOGGING_LEVEL = logging.INFO
SCRIPT_NAME = "MDSShardCompactCleaner"

# Refer to
# https://druvajira.atlassian.net/browse/REAL-13805
# https://druvajira.atlassian.net/browse/REAL-13395


def get_db_connection():
    # CHARACTER_SET_NAME = "utf8mb4"
    db_connection = MySQLdb.connect(
        user=MYSQL_USERNAME,
        passwd=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        db=MYSQL_DBNAME,
        driver=MYSQL_DRIVER
    )
    SyncLog.info("DB Connection successful")
    return db_connection


def init_logging(logging_dir=None, log_stdout=True):
    import __builtin__
    if not logging_dir:
        log_dir = os.getcwd()
    log_dir = logging_dir
    log_dir = os.path.join(log_dir, SCRIPT_NAME + ".log")

    # create logger
    logger = logging.getLogger()
    logger.setLevel(LOGGING_LEVEL)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(LOGGING_LEVEL)

    fh = logging.FileHandler(log_dir + '/logfile.txt')
    fh.setLevel(LOGGING_LEVEL)

    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s - {%(filename)s:%(lineno)d} [%(levelname)s] %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch to logger
    if log_stdout:
        logger.addHandler(ch)
    logger.addHandler(fh)

    __builtin__.SyncLog = logger
    logger.info('--------LOGGER INITIATED--------')


def get_shards_with_duplicate_entries(cursor):
    """
    get_shards_with_duplicate_entries : Returns rows from mds_shard_compact
    which have more than 1 entries for a combination of
    customerid, sid, shard_id, doc_type
    :param cursor: DB cursor
    :return: SQL Rows list
    """
    query = """SELECT customerid,sid,doc_type,shard_id
    FROM mds_shard_compact
    GROUP BY customerid,sid,doc_type,shard_id
    HAVING COUNT(last_completed)>1
    ORDER BY id ASC);
    """
    cursor.execute(query)
    all_rows = list(cursor)
    return all_rows


def cleanup_duplicate_shard_entries(cursor, row):
    """
    :param cursor:
    :param row:
    :return:
    """
    SyncLog.debug("cleanup_duplicate_shard_entries row: %s", row)
    customerid = row.get('customerid')
    sid = row.get('sid')
    shard_id = row.get('shard_id')
    doc_type = row.get('doc_type')
    # Explanation for Below query
    # For all rows with particular (customerid,sid,shard_id, doc_type)
    # find the row with max last_completed, call this row_a
    # Now, delete all rows for combination of (customerid,sid,shard_id, doc_type)
    # except the row_a
    query2 = """DELETE FROM mds_shard_compact
    WHERE customerid={customerid}
    AND sid={sid}
    AND shard_id={shard_id}
    AND doc_type={doc_type}
    AND ID NOT IN (
        SELECT id FROM (
        SELECT id,MAX(last_completed) FROM mds_shard_compact
        WHERE customerid={customerid}
        AND sid={sid}
        AND shard_id={shard_id}
        AND doc_type={doc_type}
        ) AS T)
    """
    new_query2 = query2.format(
        customerid=customerid,
        sid=sid,
        shard_id=shard_id,
        doc_type=doc_type,
    )
    SyncLog.debug("cleanup_duplicate_shard_entries : 3 : %s", new_query2)
    cursor.execute(new_query2)
    SyncLog.info("cleanup_duplicate_shard_entries : Finished for cid=%s, sid=%s, shard_id=%s, doc_type=%s",
                 customerid, sid, shard_id, doc_type)


if __name__ == '__main__':
    init_logging()
    db_con = get_db_connection()
    # cursor = db_con.cursor(cursor=DictCursor)
    # duplicate_shard_entries = get_shards_with_duplicate_entries(cursor)
    # for each_row in duplicate_shard_entries:
    # cleanup_duplicate_shard_entries(cursor, each_row)
