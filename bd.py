"""
	Вся работа с БД будет тут
"""
import sqlite3


class BD:
	def __init__(self, name_bd="mybd.sqlite"):
		""" инитиализация курсора и бд"""
		self.conn = sqlite3.connect(name_bd)
		self.cursor = self.conn.cursor()

	def create_tables(self):
		""" Creating new base of date"""
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS details 
			(id, name_detail, type)
			""")
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS drons
			(id, name_dron, cost)
			""")
		self.cursor.execute("""
			CREATE TABLE  IF NOT EXISTS dron_map
			(id, name, detail, count_detail)
			""")
		self.conn.commit()
		return True

	def insert_in_tables(self, details_table=[], drons_table=[], dron_map=[]):

		self.cursor.executemany("INSERT INTO details VALUES (?,?,?)", details_table)
		self.conn.commit()
		self.cursor.executemany("INSERT INTO drons VALUES (?,?,?)", drons_table)
		self.conn.commit()
		self.cursor.executemany("INSERT INTO dron_map VALUES (?,?,?,?)", dron_map)
		self.conn.commit()


def test():
	# Тестовые данные
	details_table = [
		(1, 'detail1', 'batter'),
		(2, 'detail2', 'batter'),
		(3, 'dateil3', 'other')
	]
	drons_table = [
		(1, 'dron1', 100),
		(2, 'dron2', 300)
	]
	dron_map = [
		(1, 'dron1', 'detail1', 23),
		(1, 'dron1', 'detail2', 2),
		(2, 'dron2', 'detail1', 1),
		(2, 'dron2', 'detail2', 345)
	]
	bd = BD()
	bd.create_tables()
	bd.insert_in_tables(drons_table=drons_table,
						dron_map=dron_map,
						details_table=details_table)
