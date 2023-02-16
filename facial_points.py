# MOUTH_TOP = 13
# MOUTH_BOTTOM = 14
# MOUTH_RIGHT = 78
#
# # There is no MOUTH_LEFT point in Mediapipe, So I approximate MOUTH_RIGHT point using rip`s points
# MOUTH_LEFT1 = 409
# MOUTH_LEFT2 = 375
#
# IRIS_L_TOP = 386
# IRIS_L_BOTTOM = 374
# IRIS_L_LEFT = 263
# IRIS_L_RIGHT = 382
#
# IRIS_R_TOP = 159
# IRIS_R_BOTTOM = 145
# IRIS_R_LEFT = 155
# IRIS_R_RIGHT = 33
#
# NOSE_CENTER = 197
# EYEBROW_CENTER = 9
# SILHOUETTE_BOTTOM = 152

# ----------------------- #
# 68 3d facial landmarks

MOUTH_TOP = 62
MOUTH_BOTTOM = 66
MOUTH_RIGHT = 60

MOUTH_LEFT1 = 53
MOUTH_LEFT2 = 55

IRIS_L_TOP = 43
IRIS_L_BOTTOM = 47
IRIS_L_LEFT = 45
IRIS_L_RIGHT = 42

IRIS_R_TOP = 38
IRIS_R_BOTTOM = 41
IRIS_R_LEFT = 39
IRIS_R_RIGHT = 36

NOSE_CENTER = 29

# There is no EYEBROW_CENTER point in 3d 68 facial landmarks, So I approximate EYEBROW_CENTER point using L&R eyebrows' points
# EYEBROW_CENTER = 9
EYEBROW_L_RIGHT = 22
EYEBROW_R_LEFT = 21

SILHOUETTE_BOTTOM = 8


# silhouette: [
#     10,  338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288,
#     397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136,
#     172, 58,  132, 93,  234, 127, 162, 21,  54,  103, 67,  109
#   ],
#
#   lipsUpperOuter: [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291],
#   lipsLowerOuter: [146, 91, 181, 84, 17, 314, 405, 321, 375, 291],
#   lipsUpperInner: [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308],
#   lipsLowerInner: [78, 95, 88, 178, 87, 14, 317, 402, 318, 324, 308],
#
#   rightEyeUpper0: [246, 161, 160, 159, 158, 157, 173],
#   rightEyeLower0: [33, 7, 163, 144, 145, 153, 154, 155, 133],
#   rightEyeUpper1: [247, 30, 29, 27, 28, 56, 190],
#   rightEyeLower1: [130, 25, 110, 24, 23, 22, 26, 112, 243],
#   rightEyeUpper2: [113, 225, 224, 223, 222, 221, 189],
#   rightEyeLower2: [226, 31, 228, 229, 230, 231, 232, 233, 244],
#   rightEyeLower3: [143, 111, 117, 118, 119, 120, 121, 128, 245],
#
#   rightEyebrowUpper: [156, 70, 63, 105, 66, 107, 55, 193],
#   rightEyebrowLower: [35, 124, 46, 53, 52, 65],
#
#   rightEyeIris: [473, 474, 475, 476, 477],
#
#   leftEyeUpper0: [466, 388, 387, 386, 385, 384, 398],
#   leftEyeLower0: [263, 249, 390, 373, 374, 380, 381, 382, 362],
#   leftEyeUpper1: [467, 260, 259, 257, 258, 286, 414],
#   leftEyeLower1: [359, 255, 339, 254, 253, 252, 256, 341, 463],
#   leftEyeUpper2: [342, 445, 444, 443, 442, 441, 413],
#   leftEyeLower2: [446, 261, 448, 449, 450, 451, 452, 453, 464],
#   leftEyeLower3: [372, 340, 346, 347, 348, 349, 350, 357, 465],
#
#   leftEyebrowUpper: [383, 300, 293, 334, 296, 336, 285, 417],
#   leftEyebrowLower: [265, 353, 276, 283, 282, 295],
#
#   leftEyeIris: [468, 469, 470, 471, 472],
#
#   midwayBetweenEyes: [168],
#
#   noseTip: [1],
#   noseBottom: [2],
#   noseRightCorner: [98],
#   noseLeftCorner: [327],
#
#   rightCheek: [205],
#   leftCheek: [425]