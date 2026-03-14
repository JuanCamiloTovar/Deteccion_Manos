import cv2
import mediapipe as mp
import pygame

mp_hands = mp.solutions.hands # SE USA PARA INDICAR QUE SE VA A TRABAJAR CON LAS MANOS
mp_drawing = mp.solutions.drawing_utils # SE USA PARA DIBUJAR LOS LANDMARKS DE LAS MANOS

pygame.mixer.init() 

sounds = [
    pygame.mixer.Sound("sounds/#fa.wav"), # Indice izquierdo
    pygame.mixer.Sound("sounds/la.wav"), # Medio izquierdo
    pygame.mixer.Sound("sounds/re.wav"), # Anular izquierdo
    pygame.mixer.Sound("sounds/#do.wav"), # Indice derecho
    pygame.mixer.Sound("sounds/#sol.wav"), # Medio derecho
    pygame.mixer.Sound("sounds/si.wav"), # Anular derecho
]

def is_finger_down(landmarks, finger_tip, finger_mcp):
    return landmarks[finger_tip].y > landmarks[finger_mcp].y

cap = cv2.VideoCapture(0) # Se le indica la camara, la principal es 0, se puede pasar un video pregrabado

with mp_hands.Hands(min_detection_confidence = 0.5, min_tracking_confidence = 0.5,
                    max_num_hands = 2) as hands:
    finger_state = [False]*6
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame,1) # Se convierte la imagen en espejo
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # se cambia de formato bgr a rgb
        results = hands.process(rgb_frame)
        
        # SIRVE PARA GRAFICAR EN EL FRAME LOS LANDMARKS
        if results.multi_hand_landmarks: # SE ITERAN LOS LANDMARKS
            for h,hand_landmarks in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                finger_tips = [8,12,16]
                finger_mcp = [5,9,13]
                
                for i in range(3):
                    finger_index = i + h *3
                    if is_finger_down(hand_landmarks.landmark, finger_tips[i], finger_mcp[i]):
                        if not finger_state[finger_index]:
                            sounds[finger_index].play()
                            finger_state[finger_index] = True
                    else:
                        finger_state[finger_index] = False
        
        
        cv2.imshow("Hand detection", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()