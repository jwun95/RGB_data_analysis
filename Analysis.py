import Database

def data_analysis():
    data_default = 0 
    b_r = 0
    b_g = 0
    b_b = 0

    while 1:
        total  = Database.total_run()
        r,g,b,time = Database.rgb_run()
        #print(f'바뀐 측정 값: R {b_r} -> {r}, G {b_g} -> {g}, B {b_b} -> {b} 변화 시간 : {time}')
        

        if total != data_default:
            print('알림! 측정값이 바뀌었습니다.')
            print(f'바뀐 측정 값: R {b_r} -> {r}, G {b_g} -> {g}, B {b_b} -> {b} 변화 시간 : {time}\n')

        data_default = total
        b_r = r
        b_g = g
        b_b = b

if __name__ == "__main__":
    data_analysis()
            

