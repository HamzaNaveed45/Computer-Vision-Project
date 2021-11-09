import cv2


def main():

    print("Press 1 for pre-recorded videos, 2 for live stream: ")
    option = int(input())

    if option == 1:
        # Record video
        windowName = "Sample Feed from Camera 1"
        windowName2 = "Sample Feed from Camera 2"
        windowName3 = "Sample Feed from Camera 3"
        cv2.namedWindow(windowName)
        cv2.namedWindow(windowName2)
        cv2.namedWindow(windowName3)

        #capture1 = cv2.VideoCapture(0)  # laptop's camera11
        capture2 = cv2.VideoCapture("http://10.130.17.247:8080/video")   # vivo
        capture3 = cv2.VideoCapture("http://10.130.16.240:8080/video")  # samsung zoha
        capture4 = cv2.VideoCapture("http://10.130.10.191:8080/video") #hamza samsung

        # define size for recorded video frame for video 1
        width1 = int(capture2.get(3))
        height1 = int(capture2.get(4))
        size1 = (width1, height1)

        width2 = int(capture3.get(3))
        height2 = int(capture3.get(4))
        size2 = (width2, height2)

        width3 = int(capture4.get(3))
        height3 = int(capture4.get(4))
        size3 = (width3, height3)


        # frame of size is being created and stored in .avi file
        optputFile1 = cv2.VideoWriter(
            'vivo.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size1)
        optputFile2 = cv2.VideoWriter(
            'Zohasamsung.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size2)
        optputFile3 = cv2.VideoWriter(
            'Hamzasamsung.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size3)

        # check if feed exists or not for camera 1
        if capture2.isOpened():
            ret1, frame1 = capture2.read()
        else:
            ret1 = False

        if capture3.isOpened():
            ret2, frame2 = capture3.read()
        else:
            ret2 = False

        if capture3.isOpened():
            ret3, frame3 = capture4.read()
        else:
            ret3 = False

        while ret1 and ret2 and ret3:
            ret1, frame1 = capture2.read()
            ret2, frame2 = capture3.read()
            ret3, frame3 = capture4.read()
            # sample feed display from camera 1
            cv2.imshow(windowName, frame1)
            optputFile1.write(frame1)
            cv2.imshow(windowName2, frame2)
            optputFile2.write(frame2)
            cv2.imshow(windowName3, frame3)
            optputFile3.write(frame3)
            #cv2.imshow(windowName2, frame2)
            # saves the frame from camera 1



            # escape key (27) to exit
            #if cv2.waitKey(1) == 27:
            #    break
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break


        capture2.release()
        capture3.release()
        capture4.release()
        optputFile1.release()
        optputFile2.release()
        optputFile3.release()
        cv2.destroyAllWindows()

    elif option == 2:
        # live stream

        windowName = "Sample Feed from Camera 1"
        windowName2 = "Sample Feed from Camera 2"
        windowName3 = "Sample Feed from Camera 3"
        cv2.namedWindow(windowName)
        cv2.namedWindow(windowName2)
        cv2.namedWindow(windowName3)

        # capture1 = cv2.VideoCapture(0)  # laptop's camera11
        capture2 = cv2.VideoCapture("http://10.130.17.247:8080/video")  # vivo
        capture3 = cv2.VideoCapture("http://10.130.16.240:8080/video")  # samsung zoha
        capture4 = cv2.VideoCapture("http://10.130.10.191:8080/video")  # hamza samsung

        # check if feed exists or not for camera 1
        if capture2.isOpened():
            ret1, frame1 = capture2.read()
        else:
            ret1 = False

        if capture3.isOpened():
            ret2, frame2 = capture3.read()
        else:
            ret2 = False

        if capture3.isOpened():
            ret3, frame3 = capture4.read()
        else:
            ret3 = False

        while ret1 and ret2 and ret3:
            ret1, frame1 = capture2.read()
            ret2, frame2 = capture3.read()
            ret3, frame3 = capture4.read()
            # sample feed display from camera 1
            cv2.imshow(windowName, frame1)
            # optputFile1.write(frame1)
            cv2.imshow(windowName2, frame2)
            # optputFile2.write(frame2)
            cv2.imshow(windowName3, frame3)
            # optputFile3.write(frame3)
            # cv2.imshow(windowName2, frame2)
            # saves the frame from camera 1

            # escape key (27) to exit
            # if cv2.waitKey(1) == 27:
            #    break
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        capture2.release()
        capture3.release()
        capture4.release()
        cv2.destroyAllWindows()

    else:
        print("Invalid option entered. Exiting...")


main()
