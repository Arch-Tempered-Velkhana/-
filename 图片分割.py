# -*- coding:utf-8 -*-
"""
作者：Administrator
日期：2022-07-18
时间：18:30
"""
import tkinter
from tkinter.filedialog import askopenfilenames, askdirectory
from PIL import Image as Img
import os
tk = tkinter.Tk()


def output(wpx, hpx, filenames, output_folder):
    if not filenames:
        print('end\n')
        return
    if not output_folder:
        print('end\n')
        return

    for ui in filenames:
        img = Img.open(ui)
        if img.size[0] / wpx == img.size[1] / hpx:
            pic = img.resize((wpx * 128, hpx * 128))
        else:
            if int(wpx / img.size[0] * img.size[1]) < hpx:
                bg_cut_px = int((hpx * 128 - int(wpx * 128 / img.size[0] * img.size[1])) / 2)
                pic = img.resize((int(hpx * 128 / img.size[1] * img.size[0]), hpx * 128)).crop(
                    (0 + bg_cut_px, 0, wpx * 128 + bg_cut_px, hpx * 128))
            else:
                bg_cut_px = int((wpx * 128 - int(hpx * 128 / img.size[1] * img.size[0])) / 2)
                pic = img.resize((wpx * 128, int(wpx * 128 / img.size[0] * img.size[1]))).crop(
                    (0, 0 + bg_cut_px, wpx * 128, hpx * 128 + bg_cut_px))
        img.close()
        folder_name = '{0}/{1}'.format(output_folder, os.path.splitext(ui)[0].split('/')[-1])
        s = 0
        while os.path.exists(folder_name):
            s += 1
            folder_name = '{0}/{1}({2})'.format(output_folder, os.path.splitext(ui)[0].split('/')[-1], s)
        os.mkdir(folder_name)
        for i in range(wpx):
            for j in range(hpx):
                pic.crop((i * 128, j * 128, (i + 1) * 128, (j + 1) * 128)).save(
                    '{0}/{1}_{2}.png'.format(folder_name, j, i))
    print('end\n')


if __name__ == '__main__':
    output(int(input('长（格）：')), int(input('高（格）：')), askopenfilenames(), askdirectory())
tk.mainloop()
