#coding:utf8
import numpy as np
import cv2

# 画像読み込み(alphaチャンネル有り)
src_mat = cv2.imread("001.png", cv2.IMREAD_UNCHANGED)
print(src_mat.shape) # 32,32,4

# 画像サイズの取得(横, 縦)
size = tuple([src_mat.shape[1], src_mat.shape[0]])

# dst 画像用意
dst_mat = np.zeros((size[1], size[0], 4), np.uint8)

# 画像の中心位置(x, y)
center = tuple([int(size[0]/2), int(size[1]/2)])

# 回転させたい角度（正の値は反時計回り）
#angle = -45.0

# 拡大比率
#scale = 1.0
# 回転させたい角度
rad = np.pi / 10
    # x軸方向に平行移動させたい距離
move_x = 2
    # y軸方向に平行移動させたい距離
move_y = 0
 
matrix = [
            [1,  np.tan(rad), move_x],
            [0,   1, move_y]
        ]
 
affine_matrix = np.float32(matrix)

# 回転変換行列の算出
#rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# アフィン変換
img_dst = cv2.warpAffine(src_mat, affine_matrix, size, dst_mat,
                         flags=cv2.INTER_LINEAR,
                         borderMode=cv2.BORDER_TRANSPARENT)

# 表示
cv2.imwrite("dst.png", img_dst)
