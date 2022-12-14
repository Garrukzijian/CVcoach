import argparse
import math
import os
import sys

import cv2
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from loguru import logger
from ui.lunge_form import Ui_Frame as ui_form

userWantsToExit = False
# Import Openpose (Windows/Ubuntu/OSX)
dir_path = os.path.dirname(os.path.realpath(__file__))

# Change these variables to point to the correct folder (Release/x64 etc.)
sys.path.append(dir_path + '/../../../bin/python/openpose/Release')
os.environ['PATH'] = os.environ['PATH'] + ';' + dir_path + '/../../../x64/Release;' + dir_path + '/../../../bin;'
import pyopenpose as op


def angle_between_points(p0, p1, p2):
    # 计算角度
    a = (p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2
    b = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    c = (p2[0] - p0[0]) ** 2 + (p2[1] - p0[1]) ** 2
    if a * b == 0:
        return -1.0

    return math.acos((a + b - c) / math.sqrt(4 * a * b)) * 180 / math.pi


def length_between_points(p0, p1):
    # 2点之间的距离
    return math.hypot(p1[0] - p0[0], p1[1] - p0[1])


def get_angle_point(human, pos):
    # 返回各个部位的关键点
    pnts = []

    if pos == 'left_elbow':
        pos_list = (5, 6, 7)
    elif pos == 'left_hand':
        pos_list = (1, 5, 7)
    elif pos == 'left_knee':
        pos_list = (12, 13, 14)
    elif pos == 'left_ankle':
        pos_list = (5, 12, 13)
    elif pos == 'right_elbow':
        pos_list = (2, 3, 4)
    elif pos == 'right_hand':
        pos_list = (1, 2, 4)
    elif pos == 'right_knee':
        pos_list = (9, 10, 11)
    elif pos == 'right_ankle':
        pos_list = (2, 9, 10)
    elif pos == 'left_hip':
        pos_list = (8, 9, 10)
    elif pos == 'right_hip':
        pos_list = (11, 8, 9)
    elif pos == 'waist':
        pos_list = (1, 8, 10)
    elif pos == 'waist2':
        pos_list = (1, 8, 13)
    else:
        print('Unknown  [%s]', pos)
        return pnts

    for i in range(3):
        if human[pos_list[i]][2] <= 0.1:
            return pnts

        pnts.append((int(human[pos_list[i]][0]), int(human[pos_list[i]][1])))
    return pnts


def angle_left_hand(human):
    pnts = get_angle_point(human, 'left_hand')
    if len(pnts) != 3:
        return -1

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
    return angle


def angle_left_hip(human):
    pnts = get_angle_point(human, 'left_hip')
    if len(pnts) != 3:
        return -1

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
    return angle


def angle_waist(human):
    pnts = get_angle_point(human, 'waist')
    if len(pnts) != 3:
        return -1

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
    return angle


def angle_waist2(human):
    pnts = get_angle_point(human, 'waist2')
    if len(pnts) != 3:
        return -1

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
    return angle


def angle_left_elbow(human):
    pnts = get_angle_point(human, 'left_elbow')
    if len(pnts) != 3:
        return

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
    return angle


def angle_left_knee(human):
    pnts = get_angle_point(human, 'left_knee')
    if len(pnts) != 3:
        return

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
    return angle


def angle_left_ankle(human):
    pnts = get_angle_point(human, 'left_ankle')
    if len(pnts) != 3:
        return

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
    return angle


def angle_right_hand(human):
    pnts = get_angle_point(human, 'right_hand')
    if len(pnts) != 3:
        return

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
    return angle


def angle_right_elbow(human):
    pnts = get_angle_point(human, 'right_elbow')
    if len(pnts) != 3:
        return

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
    return angle


def angle_right_knee(human):
    pnts = get_angle_point(human, 'right_knee')
    if len(pnts) != 3:
        return

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
    return angle


def angle_right_ankle(human):
    pnts = get_angle_point(human, 'right_ankle')
    if len(pnts) != 3:
        return

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
    return angle


def angle_right_hip(human):
    pnts = get_angle_point(human, 'right_hip')
    if len(pnts) != 3:
        return

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
    return angle


def angle_left_hip(human):
    pnts = get_angle_point(human, 'left_hip')
    if len(pnts) != 3:
        return

    angle = 0
    if pnts is not None:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
    return angle


def lunge(human):
    pnts = get_angle_point(human, 'left_knee')
    pnts2 = get_angle_point(human, 'waist')
    pnts3 = get_angle_point(human, 'right_knee')
    pnts4 = get_angle_point(human, 'left_ankle')
    pnts5 = get_angle_point(human, 'right_ankle')
    pnts6 = get_angle_point(human, 'waist2')

    if len(pnts) != 3:
        return 6
    if len(pnts3) != 3:
        return 6
    if len(pnts2) != 3:
        return 6
    if len(pnts4) != 3:
        return 6
    if len(pnts5) != 3:
        return 6
    if len(pnts6) != 3:
        return 6

    angle = 0
    count_of_squats = 0
    if len(pnts3) == 3:
        angle = angle_between_points(pnts[0], pnts[1], pnts[2])
        angle2 = angle_between_points(pnts2[0], pnts2[1], pnts2[2])
        angle3 = angle_between_points(pnts3[0], pnts3[1], pnts3[2])
        angle4 = angle_between_points(pnts4[0], pnts4[1], pnts4[2])
        angle5 = angle_between_points(pnts5[0], pnts5[1], pnts5[2])
        angle6 = angle_between_points(pnts6[0], pnts6[1], pnts6[2])

        prev_squat_pos = 1
        if angle4 > angle5:
            if angle <= 95 and angle2 >= 100 and angle3 <= 95:
                squat_pos = 0
            elif 95 <= angle <= 169 and angle2 >= 100 and 95 <= angle3 <= 169:
                squat_pos = 2
            elif angle <= 95 and angle2 <= 100 and angle3 <= 95:
                squat_pos = 3
            elif 170 <= angle and 100 <= angle2 and 170 <= angle3:
                squat_pos = 4
            else:
                squat_pos = 1
            if prev_squat_pos - squat_pos == 1:
                count_of_squats = 1
            if prev_squat_pos - squat_pos == -1:
                count_of_squats = 2
            if prev_squat_pos - squat_pos == -2:
                count_of_squats = 3
            if prev_squat_pos - squat_pos == -3:
                count_of_squats = 4
            return count_of_squats
        elif angle5 > angle4:
            if angle <= 95 and angle6 >= 100 and angle3 <= 95:
                squat_pos = 0
            elif 95 <= angle <= 169 and angle6 >= 100 and 95 <= angle3 <= 169:
                squat_pos = 2
            elif angle <= 95 and angle6 <= 100 and angle3 <= 95:
                squat_pos = 3
            elif 170 <= angle and 100 <= angle6 and 170 <= angle3:
                squat_pos = 4
            else:
                squat_pos = 1
            if prev_squat_pos - squat_pos == 1:
                count_of_squats = 1
            if prev_squat_pos - squat_pos == -1:
                count_of_squats = 2
            if prev_squat_pos - squat_pos == -2:
                count_of_squats = 3
            if prev_squat_pos - squat_pos == -3:
                count_of_squats = 4
            return count_of_squats

        else:
            return 6
    else:
        return 6


def display(datums):
    datum = datums[0]
    key = cv2.waitKey(1)
    return key == 20


def printKeypoints(datums):
    datum = datums[0]
    count = 0
    if datum.poseKeypoints is not None:
        for i in range(1):
            count = lunge(datum.poseKeypoints[i])
        return count
    else:
        return 0


class lunge_form(ui_form, QFrame):
    def __init__(self):
        super(lunge_form, self).__init__()
        self.setupUi(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/探测声音.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # 加载字体
        QtGui.QFontDatabase.addApplicationFont("res/Social Media Circled.otf")
        # 隐藏原始的框
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 按钮事件绑定
        self.close_pushButton.clicked.connect(self.close_event)
        self.min_pushButton.clicked.connect(self.showMinimized)
        self.start_pushButton.clicked.connect(self.start_test)

    def start_test(self):
        value = self.textEdit.toPlainText()
        if value.isdigit():
            target = int(value)
            # Flags
            global userWantsToExit

            parser = argparse.ArgumentParser()
            parser.add_argument("--no-display", action="store_true", help="Disable display.")
            args = parser.parse_known_args()

            # Custom Params (refer to include/openpose/flags.hpp for more parameters)
            params = dict()
            params["model_folder"] = "../../models/"

            # Add others in path?
            for i in range(0, len(args[1])):
                curr_item = args[1][i]
                if i != len(args[1]) - 1:
                    next_item = args[1][i + 1]
                else:
                    next_item = "1"
                if "--" in curr_item and "--" in next_item:
                    key = curr_item.replace('-', '')
                    if key not in params:  params[key] = "1"
                elif "--" in curr_item and "--" not in next_item:
                    key = curr_item.replace('-', '')
                    if key not in params: params[key] = next_item

            # Starting OpenPose

            opWrapper = op.WrapperPython(op.ThreadManagerMode.AsynchronousOut)
            opWrapper.configure(params)
            opWrapper.start()

            # Main Loop
            global userWantsToExit
            userWantsToExit = False
            count_of_squats = 0
            count_of_wrong = 0
            count_switch = True
            count_switch_wrong = True
            while not userWantsToExit:
                datumProcessed = op.VectorDatum()
                if opWrapper.waitAndPop(datumProcessed):
                    if not args[0].no_display:
                        userWantsToExit2 = display(datumProcessed)
                        number = printKeypoints(datumProcessed)
                        if number == 1 and count_switch == True:
                            count_of_squats = count_of_squats + 1
                            count_switch = False
                            self.suggest_label.setText("successful")
                        elif number == 2 and count_switch == True:
                            self.suggest_label.setText("keep doing, bend knee")
                        elif number == 2 and count_switch == False:
                            self.suggest_label.setText("straight your knee")
                        elif number == 3 and count_switch == True and count_switch_wrong == True:
                            self.suggest_label.setText("straight your waist")
                            count_of_wrong = count_of_wrong + 1
                            count_switch_wrong = False
                            count_switch = False
                        elif number == 4 and count_switch == False:
                            count_switch = True
                            self.suggest_label.setText("continue")
                        elif number == 4 and count_switch_wrong == False:
                            count_switch_wrong = True
                            self.suggest_label.setText("continue")
                        if count_of_squats == target:
                            userWantsToExit = True
                            self.close()
                            QMessageBox.information(self, "Finish exercise", "Congratulation,you finish your goal！")
                        datum = datumProcessed[0]
                        a = datum.cvOutputData
                        image_height, image_width, image_depth = a.shape
                        QIm = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
                        QIm = QImage(QIm.data, image_width, image_height,  # 创建QImage格式的图像，并读入图像信息
                                     image_width * image_depth,
                                     QImage.Format_RGB888)
                        self.camera_label.setPixmap(QPixmap.fromImage(QIm))

                        count_string = str(count_of_squats)
                        count_worng_string = str(count_of_wrong)
                        self.right_label.setText(count_string)
                        self.wrong_label.setText(count_worng_string)
                else:
                    self.camera_label.clear()
                    break
            self.camera_label.setPixmap(QPixmap(""))
        else:
            self.wrong_label.setText("not have number")

    def close_event(self, event):
        logger.info("Close lunge window")
        global userWantsToExit
        userWantsToExit = True
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(app.exec_())
