import datetime
import multiprocessing
import os
import time
import cv2
import face_recognition
from FalconSearch.clear import clear
from moviepy.editor import VideoFileClip

def process_images(_,unknown_folder,known_image_list):
    global hits
    frame_rate = VideoFileClip(unknown_folder + "/" + _).fps
    duration = int(VideoFileClip(unknown_folder + "/" + _).fps * VideoFileClip(unknown_folder + "/" + _).duration)
    capture = cv2.VideoCapture(unknown_folder + "/" + _)
    frame_position = capture.get(cv2.CAP_PROP_POS_FRAMES)
    frame_list = []
    while frame_position <= duration:
        flag,frame = capture.read()
        if flag:
            frame_position = capture.get(cv2.CAP_PROP_POS_FRAMES)
            rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame,face_locations)
            for face_encoding in face_encodings:
                for image in known_image_list:
                    result = bool(face_recognition.compare_faces(image,face_encodings)[0])
                    if result:
                        hits.append(f"{_} | " + str(datetime.timedelta(seconds=int(frame_position / frame_rate))))

        else:
            capture.set(cv2.CAP_PROP_POS_FRAMES,frame_position-1)

def FalconSearch(known_folder,unknown_folder):
    global hits
    hits = []
    clear()
    hits = []
    core_count = multiprocessing.cpu_count()

    # prep work
    home = os.path.expanduser("~")

    if not os.path.exists(f"{home}/FalconSearch_output"):
        os.makedirs(f"{home}/FalconSearch_output")

    known_files = os.listdir(known_folder)
    unknown_files = os.listdir(unknown_folder)

    clear()
    print("running face recognition")

    known_image_list = []
    start = time.time()
    for _ in known_files:
        known_image = face_recognition.load_image_file(known_folder + "/" + _)
        known_image = face_recognition.face_encodings(known_image,)[0]
        known_image_list.append(known_image)

    core_tracker = 0
    p_list = []
    for _ in unknown_files:
        core_tracker += 1
        p = multiprocessing.Process(target=process_images,args=(_,unknown_folder,known_image_list))
        p_list.append(p)
        p.start()
        if core_tracker % core_count == 0:
            for __ in p_list:
                __.join()

    for __ in p_list:
        __.join()

    end = time.time()
    total_time = end - start
    hits = list(set(hits[:]))
    with open(f"{home}/FalconSearch_output/matches.txt","a") as file:
        for hit in hits:
            file.write(hit + "\n")

    print("",end="\n")
    print("done in " + str(datetime.timedelta(seconds=int(total_time / frame_rate))))

clear()
known_folder = input("known folder:\n")
unknown_folder = input("unknown folder:\n")
FalconSearch(known_folder,unknown_folder)
