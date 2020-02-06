首先使用binwalk查看cat.png

发现存在两张图片

使用foremost提取出来得到00000000.png和00000725.png和00000725

用stegsolve.jar将两张图片做SUB得到一张残缺的二维码，命名为part01.png

随后将part01.png与cat.png做MUL得到一张彩色的二维码

和张二维码扫描不出来，需要对其进行处理，处理脚本如getflag.py

将其转化为黑白图片以后，二维码扫描即可得到https://imgur.com/download/Xrv86y2

下载下来对应图片Xrv86y2-....

用strings Xrv86... | grep BAMBOOFOX{

即可获取flag：BAMBOOFOX{Y0u_f1nd_th3_h1dd3n_c4t!!!}
