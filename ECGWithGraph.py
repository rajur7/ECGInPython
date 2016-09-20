import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

def ElectroCardioGram():
    fig = plt.figure(figsize=(12,7))
    ax = plt.axes(xlim=(0,100), ylim=(0,1024))
    line, = ax.plot([],[],'',lw = 2)
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
    standardX = list(np.arange(0, len(BPMs), 1))
    plt.plot(standardX,BPMs)
    def animate(y):
        standardX.append(standardX[-1]+1)
        BPMs.append(y)
        line.set_data(standardX[-1])
        line.set_data(y)
        return line

    bpms = [445, 451, 461, 473, 487, 494, 479, 492, 493, 552, 670, 495, 501, 510, 501, 502, 515, 510, 511, 526, 509,
            515, 505, 467, 426, 405, 384, 373, 372, 357, 348, 333, 330, 311, 303, 296, 284, 289, 275, 261, 261, 256,
            251, 247, 247, 259, 248, 249, 225, 228, 235, 374, 335, 270, 253, 270, 278, 298, 316, 317, 346, 368, 389,
            397, 382, 380, 356, 354, 356, 366, 387, 386, 407, 423, 428, 415, 441, 444, 447, 446, 464, 475, 470, 467,
            463, 468, 460, 466, 471, 450, 442, 428, 424, 593, 435, 419, 408, 396, 391, 400, 392, 379, 384, 393, 380,
            394, 377, 327, 311, 282, 277, 279, 272, 264, 273, 263, 259, 255, 254, 254, 244, 267, 267, 265, 283, 284,
            288, 308, 306, 299, 310, 320, 406, 476, 345, 367, 371, 392, 395, 411, 425, 440, 455, 477, 494, 495, 454,
            444, 428, 439, 436, 445, 448, 449, 460, 459, 450, 442, 448, 438, 450, 434, 444, 438, 405, 392, 384, 366,
            487, 426, 367, 349, 331, 337, 334, 333, 339, 328, 336, 346, 347, 314, 274, 245, 236, 231, 227, 234, 237,
            242, 235, 244, 244, 248, 252, 260, 270, 296, 300, 311, 302, 299, 321, 387, 514, 339, 369, 373, 394, 407,
            426, 434, 456, 478, 507, 504, 501, 475, 458, 440, 448, 459, 451, 465, 467, 458, 471, 470, 468, 463, 463,
            453, 454, 462, 459, 434, 421, 401, 399, 504, 492, 385, 362, 363, 341, 346, 348, 333, 341, 345, 343, 350,
            312, 262, 242, 228, 221, 220, 218, 221, 215, 227, 228, 226, 242, 245, 245, 257, 272, 297, 287, 285, 295,
            299, 435, 402, 355, 347, 361, 380, 411, 413, 427, 450, 485, 498, 502, 483, 445, 445, 433, 448, 447, 459,
            460, 469, 468, 468, 472, 470, 475, 458, 473, 478, 479, 463, 436, 445, 429, 532, 513, 431, 404, 395, 394,
            389, 384, 373, 381, 387, 384, 387, 354, 306, 269, 273, 252, 259, 242, 253, 244, 240, 249, 245, 251, 256,
            248, 252, 269, 266, 269, 283, 289, 310, 325, 330, 324, 320, 346, 384, 541, 356, 388, 395, 411, 413, 441,
            449, 472, 482, 508, 522, 520, 492, 472, 452, 448, 469, 454, 464, 469, 477, 468, 465, 459, 450, 450, 447,
            439, 434, 450, 446, 439, 422, 432, 404, 383, 381, 366, 414, 498, 331, 326, 323, 319, 295, 282, 284, 290,
            286, 300, 306, 303, 248, 231, 208, 218, 223, 221, 230, 237, 243, 262, 271, 269, 283, 288, 300, 310, 323,
            324, 341, 349, 365, 385, 405, 410, 405, 399, 413, 454, 618, 436, 459, 468, 462, 474, 489, 490, 511, 525,
            535, 546, 542, 508, 467, 453, 443, 436, 432, 423, 415, 411, 398, 390, 373, 365, 360, 344, 337, 336, 326,
            308, 300, 292, 286, 285, 285, 281, 265, 246, 239, 229, 343, 347, 250, 242, 243, 244, 252, 270, 277, 290,
            313, 329, 350, 338, 302, 300, 295, 302, 314, 326, 333, 345, 358, 367, 376, 383, 394, 403, 409, 426, 431,
            436, 448, 447, 459, 470, 483, 487, 500, 484, 472, 469, 471, 619, 521, 483, 476, 465, 467, 476, 484, 491,
            491, 494, 489, 487, 446, 401, 361, 348, 342, 333, 325, 310, 302, 294, 292, 275, 279, 263, 260, 268, 253,
            242, 260, 244, 258, 263, 275, 260, 265, 265, 282, 440, 300, 307, 304, 316, 326, 341, 348, 374, 388, 417,
            441, 443, 423, 404, 384, 395, 397, 409, 411, 425, 437, 448, 452, 438, 454, 455, 448, 457, 454, 455, 450,
            467, 476, 467, 448, 443, 441, 482, 608, 413, 420, 414, 411, 405, 405, 394, 403, 397]

    def get_y():
        for y in bpms:
            yield y

    anim = animation.FuncAnimation(fig, animate, frames=get_y(),interval=100)
    plt.show()

ElectroCardioGram()
