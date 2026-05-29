import self


class Sieunhan:
    def __init__ (self,para_ten,para_vukhi,para_mausac):


# sieu_nhan_A= Sieunhan()
# print(sieu_nhan_A)
#
# sieu_nhan_A.ten = "sieu nhan do"
# sieu_nhan_A. vukhi = ' kiem, sung'
# sieu_nhan_A. mausac = 'Do'
# print(f"vu khi cua sieu nhan A la {sieu_nhan_A.vukhi} va ten cua sieu nhan A la {sieu_nhan_A.ten}")
        self.ten = 'Sieu nhan'+ para_ten
        self.vu_khi= 'vu khi' + para_vukhi
        self.mausac= 'mau' + para_mausac
sieu_nhan_A = Sieunhan('do', 'dao', 'do')
sieu_nhan_B = Sieunhan('do','sung', 'vang')
print(sieu_nhan_B.mausac )