#bài 25
import random
import time


class Post:
    def __init__(self,noi_dung,tac_gia):
        self.noi_dung=noi_dung
        self.tac_gia=tac_gia
        self.so_like=0
    def like(self):
        self.so_like+=1
        print("đã like")
bai_dang=Post("ăn cơm muộn","Phong",)
print(f"Post:'{bai_dang.noi_dung}'- tác giả:{bai_dang.tac_gia}- số like:{bai_dang.so_like}")
bai_dang.like()
print(bai_dang.so_like)
bai_dang.like()
print(f"Post:'{bai_dang.noi_dung}'- tác giả:{bai_dang.tac_gia}- số like:{bai_dang.so_like}")
#bài 26 và bài 27
class User:
    def __init__(self,ten,he,mau,tan_cong):
        self.ten=ten
        self.cap_bac=1
        self.he=he
        self.exp=0
        self.mau=mau
        self.diem_tan_cong= tan_cong
    def nhan_exp(self,diem):
        self.exp=self.exp+diem
        print(f"chúc mừng!{self.ten}đã nhận {self.exp}")

        if self.exp>1000:
            self.cap_bac+=1
            self.exp=0
            print(f"chúc mừng!{self.ten}đã lên cấp{self.cap_bac}")
    def bi_dam(self,sat_thuong):
        self.mau=self.mau-sat_thuong
        print(f"Ây da!{self.ten}đã bị đấm mất{sat_thuong}. Còn lai: {self.mau}")

        if self.mau<=0:
            print("GAME OVER")

    def dung_chieu_thuc(self,ke_thu):
        print(f"{self.ten} lao vào tấn công{ke_thu.ten}")
        sat_thuong_that=self.diem_tan_cong
        if self.he=="điện"and ke_thu.he=="nước":
            sat_thuong_that=sat_thuong_that*2
            print("vừa gây ra chí mạng,*2 sát thương")

        ke_thu.mau=ke_thu.mau-sat_thuong_that

        print(f"{ke_thu.ten} mất {sat_thuong_that} máu")
        print(f"máu còn lại của {ke_thu.ten}:{ke_thu.mau}")

pikachu=User("Pikachu","điện",1000,5000)
squirtle = User("Squỉtle","nước",100,200)

pikachu.dung_chieu_thuc(squirtle)
squirtle.dung_chieu_thuc(pikachu)
class Weapon:
    def __init__(self,name,sat_thuong,do_ben):
        self.name=name
        self.sat_thuong=sat_thuong
        self.do_ben=do_ben
    def cuong_hoa(self):
        self.sat_thuong+=1000
        print("cường hóa +1000")
        self.do_ben+=3

class Enemy:
    def __init__(self,ten,cap_do,luong_mau):
        self.ten=ten
        self.cap_do=cap_do
        self.luong_mau=luong_mau

sung_nuoc=Weapon("súng nước",1000,1)
ke_thu=Enemy("Ruby",1,100)
print(f"Weapon:'{sung_nuoc.name}'-sát thương:{sung_nuoc.sat_thuong}-độ bền{sung_nuoc.do_ben}")
print(f"Enemy:'{ke_thu.ten}'-cấp độ{ke_thu.cap_do}-luong_mau{ke_thu.luong_mau}")
sung_nuoc.cuong_hoa()
print(f"Weapon:'{sung_nuoc.name}'-sát thương:{sung_nuoc.sat_thuong}-độ bền{sung_nuoc.do_ben}")
sung_nuoc.cuong_hoa()
print(f"Weapon:'{sung_nuoc.name}'-sát thương:{sung_nuoc.sat_thuong}-độ bền{sung_nuoc.do_ben}\n \n \n")

class nhan_vat:
    def __init__(self,ten,mau_toi_da,suc_manh,):
        self.ten=ten
        self.mau_toi_da=mau_toi_da
        self.mau_hien_tai=mau_toi_da
        self.suc_manh=suc_manh
    def tan_cong(self,doi_thu):
        sat_thuong=random.randint(self.suc_manh + 1,self.suc_manh + 5)
        if sat_thuong<0:
            sat_thuong=0
        doi_thu.nhan_sat_thuong(sat_thuong)
        print(f"{self.ten}đã tấn công{doi_thu.ten}")
        print(f"gây ra{sat_thuong}sát thương")
    def nhan_sat_thuong(self,sat_thuong):
        self.mau_hien_tai-=sat_thuong
        if self.mau_hien_tai<0:
            self.mau_hien_tai=0
    def con_song( self):
        return self.mau_hien_tai>0
    def hien_thi_trang_thai(self):
        thanh_mau="█" * (self.mau_hien_tai//10)+ "░" * ((self.mau_toi_da - self.mau_hien_tai)//10)
        print(f"{self.ten}:[{thanh_mau}] {self.mau_hien_tai}/{self.mau_toi_da}hp")

def bat_dau_game():
    print("trận chiến bắt đầu")

    dung_si=nhan_vat(ten="Phong",mau_toi_da=100,suc_manh=1)
    quai_vat=nhan_vat(ten="Tuấn",mau_toi_da=100,suc_manh=1)
    hiep=1
    while dung_si.con_song()and quai_vat.con_song():
        print(f"hiệp {hiep}")
        dung_si.tan_cong(quai_vat)
        if not quai_vat.con_song():
            print(f"{quai_vat.ten} đã bị hạ gục!{dung_si.ten}chiến thắng")
            break

        time.sleep(1)
        quai_vat.tan_cong(dung_si)
        if not dung_si.con_song():
            print(f"{dung_si.ten}đã thua")
            break
        print("\n [trạng thái]")
        dung_si.hien_thi_trang_thai()
        quai_vat.hien_thi_trang_thai()
        hiep+=1
        time.sleep(2)

if __name__ == "__main__":
    bat_dau_game()