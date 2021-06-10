import pymysql

class Dbclass(object):#데이터베이스 접속 데이터베이스 사용준비완료
     conn = pymysql.connect(host='192.168.0.16', user='root', password='1234', db='rpidb')
     curs = conn.cursor()

     def __init__(self):
          pass

     def Db_del(self):#데이터베이스 자료 삭제
          sql = "DELETE FROM color"
          self.curs.execute(sql)
          self.conn.commit()

     def Db_R(self):#데이터베이스 컬럼R값 리턴
          sql = "select R from color order by Indexnum desc limit 1"
          self.curs.execute(sql)
          self.conn.commit()
          return self.curs.fetchone()
          
     def Db_G(self):#데이터베이스 컬럼G값 리턴
          sql = "select G from color order by Indexnum desc limit 1"
          self.curs.execute(sql)
          self.conn.commit()
          return self.curs.fetchone()

     def Db_B(self):#데이터베이스 컬럼B값 리턴
          sql = "select B from color order by Indexnum desc limit 1"
          self.curs.execute(sql)
          self.conn.commit()
          return self.curs.fetchone()

     def Db_time(self):#데이터베이스 컬럼 time 값
          sql = "select time from color order by Indexnum desc limit 1" 
          self.curs.execute(sql)
          self.conn.commit()
          return self.curs.fetchone()

     def calculate(self,r,g,b):#데이터베이스 RGB값 평균 리턴
          total = r + g + b
          return total/3

     def Db_rgb(self):
          r = self.Db_R()
          g = self.Db_G()
          b = self.Db_B()
          return r[0],g[0],b[0]

     def Db_run_total(self):#R,G,B값을 받고 각 멤버함수로 넘겨주어서 RGB값 평균값 리턴
          r = self.Db_R()
          g = self.Db_G()
          b = self.Db_B()
          total = self.calculate(r[0],g[0],b[0])
          return total

def total_run():#모듈 실행 main
     dbclass = Dbclass()
     db_run = dbclass.Db_run_total()
     return db_run

def rgb_run():
     dbclass = Dbclass()
     db_r, db_g, db_b = dbclass.Db_rgb()
     db_time = dbclass.Db_time()
     return  db_r, db_g, db_b, db_time[0]

if __name__ == "__main__":
    pass