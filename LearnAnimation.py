# import pylab
#
# pylab.xlim(0,10)
# pylab.ylim(0,1024)
# pylab.plot()
# pylab.show()
#





#
#
# import matplotlib.pyplot as plt
#
# plt.axis([0, 1, 1000, 1])
# plt.ion()
# x1 = 0
# x2 = 2
# y1 = 500
# y2 = 3
# y = 0
# for i in range(20):
#     y += 3
#     # plt.plot(currentPoint,comingPoint)
#     plt.plot((x1, x2), (y1, y2))
#     plt.pause(1)
#     x1 = x2
#     y1 = y2
#     x2 = i
#     y2 = y
# for i in range(20,40):
#     y -= 3
#     # plt.plot(currentPoint,comingPoint)
#     plt.plot((x1, x2), (y1, y2))
#     plt.pause(1)
#     x1 = x2
#     y1 = y2
#     x2 = i
#     y2 = y
#
# while True:
#     plt.pause(0.5)


# import matplotlib.pyplot as plt
# pairs=[(3,6),(1,1)]
# currentpoint = pairs[0]
# del pairs[0]
# for point in pairs:
#     plt.plot(currentpoint,point)
#
#     # pairs.append()
# plt.show()













import matplotlib.pyplot as plt

plt.axis([0, 50, 1000, 1])
plt.figure(1,figsize=(20,7))
plt.xlim(0,50)
plt.ylim(0,1024)

BPMs = [462, 444, 452, 432, 413, 417, 387, 396, 390, 390, 361, 354, 337, 337, 489, 347, 356, 302, 318, 293, 292,
            292, 298, 287, 295, 297, 282, 264, 234, 193, 199, 196, 202, 190, 207, 233, 236, 246, 269, 275, 295, 295,
            302, 332, 340, 367, 357, 358, 385, 383, 534, 470, 441, 443, 455, 441, 477, 490, 498, 514, 523, 542, 557,
            522, 483, 464, 459, 439, 430, 417, 401, 395, 400, 385, 378, 387, 373, 362, 356, 353, 351, 355, 342, 342,
            311, 303, 313, 343, 476, 286, 297, 270, 268, 280, 281, 283, 277, 298, 310, 313, 302, 280, 246, 233, 229,
            239, 256, 255, 282, 275, 282, 302, 295, 322, 328, 333, 344, 358, 370, 383, 410, 421, 442, 428, 437, 439,
            465, 645, 470, 501, 486, 492, 504, 512, 524, 530, 548, 549, 577, 562, 539, 496, 469, 472, 451, 450, 448,
            435, 433, 433, 423, 420, 395, 390, 381, 365, 355, 350, 342, 332, 338, 337, 299, 294, 291, 277, 428, 306,
            283, 262, 278, 276, 276, 288, 303, 306, 320, 345, 349, 330, 300, 287, 291, 298, 309, 319, 334, 340, 359,
            359, 377, 393, 401, 412, 419, 428]
x1 = 0
x2 = 1
y1 = BPMs[0]
y2 = BPMs[1]
i=2
while i < len(BPMs):
    # if (x2 == 50):
    #     x1 = 0
    #     x2 = 1
    plt.plot((x1, x2), (y1, y2), c='g')
    plt.pause(0.1)
    x1 = x2
    y1 = y2
    x2 = i
    y2 = BPMs[i]
    i += 1
