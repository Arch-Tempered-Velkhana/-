# -*- coding:utf-8 -*-
"""
作者：Administrator
日期：2022-07-18
时间：18:30
"""
from PIL import Image as Img
import os


def output(wpx, hpx, filenames, output_folder, px=128):
    if not filenames:
        print('end\n')
        return
    if not output_folder:
        print('end\n')
        return
    for ui in filenames:
        img = Img.open(ui)
        if img.size[0] / wpx == img.size[1] / hpx:
            pic = img.resize((wpx * px, hpx * px))
        else:
            if int(wpx / img.size[0] * img.size[1]) < hpx:
                bg_cut_px = int((hpx * px - int(wpx * px / img.size[0] * img.size[1])) / 2)
                pic = img.resize((int(hpx * px / img.size[1] * img.size[0]), hpx * px)).crop(
                    (0 + bg_cut_px, 0, wpx * px + bg_cut_px, hpx * px))
            else:
                bg_cut_px = int((wpx * px - int(hpx * px / img.size[1] * img.size[0])) / 2)
                pic = img.resize((wpx * px, int(wpx * px / img.size[0] * img.size[1]))).crop(
                    (0, 0 + bg_cut_px, wpx * px, hpx * px + bg_cut_px))
        img.close()
        folder_name = '{0}/{1}'.format(output_folder, os.path.splitext(ui)[0].split('/')[-1])
        s = 0
        while os.path.exists(folder_name):
            s += 1
            folder_name = '{0}/{1}({2})'.format(output_folder, os.path.splitext(ui)[0].split('/')[-1], s)
        os.mkdir(folder_name)
        for i in range(wpx):
            for j in range(hpx):
                pic.crop((i * px, j * px, (i + 1) * px, (j + 1) * px)).save(
                    '{0}/{1}_{2}.png'.format(folder_name, j, i))
    print('end\n')


if __name__ == '__main__':
    import tkinter
    from tkinter.filedialog import askopenfilenames, askdirectory
    tk = tkinter.Tk()
    output(int(input('长（格）：')), int(input('高（格）：')), askopenfilenames(), askdirectory())
    tk.mainloop()
