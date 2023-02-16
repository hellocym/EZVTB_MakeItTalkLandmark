import math

import numpy as np
from pose import Landmark, get_pose
import matplotlib.pyplot as plt


def smooth(x, window_len=11, window='hanning'):
    # print(x)
    # print(f'size: {x.size}')
    if x.ndim != 1:
        raise (ValueError, "smooth only accepts 1 dimension arrays.")
    if x.size < window_len:
        raise (ValueError, "Input vector needs to be bigger than window size.")
    if window_len < 3:
        return x
    if window not in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise (ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")
    s = np.r_[2 * x[0] - x[window_len - 1::-1], x, 2 * x[-1] - x[-1:-window_len:-1]]
    if window == 'flat':  # moving average
        w = np.ones(window_len, 'd')
    else:
        w = eval('np.' + window + '(window_len)')
    y = np.convolve(w / w.sum(), s, mode='same')
    return y[window_len:-window_len + 1]


if __name__ == '__main__':
    def blink_function(t_):
        # 1-sqrt(2e)/(sqrt(3)-1)*(t/ect)*exp(-(t/ect)^2)*sin(t/ect)
        ect = 1 / 6  # eye_close_time
        constant = math.sqrt(2 * math.e) / (math.sqrt(3) - 1)
        return 1 - constant * (t_ / ect) * math.exp(-(t_ / ect) ** 2) * math.sin(t_ / ect)
    plt.plot(np.arange(0, 1, 0.01), [blink_function(t) for t in np.arange(0, 1, 0.01)])
    plt.show()

    # landmarks = 'landmarks/pred_fls_下载_audio_embed.txt'
    # landmarks = np.loadtxt(landmarks)
    #
    # # #print(landmarks)
    # # landmarks = landmarks.reshape(-1, 68 * 3)
    # # #landmarks = landmarks[0:1000]
    # # # print(landmarks[1])
    # # t = landmarks.T
    # # t_0 = t[0]
    # # # plot using matplotlib
    # # plt.plot(t_0, 'r')
    # # # apply smooth() to every row of t
    # # t = np.apply_along_axis(smooth, 1, t, *(60, 'hanning'))
    # # t_0 = t[0]
    # # # plot using matplotlib
    # # plt.plot(t_0, 'b')
    # # landmarks = t.T
    # # # print(landmarks[1])
    # # plt.show()
    # # landmarks = landmarks.reshape(-1, 68, 3)
    # landmarks = landmarks.reshape(-1, 68, 3)
    # frames_mdpp = []
    # print(f'Clip length: {len(landmarks)} frames.')
    #
    # for frame in landmarks:
    #     frame_mdpp = []
    #     #print(frame)
    #     for landmark in frame:
    #         frame_mdpp.append(Landmark(*landmark))
    #     frames_mdpp.append(frame_mdpp)
    #
    # poses = [get_pose(f)[0] for f in frames_mdpp]
    # poses = np.array(poses)
    # # 偷偷平滑下数据
    # t = poses.T
    # t_0 = t[0, :1000]
    # plt.plot(t_0, 'r')
    # t = np.apply_along_axis(smooth, 1, t, *(60, 'hanning'))
    # t_0 = t[0, :1000]
    # plt.plot(t_0, 'b')
    # poses = t.T
    #
    # plt.show()
    #
    # # for facial_landmarks in frames_mdpp:
    # #     pose = get_pose(facial_landmarks)
    # #     print(pose[0])
    #
    # # for frame in frames_mdpp:
    # #     # pass
    # #     print(frame[0].x, frame[0].y, frame[0].z)
    # #         # print(landmark.shape)
