import Database as db
import Graph
import Analysis

print("색상분석 프로그램입니다.")
print("원하시는 모드를 선택해주세요")
print("1번 실시간 변화 그래프")
print("2번 데이터베이스 초기화")
print("3번 색변화 알람")
print("---------------------")
mode_num = int(input("모드를 입력해주세요. :"))

if mode_num == 1:
    Graph.run()

if mode_num == 2:
    database_del = db.Dbclass()
    database_del.Db_del()
    print("데이터베이스가 초기화 되었습니다.")

if mode_num == 3:
    Analysis.data_analysis()